// Checks that every ingested public-domain Minckley or Marsh Library item has a PDF on marsheducation.org.
// Writes site/pdf-missing.json (read by build-data.mjs, which then omits those links) and
// exits non-zero with --strict when any are missing. Network errors never mark a PDF missing.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const items = JSON.parse(fs.readFileSync(path.resolve(here, "../src/generated/sources.json"), "utf-8"));
const urls = new Map(items.filter((i) => i.pdfCandidate).map((i) => [i.pdfKey, i.pdfCandidate]));
const out = path.resolve(here, "../pdf-missing.json");
const prev = new Set((fs.existsSync(out) ? JSON.parse(fs.readFileSync(out, "utf-8")).missing : []) || []);

// Re-check everything that is public domain, including links previously dropped.
const candidates = [...urls.keys()];
const unique = [...new Set(candidates)];

const missing = [], errors = [];
let idx = 0;
async function worker() {
  while (idx < unique.length) {
    const mid = unique[idx++];
    try {
      const r = await fetch(urls.get(mid), {
        method: "HEAD",
        headers: { "User-Agent": "Mozilla/5.0 (FisheriesAssistant pdf check)" },
        signal: AbortSignal.timeout(20000),
      });
      if (r.status === 404 || r.status === 410) missing.push(mid);
      else if (!r.ok) errors.push(`${mid}: HTTP ${r.status}`);
    } catch (e) {
      errors.push(`${mid}: ${e.message}`);
    }
  }
}
await Promise.all(Array.from({ length: 8 }, worker));

missing.sort();
fs.writeFileSync(out, JSON.stringify({ missing }, null, 2) + "\n");
console.log(`Checked ${unique.length} public-domain PDFs: ${missing.length} missing, ${errors.length} unverifiable.`);
if (missing.length) console.log("Missing:", missing.join(", "));
if (errors.length) console.log("Unverifiable:", errors.join("; "));
if (missing.length && process.argv.includes("--strict")) process.exit(1);
