# Oscar's X bookmarks: simulated hardware demos, for Pocket Factory

Written 13 Nov 2026 (Europe/Madrid). Source: a read-only sweep of Oscar's two connected X accounts, taken the same day. No bookmarks were created, deleted or moved. Nothing was posted. Times below are converted from the posts' UTC timestamps to Europe/Madrid (UTC+1). Opinions are labelled as mine.

**Fable 5.2 examples of people designing chips or whole robots are absent from these bookmarks.** Fable 5.2 does appear, but the bookmarked uses are a code-driven paint simulation, a generated video, a short "life hack" clip, and a model-selection guide, not hardware. The hardware and simulation examples that *are* bookmarked use Opus 5.5, Claude Code, or an unspecified assistant, or they publish a digital twin of a robot that already exists in hardware.

## Counts

| Account | Handle | Bookmarks read | Folders | Kept as relevant |
|---|---|---:|---|---:|
| Main (user-X) | [@oscarbonnefon](https://x.com/oscarbonnefon) | 56 (all pages) | 4: Art (17), Braindump Innovation Hub (2), Startup (4), AI (3). Every folder id already sat in the main bookmark list. | 4 |
| Old (user-X--oldaccount) | [@TheSwampMagos](https://x.com/TheSwampMagos) | 164 (all pages) | none | 0 |
| **Total** | | **220** | | **4** |

Relevance rule: AI-designed hardware (chips, PCBs, robots, mechanisms, CAD), simulated or virtual demos, robot arms, microfactories, manufacturing automation, or pitching hardware with a sim. Mentions that only used a keyword in passing (a "chip designer" analogy in a Jensen Huang quote, a Honda factory anecdote, Palmer Luckey on weapons production) were read and dropped.

## Table of kept items

| Date (Europe/Madrid) | Author | Folder | What it shows | Tools / models stated | Link |
|---|---|---|---|---|---|
| 11 Aug 2026, 06:57 | [@asimovinc](https://x.com/asimovinc) (Asimov, Menlo Research) | AI | Open-source reference humanoid, sold as a DIY kit. The listing promises published BOM and CAD, a digital twin, and an agent-friendly SDK. Official docs add a free in-browser twin and MuJoCo / URDF models aimed at sim-to-real. | In-browser twin at [try.menlo.ai](https://try.menlo.ai); MuJoCo (MJCF) and URDF, with Isaac Lab or MJLab templates named in the docs. The bookmarked post does not name Fable 5.2. | [x.com/asimovinc/status/2087040759140855981](https://x.com/asimovinc/status/2087040759140855981) |
| 22 Oct 2026, 16:34 | [@0xMovez](https://x.com/0xMovez) | AI | Interactive site: 13 real drone types built part by part (frame, motors, wiring), then flown in first-person FPV, so you do not have to crash a $400 FPV build to learn the layout. Built, the author says, with a Claude skill and no hand-written code for the figures. | Opus 5.5 plus the [/colorfigures skill](https://april-zhu.com/colorfigures) (interactive HTML figures; MIT licensed). Not a physics engine like MuJoCo. | [x.com/0xMovez/status/2113292903741116893](https://x.com/0xMovez/status/2113292903741116893) |
| 31 Oct 2026, 19:07 | [@justinplaygame](https://x.com/justinplaygame) (Justin Kim, HeyPCB) | Braindump Innovation Hub | "We built Lovable for hardware." Describe a machine in plain language and get a schematic, layout and fab files as real KiCad you keep. A later company post (not itself bookmarked) shows Claude Code driving the same stack over MCP to route an 8x8 RGB display that then opened clean in KiCad. | [heypcb.ai](https://heypcb.ai/), KiCad-native files, optional [HeyPCB MCP](https://heypcb.ai/blog/your-agent-can-now-build-hardware) for Claude Code, Codex, Cursor and ChatGPT. The bookmarked post does not name Fable 5.2. | [x.com/justinplaygame/status/2116592942030758181](https://x.com/justinplaygame/status/2116592942030758181) |
| 9 Nov 2026, 20:25 | [@jkeatn](https://x.com/jkeatn) | (unfiled) | The only bookmarked Fable 5.2 *simulation*. The author has Fable 5.2 invent painter personas and write Python programs (described as one to two thousand lines) that place every stroke through a simulated paint engine. "Claude does not use an image model, nor render or trace in advance." It is art, not hardware, but it is a frontier model authoring a sim. | Fable 5.2, Python, a custom simulated paint engine. | [x.com/jkeatn/status/2119874007382299087](https://x.com/jkeatn/status/2119874007382299087) |

Other Fable 5.2 bookmarks, not kept as hardware demos: [@anabology](https://x.com/anabology/status/2120010995309457643) (Fable 5.2 asked to "make the video of it's dreams"), [@PromptLLM](https://x.com/PromptLLM/status/2119909505618280749) ("Fable 5.2 on the worlds greatest life hack"), and [@ClaudeDevs](https://x.com/ClaudeDevs/status/2119898687803621427) (when to use Fable 5.2 vs Opus 5.5, Sonnet or Haiku).

Pages opened to confirm the stack: [heypcb.ai](https://heypcb.ai/), [heypcb.ai/blog/your-agent-can-now-build-hardware](https://heypcb.ai/blog/your-agent-can-now-build-hardware), [menlo.ai/asimov-1](https://menlo.ai/asimov-1), [docs.menlo.ai/asimov/digital-asimov](https://docs.menlo.ai/asimov/digital-asimov), [docs.menlo.ai/asimov/1/overview](https://docs.menlo.ai/asimov/1/overview), [github.com/menloresearch/asimov-1](https://github.com/menloresearch/asimov-1/), [april-zhu.com/colorfigures](https://april-zhu.com/colorfigures). The original posts' reply threads were also read.

## What this means for a simulated Pocket Factory demo

### Likely stack

**Sim engine.** My pick is MuJoCo (MJCF / URDF) as the core, with an optional Isaac Lab path later, following the stack Asimov already publishes ([overview](https://docs.menlo.ai/asimov/1/overview), [repo](https://github.com/menloresearch/asimov-1/)). That is the right engine for two arms, tool changes, collisions and a scripted "raw stock to finished part" cycle. For the pitch itself, wrap it the way Menlo does: a zero-install browser twin an investor can drive in a tab ([Digital Asimov](https://docs.menlo.ai/asimov/digital-asimov), [try.menlo.ai](https://try.menlo.ai)). LeRobot in simulation, already named in `plan.md` as the software-first hold-over, can sit on the same URDF and does not conflict with this. Colorfigures-style interactive HTML is a complement, not a substitute: it explains the cell, it does not prove the motion.

**CAD route.** Keep mechanical CAD in an open, exportable form (STEP / URDF generated from the same source), and use KiCad for boards. HeyPCB is the bookmarked on-ramp: plain-language in, schematic, layout, Gerbers, BOM and CPL out, as files you keep ([about](https://heypcb.ai/about)). Agents can drive it over MCP; HeyPCB says Claude Code used that path to place 145 parts, reach 0 DRC and 0 ERC errors, and open the project in KiCad ([16 Oct 2026 post](https://heypcb.ai/blog/your-agent-can-now-build-hardware)). That is electronics CAD, not a chip (ASIC) flow, and it is also not proof the board would fab or boot on the first try.

**Model role.** Match the split already on the MicroFactory side: a frontier model plans the job and writes or calls tools, and small, fast, inspectable code runs the motion (see `ihorbeaver-sweep.md`). In this stack the model (Fable 5.2 is a fair candidate, given Oscar's direction, even though these bookmarks do not show it designing hardware) writes the process plan, talks to HeyPCB MCP for any board, and can emit Colorfigures-style HTML for the deck. It should not be the real-time motion controller inside the physics loop.

One caution, labelled as mine: Digital Asimov can claim "the same control stack a physical Asimov runs" and "real actuator models measured from physical hardware" because Menlo already has the robot ([docs](https://docs.menlo.ai/asimov/digital-asimov)). A Pocket Factory twin built before any cell exists would be a specified, idealized sim, not a measured one. That is still the right proof of concept under the no-spend path. It is not the same claim.

### Demo ideas that would impress an investor

1. **Top pick, my opinion: the one-job browser twin.** A zero-install page, in the Digital Asimov style, showing a two-arm cell run one canonical job from raw stock to an accepted finished part. The viewer can orbit the cell, watch tool changes, and see a live log of the planner's steps. This is the artefact that belongs in the pitch deck. It costs no hardware.
2. **See-through explainer of the same cell.** Use the Colorfigures skill (or a close fork) so Fable 5.2, or another Claude, emits an interactive HTML model of the box: labelled stations, a see-through of the tool rack and gripper change, buttons that step the process. [Colorfigures](https://april-zhu.com/colorfigures) is built for "everyday machines and devices with parts you can press," and @0xMovez already showed the same skill teaching a real machine family. This is the slide you leave behind. It does not replace the physics twin.
3. **Prompt-to-board for one cell module.** Drive HeyPCB MCP from Claude Code to design a simple, real KiCad board the cell would need (a sensor or tool-head controller, not a fantasy ASIC), export Gerbers, and show the board opening with a clean DRC in KiCad, the way HeyPCB did with the 8x8 display. This shows electronics competence without a purchase.
4. **Planner-and-motion split, filmed.** On screen: Fable (or Claude) writes a process plan in plain language and code; a small script executes it in MuJoCo, including a forced fault (part missed, stock short) and the recovery the planner writes. This is the control story Igor is already telling, made visible.
5. **Module ladder in one scene.** The same twin, with a second camera pull-back: the bench cell, then a rail and a larger process module (saw, mill, or printer) the arms tend. This is how "solder and also make bigger things" is shown without promising a giant robot.

### What such demos usually do not prove (the sim-to-real gap)

A convincing sim does not prove the cell will work on a bench. In particular it does not prove:

- Real friction, compliance, backlash, cable snags, or a soft or warped piece of stock.
- Calibration, camera-to-arm registration, lighting, or fixture tolerances over a long run.
- Cycle time, yield, or tool wear under a real payload. Asimov's own docs still treat "train in MuJoCo / Isaac Lab, then deploy" as a claimed path ("Sim2Real Ready", [overview](https://docs.menlo.ai/asimov/1/overview)), not as something a new cell gets for free.
- Solder quality, cut quality, or whether a HeyPCB board fabs, assembles and boots.
- Safety, guarding, or anything an investor should treat as a factory certification.
- That "build anything, given tools and materials" is a current method. It remains the ambition. The honest demo is one constrained job in a constrained box, with a path to add modules.

The no-spend path still holds: refine the idea, research what exists, build the deck (with this sim as the proof of concept), then Oscar does investor outreach. Quitting ARESA stays gated on an investor being interested. The robot arms decision and the 3D printer decision stay at no purchase.
