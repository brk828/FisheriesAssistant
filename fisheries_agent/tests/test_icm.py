import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import json
import sqlite3

from utils import brain_index, gitsync, icm_git, icm_scaffold, icm_seed, icm_skills, icm_validate, icm_wizard
from utils import icm_data, icm_integration, icm_restructure
import hashlib
import os


class FolderNameTests(unittest.TestCase):
    def test_restructured_keeps_original(self):
        self.assertEqual(icm_scaffold.folder_name("x", "Colorado_Pikeminnow"), "Colorado_Pikeminnow_icm")

    def test_new_is_sanitized_and_shortened(self):
        name = icm_scaffold.folder_name("Humpback chub: mark-recapture & abundance for the Little Colorado River 2024")
        self.assertTrue(name.endswith("_icm"))
        self.assertLessEqual(len(name), 44)
        self.assertRegex(name, r"^[A-Za-z0-9_]+$")

    def test_empty_name(self):
        self.assertEqual(icm_scaffold.folder_name("***"), "Project_icm")


class SuggestTests(unittest.TestCase):
    def test_mark_recapture_first(self):
        self.assertEqual(icm_scaffold.suggest_type("PIT tag mark-recapture abundance")[0], "mark_recapture")


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_each_type_scaffolds_and_validates(self):
        for key in icm_scaffold.load_types():
            dest = icm_scaffold.scaffold(self.root, f"{key}_icm", key, key, profile="Prefers R and Quarto.")
            self.assertEqual(icm_validate.validate(dest), [], key)

    def test_same_type_same_tree(self):
        a = icm_scaffold.scaffold(self.root, "a_icm", "A", "mark_recapture", profile="p")
        b = icm_scaffold.scaffold(self.root, "b_icm", "B", "mark_recapture", profile="p")
        tree = lambda d: sorted(p.relative_to(d).as_posix() for p in (d / "stages").rglob("*"))
        self.assertEqual(tree(a), tree(b))

    def test_never_overwrites(self):
        icm_scaffold.scaffold(self.root, "a_icm", "A", "report", profile="p")
        with self.assertRaises(FileExistsError):
            icm_scaffold.scaffold(self.root, "a_icm", "A", "report", profile="p")

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            icm_scaffold.scaffold(self.root, "a_icm", "A", "nope")

    def test_agents_has_profile_and_routing(self):
        dest = icm_scaffold.scaffold(self.root, "a_icm", "A", "report", routing="Custom routing.", profile="Likes R.")
        text = (dest / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Likes R.", text)
        self.assertIn("Custom routing.", text)

    def test_validator_catches_problems(self):
        dest = icm_scaffold.scaffold(self.root, "a_icm", "A", "mark_recapture", profile="p")
        stage = dest / "stages" / "02-model-design" / "CONTEXT.md"
        stage.write_text(stage.read_text(encoding="utf-8").replace("../01-data-prep/output/", "../05-report/output/"), encoding="utf-8")
        (dest / "stages" / "03-analysis" / "CONTEXT.md").unlink()
        issues = "\n".join(icm_validate.validate(dest))
        self.assertIn("one-way", issues)
        self.assertIn("03-analysis: CONTEXT.md is missing", issues)


class GitTests(unittest.TestCase):
    def test_disabled_creates_no_repo(self):
        with tempfile.TemporaryDirectory() as t:
            dest = icm_scaffold.scaffold(t, "a_icm", "A", "report", profile="p")
            self.assertFalse((dest / ".git").exists())
            self.assertFalse((dest / ".gitignore").exists())

    def test_enabled_ignores_data_and_large_files(self):
        with tempfile.TemporaryDirectory() as t:
            cfg = icm_git.settings(True, max_file_mb=1)
            dest = icm_scaffold.scaffold(t, "a_icm", "A", "mark_recapture", git_cfg=cfg, profile="p")
            (dest / "data" / "models" / "fit.rds").write_bytes(b"x" * 10)
            (dest / "shared" / "big.csv").write_bytes(b"x" * (2 * 1024 * 1024))
            (dest / "shared" / "small.csv").write_bytes(b"x")
            icm_git.apply_size_cap(dest, cfg)
            subprocess.run(["git", "add", "-A"], cwd=dest, check=True)
            staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=dest, capture_output=True, text=True).stdout
            self.assertNotIn("fit.rds", staged)
            self.assertNotIn("big.csv", staged)
            self.assertIn("small.csv", staged)


