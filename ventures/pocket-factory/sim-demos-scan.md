# Simulated hardware demos scan, for Pocket Factory

Date: 2026-11-13 (Europe/Madrid). Written by Innovator. Read only: nothing was posted, liked, followed, bookmarked or messaged.

**Question.** Oscar wants the Pocket Factory proof of concept to be a fully simulated demo, designed with frontier models, good enough to raise angel or VC money. He says people on X are designing chips and whole robots with Fable 5.2 and showing virtual demos. This file maps what exists, how it is made, and what it does and does not prove.

**Sources.**
- Oscar's X bookmarks on both connected accounts (read only), including the four bookmark folders.
- Public X full-archive search (13 query families, listed in Coverage notes), the full threads and replies of the strongest posts, and quote posts of the top post.
- Web pages opened to learn the stack: [Anthropic, "Testing Claude on real-world electronics design"](https://www.anthropic.com/research/claude-electronics-design) (9 Nov 2026), the [text-to-cad README](https://github.com/earthtojake/text-to-cad), the [Manda Robotics Real2Sim assets repo](https://github.com/Manda-Robotics/real2sim-frontier-assets), and four investor-side pages listed in section 5.
- Vela's separate bookmark note is at `ventures/pocket-factory/bookmarks-sim-demos.md` (commit f39dc5d). This file covers the same bookmarks and goes much wider.

**Counts.**

| Source | Read | Kept |
|---|---|---|
| Bookmarks, @oscarbonnefon (main account, all pages plus 4 folders: Art 17, Braindump Innovation Hub 2, Startup 3, AI 4; every folder item was already in the main list) | 56 | 3 |
| Bookmarks, @TheSwampMagos (old account, no folders) | 98 | 1 (context only) |
| Public X posts reviewed (search results, full threads, replies, quotes) | 405 unique posts | 34 in the table below |
| Web pages opened | 7 | 7 |

**Headline fact.** Fable 5.2 examples are not rare. Fable 5.2 launched on 9 Nov 2026 ([Anthropic launch post](https://x.com/claudeai/status/2119867114450268322)), and in the four days since, at least 18 public posts in this scan show it designing hardware, robots, CAD or simulations. Most have small audiences. Two carry the weight: Anthropic's own three-device electronics demo ([thread](https://x.com/claudeai/status/2119899459761131615)) and Jake Fitzgerald's overnight humanoid robot ([post](https://x.com/earthtojake/status/2120247469900800316), about 614,000 views). Chip design is the weakest area: one hobby FPGA CPU, and benchmark people saying Fable 5.2 did not move their chip tasks ([Ergodex](https://x.com/YugeshKothari/status/2120239115526689018)).

## 1. Examples table

B = from Oscar's bookmarks. Video = the post has a video attached, as returned by the X API. Engagement figures are from the API on 13 Nov 2026.

| # | Date | Handle | What it shows | Model and tools | Video | Link |
|---|---|---|---|---|---|---|
| 1 | 2026-11-09 | @claudeai | Fable 5.2 designs three working devices (speakerphone, voice hub, handheld pet) from one-paragraph prompts: spec, parts, 4-layer PCB, 3D-printable enclosure, firmware. Humans at Diode built them; no circuit fixes needed | Fable 5.2, KiCad, its own router, CAD | yes | [post](https://x.com/claudeai/status/2119899459761131615) |
| 2 | 2026-11-10 | @earthtojake | Humanoid robot "Galatea" designed overnight: full CAD, MuJoCo balance sim, Blender sizzle reel. 614k views, 587 likes | Fable 5.2 at max effort, text-to-cad (build123d, OpenCASCADE), MuJoCo, Blender | yes | [post](https://x.com/earthtojake/status/2120247469900800316) |
| 3 | 2026-11-11 | @earthtojake | MuJoCo 4 added to text-to-cad: CAD to MuJoCo sim, mass and inertia extracted from CAD, robots and scenes composed in Python | text-to-cad, MuJoCo 4, Claude Code or Codex | not checked | [post](https://x.com/earthtojake/status/2120578094167965913) |
| 4 | 2026-11-11 | @clankrmedia | Recap of Galatea: 689 parts of code-built CAD, 33 RobStride drives, balance iterated in MuJoCo until stable, every shot a Blender render | Fable 5.2, build123d, MuJoCo, Blender | yes | [post](https://x.com/clankrmedia/status/2120419130515804329) |
| 5 | 2026-11-11 | @TangataNui | "BRUTUS" joke humanoid: 540 CAD parts, 1.44 m, 22 catalogue actuators, MuJoCo sim that walks and dances; torque, balance and clearance checks changed the design five times. "Hardware is next" | Fable 5.2, build123d to STEP, MuJoCo | yes | [thread](https://x.com/TangataNui/status/2120537650713231687) |
| 6 | 2026-11-10 | @spaleon_x | One prompt: desktop robot arm with 13 printable parts, routed PCB, ESP32 firmware and a 3D simulator, no CAD tools | Fable 5.2 | yes | [post](https://x.com/spaleon_x/status/2120017913390227564) |
| 7 | 2026-11-12 | @ja_rothschild | Side by side: real robot rollout vs the same joint targets replayed in a digital twin Fable 5.2 built, for RL and evals on a DeepMind robotics task | Fable 5.2, Isaac Lab (PhysX) | yes | [thread](https://x.com/ja_rothschild/status/2120834975276622317) |
| 8 | 2026-11-10 | @NGO275 | Fable 5.2 controlling a robot inside Isaac Lab (inference pauses cut from the video) | Fable 5.2, Isaac Lab | yes | [post](https://x.com/NGO275/status/2119998988900561026) |
| 9 | 2026-11-11 | @Av1dlive | HomePod mini class speaker from one prompt, with the full prompt published: schematic, PCB, enclosure, software | Fable 5.2 | yes | [post](https://x.com/Av1dlive/status/2120544973590564875) |
| 10 | 2026-11-10 | @_MaxBlade | Working 3D-printed herringbone-gear fidget spinner. Tip: export 3MF, not STL, so the model can pass print settings to the printer | Fable 5.2, 3MF | yes | [post](https://x.com/_MaxBlade/status/2120176997187858763) |
| 11 | 2026-11-12 | @cherbini | Fable 5.2 designs a new camera tilt head to reduce ringing, being printed | Fable 5.2 | yes | [post](https://x.com/cherbini/status/2120983739127964106) |
| 12 | 2026-11-11 | @Sanemavcil | A CPU written by Fable 5.2 taken to a ready-to-flash FPGA bitstream through real FPGA tools ("per the creator") | Fable 5.2, FPGA toolchain | yes | [post](https://x.com/Sanemavcil/status/2120505427750195343) |
| 13 | 2026-11-13 | @RealMarvelX | Interactive browser 3D "humanoid robotics lab" with 10 real robots | Fable 5.2, web 3D | yes | [post](https://x.com/RealMarvelX/status/2121072955148902619) |
| 14 | 2026-11-13 | @ghosstty_ | Code-drawn animation of a robot growing from one LED circuit to an arm and lidar mapping | Fable 5.2, code-only animation | yes | [post](https://x.com/ghosstty_/status/2121224479040848087) |
| 15 | 2026-11-12 | @trokhimchuk003 | Humanoid blueprint sheets (28 joints, actuator table, peak torque per joint) produced by 24 subagents | Fable 5.2, subagents | yes | [post](https://x.com/trokhimchuk003/status/2120969000222146977) |
| 16 | 2026-11-12 | @MaybushSha16067 | Fable 5.2 testing in MuJoCo a gripper that Opus 5.5 designed earlier | Fable 5.2, MuJoCo | yes | [post](https://x.com/MaybushSha16067/status/2120715787543482448) |
| 17 | 2026-11-11 | @embodianalysis | Honest sim test: pack four objects into a box. Neither Fable 5.2 nor GPT-6 Astra packs all four | Fable 5.2, GPT-6 Astra, sim | yes | [post](https://x.com/embodianalysis/status/2120562525528076620) |
| 18 | 2026-11-09 | @withplayground | Fable 5.2 reported at 64.9% on RoboDojo Sim, 2nd behind Q0-Preview; first frontier LLM launch to report a robot manipulation benchmark (their claim) | Fable 5.2, RoboDojo Sim | no | [post](https://x.com/withplayground/status/2119889288229802268) |
| 19 | 2026-11-10 | @YugeshKothari | Chip design reality check: Fable 5.2 moved the overall GDPx chip score but Ergodex's own chip tasks saw no gains | Fable 5.2, SemiAnalysis GDPx | no | [post](https://x.com/YugeshKothari/status/2120239115526689018) |
| 20 | 2026-11-12 | @vzcode | Cold-chain logistics digital twin in one HTML file: 3D site, energy agent, failure prediction | Fable 5.2, three.js | yes | [post](https://x.com/vzcode/status/2120939264380940589) |
| 21 | 2026-10-14 | @ky_eric_chen | RoboSimStudio: from a phone video of a robot wiping, Claude and GPT agents each built a full-dynamics digital twin in about an hour, including sponges, cables, cloth | Fable 5.1, GPT-6 Astra, Gemini Argon, RoboSimStudio | yes | [post](https://x.com/ky_eric_chen/status/2110405269171921243) |
| 22 | 2026-09-23 | @Mandarobotics | Real2Sim: 12 to 25 iPhone photos plus short videos turned into functional Isaac Sim (.usd) assets; Astra most detailed, "only Fable got some of the mechanics right" on an IKEA corkscrew; prompts and assets published | Fable 5.1, Opus 5.5, GPT-6 Astra, Gemini 3.8 Flash, Isaac Sim | yes | [thread](https://x.com/Mandarobotics/status/2102811446052827455) |
| 23 | 2026-09-22 | @VRC1416731 | Fable 5.1 writes code used as a policy in Isaac Sim through NVIDIA ENPIRE, moving a Franka arm with RMPFlow | Fable 5.1, Isaac Sim, ENPIRE | yes | [post](https://x.com/VRC1416731/status/2102276288992166236) |
| 24 | 2026-09-14 | @meowsu24 | Fable 5.1 drives a real ARX R5 arm with a wrist depth camera: no demos, no training, no VLA, no calibration | Fable 5.1, RealSense D405 | yes | [post](https://x.com/meowsu24/status/2099471621480489391) |
| 25 | 2026-09-08 | @dimentary | GPT-6 Astra builds a MuJoCo scene and controller so an arm with a five-finger hand draws Picasso's dove. 110k views | GPT-6 Astra, MuJoCo | yes | [post](https://x.com/dimentary/status/2097141042214797801) |
| 26 | 2026-09-26 | @duodottech | Coding agent teaches a simulated Franka to pick up, stand and screw in a lightbulb (EmbodiedSWE benchmark reproduction) | GPT-6 Astra, Isaac Sim | yes | [post](https://x.com/duodottech/status/2103874405130805626) |
| 27 | 2026-09-08 | @MichaelAZeuner | Digital twin of an R&D CNC router in Isaac Sim, testing part unloading with and without a hinged retainer; "physical validation is next" | GPT-6 Astra, Isaac Sim | yes | [post](https://x.com/MichaelAZeuner/status/2097139207898595800) |
| 28 | 2026-10-29 | @Promixyz | Single-prompt browser "robotic factory": a 3D arm moves parts between stations and tracks operations (a quote of another builder's demo) | Claude Code, web 3D | yes | [post](https://x.com/Promixyz/status/2115773305042944150) |
| 29 | 2026-10-28 | @sopersone | Four-legged robot with an arm, custom gait, and a 3D digital twin mirroring it live | Opus 5.5 | yes | [post](https://x.com/sopersone/status/2115423497338150989) |
| 30 | 2026-09-27 | @marcodisarra | Astra turns photos and STLs of a cheap AliExpress 6-DOF arm into a URDF; "every other model couldn't" | GPT-6 Astra, URDF | yes | [post](https://x.com/marcodisarra/status/2104228639181001189) |
| 31 | 2026-08-21 | @mferraro89 | AI-generated CAD with a working feature tree and assembly, and the line "Text-to-CAD is not the hard part and it is not the interesting part!" | Their own CAD platform (Parasolid kernel, per a reply) | yes | [post](https://x.com/mferraro89/status/2090903470819733753) |
| 32 | 2026-08-08 | @glowcone | text-to-CAD analyses 3D scans of hard objects and models better grippers for the SO-ARM101 | text-to-cad | yes | [post](https://x.com/glowcone/status/2086201864589291812) |
| 33 | 2026-10-31 | @justinplaygame (B) | "Lovable for hardware": heypcb.ai | heypcb.ai | yes | [post](https://x.com/justinplaygame/status/2116592942030758181) |
| 34 | 2026-10-22 | @0xMovez (B) | Interactive drone engineering site: 13 real drones you can build part by part in the browser. 99k views | Opus 5.5, /colorfigures skill | yes | [post](https://x.com/0xMovez/status/2113292903741116893) |

Also from the bookmarks, not in the table because they are context rather than demos: @asimovinc's open-source DIY humanoid kit at "$20,000 total" ([post](https://x.com/asimovinc/status/2087040759140855981), B, Startup folder) and Palmer Luckey on engineers who no longer learn design for manufacture ([post](https://x.com/Jawwwn/status/2058375830670327827), B, old account).

## 2. Workflows: how people go from prompt to CAD to simulation to video

### 2.1 Code CAD, then MuJoCo, then Blender (the humanoid pattern)

This is the stack behind the most viewed example and its copies.

1. **Prompt.** Jake Fitzgerald posted his prompt in a reply: "Design and model a visually stunning humanoid robot with exceptional attention to detail. Choose your own aesthetic and mechanical architecture. Its structure, joints, and assembly should make physical sense, with careful thought about how it would actually move..." ([reply](https://x.com/earthtojake/status/2120680213470228960)). He ran it at "Max effort" ([reply](https://x.com/earthtojake/status/2120276120235053108)) overnight, and it "used about half of my weekly sub" ([reply](https://x.com/earthtojake/status/2120259390900932877)).
2. **CAD as code.** Every part is a Python script in build123d on the OpenCASCADE kernel, exported as STEP ([reply](https://x.com/earthtojake/status/2120325215054090373)). The open-source text-to-cad plugin gives the agent skills for parts and assemblies, KiCad circuit boards with ERC and DRC, manufacturing checks (machining, sheet metal, molding, printing), CalculiX stress checks, dimensioned drawings, Blender renders, SendCutSend and Bambu print handoff, and URDF, SRDF and MJCF robot files ([README](https://github.com/earthtojake/text-to-cad)). The repo was reported at 18,142 GitHub stars on 7 Oct 2026 ([post](https://x.com/chinchoukou/status/2107788066412957928)).
3. **Physics.** The model exported the robot to MuJoCo and "tested balance on a few actions and iterated in a loop until it was stable" ([reply](https://x.com/earthtojake/status/2120298168688451946)). Two days later text-to-cad added MuJoCo 4 with mass and inertia taken from the CAD solids ([post](https://x.com/earthtojake/status/2120578094167965913)).
4. **Film.** STEP files exported to GLB and animated in Blender ([reply](https://x.com/earthtojake/status/2120325215054090373)). BRUTUS shows the same chain, plus beat-matched editing: the model found the track tempo and put every cut on a bar line ([thread post](https://x.com/TangataNui/status/2120537658174869909)).
5. **Self-checks.** BRUTUS's author says one model and one set of numbers drove CAD, simulation, and torque, balance and clearance checks, and that the checks "changed the design five times" ([thread post](https://x.com/TangataNui/status/2120537656786641087)).

### 2.2 Electronics: spec to board to enclosure (the Anthropic and Diode pattern)

From [Anthropic's write-up](https://www.anthropic.com/research/claude-electronics-design):
- A short prompt (for the speakerphone: "a puck that plugs into a computer over USB-C and includes microphones and a speaker, supporting Bluetooth with a PCB antenna").
- Fable 5.2 wrote the spec, drew schematics, placed and routed 4-layer boards in KiCad, and wrote its own grid router in about half an hour when KiCad's one-track-at-a-time router was too slow.
- It checked board-in-enclosure fit in code (found the board must be tilted about 25 degrees to install), ran DFM and sourcing checks, and wrote firmware.
- Diode engineers built and tested the boards, because Claude "wasn't connected to test equipment or to the machines that make and assemble circuit boards."
- Reported scores: PCB Gym 69% vs 25% for Fable 5; BenchCAD 2.1 83.5%.
- Stated limits: no electrical validation, antenna tuning, thermal testing or certification yet. Anthropic has a commercial relationship with Diode.

### 2.3 Real to sim: building a digital twin from photos or video

- Manda Robotics fed 12 to 25 iPhone photos and 1 to 4 short videos per object to frontier agents, zero-shot, and got Isaac Sim .usd assets. Reported runs: Fable 5.1 built a working office chair in 22 minutes for $7.38; on the corkscrew "only Fable got some of the mechanics right" ([thread](https://x.com/Mandarobotics/status/2102811446052827455); [chair post](https://x.com/Mandarobotics/status/2102811452340154540); [corkscrew post](https://x.com/Mandarobotics/status/2102811450289111215); [prompts and assets](https://github.com/Manda-Robotics/real2sim-frontier-assets)).
- RoboSimStudio: phone video in, full-dynamics digital twin out in about an hour, with deformables ([post](https://x.com/ky_eric_chen/status/2110405269171921243)).
- @ja_rothschild's twin for a DeepMind robotics task, built by Fable 5.2 in Isaac Lab from CAD, old episodes and about 90 close-up photos. His numbers: joint error 0.2 to 0.4 degrees RMS in free space, but "Final success with replayed targets in sim is about half of what it was in the original episodes" ([reply](https://x.com/ja_rothschild/status/2120841577933197413)). He renders 224x224 for policy views and 1280x720 for videos, uses Isaac's renderer with materials tuned against real camera frames, no Blender ([reply](https://x.com/ja_rothschild/status/2121253957079015527); [reply](https://x.com/ja_rothschild/status/2121253895137632644)).

### 2.4 The LLM as the controller inside the sim

- Code as policy: Fable 5.1 writes code that runs as the policy for a Franka arm in Isaac Sim through NVIDIA ENPIRE ([post](https://x.com/VRC1416731/status/2102276288992166236)).
- Benchmarks now exist for this: RoboDojo Sim, where Fable 5.2 is reported at 64.9% ([post](https://x.com/withplayground/status/2119889288229802268)), and EmbodiedSWE, reproduced in Isaac Sim with a lightbulb task ([post](https://x.com/duodottech/status/2103874405130805626)).
- The same pattern runs on real arms: Fable 5.1 on an ARX R5 with no training ([post](https://x.com/meowsu24/status/2099471621480489391)). It is also MicroFactory's production stack: a frontier model plans and writes vision code, and the code runs the motion (see `ihorbeaver-sweep.md`).

### 2.5 Browser 3D for an interactive pitch

- Single-file three.js twins and interactive labs are cheap to make and easy to share: cold-chain twin ([post](https://x.com/vzcode/status/2120939264380940589)), humanoid lab ([post](https://x.com/RealMarvelX/status/2121072955148902619)), drone builder ([post](https://x.com/0xMovez/status/2113292903741116893), B), browser robotic factory ([post](https://x.com/Promixyz/status/2115773305042944150)).
- These are visual explainers, not physics simulations. None of these posts claim validated physics.

### 2.6 Builder tips collected from threads and replies

- Export 3MF rather than STL so print settings travel with the part ([post](https://x.com/_MaxBlade/status/2120176997187858763)).
- Simulation assumes zero tolerance: "Then the first printed joint doesn't fit because the sim assumed zero tolerance, and you're back to calipers" (18 likes, the top reply on the humanoid post) ([reply](https://x.com/pggalaviz/status/2120289078310584589)).
- If masses and inertias flow straight from the CAD solids, every text-to-CAD design gets a free physics check ([reply](https://x.com/RoviidDesissa/status/2120303320464076897)). text-to-cad shipped exactly that two days later ([post](https://x.com/earthtojake/status/2120578094167965913)).
- MuJoCo for fast experiments, Isaac Lab for ray-traced realism at a heavier setup cost ([reply](https://x.com/ja_rothschild/status/2121253895137632644); [reply](https://x.com/Schmidiee/status/2121265645904150843)).
- Small features decide contact. A notch about 1.5 mm across looked like point-cloud noise, so the agent had to read close-up frames to find it ([reply](https://x.com/ja_rothschild/status/2120845606113390998)). A PCB laid out blind "missed the small mechanical detail that decides if it works (board didnt fit the enclosure lol)" ([reply](https://x.com/SoumilBhandari/status/2120960440998015158)).
- Reviewing output is the bottleneck, not generating it: "Whether the part is actually right I learn 3 hours later at the printer" ([reply](https://x.com/dannyow/status/2091078881574846562)).
- Text-to-CAD is only useful with validation: "Text to cad is garbage unless you have powerful ways to validate that the parts are actually manufacturable and performant, which we believe is mostly an simulation and FEA problem!" ([reply](https://x.com/mferraro89/status/2090919856749125909)).
- Real2Sim assets often look right but lack usable collision geometry and mass or inertia data ([reply](https://x.com/RocketDIYerBen/status/2103485956192141315)).

### 2.7 Pushback and skeptic replies worth knowing

- "the reel looks elite but the physics are sus" ([reply](https://x.com/vioinabox/status/2120270279251558419)). Another reply says the MuJoCo clip "ends with Galatea squatting and tipping straight onto its back" ([reply](https://x.com/Yvan_Ciz/status/2120257229886742693)).
- "CAD, sim, sizzle reel overnight. The step nobody shows is the first physical build." ([quote](https://x.com/amanvaibhav/status/2120411772532445430))
- "The test is whether a part machined from those files behaves like the mujoco model says it will. That is the step where these runs have died before." ([reply](https://x.com/AIQuanting/status/2120300167970893894))
- "matching one wiping video doesn't prove contact dynamics under unseen robot actions" ([reply](https://x.com/sebuzdugan/status/2110695767073558776))
- "Friction and impacts are always where the sim starts lying." ([reply](https://x.com/Joshua_WD/status/2120843169596117177))
- Text-to-CAD "creates instant garbage" because a two-sentence prompt cannot describe a non-trivial part ([reply](https://x.com/Jern123d/status/2090917765976609253)).
- Chip design: the best agent scored 16.6% on the full spec-to-GDS Build-A-Chip-Bench, and "People will treat this as AI already designing chips. It is not." ([post](https://x.com/therealvane11/status/2110524934388678979))
- **From the closest competitor.** Asked "do you use isaac sim?", MicroFactory cofounder Viktor Petrenko replied: "No, it doesn't work well for simulating precise tasks like electronics assembly." ([question](https://x.com/A1_Projects/status/2080811403326185608); [reply](https://x.com/viktor_vrp/status/2080824882582151569), 25 Jul 2026)

## 3. What this means for a simulated Pocket Factory demo (opinion)

Everything in this section is my opinion unless a link is attached.

### 3.1 Recommended stack (opinion)

1. **Design.** Fable 5.2 in Claude Code with the free text-to-cad plugin. Parts, fixtures and the cell frame are build123d code exported to STEP, with manufacturing checks and CalculiX stress checks from the same plugin ([README](https://github.com/earthtojake/text-to-cad)). Do not design the robot arms. Use published arm models instead; the Franka arm is already the default in the Isaac Sim examples above ([post](https://x.com/VRC1416731/status/2102276288992166236)), and DeepMind's [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) collects ready-made robot models.
2. **Simulate.** MuJoCo first, through text-to-cad's MuJoCo 4 path, so masses come from the CAD ([post](https://x.com/earthtojake/status/2120578094167965913)). Move to Isaac Sim or Isaac Lab only if you need photoreal footage or many parallel runs ([reply](https://x.com/ja_rothschild/status/2121253895137632644)). Let the LLM write the controller code and keep motion in code, which is the pattern MicroFactory uses in production.
3. **Show.** Blender for the film, cut from real sim runs, never hand-animated ([earthtojake reply](https://x.com/earthtojake/status/2120325215054090373)). Add a three.js browser twin an investor can click through on their own laptop ([example](https://x.com/vzcode/status/2120939264380940589)).

### 3.2 Demo ideas that could impress an angel or VC (opinion)

1. **"Bar stock in, finished part out" (top pick).** The two-arm cell loads aluminium bar into a desktop mill, swaps tools, deburrs, measures with a simulated probe, and assembles the part into a small product. This is the gap MicroFactory has not shown: its public work is assembly of bought-in parts (see `microfactory-catalogue.md`). Every step must run in MuJoCo from the CAD, with the sim telemetry shown next to the render.
2. **"Text order to product."** Someone types "a bracket that holds a 40 mm fan at 30 degrees." Fable 5.2 designs it, runs stress and manufacturing checks, plans the toolpath and arm motions, and the twin builds it. This mirrors the Anthropic device story ([write-up](https://www.anthropic.com/research/claude-electronics-design)), applied to a whole cell instead of one board.
3. **"The cell builds its own spare part."** The cell makes a gripper finger or fixture for itself, then swaps it in. This answers MicroFactory's self-replication narrative with a manufacturing step, not an assembly step.
4. **"Unboxing day in a remote place."** A container cell arrives somewhere remote, calibrates itself, and produces a needed spare part (a pump impeller, say). It is strong for the vision slide, but it is where the demo is most likely to look like a render. Use it as the closing film only.
5. **"Agent recovers from a failure."** Inject faults in sim, such as a dropped part, a worn tool or a misaligned stock bar, and show the agent rewriting its own code to recover. MicroFactory sells this behaviour on real hardware ([System 1 / System 2 post](https://x.com/ihorbeaver/status/2110866012333838675)), so showing it in sim is table stakes, not a differentiator.

A later option, parked: one cheap real arm mirrored to the twin, for a sim-versus-real overlay like @ja_rothschild's ([post](https://x.com/ja_rothschild/status/2120834975276622317)). That would mean revisiting the robot arms decision (no purchase, decided 13 Nov), so it is not part of this plan.

### 3.3 What a sim demo does not prove

Facts first:
- Contact is where twins break. Free space tracked within 0.2 to 0.4 degrees, but success in replayed contact tasks dropped to about half ([reply](https://x.com/ja_rothschild/status/2120841577933197413)).
- Zero-tolerance sims hide fit problems ([reply](https://x.com/pggalaviz/status/2120289078310584589)). Friction and impacts are where the sim "starts lying" ([reply](https://x.com/Joshua_WD/status/2120843169596117177)).
- Even Anthropic's showcase needed human engineers to build and test the hardware, and has not been through validation or certification ([write-up](https://www.anthropic.com/research/claude-electronics-design)).
- The closest competitor says Isaac Sim "doesn't work well for simulating precise tasks like electronics assembly" ([reply](https://x.com/viktor_vrp/status/2080824882582151569)).
- Machining forces, chip formation, tool wear, thermal growth and weld or solder behaviour are not what MuJoCo or PhysX model. Industrial CNC twins rely on the controller vendor's real machine data ([Siemens example](https://x.com/fogoros/status/2103122735484325903)).

Opinion: a sim shows the design is coherent and the agent pipeline works end to end. It does not show the cell is reliable, accurate, fast or cheap. For a factory product, those four are the whole business.

### 3.4 How hardware investors treat sim-only proofs of concept

- A 2026 robotics fundraising guide says the old "smart team and a sim" round "still exists, but it is now called pre-seed and it caps closer to $1.5M." For seed it asks for a working prototype, "Not a CAD render, not a Unity sim," plus a paid pilot ([Causo Hub](https://hub.causo.ai/guides/raising-seed-robotics-startup-2026)). These figures are that guide's claims.
- A pre-seed robotics investor: "A software-only simulation is not enough: we want to see the robot complete a named task in real ... conditions" ([Valu.vc](https://valu.vc/robotics-investment/)).
- Salesforce Ventures' robotics checklist asks whether the investor has seen the robot in person, whether the demo is "staged, sped up, teleoperated, or overly polished," and "What's the real-world vs. simulated data split?" ([checklist PDF](https://salesforceventures.com/wp-content/uploads/2025/08/25_EA_SFV_Checklist_Investing_Final.pdf)).
- Sky9 Capital: "Embodied AI investors have seen impressive simulation benchmarks that did not survive contact with the real world... A single authentic field deployment story is more persuasive than a strong simulation result." ([Sky9](https://www.sky9capital.com/blog/investors-ai-robotics-embodied-ai/))
- Underscore VC: simulation works well in structured settings, but the sim-to-real gap "remains wide" for unstructured ones ([Underscore](https://underscore.vc/blog/investing-in-robotics/)).
- A counterpoint from the field: MicroFactory raised $1.5M pre-seed at a $30M post-money valuation on the back of a viral real-hardware video, not a sim ([TechCrunch](https://techcrunch.com/2025/09/16/this-30m-startup-built-a-dog-crate-sized-robot-factory-that-learns-by-watching-humans/); [launch video post](https://x.com/ihorbeaver/status/1928154351383580800), 6,029 likes).

Opinion: a sim-only POC can open angel and small pre-seed conversations, especially with a founder story and a credible hardware cofounder. Expect every serious hardware investor to ask "when does it run on real metal?" Answer that question in the deck, with a dated plan, rather than leave it to them.

## 4. Coverage notes

- Bookmarks: the API returned all pages in one call per account (56 and 98, with no next-page token). The four folders on the main account held 26 items, and every one was already in the main list. The old account has no folders. Nothing was changed.
- Query families used on public X search (full archive, mostly from 1 Aug 2026): "Fable 5.2" with CAD, STEP, OpenSCAD, CadQuery, URDF, robot, hardware, PCB or chip; Fable with MuJoCo, Isaac Sim or Lab, Genesis, Omniverse, digital twin, LeRobot, Gazebo or PyBullet; "designed with Fable" variants; Fable with Verilog, RTL, chip design, tapeout, ASIC, FPGA or silicon; text-to-CAD, build123d, CadQuery or LLM CAD with robot, arm or gripper; frontier models with robot arm, humanoid or gripper and MuJoCo, simulation, URDF, MJCF or Isaac (video only); microfactory, factory in a box, lights-out, robotic cell, machine shop or CNC with Fable, Claude, digital twin or simulation; "Fable 5.2" robot-and-mechanism terms (video only, since 9 Nov); investor plus sim-to-real terms. Full threads were read for earthtojake, ja_rothschild, TangataNui, Mandarobotics, ky_eric_chen, mferraro89 and both Anthropic launch threads, plus quote posts of the humanoid post.
- Threads (threads.net) and very small accounts beyond what X search surfaced were not searched in this pass.
- Videos were not watched; descriptions come from post text and replies. "Video yes" means the X API listed a video attachment.
- Engagement is low on most Fable 5.2 posts besides the Anthropic thread and earthtojake. Several posts (clankrmedia, the FinanceYF5 quote) are recaps of the same Galatea run, so this is fewer independent demos than the post count suggests.
