---
title: "Fix index.html: cleanup CSS, improve images and accessibility"
labels: "automated,needs-review"
assignees: ""

---

This pull request applies the following changes to index.html on branch `fix/index-html-errors`:

- Replace hard-coded white backgrounds with theme variable `var(--bg-raised)`.
- Consolidate and move inline styles into the stylesheet.
- Add `.hidden` and `.placeholder` classes to manage image fallbacks and visibility.
- Show placeholder until image onload, reveal high-res download link only after successful load.
- Add `loading="lazy"`, basic `srcset`/`sizes` attributes for images to improve performance.
- Avoid duplicate `h1` headings: biography uses `h2` when rendered as a section.
- Minor JS safety checks in image handlers.

Testing performed:
- Manual checks of Home / Obra / Biografía views: placeholders, onload behavior, hires link visibility, theme toggling.

Suggested next steps:
- Consider adding WebP / multiple resolution images in `srcset` and server-side support.
- Move remaining small inline styles into CSS (if desired) and add visual regression tests.