class WizardTests(unittest.TestCase):
    def run_wizard(self, answers, llm=None):
        with tempfile.TemporaryDirectory() as t:
            profile = Path(t) / "user_profile.md"
            profile.write_text("- **Tools:** R and Quarto\n", encoding="utf-8")
            root = Path(t) / "projects"
            root.mkdir()
            with mock.patch.object(icm_wizard, "PROFILE_PATH", profile), \
                 mock.patch.object(icm_scaffold, "PROFILE_PATH", profile), \
                 mock.patch("builtins.input", side_effect=answers):
                dest = icm_wizard.run(llm=llm, root=root)
            return dest.name, (dest / "AGENTS.md").read_text(encoding="utf-8"), (dest / ".git").exists(), icm_validate.validate(dest)

    def test_new_project_flow_with_llm_routing(self):
        answers = ["Chub MR 2024", "Estimate chub abundance", "Humpback chub, LCR", "PIT tag detections", "mark-recapture abundance",
                   "report", "1", "", "n", "", "n"]
        name, agents, has_git, issues = self.run_wizard(answers, llm=lambda p: "## Project\nLLM routing text.")
        self.assertEqual(name, "Chub_MR_2024_icm")
        self.assertIn("LLM routing text.", agents)
        self.assertIn("R and Quarto", agents)
        self.assertFalse(has_git)
        self.assertEqual(issues, [])

    def test_git_option_and_cancel(self):
        answers = ["P", "g", "s", "d", "mark-recapture", "r", "1", "",
                   "y", "*.tif", "raw_downloads/", "20", "y", "n"]
        with mock.patch.object(icm_wizard, "make_llm", return_value=None):
            name, _, has_git, _ = self.run_wizard(answers)
        self.assertTrue(has_git)
        with self.assertRaises(SystemExit):
            with mock.patch.object(icm_wizard, "make_llm", return_value=None):
                self.run_wizard(["P", "g", "s", "d", "a", "r", "1", "", "n", "n"])


class GitsyncCapTests(unittest.TestCase):
    def test_commit_skips_files_over_cap(self):
        with tempfile.TemporaryDirectory() as t:
            cfg = icm_git.settings(True, ignore_types=[], ignore_paths=[], max_file_mb=1)
            dest = icm_scaffold.scaffold(t, "a_icm", "A", "report", git_cfg=cfg, profile="p")
            for k, v in (("user.email", "a@b.c"), ("user.name", "t")):
                subprocess.run(["git", "config", k, v], cwd=dest, check=True)
            before = gitsync.snapshot(dest)
            (dest / "shared" / "big.bin").write_bytes(b"x" * (2 * 1024 * 1024))
            (dest / "shared" / "small.txt").write_text("hi")
            msg = gitsync.commit_changes(dest, before, "test")
            tracked = subprocess.run(["git", "ls-files"], cwd=dest, capture_output=True, text=True).stdout
            self.assertIn("small.txt", tracked)
            self.assertNotIn("big.bin", tracked)
            self.assertIn("size cap", msg)


def _cand(sid, cov=1.0):
    return {"source_id": sid, "title": f"Title {sid}", "year": "1999", "cite": f"Author (1999). Title {sid}. [{sid}]", "short": "(Author 1999)",
            "heading": "H", "excerpt": f"Excerpt about {sid}.", "coverage": cov, "score": -5.0}


class SeedSkillTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.brain = t / "brain"
        self.brain.mkdir()
        for sid in ("a", "b"):
            (self.brain / f"{sid}.md").write_text(f"---\nsource_id: {sid}\n---\n# {sid}\n", encoding="utf-8")
        self.root = icm_scaffold.scaffold(t, "p_icm", "P", "mark_recapture", answers={"species": "razorback sucker"}, profile="p")
        # Only topics whose query mentions pikeminnow-free text match; "Closed" topic is covered, the rest are gaps.
        def fake_find(query, limit=10, core=""):
            return [_cand("a"), _cand("b"), _cand("weak", 0.2)] if "closed population" in query else []
        self.patches = [mock.patch.object(brain_index, "SOURCES_DIR", self.brain),
                        mock.patch.object(brain_index, "find_sources", side_effect=fake_find)]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def test_seed_copies_snapshot_with_provenance_and_gaps(self):
        with mock.patch.object(icm_seed, "propose", return_value={"02-model-design": [
                icm_seed.search_topic({"topic": "Covered", "query": "closed population models", "why": "w", "source_hint": "h"}, {}),
                icm_seed.search_topic({"topic": "Missing", "query": "unmatched thing", "why": "w2", "source_hint": "a primary paper"}, {})]}):
            res = icm_seed.seed(self.root)
        refs = self.root / "stages" / "02-model-design" / "references"
        self.assertEqual(res, {"copied": 2, "gaps": 1})
        self.assertTrue((refs / "a.md").is_file())
        prov = json.loads((refs / "_provenance.json").read_text())
        self.assertEqual(set(prov), {"a", "b"})
        self.assertIn("| a |", (self.root / "shared" / "sources.md").read_text())
        gaps = (self.root / "GAPS.md").read_text()
        self.assertIn("Missing", gaps)
        self.assertIn("a primary paper", gaps)
        self.assertNotIn("Covered", gaps)
        self.assertEqual(icm_validate.validate(self.root), [])

    def test_refresh_detects_and_applies_changes(self):
        icm_seed.copy_note(_cand("a"), self.root / "stages" / "02-model-design" / "references")
        self.assertEqual(icm_seed.refresh(self.root), [])
        (self.brain / "a.md").write_text("new text", encoding="utf-8")
        self.assertEqual(icm_seed.refresh(self.root)[0][1:], ("a", "changed in brain"))
        icm_seed.refresh(self.root, apply=True)
        self.assertEqual((self.root / "stages" / "02-model-design" / "references" / "a.md").read_text(), "new text")
        self.assertEqual(icm_seed.refresh(self.root), [])

    def test_external_reference_survives_rewrite(self):
        icm_seed.supply(self.root, "Smith 2001. A paper. https://example.org/x")
        icm_seed.write_sources(self.root)
        self.assertIn("Smith 2001", (self.root / "shared" / "sources.md").read_text())

    def test_skill_generation_audit_and_gaps(self):
        draft = "## When to use\nWhenever a mark-recapture study is planned across occasions.\n## Closed-population models\nUse the Huggins estimator for short windows [[a]] [[ghost]].\nAn uncited statement about assumptions that is long enough to flag.\n"
        res = icm_skills.generate(self.root, "mark-recapture", lambda prompt: draft)
        text = (self.root / "skills" / "mark-recapture" / "SKILL.md").read_text()
        self.assertEqual(res["status"], "draft")
        self.assertIn("status: draft", text)
        self.assertNotIn("ghost", text)
        self.assertIn("(unsourced)", text)
        self.assertEqual(res["audit"]["unknown_cites"], ["ghost"])
        self.assertEqual(res["gaps"], 6)   # six of seven topics have no evidence
        self.assertIn("Tag loss and detection", (self.root / "skills" / "mark-recapture" / "GAPS.md").read_text())
        self.assertEqual(icm_validate.validate(self.root), [])

    def test_reviewed_skill_is_protected(self):
        icm_skills.generate(self.root, "mark-recapture", lambda p: "## x\ntext [[a]]\n")
        md = self.root / "skills" / "mark-recapture" / "SKILL.md"
        md.write_text(md.read_text().replace("status: draft", "status: reviewed"))
        self.assertEqual(icm_skills.generate(self.root, "mark-recapture", lambda p: "new")["status"], "protected")
        self.assertEqual(icm_skills.generate(self.root, "mark-recapture", lambda p: "## x\ntext [[a]]\n", force=True)["status"], "draft")

    def test_no_llm_still_seeds_references(self):
        res = icm_skills.generate(self.root, "mark-recapture", None)
        self.assertEqual(res["status"], "refs-only")
        self.assertTrue((self.root / "skills" / "mark-recapture" / "references" / "a.md").is_file())


