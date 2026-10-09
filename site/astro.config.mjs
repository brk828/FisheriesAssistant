import { defineConfig } from "astro/config";

// For GitHub Pages: https://<user>.github.io/<repo>/. Override with SITE_URL / SITE_BASE (use "/" for a custom domain).
export default defineConfig({
  site: process.env.SITE_URL || "https://brk828.github.io",
  base: process.env.SITE_BASE || "/FisheriesAssistant",
  trailingSlash: "always",
});
