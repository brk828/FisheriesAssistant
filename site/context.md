# Site context: Minckley Library Search

Read this before fixing or changing anything on the website. For commands and deployment notes see [README.md](README.md).

## What it is
A static [Astro](https://astro.build) site (Astro 7, `marked` for Markdown, Pagefind for search) that publishes the AI-generated summaries in `fisheries_agent/00_Fisheries_Brain/01_Sources`. There is no server. Search runs in the browser. Results show the citation first; clicking one opens the full summary page.

## Data flow
1. `scripts/build-data.mjs` (`npm run prepare-data`) reads, from `../fisheries_agent`:
   - `00_Fisheries_Brain/01_Sources/*.md` (summary notes with YAML frontmatter)
   - `brain_meta/citations.json` and `brain_meta/external_citations.json` (citations; the sheet citation wins over the external one)
   - `brain_meta/minckley_library.csv` (the `permission` column)
   It writes `src/generated/sources.json` (git-ignored, regenerated each build). Citation lookup mirrors `fisheries_agent/utils/brain_citations.py`: id, then MID, then filename MID, then filename.
2. `scripts/verify-pdfs.mjs` HEAD-checks the public-domain PDF links and records 404s in `pdf-missing.json` (committed). `build` runs prepare-data, verify-pdfs, then prepare-data again so missing PDFs are dropped.
3. `astro build` renders one page per source, then `pagefind --site dist` indexes `dist/`.

## Files
| File | Role |
|---|---|
| `src/config.ts` | Site title, blurb, and request-a-PDF text. Edit wording here. |
| `src/layouts/Base.astro` | Page shell: global CSS (color variables), header, footer disclaimer. |
| `src/pages/index.astro` | Search page: search box, filters, sort, "Show more". Search logic is an inline script that loads `pagefind/pagefind.js` from `BASE_URL`. |
| `src/pages/source/[slug].astro` | One summary page per source, built from `sources.json`. Holds the Pagefind attributes. |
| `scripts/build-data.mjs` | Builds `sources.json`; item fields are slug, title, authors, year, publication, type, doi, minckleyId, pdfUrl, species, location, citation, hasCitation, html. |
| `scripts/verify-pdfs.mjs` | PDF link checker (`--strict` option). Network errors never mark a PDF missing. |
| `pdf-missing.json` | MIDs whose PDF returned 404. Remove an entry once the PDF is uploaded. |
| `astro.config.mjs` | `site` and `base` from `SITE_URL` / `SITE_BASE` (defaults `https://brk828.github.io`, `/FisheriesAssistant`). |

## Design rules
- **Search state:** query, filters and sort are mirrored into the URL query string (`q`, `library`, `decade`, `fullpdf`, `sort`) and restored on load; the summary page's "Back to search" link calls `history.back()` when the visitor came from the site. Results open in the same tab.
- **Search filters** (set on the `<article>` in `[slug].astro`, read in `index.astro`): `library` (Minckley Library or Other sources, based on whether the note has a Minckley ID), `decade`, `fullpdf` (Available / Not available). Sort key: `year`. A new filter needs changes in both files.
- **Minckley vs other documents:** Minckley notes show their Minckley Library ID. Others (source_id like `X-<hash>`) show the full citation and a DOI link when known.
- **PDF links:** only Minckley items with `permission = public domain` get a link to `https://www.marsheducation.org/library/textpdf/<MID>.pdf`, unless listed in `pdf-missing.json`. Everything else shows the request-a-PDF text.
- **Cleanup of note bodies:** hashtag-only lines are removed and Obsidian `[[wikilinks]]` become plain text. There are no concept stubs.
- **Style:** plain system font, blue accent (`--accent:#0b5d7a`), max width 56rem, no UI framework. Every page carries the footer warning that summaries are AI-generated.
- **URLs:** always build links from `import.meta.env.BASE_URL` (the site lives under `/FisheriesAssistant`).

## Deployment
`.github/workflows/deploy-site.yml` builds (Node 22, `npm ci`, `npm run build` in `site/`) and publishes `site/dist` to GitHub Pages on pushes to `main` that touch `site/**`, the summaries, the two citation JSON files, or the workflow. The published site is public.

## Common fix checklist
- Wrong or missing citation: fix it in `fisheries_agent/brain_meta` (not in the site), then rebuild.
- Wording change: `src/config.ts`.
- Layout or styling: `Base.astro` (global) or the page's own `<style>`.
- Search behavior: the script in `index.astro`; verify with `npm run build` then `npm run preview` (dev mode has no Pagefind index until a build has run).
