# Pocket Factory: is there something here, what to chase first

Reworked 2026-11-16 from Oscar's notes on the 13 Nov version. The old version is in git history (last old version: commit 23da7ed). Status: thinking only. Nothing here is bought, contacted, signed up for or published. Opinions are marked as mine. Where I could not verify something I say so.

## 1. Where Oscar is

- He has the idea. There seems to be demand. He is at step 1: refine the idea.
- His path: vision, a bit of work done, a pitch deck, investment, quit his job, find an engineer cofounder (LinkedIn, X or in person).
- Uses no ARESA resources, contacts, customers or yard for any of this.
- The market is the whole world, eventually. Europe is not the only one.
- The goal right now is to explore: does it have potential, what final form could it take, what is the immediate roadmap.

His own words for the idea (voice memo, 13 Nov, https://web.plaud.ai/s/pub_37a79fe3-22f4-4f8c-ac54-3d77316d87fb): "a miniature garage that's run with AI," "two arms that can basically connect to any tool," "you just throw it the raw materials in it," "a Shenzhen factory in a pocket." Where it could go: ships to new planets, and places where people "can't build anything themselves." At the start: "anything you can do kind of like in a workbench."

## 2. Does it have potential? (my opinion, with the facts under it)

My view: yes, enough to keep exploring. It is not proven, and I could not size the world market outside defence.

Facts:
- Money is already spent on making parts where the part is needed. The US Navy's FY2026 budget has a 196.585M USD line for afloat and deployable manufacturing (https://www.highergov.com/budget/navy-advanced-manufacturing-5483f47). A US Defense programme awarded 30M USD in May 2026 for five containerised print cells (https://www.tectonicdefense.com/exclusive-firestorm-snags-30m-apfit-contract/).
- Every deployable factory sold today comes with trained people: two engineers in the US Army container (https://singularityhub.com/2013/02/28/3d-printing-on-the-frontlines-army-deploying-2-8m-mobile-fabrication-labs), a 15-day operator course for SPEE3D (https://www.spee3d.com/metal-parts-on-the-frontlines-spee3ds-impact-on-ukrainian-military-operations/).
- Desktop fabrication machines have no hands, and robot cells assemble parts someone else made (`market-map.md`, section 4). I found no product that closes the loop with nobody inside.
- The paid buyers I found are mostly US and UK armed forces. That says nothing about the rest of the world either way: I found no evidence, so I don't know.

MicroFactory has the same far-off vision (factories on other planets). My view: that does not hurt. Anyone can state the vision, and NASA did not stop SpaceX; the pie is big enough for several players. What matters is what each one ships first. MicroFactory ships a boxed one- or two-arm assembly cell, from 11,950 USD (https://microfactory.com/), raised 1.5M USD pre-seed (https://techcrunch.com/2025/09/16/this-30m-startup-built-a-dog-crate-sized-robot-factory-that-learns-by-watching-humans/), and its cell handles parts the customer supplies (`microfactory-catalogue.md`).

Europe: most funded players in `market-map.md` are American. Europe has some (Theker, Barcelona, 85M USD Series A, https://tech.eu/2026/06/11/barcelona-based-ai-robotics-outfit-theker-raises-85m/; Sunrise Robotics, 8.5M USD seed, https://tech.eu/2025/06/13/sunrise-robotics-emerges-from-stealth-with-85m-to-democratise-factory-automation/). Being behind at home does not limit where he sells.

Market sizing: `report.md`, section 3, with every estimate labelled there. Its section 8 recommends a wedge through the yard; that no longer applies.

## 3. Final form (his picture, my reading)

A small box you put raw material into and ask for something; it makes it, checks it, hands it over, anywhere, with no skilled person needed. What travels is the knowledge, like the Warhammer STC he described. How big the box is and how many tools it has are open. I am not designing any of that now.

**Any material as the end goal (Oscar, 16 Nov, 14:48).** His words: "ultimately it'd be great to have it be anyfactory (unless that's just not practical or maybe I gotta start with something else first)." Wood and plastic were only ideas for a first material.

Is it practical? My opinion: as a direction, yes. As a literal "anything", not as written, and I know of no product that does it.
- Machines that do several processes already exist, so widening is real engineering, not fantasy. The Snapmaker Artisan combines an FDM printer, a 10 W laser and a 200 W CNC in one machine (https://matterhackers.com/r/H534oP, list price 2,999 USD). The Marine Corps AIMMS shelter fields CNC, welding, scanning and hybrid metal printing (https://www.navsea.navy.mil/Media/News/Article/4511482/carderock-supports-marine-corps-new-mobile-manufacturing-capability-for-forward/).
- Both still need a trained person to move the part and the material (`market-map.md`, section 4). Each new material brings its own process, tool, feed and finishing, so "any" gets built one process at a time. It does not arrive in one go.
- "Anything from raw material" has a ceiling that I believe is real but did not source: parts like chips or batteries cannot be made from raw stock in a small box, so soldering means buying components. That is a limit on "anything", not on a very wide workbench.

Sensible first step (my opinion): start with one material, and treat it as the way into any-material, not the destination. The part to build once and reuse is the operator: read the request, plan the job, make the part, check it, redo it. The tools and materials are what change from one to the next. Whether the checking step transfers across materials I do not know; that is the thing the first material would teach. The second material comes after the first loop works.

## 4. The MVP to chase (my opinion)

**One material, one way of making, one family of parts, with nobody touching anything between request and accepted part.** The request is text or a photo of a broken part. The box makes the part, checks it, and either hands it over or redoes it.

Why this is the Pareto version:
1. It is the one thing in the gap above that nobody ships. Everything else in the idea (more tools, soldering, bigger parts, remote places) is worth only as much as this loop works.
2. Narrowing the material and the process is what makes it testable. Something like "it made 17 of 20 parts of one family and the check caught the other 3" (an invented example) is a statement an investor or an engineer can judge. "It builds anything" is not.
3. It is what a pitch deck and an engineer cofounder can react to. HAX lists "concept stage without a working prototype" and "a sole founder working with contracted engineers" among its rejection reasons (https://hax.co/faq/). I found no investor who says a simulation alone is enough at pre-seed (`report.md`, section 7).

Left out on purpose: soldering, many tools, big parts, shipping it anywhere. Those are the vision, not the first thing. The first material is the way into the any-material end goal in section 3, not a replacement for it.

## 5. Side question: just wood, or just plastic?

Oscar's 16 Nov follow-up: these two were only ideas and the end goal is any material (section 3). This section only helps pick the first one. Short answer (mine): yes to starting with one material, it is the same Pareto move as above. Whether either is "still big" I do not know: I found no sizing of either for this kind of box. Between the two I would start with plastic.

**Wood.**
- For: the material is local in many places, and cutting sheet on a CNC router is a mature process. WikiHouse works this way: "locally sourced plywood cut on a CNC mill from openly shared template files," assembled "with minimal skill by local people" (https://makezine.com/article/home/wikihouse-open-source-home-building/). In a quick search I found no confirmed WikiHouse build in Africa.
- Against: local makers already supply about 70 percent of the furniture market in Africa, and about 32 percent is imported (CSIL report, March 2019, https://www.worldfurnitureonline.com/news/status-and-prospects-of-the-furniture-industry-in-africa/; the import value, about 3B USD, is for 2017 and covers all furniture, not the market for this box). A drop-in woodshop sells against carpenters who already exist. Its edge would be precision and repeatable copies from a drawing; that is my guess, not something I measured.
- A router that takes a 4 by 4 ft sheet is not pocket-sized (Shapeoko 5 Pro, 4,069.89 USD at a reseller, https://www.robotshop.com/products/carbide-3d-shapeoko-5-pro-4x4-cnc-router-w-compact-router).
- Cutting is already automatic. What a person still does is load sheets, change bits, clamp and sand. That is the same missing-hands problem as the general idea, so wood does not remove the hard part.
- Value per part is low (my opinion; no number).

**Plastic (3D printing).**
- For: the smallest, cleanest and cheapest machine (Prusa MINI+, 509 EUR, https://www.prusa3d.com/category/original-prusa-mini/), no dust, and the demand evidence above is mostly spare parts in plastic and metal. US Marines printed a Coast Guard boat strainer for 12 USD (https://3dprintingindustry.com/news/marine-corps-x-fab-saves-coast-guard-patrol-boats-253447/).
- Against: in remote places the filament may itself be the thing that is not there (my reasoning, not sourced). Printed parts are weaker and slow to make. Past some volume moulding wins: one printer maker puts the crossover at 13,050 parts for its example (https://formlabs.com/global/blog/race-to-1000-parts-3d-printing-injection-molding/), a mould maker at 100 to 500 (https://zetarmold.com/?p=51571). The sources disagree because the part and tooling assumptions differ. Printing fits one-offs and spares, not volume.

My pick, plastic first: the simplest machine, the clearest paid demand, and the loop is easiest to close. Wood is the better story for "build locally from local material," but weaker on demand evidence. If that story is what pulls him, wood is the honest alternative. The material does not have to be final: the product is the operator, and the first material is only where it proves itself.

## 6. Immediate roadmap, on his path

1. **Vision (now).** One sentence: who gets the first box and what it makes for them. This file gives him the MVP and the material question to answer it with. This is the step he is on.
2. **A bit of work done.** The simulated demo he asked for on 13 Nov (step 3 of `ventures/_company/cofounder/roadmap.md`). It should show the MVP loop in section 4 and nothing more. No spend.
3. **Pitch deck.** After the vision sentence and the demo. Competitors with MicroFactory first.
4. **Investment.** Oscar contacts investors himself. Assistants prepare lists and drafts only when he asks.
5. **Quit the job** only once an investor is interested.
6. **Engineer cofounder** (LinkedIn, X, in person). My opinion: start these conversations alongside the deck, not after the money, because the investor evidence above asks for a builder on the team. His call.

## 7. Open question for Oscar

- Is the vision sentence "an any-material factory, starting with one material", with the first material (plastic, wood or another) left open until he has slept on it?
