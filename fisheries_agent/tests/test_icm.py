import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from utils import gitsync, icm_git, icm_scaffold, icm_validate, icm_wizard


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
                   "report", "1", "", "n", ""]
        name, agents, has_git, issues = self.run_wizard(answers, llm=lambda p: "## Project\nLLM routing text.")
        self.assertEqual(name, "Chub_MR_2024_icm")
        self.assertIn("LLM routing text.", agents)
        self.assertIn("R and Quarto", agents)
        self.assertFalse(has_git)
        self.assertEqual(issues, [])

    def test_git_option_and_cancel(self):
        answers = ["P", "g", "s", "d", "mark-recapture", "r", "1", "",
                   "y", "*.tif", "raw_downloads/", "20", "y"]
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


if __name__ == "__main__":
    unittest.main()
