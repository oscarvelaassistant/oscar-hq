# Pocket Factory: Claude's view and a macro roadmap

Written 2026-11-13 by the wake run (task 2026-11-13-001, HUB note 20261113090143597-87c0b317 via Vela, D-011). Status: plan only. Nothing here has been bought, contacted, applied for or published. Oscar asked for a realistic roadmap, so durations are included and every one of them is my estimate. Prices are quoted with the URL next to them or marked unknown. Opinions are labelled as mine.

Source read in full: `ventures/pocket-factory/transcript-2026-11-13.md` (4 min 36 s, https://web.plaud.ai/s/pub_37a79fe3-22f4-4f8c-ac54-3d77316d87fb).

## 1. What Oscar said, in his words

- "I want to build things." The next frontier of building things is Shenzhen; software is "solved just by LLMs."
- The product: "a miniature garage that's run with AI," "two arms that can basically connect to any tool," "you just throw it the raw materials" and "it's just gonna build you whatever." An STC from Warhammer: the knowledge travels with the box.
- Reach: spacecraft to new planets, and places without local manufacturing. Start: "cutting plants or soldering stuff," anything you can do on a workbench. Next: flesh it out, then look for investment.
- Underneath it: "I just want my success to not be tied to any one country, organization."

## 2. What I think (my opinion)

The kernel is right, and its timing is right. A workshop was never short of machines; it was short of the skilled person who knows which tool, which order, which tolerance. In the last eighteen months that person started becoming software: Physical Intelligence released the weights of its π0.5 generalist policy under Apache 2.0 (https://github.com/Physical-Intelligence/openpi), Google DeepMind's Gemini Robotics 1.5 reasons in language before acting and transfers motion across robot bodies (https://arxiv.org/abs/2510.03342), and Hugging Face's SmolVLA runs on a 3D-printed arm whose parts cost about a hundred dollars (https://huggingface.co/blog/smolvla, https://huggingface.co/docs/lerobot/so101). Oscar's "connect it to AI and it builds you whatever" is no longer science fiction. It is a product category forming right now.

Three things I would change, said once.

1. **The Africa framing is wrong, and it would hurt him.** "These people just can't build anything themselves" is false. Suame Magazine in Kumasi is an informal manufacturing cluster on which over 200,000 livelihoods depend, doing metal cutting, welding, machining, spare parts and small-scale manufacturing (https://openair.africa/skills-development-knowledge-and-innovation-at-suame-magazine-kumasi/). Gearbox in Nairobi runs 20,000 square feet of metal, wood, plastics and electronics equipment (https://www.lemelson.org/gearbox/). What those places lack is not the ability to build. It is precision, repeatability, drawings and skilled hours. Those are exactly what a pocket factory sells. The honest and stronger pitch is "for places that already build, slowly and by hand." Said once, and the Cecil Rhodes line stays out of every deck and every interview; it is an unforced error with any investor, partner or officer.

2. **General-purpose first is the capital trap.** The "brain for any robot" layer is already a war between companies with billions: Skild AI raised 1.4 billion USD at a 14 billion valuation in January 2026 (https://pulse2.com/skild-ai-1-4-billion-funding/), Physical Intelligence 600 million at 5.6 billion in November 2025 (https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding). Oscar has a venture hour and no API budget. He cannot win there and does not need to: those companies release their weights and need exactly what he can produce, a domain, its tasks, its data and a customer who pays per finished part. The pocket factory is the library of tasks, not the arms.

3. **His insider knowledge is the shipyard, and he is not using it.** Aresa in Arenys de Mar builds aluminium and composite vessels up to 60 m, patrol boats for navies and police (https://www.naval-technology.com/contractors/patrol/grup-aresa-internacional/). A shipyard is the clearest "factory that makes one of everything" on Earth: low volume, high mix, bench work by skilled fitters. Robot welding is entering yards now, from Austal's WeCobot for aluminium and steel (https://www.defenceconnect.com.au/industry/18483-austal-rolling-out-wecobot-robotic-welding-systems-for-henderson-shipyard) to Comau and Fincantieri's MR4WELD, pitched as an answer to the welder shortage (https://control.com/news/comau-and-fincantieri-team-up-to-create-a-ship-building-robot/). The first pocket factory is a bench cell that does one fitter's task in a yard. That is Shenzhen in a box for the place Oscar already stands in every day.

Against his own record (`roles/cofounder.md`: closed ventures were software too easy to copy, work that bored him, missing insider knowledge): this is hardware, it will not bore him, and the insider knowledge is there only if the wedge is the yard. It is also the third new idea in three days (drone 11 Nov, Digest 12 Nov, Pocket Factory 13 Nov). Cofounder already challenged that once; I will not repeat it, except to say the roadmap below only works as a sole focus for ninety days, which is what D-011 says. Fionn's advice (brainstorm.md, 13 Nov) points the same way: pick a robotics niche learnable fast enough to reach the frontier and go deep on foundations.

On space: real, and staged. Metal was 3D printed on the ISS for the first time in August 2024 on an Airbus-built ESA printer (https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station). The route from a shed in Arenys to a habitat workbench is an ESA Business Incubation Centre: ESA BIC Barcelona in Castelldefels gives a 60,000 EUR non-equity incentive, half ESA and half the Generalitat, to startups building for the space sector (https://www.ieec.cat/en/?p=41772, https://www.upc.edu/en/press-room/news/esa-bic-barcelona-issues-a-call-to-incubate-aerospace-start-ups). Applying is gate 3 and belongs after a working demo, not before.

## 3. Ambition framing (be-ambitious, Felix Rieseberg's three types)

- **Goal beyond the goal:** Oscar's success tied to no country: a company whose product is the capability to make finished parts wherever there is stock, power and a box.
- **Types used:** Altitude (this serves an outcome, a fundable company), Depth (the best robotics founders show numbers, not slides), Range (fab labs, in-space manufacturing, machine-tending-as-a-service and an informal-sector artisan each know something the robotics field does not). Speed skipped, as the skill says.
- **Altitude ladder:**
  1. Write the plan Oscar asked for (this file).
  2. Make the idea falsifiable within ninety days: one task, one pair of arms, one measured success rate, judged by someone who is not Oscar or Claude.
  3. Build the thing that compounds: a library of workbench recipes (demonstrations, policies, fixtures, acceptance tests) learned on a real yard's bench and sold per finished part, on commodity arms. The STC is the library. The arms are whatever is cheapest that year.
- **Depth (Felix's four questions):** What a top founder would do that was not asked: skip the deck and film a robot finishing fifty parts. Rawest material: the yard's own bench tasks, timed, with scrap rates, not market reports. Methods and tools: LeRobot teleoperation and imitation learning, SmolVLA or π0.5 fine-tuning, a fixed fifty-trial protocol on unseen parts. Outside judge: a fitter accepts or rejects each part; the success rate is counted on video by someone else.
- **Range (the verbs):** "turning raw stock into an accepted part without a skilled person present, anywhere." The crew and what each does: a fab-lab veteran (the Fab Foundation counts 2,300 or more labs, https://fabfoundation.org/; they proved machines spread easily and skilled time does not, so measure skilled minutes saved, not machines shipped); an in-space manufacturing engineer (ESA's printer: design for no resupply, so every consumable in the box is on a list); a machine-tending-as-a-service operator (Formic bills from 8 USD an hour and only when the machine runs, https://www.automate.org/news/why-do-customers-choose-formic/anc; price per output hour, never per robot); a Suame artisan (what they would pay for is a drawing turned into an identical part ten times); a short seller as red team (what kills this: gripper and fixture reliability, lab success rates that do not survive a yard floor, machinery certification, capital).

## 4. The macro roadmap

Durations are my estimates. Each stage has a test, a pass line, a cost, the gate it crosses and a kill criterion. Stages 1 and 2 run in parallel.

### Stage 0: Thesis and wedge (now to 2026-11-30)
- Do: a one-page thesis in this folder (`thesis.md`): first customer, first task, why now, what the box is in year one and year five. List ten bench tasks Oscar sees done by hand at the yard, each with the skill needed and the minutes it takes. Read the employment contract for IP, non-compete and side-activity clauses (a yard automation venture is adjacent to his employer's business; this is checked before anything is built). Fold in Cofounder's X and Threads research (D-011) for overlaps.
- Pass: Oscar can say the first customer and the first task in one sentence, and the contract question has an answer.
- Cost: 0. Gate: none. Kill: the contract forbids it and cannot be renegotiated; then the wedge changes (small fabricators outside shipbuilding), the roadmap stays.

### Stage 1: Hands and literacy (2026-12-01 to 2027-02-15, about ten weeks of venture hours)
- Do: build or buy one SO-101 leader and follower pair. Parts for a pair are listed at about 230 USD on third-party bill-of-materials pages (https://www.roboticscenter.ai/hardware/so-101/specs); an assembled Seeed kit without printed parts is listed at 312 USD (https://rcdrone.top/products/so-arm101-low-cost-ai-arm-servo-motor-kit-pro-for-lerobot-without-3d-printed-parts); the official bill of materials and print files are in https://github.com/TheRobotStudio/SO-ARM100 and must be re-checked before buying. 3D printing: price unknown until Oscar says whether he has a printer or a makerspace. Install LeRobot on the Mac or the box, record fifty demonstrations of one bench task from the Stage 0 list (my pick: cut a cable to a marked length and strip both ends; alternatives: sort and bag fasteners by size, or deburr a cut aluminium edge), fine-tune SmolVLA from `lerobot/smolvla_base`, then run the fifty-trial protocol on parts not used in training. Learning programme alongside (Fionn's point): the LeRobot documentation and course, the π0.5 paper (https://arxiv.org/abs/2504.16054), Gershenfeld's fab lab material.
- Pass (hard target, treated as reasonable): 80 percent success over fifty unseen trials, filmed, scored by someone other than Oscar. For calibration: SmolVLA's authors report 78.3 percent on real SO-100 tasks (https://huggingface.co/blog/smolvla); Gemini Robotics reported above 80 percent on half of twenty short-horizon dexterous tasks (https://www.alphaxiv.org/abs/2503.20020v1). A yard bench is harder than a lab table, so a missed target with real numbers is a good result.
- Cost: the arm pair above plus printing. Gate 2 for the purchase: decision D-012 in the report of this run. Kill: after ten weeks no task is above 50 percent and Oscar cannot say why; the thesis survives, but Oscar is not the sole builder, and the next step is a technical cofounder, not more hardware.

### Stage 2: Wedge discovery at the yard (2027-01-01 to 2027-03-15, in parallel)
- Do: Mom Test conversations (the playbook Cofounder already chose for crowd control) with five fitters or foremen at the yard and five small fabricators outside it. Questions about what they did last week by hand, what a bad part cost, which jobs wait for the one person who can do them. A timed task inventory: skilled minutes per task, scrap rate, rework. Conversations at his own workplace are Oscar's own life; anything written to anyone outside the yard is a draft first (gate 1).
- Pass: one task where a foreman says, unprompted, what he would pay per hour of output for it, and the arithmetic beats the fitter's loaded hour.
- Cost: 0. Gate 1 for outside messages. Kill: nobody names a task they would pay for; then the first customer is not a yard, and Stage 3 waits until one is found.

### Stage 3: Pocket Factory v0, one bench cell (2027-03-15 to 2027-07-31)
- Do: one cell for the Stage 2 task, in a shed or a garage: two arms of whatever class the task needs (from a second SO-101 pair to a used cobot; prices unknown until quoted, the hardware-engineer role gets manufacturer quotes), fixtures, two cameras, a tool holder for two or three tools, the recipe from Stage 1 scaled to the real part. Design for the yard floor: dust, aluminium swarf, a fitter who kicks the table. Add the acceptance test to the recipe so the cell rejects its own bad parts.
- Pass: four hours unattended at 90 percent or better, parts accepted by a fitter, cost per part below the fitter's hour. Film all of it.
- Cost: unknown until quotes. Gate 2 for every purchase. Also here, if the demo exists: the ESA BIC Barcelona application with the habitat-workbench angle (gate 3, next call after the December 2025 one is unknown, check https://www.ieec.cat/en/). Kill: the task works on the lab table and fails on real parts after two redesigns; write down why and pick the next task from the Stage 2 list.

### Stage 4: Paid pilot and pre-seed (2027-08-01 to 2027-12-31)
- Do: one paid pilot, priced per hour of output like Formic, at the yard or at a fabricator from Stage 2 (gate 1 for the approach, and the employer conflict from Stage 0 settled in writing). The pre-seed material is the Stage 3 film, the fifty-trial numbers, the pilot letter and the task library roadmap. Targets for money: robotics pre-seed funds and the ESA BIC incentive; names and terms are a Stage 3 research task, not guessed here.
- Pass: a signed pilot and a term sheet, or a clear no from ten investors with reasons written down.
- Cost: travel and the cell's running costs, quoted then. Gates 1, 2 and 3 all appear here. Kill: no one will pay even per hour; the library stays open source and Oscar has learned robotics at the frontier, which was Fionn's ask anyway.

### Stage 5: The library (2028 onwards, not planned in detail)
More tasks, more sites, the same box. The product is recipes and acceptance tests; arms stay commodity and get swapped as the brain companies ship better weights. Space enters through the ESA BIC and an in-space manufacturing partner once the terrestrial cell has run for a year. "Throw in raw materials and it builds you whatever" is the Stage 5 sentence; every stage before it is one task at a time.

## 5. Risks, stated plainly

- **Capital.** The company after Stage 3 needs money Oscar does not have, and robotics hardware burns it. The roadmap is built so the fundable demo costs one arm pair, printing and quotes; after that, fundraising is the job.
- **Day-job conflict.** A bench automation venture next to his employer's trade needs the contract read and, when a pilot comes, a written agreement. Stage 0 item, not negotiable.
- **Hype.** Published success rates are on lab tasks chosen by the authors. His bench numbers will be lower. Stage 1 exists to replace belief with a measured rate.
- **Safety and certification.** A cell on a yard floor is a machine under the EU Machinery Regulation 2023/1230, which applies from 20 January 2027 (EU-OSHA summary: https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery; text: https://eur-lex.europa.eu/eli/reg/2023/1230/oj). Whoever substantially modifies a machine counts as its manufacturer under Article 18, so a retrofitted cell carries the full obligation. Collaborative operation without a cage needs a risk assessment per task; the regulation-procurement role maps this before Stage 3.
- **Focus.** Three ideas in three days. Digest Phase 0 is approved and unbuilt; crowd control has a session today. D-011 makes this the sole focus, which means those two get parked lines with revisit dates in Cofounder's files, not silent neglect.
- **Team.** Fionn's advice stands: wait on a startup with Paul and Mathieu until team fit is clear. Stage 1 answers whether Oscar is the builder; that answer decides what kind of cofounder he needs.

## 6. The first thirty days, concretely

1. This week: read the employment contract clauses; write `thesis.md` (one page); start the ten-task list on the yard floor (phone notes, no names).
2. Answer D-012 (the arm pair); if yes, order the parts and the printing; install LeRobot on the Mac in one venture hour and run the simulated examples before the hardware arrives.
3. Cofounder's X research lands; overlaps go into `thesis.md` under "who else is here."
4. 30 November: Stage 0 review in the venture hour: customer sentence, task sentence, contract answer, hardware status.

## 7. Open inputs from Oscar (Vela batches them)

- Does his contract at Aresa allow a side venture in bench automation, and does the yard own what he builds at home?
- Does he have access to a 3D printer (home, friend, makerspace, the yard)? This sets the Stage 1 cost.
- D-012: a spend ceiling for the Stage 1 arm pair (memo in the run report).
