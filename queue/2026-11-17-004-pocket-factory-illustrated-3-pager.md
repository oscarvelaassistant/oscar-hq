---
id: 2026-11-17-004
title: Pocket Factory illustrated 3-page PDF with pixel-art drawings and flowcharts
role: cofounder
priority: P1
status: done
created: 2026-11-17
created_by: Innovator, from Oscar in chat (21:25 Madrid, 17 Nov)
due: 2026-11-18
effort: high
approval: Oscar asked for it in chat ("use claude to make a 3 page illustrative with images, flowcharts, and pretty non-slop"); research and design only
---

## Goal
A 3-page illustrated PDF that explains Pocket Factory and shows what it could look like. Oscar may attach it to his Powerhouse application or send it to Ryan Dunwoody and future programmes, so it must impress a hardware founder.

Oscar's words: "images, flowcharts, and pretty non-slop (i'd love some claude making drawings in like 64-bit showing what the pocket factory could look like)". Read "64-bit" as retro pixel art (crisp 16-bit console style); Claude draws them itself, as SVG or HTML canvas pixel grids, no stock images, no generic AI art.

## HARD RULE from Oscar (21:28, 17 Nov)
No ships, no shipyard, no naval, no forward sites, no deployable factories, no US Navy budget line anywhere: Oscar told us to drop the ship focus. First use stays general: making parts without skilled hands; arms are cheap and open now, the skills are not. Page 3 panels: a cell on a workbench, many cells in a small workshop, cells sharing skills.

## Oscar's framing (21:30, 17 Nov), use this as the spine
The machine is called Artisan (Oscar's name, 14 Nov voice memo). Artisan is an AI factory worker, an artisan you can set down anywhere in the world, or one day on another planet, give raw material, and it does anything a team of skilled workers could do: two open arms that pick up any tool (cut, solder, machine, assemble, check). Inspiration: Warhammer STCs, a Shenzhen factory in a pocket (13 Nov voice memo, vault 🎙️ Transcripts/2026-11-13 - Pocket Factory voice memo.md). Every skill one Artisan learns, every Artisan gets. Pixel art: Artisan at a workbench; Artisan in a remote town workshop; Artisan in a dome on another planet; many Artisans sharing skills. Do not use Oscar's 'Africa' or Rhodesia wording; say remote places.

## Pages
1. What it is: a hero pixel-art drawing of the cell (a workbench with two open robot arms, stock rack, a machining or finishing station, an inspection camera, an output tray with an accepted part), plus the one-line idea and the first use (repair parts at the point of need, on ships and at forward sites).
2. How it works: a flowchart of the loop (file or request in, bar stock picked, held, machined, finished, checked, accepted or rejected and retried, part out) with small pixel icons per step, and the layer that is ours: the learned skill library and the factory process on off-the-shelf open arms (Seeed reBot-DevArm, open since May 2026).
3. The vision and the ten weeks: pixel-art panels of where it goes (a cell on a ship, a cell in a container at a forward site, many cells sharing skills: "every skill one cell learns, every cell gets"), and the ten-week Powerhouse goal: one loop working and filmed, one material, one process, one family of parts, or an agreed subsystem.

## Context and sources
- Facts only from `ventures/pocket-factory/powerhouse-message.md`, `powerhouse-application.md`, `plan.md`, `market-map.md`. Every number on the page carries its source in a footer (e.g. USD 196.585M Navy FY2026 line).
- Drawings are illustrations of a concept, labelled "concept" so nobody reads them as a built product.
- ARESA is never named.

## Done when
`ventures/pocket-factory/illustrated/pocket-factory-3pager.pdf` (A4, exactly 3 pages) plus its HTML source and the pixel-art files, pushed. Render the PDF and look at every page as an image before pushing; fix overflow, clipped text and unreadable art. Report the path.

## Style rules
Oscar's rules: no em dashes ever, no estimates (label any as one), plain English, short sentences. Non-slop: no "revolutionary", no lists of three adjectives, no gradients-and-emoji look, generous white space, one accent colour, pixel art as the visual signature.

## Gates
Design only. Nothing sent, no account, no spend.

## Log
- 2026-11-17 21:26 filed by Innovator.
- 2026-11-17 21:50 done by the wake-3 run: `ventures/pocket-factory/illustrated/pocket-factory-3pager.pdf` (A4, 3 pages), with `build.py`, `art.py`, `art/` and `preview/`. Every page checked as an image; pypdf confirms 3 pages at 210 x 297 mm, a selectable text layer, and none of the excluded words. Deviations: the source is Python, not HTML, because Chrome and the PDF tools are blocked by `.claude/settings.json` in a run; pages are 336 dpi images with a text layer. The hard rule and Oscar's framing override the older Pages section above (no ships, no forward sites, no Navy line). Two flags in the report: the name Artisan is also a Snapmaker product, and the arm's payload and reach figures need a check against the arm's page.
