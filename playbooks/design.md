# Design work

Use this for anything visual: decks, one-pagers, posters, documents, sheets, UI mockups.
Approved by Oscar on 1 Nov 2026.

## Tools and formats

Oscar's ArtCraft suite (https://getartcraft.com/apps, code at https://github.com/storytold) opens and polishes the files you write.

- Cloud runs cannot run ArtCraft. Write open formats the apps open later:
  - SVG for illustration and diagrams (VectorCraft, FigCraft)
  - `.pptx` for decks (DeckCraft)
  - `.docx` or `.md` for documents (WordCraft)
  - `.xlsx` or `.csv` for data (GridCraft)
  - IDML for page layouts (DesignCraft)
- Save design files next to the task output, with a short note of what each file is for.
- Vela can render, check or convert them with ArtCraft on her box (`/home/box/apps/artcraft`, CLIs and MCP servers for every app). Ask for a render in your report when a visual check matters.
- On Oscar's Mac, Claude Code can drive the apps directly once their CLIs are set up there.

## Principles (no AI slop)

- Typography first. Pick one or two typefaces on purpose, set a clear size scale, and let type carry the hierarchy.
- Restraint. One accent colour, plenty of white space, fewer elements. Cut anything that does not help the reader.
- No default gradients, glows, glassmorphism, stock 3D blobs or emoji as decoration.
- A real grid. Fixed margins and columns, aligned edges, consistent spacing steps.
- Content decides the layout. Real data and real copy, never lorem ipsum or invented numbers.
- Check it as an image before calling it done: render it, look at it, fix what looks off.

## Skills

Skills live in `.claude/skills/` (see its README):

- `frontend-design`: UI and web pages that do not look templated.
- `canvas-design`: posters and static visual pieces as PNG or PDF.
- `theme-factory`: colour and font themes to apply to decks, docs and pages.

For `.pptx`, `.docx`, `.xlsx` and PDF files, use Anthropic's document skills where your environment provides them (claude.ai has them built in; Claude Code installs them with `/plugin install document-skills@anthropic-agent-skills`). Their licence does not allow copies in this repo.
