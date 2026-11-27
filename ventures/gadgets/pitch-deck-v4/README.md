# Gadgets pitch deck v4

Draft for Oscar's edit, built on 27 Nov 2026 from v3 (`../pitch-deck-v3/`, untouched). The flagship is the concept itself: one premium brand with a multi-category collection of decorations, gadgets and other objects for the home; no single hero product. The personal digest product is not in the collection and not in the deck. Gadgets is Oscar's solo project, so no slide names anyone else; the authors of the saved posts appear only as X handles in credit lines. No valuation, round size or equity. Private. Nothing here has been sent, shared or made public.

## What changed from v3

Oscar's ask: update the deck with the X inspiration in `../inspiration/` (29 saved posts with an image each, grouped by category, ending with a patterns section). v3's content, numbers and layout fixes are kept; the changes below are the whole difference.

1. **Slide 4, inspiration (new).** A moodboard of twelve of the 29 posts (the first image of each post, cropped to a 192x100 cell), each with its category, a one-line caption describing the object, and a credit line: X handle, post date, post URL and appendix number. Right column: the patterns in the 29 posts, each labelled an observation and never a market measurement, with the posts it rests on cited, and a count of posts by category. The lighting gap is stated as a gap in the saved material, not a statement about demand. Every one of the 29 posts is cited on this slide.
2. **Slide 3, the brand.** A thumbnail and a credit line beside each brand rule: the ceramic ashtray (rule 1, beautiful first), the bookcase with one small smart function (rule 2, smart only where it helps), the five promptable devices in one design language (rule 3, one family). Footer updated.
3. **Slide 5, the collection** (v3's slide 4). The e-ink display, the desk display and the wall aquarium carry "(saved post: slide 4)". The footer says no saved post shows lighting, so the light family rests on the 26 Nov catalogue decision, not on the posts.
4. **Slide 7, market funnel** (v3's slide 6). One tile, "What the saved posts add (observation)": the founder's two readings from the posts (these gadgets are made for tech people while the wider market is open; cheap hardware plus an app is what people buy), labelled as readings that leave the funnel's assumptions as assumptions. No market number changed.
5. **Slide 8, competition** (v3's slide 7). One table row (Inanimate: five promptable desk devices under one name, orderable; not researched; seen in one saved post) and one sentence in the gap card. Not placed on the map, where its position would be an invented score. The problem slide's cross-reference now points to slide 8.
6. **Appendix** (slides 12 to 17, 93 sources). The 29 posts are entries tagged "saved X post": handle, description, post date and URL. The intro paragraph says the posts were not re-opened for this build and that each date is decoded from the post id.
7. **Numbering and labels.** v3's slides 4 to 10 are now 5 to 11. Cover, footers, the plan row, the page title and the file headers say v4. No figure, chart or layout fix from v3 changed.
8. **Images.** `images/` holds the twelve post images the deck uses, named by post id, made by `prepare_images.py` from `../inspiration/images/`: a horizontal band at the cell ratio, resized to 384x200 px, nothing else changed. They are referenced by relative path, so `file://` rendering works. The images belong to their authors and are private reference, not for publication.
9. **Checks.** `check_deck.py` gained: no person's name from the inspiration list and no wording about who passed a post on; every `<img>` is a relative path to an existing file under `images/`; the page size is unchanged; 17 slides; slide 4 says "observation"; 29 post URLs in the appendix, and every image shown has one.
10. **Research.** `research.md` section 8: method, the twelve posts shown, the patterns and the posts behind them, the tie-ins, tags. Slide numbers in sections 1 to 7 now follow v4.

## Files

- `research.md`: every figure with URL, date and a tag (verified, snippet only, my arithmetic, assumption, opinion, placeholder; v4 adds "saved X post"). Sections 1 to 7 are v3's with v4 slide numbers. **Section 8 is new**: the saved posts.
- `deck.html`: 17 slides at 1280x720 px. Slides 1 to 11 are the pitch, 12 to 17 the numbered sources. System fonts, inline SVG charts, flat placeholder renders; the only external files are the twelve images in `images/`.
- `build_deck.py`: generates `deck.html`. All copy, numbers, chart data, the POSTS block (the 29 posts, the twelve featured, the patterns) and the source registry live here. Regenerate with `python3 -I build_deck.py` from this folder.
- `prepare_images.py`: makes `images/` from `../inspiration/images/`. Already run; run again with `python3 -I prepare_images.py` only if the crops change (needs Pillow).
- `images/`: the twelve post images, 384x200 px JPEG, named by post id.
- `check_deck.py`: the no-browser checks (below). Run with `python3 -I check_deck.py` from this folder.
- `deck.pdf`: not in this folder. **Innovator renders it** (command below). v3's PDF was not copied: it would be stale.

Slides: 1 cover; 2 problem and why now; 3 the brand; 4 inspiration; 5 the collection (nine objects, price ladder); 6 market by region; 7 market funnel; 8 competition; 9 business model; 10 plan; 11 founder and ask; 12 to 17 sources.

## Page size

The CSS page is 1280x720 px, which Chrome prints as 960x540 pt: the same page size as v3's `deck.pdf` (MediaBox 0 0 960 540). Keep both numbers as they are.

## Render the PDF (Innovator)

On the box, from `~/oscar-hq`:

```
google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=ventures/gadgets/pitch-deck-v4/deck.pdf --virtual-time-budget=4000 file:///home/box/oscar-hq/ventures/gadgets/pitch-deck-v4/deck.html
```

The `file://` URL matters: the images are relative paths. Then look at slides 3, 4, 5, 7 and 8 (the ones v4 touched) and the six source pages.

## Checks run without a browser

`python3 -I check_deck.py`: every SVG parses; no chart label runs outside its SVG, overlaps another label, or sits on a solid bar (widths estimated from character counts: 0.54 em regular, 0.58 em bold or serif); no short vertical leader line crosses a label; no em dash; none of the banned names, places or topics (the list is in `check_deck.py`: the digest product, the founder's day job and its industry, the people named in the inspiration list, wording about who passed a post on); valuation, round size and equity appear only in the lines saying they are off the table; every image exists under `images/` by a relative path; page size 1280x720 px; 17 slides; slide 4 says observation; 29 post URLs in the appendix. All passed on this build. Not covered: text overflow in the HTML blocks (the moodboard cells, the rule cards, the funnel tile, the competition table, the footers) and the real rendered widths. **A visual check of the rendered PDF is still to do**, especially slide 4 (two-line captions and credit lines in the cells, the right column's height), slide 3 (rule cards with thumbnails), slide 8 (table height with the added row) and the source pages (pagination is estimated).

## Placeholders and assumptions

Placeholders (marked `[placeholder]`): brand name, object renders, prices per object (due Sat 28 Nov), unit cost and MOQ, founder surname, photo, education and languages, team plan. Dates after December on the plan slide are proposals.

Invented for the deck and flagged on the slides: two decor objects, three brand rules, the plan rows after December; the funnel's 10% premium share, 1% to 3% capture and EUR 120 a year per customer; the regional assumptions of v3 (GMI's 42.5% non-furniture share, 41.5% online share and 29.2% premium share applied to every region, the gadget regional splits, and the 19% EU home-item rate applied to the world).

Observations, not measurements: every pattern on slide 4 and every tie-in sentence from the saved posts. They come from what the founder saved on X between 11 Aug and 26 Nov 2026 and say nothing about market size or demand.

Unverified (starred): Statista's narrow US$133.6bn segment, DataReportal's 56.2% weekly online buyers, the 2.2 billion world households (secondary page citing UN DESA), and v2's snippet-only items. The 29 posts were not re-opened for this build.

Style: any style for now, Oscar restyles later. Warm paper background, one accent (lacquer red), serif headings, system sans body, hairline grid, flat object drawings in wood tones, photographs only on slides 3 and 4.
