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

// Minckley Library permissions: only "public domain" items have a freely hosted full PDF.
const PDF_BASE = "https://www.marsheducation.org/library/textpdf/";
const publicDomain = new Set();
const csvPath = path.join(agent, "brain_meta", "minckley_library.csv");
if (fs.existsSync(csvPath)) {
  const rows = parseCsv(fs.readFileSync(csvPath, "utf-8").replace(/^\uFEFF/, ""));
  const head = rows[0] || [];
  const iMid = head.indexOf("MID"), iPerm = head.indexOf("permission");
  for (const r of rows.slice(1)) if ((r[iPerm] || "").trim().toLowerCase() === "public domain") publicDomain.add((r[iMid] || "").trim());
}
const missingPath = path.resolve(here, "../pdf-missing.json");
const missing = new Set(readJson(missingPath).missing || []);

function parseCsv(t) {
  const rows = [];
  let row = [], f = "", q = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (q) { if (c === '"') { if (t[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c; }
    else if (c === '"') q = true;
    else if (c === ",") { row.push(f); f = ""; }
    else if (c === "\n") { row.push(f.replace(/\r$/, "")); rows.push(row); row = []; f = ""; }
    else f += c;
  }
  if (f || row.length) { row.push(f); rows.push(row); }
  return rows;
}

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
    pdfUrl: minckleyId && publicDomain.has(minckleyId) && !missing.has(minckleyId) ? `${PDF_BASE}${minckleyId}.pdf` : "",
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
console.log(`Wrote ${items.length} sources (${items.filter((i) => i.minckleyId).length} with Minckley IDs, ${items.filter((i) => i.pdfUrl).length} with public-domain PDFs) to ${path.relative(process.cwd(), out)}`);