class FindSourcesTests(unittest.TestCase):
    def test_coverage_and_ranking(self):
        db_file = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
        db_file.close()
        db = sqlite3.connect(db_file.name)
        db.executescript("""
            CREATE TABLE sources(source_id TEXT PRIMARY KEY, title TEXT, year TEXT, meta TEXT, author TEXT, cite TEXT, short TEXT);
            CREATE VIRTUAL TABLE chunks_fts USING fts5(source_id UNINDEXED, heading, body, tokenize='porter unicode61 remove_diacritics 2');
        """)
        db.execute("INSERT INTO sources VALUES ('good','Mark and recapture of chub','1990','','','cite good','(A 1990)')")
        db.execute("INSERT INTO chunks_fts VALUES ('good','Methods','mark and recapture estimates of chub abundance')")
        db.execute("INSERT INTO sources VALUES ('weak','Water chemistry','1991','','','cite weak','(B 1991)')")
        db.execute("INSERT INTO chunks_fts VALUES ('weak','Intro','abundance of algae in water')")
        db.commit()
        db.close()
        try:
            with mock.patch.object(brain_index, "_connect", lambda: sqlite3.connect(db_file.name)):
                res = brain_index.find_sources("mark-recapture chub abundance", 5)
            self.assertEqual(res[0]["source_id"], "good")
            self.assertGreaterEqual(res[0]["coverage"], 0.99)
            self.assertLess(res[1]["coverage"], 0.6)
            with mock.patch.object(brain_index, "_connect", lambda: sqlite3.connect(db_file.name)):
                self.assertEqual(brain_index.find_sources("the of", 5), [])
        finally:
            Path(db_file.name).unlink(missing_ok=True)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.manifest = self.base / "project_manifest.yaml"
        self.orig = self.base / "Chub"
        self.orig.mkdir()
        self.manifest.write_text(f"projects:\n  Chub:\n    project_path: {self.orig}\n    primary_format: Quarto (qmd)\n", encoding="utf-8")
        self.ws = icm_scaffold.scaffold(self.base, "Chub_icm", "Chub", "mark_recapture", profile="Likes R.")

    def tearDown(self):
        self.tmp.cleanup()

    def test_register_links_original_and_adds_workspace(self):
        name = icm_integration.register_workspace(self.ws, original="Chub", manifest_path=self.manifest)
        import yaml
        projects = yaml.safe_load(self.manifest.read_text())["projects"]
        self.assertEqual(name, "Chub_icm")
        self.assertEqual(projects["Chub"]["icm_workspace"], str(self.ws.resolve()))
        self.assertEqual(projects["Chub_icm"]["project_path"], str(self.ws.resolve()))
        self.assertEqual(icm_integration.workspace_of(projects["Chub"]), self.ws.resolve())
        self.assertIsNone(icm_integration.workspace_of({"icm_workspace": str(self.base / "gone")}))

    def test_layered_context_loads_one_stage(self):
        text = icm_integration.layered_context(self.ws, "02-model-design")
        self.assertIn("Likes R.", text)
        self.assertIn("stages/02-model-design/CONTEXT.md", text)
        self.assertNotIn("stages/03-analysis/CONTEXT.md\n", text)
        self.assertIn("Stages (ask for one", icm_integration.layered_context(self.ws))
        self.assertIn("not found", icm_integration.layered_context(self.ws, "nope"))

    def test_validate_reports_linked_data_changes(self):
        self.assertIn("passes", icm_integration.validate_workspace(self.ws))
        linked = self.base / "caps.csv"
        linked.write_text("a\n1\n")
        icm_data.save(self.ws, [icm_data.make_entry(linked, "data")])
        linked.write_text("a\n1\n2\n")
        self.assertIn("changed", icm_integration.validate_workspace(self.ws))


class RestructureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.src = base / "projects" / "Pikeminnow"
        self.root = base / "projects"
        for rel, data in {"analysis/fit.R": b"library(marked)\nlibrary(nimble)\n", "data/caps.csv": b"a,b\n1,2\n",
                          "out/model.rds": b"x" * 100, "notes.md": b"# notes\n", ".env": b"KEY=1", "report.docx": b"d",
                          "fig.png": b"p", ".git/config": b"c", "results/summary_table.csv": b"s\n"}.items():
            f = self.src / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(data)

    def tearDown(self):
        self.tmp.cleanup()

    def digest(self):
        h = hashlib.sha256()
        for r, _, fs in sorted(os.walk(self.src)):
            for n in sorted(fs):
                h.update(n.encode() + (Path(r) / n).read_bytes())
        return h.hexdigest()

    def test_restructure_end_to_end(self):
        before = self.digest()
        plan = icm_restructure.build_plan(self.src, "mark_recapture")
        dest = icm_restructure.execute(plan, self.root, "Pikeminnow", folder="Pikeminnow_icm")
        self.assertEqual(self.digest(), before)
        self.assertEqual(dest.name, "Pikeminnow_icm")
        acts = {e["rel"]: e["action"] for e in plan["entries"]}
        self.assertEqual(acts["analysis/fit.R"], "copy")
        self.assertEqual(acts["data/caps.csv"], "link")
        self.assertEqual(acts["out/model.rds"], "link")
        self.assertEqual(acts[".env"], "skip")
        self.assertEqual(acts["fig.png"], "skip")
        self.assertFalse(any(dest.rglob(".env")))
        self.assertFalse(any("caps.csv" in str(p) for p in dest.rglob("*") if p.is_file() and "manifest" not in p.name and "MIGRATION" not in p.name))
        self.assertEqual(icm_validate.validate(dest), [])
        self.assertEqual([c for c in icm_data.check(dest) if c["status"] != "ok"], [])
        (self.src / "data" / "caps.csv").write_bytes(b"a,b\n9,9,9\n")
        (self.src / "out" / "model.rds").unlink()
        st = {c["path"]: c["status"] for c in icm_data.check(dest)}
        self.assertEqual(st[str(self.src / "data" / "caps.csv")], "changed")
        self.assertEqual(st[str(self.src / "out" / "model.rds")], "missing")

    def test_guards_and_dry_plan(self):
        plan = icm_restructure.build_plan(self.src, "mark_recapture")
        self.assertEqual(list(self.root.glob("*_icm")), [])
        dest = icm_restructure.execute(plan, self.root, "Pikeminnow", folder="Pikeminnow_icm")
        with self.assertRaises(FileExistsError):
            icm_restructure.execute(plan, self.root, "Pikeminnow", folder="Pikeminnow_icm")
        with self.assertRaises(ValueError):
            icm_restructure.execute(icm_restructure.build_plan(dest, "mark_recapture"), self.root, "x", folder="y_icm")
        with self.assertRaises(ValueError):
            icm_restructure.execute(plan, self.src, "Pikeminnow", folder="inner_icm")


if __name__ == "__main__":
    unittest.main()
