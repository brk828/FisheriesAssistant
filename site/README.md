# Fisheries Library Search site

Static Astro site that searches the AI-generated summaries in `fisheries_agent/00_Fisheries_Brain/01_Sources`.
Search runs in the browser (Pagefind); there are no concept stubs or server. Results show citations first; clicking one opens the full summary.

- `npm run build` reads the vault and the citation files, generates one page per source, builds the site, and indexes it (about 30 s for ~3,000 notes). Output is `dist/`.
- `npm run dev` regenerates the data and starts the dev server. Search needs the Pagefind index, so run `npm run build` once first, then use `npm run preview`.
- `scripts/build-data.mjs` mirrors the citation lookup in `fisheries_agent/utils/brain_citations.py` (sheet citation, then external, matched by id, MID, filename MID or filename). Minckley documents show their Minckley Library ID; other documents show the full citation and a DOI link when known.
- Edit wording (title, blurb, how to request a PDF) in `src/config.ts`.
- Deploys to GitHub Pages through `.github/workflows/deploy-site.yml` on pushes to `main` that touch the site, the summaries or the citation files. In the repo settings, set Pages > Source to "GitHub Actions". `SITE_URL` / `SITE_BASE` (default `https://brk828.github.io` and `/FisheriesAssistant`) change the address.
- Pages from a private repository needs a paid GitHub plan, and the published site is public either way.
