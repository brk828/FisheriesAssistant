// Reads the vault summaries and citation files from fisheries_agent and writes src/generated/sources.json.
// Mirrors the citation lookup in fisheries_agent/utils/brain_citations.py (id, then MID, then filename MID, then filename).
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";

const here = path.dirname(fileURLToPath(import.meta.url));
const agent = path.resolve(here, "../../fisheries_agent");
const sourcesDir = path.join(agent, "00_Fisheries_Brain", "01_Sources");
const readJson = (p) => (fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf-8")) : {});
const refs = {
  ...readJson(path.join(agent, "brain_meta", "external_citations.json")),
  ...readJson(path.join(agent, "brain_meta", "citations.json")),
};

const midFromId = (v) => (String(v || "").match(/^\s*(\d+)/) || [])[1] || "";
const midFromStem = (s) => (s.match(/_(\d{5,6})$/) || [])[1] || "";
const lookup = (id, stem) => refs[id] || refs[midFromId(id)] || refs[midFromStem(stem)] || refs[stem] || {};

function parseFrontmatter(text) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!m) return [{}, text];
  const fm = {};
  let key = "";
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z_][\w]*):\s*(.*)$/);
    if (kv) { key = kv[1]; fm[key] = kv[2]; }
    else if (key && line.trim()) fm[key] += " " + line.trim().replace(/^-\s*/, "; ");
  }
  for (const k of Object.keys(fm)) {
    fm[k] = fm[k].replace(/[\[\]"]/g, "").replace(/#/g, "").replace(/\s+/g, " ").replace(/^[;\s]+/, "").trim();
  }
  return [fm, text.slice(m[0].length)];
}

function citationText(ref, title, mid) {
  const pub = ref.publication ? ` ${ref.publication.replace(/\.$/, "")}.` : "";
  const tail = ref.type === "Personal Communication" ? " (personal communication)." : pub;
  const head = ref.authors
    ? `${ref.authors} (${ref.year || "n.d."}). ${title}.`
    : `${title} (${ref.year || "n.d."}).`;
  return head + tail + (mid ? ` Minckley Library ID: ${mid}.` : "");
}

function cleanBody(body) {
  return body
    .replace(/^\s*(#[\w-]+[ ,]*)+\s*$/gm, "") // hashtag-only lines
    .replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, "$2")
    .replace(/\[\[([^\]#|]+)(?:#[^\]]*)?\]\]/g, "$1");
}

const used = new Set();
const slugify = (stem) => {
  let s = stem.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "source";
  let out = s, n = 2;
  while (used.has(out)) out = `${s}-${n++}`;
  used.add(out);
  return out;
};

const items = [];
for (const file of fs.readdirSync(sourcesDir).filter((f) => f.endsWith(".md")).sort()) {
  const stem = file.replace(/\.md$/, "");
  const [fm, body] = parseFrontmatter(fs.readFileSync(path.join(sourcesDir, file), "utf-8"));
  const ref = lookup(fm.source_id, stem);
  const sid = String(fm.source_id || "");
  // Minckley Library notes carry a numeric source_id (or minckley_id); other libraries use "X-<hash>".
  const minckleyId = fm.minckley_id || (sid.startsWith("X-") ? "" : midFromId(sid) || midFromStem(stem));
  const title = ref.title || fm.title || stem;
  const year = (ref.year || (fm.date_published || fm.date || "").slice(0, 4) || "").toString();
  const doi = ref.doi || fm.doi || "";
  items.push({
    slug: slugify(stem),
    title,
    authors: ref.authors || "",
    year: /^\d{4}$/.test(year) ? year : "",
    publication: ref.publication || "",
    type: ref.type || "",
    doi,
    minckleyId,
    species: fm.common_name || fm.species || "",
    location: fm.location || "",
    citation: citationText(ref, title, minckleyId),
    hasCitation: Boolean(ref.title || fm.source_citation),
    html: marked.parse(cleanBody(body)),
  });
}

const out = path.resolve(here, "../src/generated/sources.json");
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify(items));
console.log(`Wrote ${items.length} sources (${items.filter((i) => i.minckleyId).length} with Minckley IDs) to ${path.relative(process.cwd(), out)}`);
