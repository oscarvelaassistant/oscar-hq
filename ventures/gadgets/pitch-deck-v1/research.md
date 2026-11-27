# Gadgets pitch deck v1: research and sources

Written 2026-11-27 by the Claude HQ wake run (task 2026-11-27-001, cofounder role) for Oscar's edit. Five parallel research subagents (market sizing; AI hardware competitors; e-ink and display competitors; business model and ODM benchmarks; problem and why now) each worked one question with WebSearch and WebFetch; this file merges their records. About 270 web calls in total.

How to read the tags:
- **verified**: the page was opened and the figure read on it.
- **snippet only**: the figure came from a search result; the page was paywalled, blocked or not opened. Weaker evidence; treat as "reported" until Oscar or Innovator opens the page.
- **my arithmetic**: a number derived from sourced inputs; the formula is shown.
- **opinion**: the author's reading, not a fact.
- **[placeholder]**: not found or allowed by Oscar as a later input (catalogue renders and prices due Sat 28 Nov, brand name, hero unit cost and MOQ).

No valuation, round size or equity appears anywhere in this file or the deck, by Oscar's rule. The deck names no team other than Oscar.

---

## 1. Market: TAM, SAM, SOM with the method shown

### 1.1 Method

Three layers, each from a different kind of source, so that one weak number does not carry the slide:

1. **TAM**: the global market every item in the catalogue lives in: connected hardware for the home. One analyst figure, verified.
2. **SAM**: the three adjacent segments the catalogue actually competes in (ambient displays and AI speakers): smart speakers and displays, e-paper displays, digital photo frames. Three sources added up; overlaps are small, but the e-paper figure counts panels for e-readers and shelf labels too, so the sum is an upper bound for the hero's reachable market.
3. **SOM**: no capture-share guess. Two things instead: a bottom-up funnel from official household counts to "households already paying for AI", and a ladder of what comparable single-product companies have actually sold. The funnel gives the ceiling; the ladder gives the realistic range of outcomes.

### 1.2 TAM: smart home hardware, global

| Metric | Value | Source | Date | Tag |
|---|---|---|---|---|
| Smart home hardware market, global | US$66.5bn 2025, US$82.6bn 2030, CAGR 4.4%; scope: controllers to end-point devices plus connectivity | https://abiresearch.com/news-resources/chart-data/smart-home-hardware-market-outlook | 4Q 2025 report | verified |
| Smart home market, broader scopes (services, appliances included) | Statista US$159.5bn 2026; GMI US$172bn 2025; MarketsandMarkets US$213.7bn 2025; Fortune BI US$147.5bn 2025 | https://www.statista.com/outlook/dmo/smart-home/worldwide ; https://www.gminsights.com/industry-analysis/smart-home-market ; https://www.marketsandmarkets.com/Market-Reports/smart-homes-market-121.html ; https://www.fortunebusinessinsights.com/smart-home-market-101900 | accessed 2026-11-27 | snippet only; shown for range, not used |
| Wearable AI market (nearest verified "AI device" category) | USD 43.6bn 2025, USD 310.6bn 2033, CAGR 27.8%; scope includes smartwatches, earwear, glasses | https://www.grandviewresearch.com/industry-analysis/wearable-ai-market-report | Sept 2026 | verified; not used in TAM (wearables are not the catalogue) |
| "AI consumer hardware" or "AI companion devices" analyst figure | none found from IDC, Canalys, Omdia or Counterpoint under that label; one low-tier publisher gives USD 0.72bn 2025 to 10.1bn 2034 (marketintelo) | https://marketintelo.com/report/consumer-ai-companion-devices-market | accessed 2026-11-27 | snippet only; opinion: not deck-grade, not used |

Deck uses: **TAM = US$66.5bn (2025), US$82.6bn (2030), ABI Research.**

### 1.3 SAM: ambient displays and AI speakers, global

| Segment | Value | Source | Date | Tag |
|---|---|---|---|---|
| Smart speakers, units and ASP | 2H25: 27.2M units, +4.6% YoY, ASP $108; 1H26: 27.5M units, +13.4% YoY, ASP $119 | https://omdia.tech.informa.com/om144910/smart-speaker-analysis-market-overview--2h25 ; https://omdia.tech.informa.com/om147033/smart-speaker-analysis-market-overview--1h26 | accessed 2026-11-27 | snippet only (Omdia pages return 403) |
| Smart speakers, rolling 12 months value | 27.2M x $108 + 27.5M x $119 = US$6.2bn | my arithmetic from the Omdia rows | | my arithmetic on snippet-only inputs |
| Smart speakers and displays, wider scope | 154.3M units forecast for 2025 (TechInsights, March 2025 forecast) | https://www.techinsights.com/ja/node/61182 | 2026-03-05 | snippet only; different scope, not mixed with Omdia |
| E-paper display market | USD 3.4bn 2025, USD 9.2bn 2034, CAGR 11.5% (IMARC) | https://www.imarcgroup.com/e-paper-display-market | updated 2026-02-26 | verified |
| E-paper display market, second source | USD 3.7bn 2025, USD 4.4bn 2026, about USD 18bn 2035, CAGR 17%; e-readers USD 1.56bn, shelf labels USD 1.17bn in 2025 (GMI) | https://www.gminsights.com/industry-analysis/e-paper-display-market | Sept 2026 | verified |
| Digital photo frame market | grows by USD 118.1M over 2025 to 2029 at CAGR 3.1%, base year 2024 (Technavio) | https://www.prnewswire.com/news-releases/digital-photo-frame-market-size-is-set-to-grow-by-usd-118-1-million-from-2025-2029--inclination-toward-high-standard-of-living-boost-the-market--technavio-302362052.html | 2025-01-28 | verified |
| Digital photo frame market, implied 2024 base | 118.1M / (1.031^5 - 1) = about USD 0.72bn | my arithmetic from the Technavio row | | my arithmetic |
| Digital photo frame market, other publishers | Mordor USD 53.6bn 2025 (opinion: not credible, about 75x the Technavio base and far above vendor revenues); Persistence USD 64.5M 2025 (implausibly low: Nixplay alone had USD 20M revenue in 2023) | https://www.mordorintelligence.com/industry-reports/digital-photo-frame-market ; https://www.persistencemarketresearch.com/market-research/digital-photo-frame-market/toc | accessed 2026-11-27 | verified (Mordor), snippet only (Persistence); not used |

Deck uses: **SAM = about US$10bn** (6.2 + 3.4 + 0.7), with the caveat printed: the e-paper figure is a panel market that includes e-readers and shelf labels; the smart speaker value rests on snippet-only inputs.

Growth signals for the SAM (all 2025 or 2026): e-paper CAGR 11.5% to 17% (IMARC, GMI, verified); E Ink Holdings revenue +19% in 2024 and +12% in 2025 (section 5.3, verified); smart glasses shipments +139% YoY in H2 2025 (Counterpoint, verified, https://www.counterpointresearch.com/en/insights/Global-Smart-Glasses-Shipments-Grew-139-Percent-YoY-in-H2-2025, 2026-02-27); US household spend on connected devices US$896 in 2025, up from US$764 (Deloitte Connected Consumer, verified, https://www.deloitte.com/us/en/insights/industry/telecommunications/connectivity-mobile-trends-survey.html, 2025-09-25).

### 1.4 SOM, part one: bottom-up funnel (EU27 plus US)

| Step | Value | Source | Date | Tag |
|---|---|---|---|---|
| EU27 households, 2025 | 203.1M | https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260513-2 | 2026-05-13 | verified, primary |
| US households, 2025 | 134.79M (CPS ASEC) | https://fred.stlouisfed.org/series/TTLHH | updated 2026-11-17 | verified (FRED mirror of Census) |
| Households, EU27 plus US | 337.9M | my arithmetic | | |
| US internet households with at least one core smart home device | 49% (Q4 2025), up 4 points YoY | https://www.parksassociates.com/blogs/home-systems-and-controls/smart-home-growth-continues-as-matter-and-ai-drive-ease-of-use | 2026-04-23 | verified |
| EU individuals 16 to 74 using home audio or smart speakers | 19% (2024); any IoT 70% | https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/140484.pdf | accessed 2026-11-27 | snippet only; measures individuals, used as a household proxy |
| Connected homes, EU27 plus US | 134.79 x 0.49 + 203.1 x 0.19 = 66.0M + 38.6M = 104.6M | my arithmetic | | the EU step mixes an individuals share with a household count; stated on the slide |
| Households paying for an AI subscription, conservative | about 3% (Bank of America Institute, account data on about 70M consumers) | https://komonews.com/news/nation-world/can-consumers-support-ai-just-3-of-households-are-paying-subscribers-bank-of-america-institute-analysis-artificial-intelligence | 2026-03-31 | verified (secondary report of the BofA analysis) |
| Consumers paying for a genAI subscription, survey | US 19.5% (from 18%), UK 20% (from 15%) (Attest, 4,000 consumers) | https://www.askattest.com/blog/research/why-gen-ai-is-the-only-subscription-category-still-growing | updated 2026-11-09 | verified |
| US online adults with a paid genAI subscription | about one in five (Forrester Consumer Pulse, Sept 2025) | https://www.forrester.com/report/consumers-show-trust-in-genai-but-few-pay-for-it/RES190146 | 2025-12-30 | verified (summary page) |
| EU individuals using generative AI, 2025 | one in three | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Digital_economy_and_society_statistics_-_households_and_individuals | Dec 2025 | verified |
| Connected homes already paying for AI | 104.6M x 3% = 3.1M (account data) to 104.6M x 19.5% = 20.4M (survey) | my arithmetic | | multiplying two shares is conservative if the two traits are positively correlated, which they almost certainly are (opinion) |

### 1.5 SOM, part two: what one product line has actually reached (comparables ladder)

| Product | Units | Period | Source | Tag |
|---|---|---|---|---|
| Fraimic Smart E Ink Canvas (AI art frame) | 1,825 backers, $1,120,290 raised | Kickstarter, Sept to Oct 2025 | https://www.kicktraq.com/projects/445470967/fraimic-smart-e-ink-canvas-digital-picture-frame-with-ai/ | snippet only |
| TRMNL X (10.3in e-ink dashboard) | 14,500 orders | 16 months to Nov 2026 | https://trmnl.com/blog/on-x | verified, 2026-11-11 |
| Tidbyt (LED ambient display) | 100,000 devices shipped | lifetime to Nov 2024 | https://modal.com/blog/tidbyt-is-joining-modal | verified, 2024-11-07 |
| Rabbit r1 | over 100,000 sold; about 5,000 daily users | to Sept 2024 | https://9to5google.com/2024/09/26/rabbit-5000-people-use-the-r1-daily/ | verified |
| reMarkable (paper tablets) | about 791,000 devices sold; about 568,000 paying Connect subscribers | 2024, one year | https://en.wikipedia.org/wiki/ReMarkable_(manufacturer) citing the 2024 annual report | snippet only (the Euronext PDF did not parse) |
| Plaud (AI note recorder) | more than 2 million devices; software ARR above US$100M | cumulative to June 2026 | https://eu.36kr.com/en/p/3961453579746437 | verified, 2026-08-30 |
| Aura (digital frames) | "single-digit millions" of frames; profitable | cumulative to Oct 2025 | https://techcrunch.com/2025/10/21/aura-introduces-a-499-e-ink-digital-photo-frame-that-lets-you-go-cordless | verified |
| Oura (smart ring, for scale) | 5.5M rings cumulative, about 3M in the last year | to Oct 2025 | https://techcrunch.com/2025/10/14/smart-ring-maker-oura-raises-900m-from-fidelity | snippet only |

### 1.6 Market gaps (not found)

Worldwide e-reader unit shipments and the Kindle installed base (Amazon does not disclose); smart displays split from smart speakers; a full-year smart speaker total from one open source; a Europe-only home décor figure (Eurostat COICOP division 05, dataset nama_10_co3_p3, is the official denominator to open next); EU households (not individuals) with smart home devices; Skylight and Aura revenue (only Nixplay files audited revenue: US$20.0M in 2023, loss US$5.0M, SEC Form 1-K, https://www.sec.gov/Archives/edgar/data/1946957/000168316824002773/nixplay_1k-123123.htm, verified); E Ink revenue in USD (needs a dated TWD/USD rate). US home décor market for context: USD 191.5bn 2025 (IMARC, verified, https://www.imarcgroup.com/united-states-home-decor-market-statistics, 2026-02-10).

---

## 2. Competition

### 2.1 AI consumer hardware

| Product | Price | Subscription | Funding | Units or revenue | Status Nov 2026 | Source | Tag |
|---|---|---|---|---|---|---|---|
| Humane Ai Pin | $699 at launch, cut to $499 Oct 2024 | $24/month | more than $230M | about 10,000 shipped, about $9M lifetime sales, about $1M returns (Aug 2024) | Dead. HP bought most assets for $116M (18 Feb 2025); devices stopped working 28 Feb 2025 | https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m ; https://www.macrumors.com/2024/08/07/humane-ai-pin-returns ; https://pcgamer.com/software/ai/the-usd699-ai-pin-that-launched-less-than-a-year-ago-is-going-to-stop-working-at-the-end-of-february | verified (TechCrunch, MacRumors); $24/month snippet only |
| Rabbit r1 | about $199 | none known | $20M led by Khosla plus $10M (2023) | over 100,000 sold, about 5,000 daily users (Sept 2024) | Alive, software-led: rabbitOS 3 generally available 22 Sep 2026; "project cyberdeck" announced Jan 2026; late-2025 Tom's Guide headline on unpaid staff | https://9to5google.com/2024/09/26/rabbit-5000-people-use-the-r1-daily/ ; https://www.rabbit.tech/updates ; https://www.scmp.com/tech/big-tech/article/3249380/ | verified (9to5Google, rabbit.tech); price and funding snippet only |
| Friend pendant | $99 announced (2024), $129 (2025), Friend 2.0 $249 (Aug 2026) | none, then $9.99/month memory on 2.0 | about $7M (Pace, Caffeinated, Solana founders) | about 3,000 sold and 1,000 shipped by Oct 2025, about $348,000 revenue; 5,000-unit v1 run sold out by Aug 2026; $1M NYC subway campaign | Shipping v2 | https://www.fortune.com/2025/10/01/who-is-avi-schiffmann-friend-ai-pendant-necklace ; https://sfstandard.com/2026/08/02/avi-schiffmann-new-ai-friend-can-talk/ | verified |
| Plaud Note, NotePin, Note Pro | Note Pro $179 | free 300 min/month; Pro $99.99/yr or $17.99/month; Unlimited $239.99/yr; "nearly 50% of users upgrading to the Pro plan" | self-funded per company (snippet) | over 1M units (Aug 2025); more than 2M devices and software ARR above $100M (June 2026) | The commercial winner of the category | https://techcrunch.com/2025/08/27/plaud-launches-a-new-ai-hardware-notetaker-the-179-note-pro ; https://eu.36kr.com/en/p/3961453579746437 ; https://www.plaud.ai/products/plaud-ai-annual-pro-plan-yearly | verified (TechCrunch, 36Kr); plan prices snippet only |
| Limitless pendant | $99 | existing customers moved to a free plan | more than $33M (a16z, First Round, NEA) | not public | Acquired by Meta, 5 Dec 2025; hardware sales stopped | https://www.techcrunch.com/2025/12/05/meta-acquires-ai-device-startup-limitless/ | verified |
| Bee Pioneer wristband | $49.99 | $19/month | $7M (2024) | not public | Acquired by Amazon, announced 22 Jul 2025 | https://techcrunch.com/2025/07/22/amazon-acquires-bee-the-ai-wearable-that-records-everything-you-say/ | verified |
| Meta Ray-Ban glasses, Ray-Ban Display | Display $799 with Neural Band | none | public companies | more than 7M smart glasses sold in 2025, more than triple 2024 (EssilorLuxottica) | Growing; the only AI wearable with mass sales | https://techcrunch.com/2025/09/17/meta-unveils-new-smart-glasses-with-a-display-and-wristband-controller ; https://uploadvr.com/meta-essilorluxottica-sold-7-million-smart-glasses-in-2025/ | verified |
| OpenAI device (with Jony Ive) | n/a | n/a | io acquired for $6.5bn (May 2025) | n/a | Court filing: no customer shipments before end of Feb 2027 | https://www.macrumors.com/2025/05/22/details-leak-jony-ive-openai-device/ ; https://www.macrumors.com/2026/02/10/openais-jony-ive-designed-device-delayed-to-2027/ | verified |
| Omi (Based Hardware) | $89 at launch | not stated | about $700k, then a $2M round (Jan 2025) | $10M ARR claim unverified | Selling | https://techcrunch.com/2025/01/08/omi-a-competitor-to-friend-wants-to-boost-your-productivity-using-ai-and-a-brain-interface | verified (TechCrunch); later figures snippet only |
| Nothing, first AI-native device | not announced | not announced | Nothing raised $200M Series C (Sept 2025) | n/a | Announced 4 Nov 2026, "ships next month" (Dec 2026); "no new screen" | https://www.techrepublic.com/article/news-nothing-ai-device-december-2026-launch/ ; https://news.crunchbase.com/ai/wearable-technology-startup-funding-oura/ | verified |

Funding context: global AI venture funding US$202.3bn in 2025 to 16 Dec, up more than 75% from US$114bn in 2024 (Crunchbase News, verified, https://news.crunchbase.com/ai/big-funding-trends-charts-eoy-2025/, 2025-12-16). Wearables take less than 1% of venture funding in a year (Crunchbase News, verified, 2025-10-20). No consumer-AI-hardware total exists from Crunchbase, PitchBook or CB Insights: [placeholder].

Lessons, each labelled: reviewers found Humane "slower than the phone in your pocket" and it died with its cloud (opinion, from the record above); Rabbit's 5,000 daily users on 100,000 sold is a 5% retention rate (9to5Google's arithmetic); Friend spent one seventh of its funding on ads and sold 3,000 units (facts above; reading is opinion); Plaud's narrow job plus a paid software tier that about half of buyers take is the pattern that worked (opinion); Meta's glasses sold because they were already good sunglasses from a trusted brand before the AI arrived (opinion, and the strongest argument for a premium-brand thesis).

### 2.2 E-ink, ambient and display products

| Product | Price | Subscription | Promptable? | Scale | Status Nov 2026 | Source | Tag |
|---|---|---|---|---|---|---|---|
| TRMNL OG 7.5in, BWRY, X 10.3in | OG $139, BWRY $139, X $229; Developer Edition $10 add-on; BYOD licence $50 one-time | none | not natively; owners write plugins with Claude or ChatGPT, one testimonial mentions MCP | 14,500 X orders in 16 months; 1,000+ plugins | Active; OG sold out until mid-December 2026 | https://trmnl.com/ ; https://trmnl.com/b2b/pricing-sheet ; https://trmnl.com/blog/on-x | verified (BYOD and stock lines snippet only) |
| Aura frames; Aura Ink 10in and 13in e-paper (Spectra 6) | Carver $139 to Astra $399; Aura Ink 13in $499 list ($469 Black Friday) | none, "no subscription fees" | no | about 1M frames by Nov 2022; "single-digit millions" by Oct 2025; $26M (2022) and $60M growth capital (2025, LAGO); profitable | Active; Aura Ink launched Oct 2025, three months battery claim | https://auraframes.com/frames ; https://techcrunch.com/2025/10/21/aura-introduces-a-499-e-ink-digital-photo-frame-that-lets-you-go-cordless ; https://techcrunch.com/2022/11/22/aura-the-frame-and-photo-startup-raises-26m-as-app-users-near-3m-and-frames-sold-pass-500k/ | verified |
| Skylight Frame 2, Calendar 2, Calendar Max | Calendar 2 $319.99; Frame 2 with Plus $209.99 | Frame Plus $39/yr; Calendar Plus $79/yr | partly: "Skylight Assistant", an AI family assistant you text (Sept 2026) | more than 12M customers; 1.7M households on Calendar; bootstrapped; credit facility $75M (Sept 2026) | Active and growing | https://finviz.com/news/397117/skylight-expands-credit-facility-to-75-million-to-help-families-share-the-load-through-every-stage-of-life ; https://myskylight.com/products/skylight-plus | verified |
| reMarkable Paper Pro (11.8in colour e-paper) | from 649 EUR with Marker | Connect 3.99 EUR/month or 39.90 EUR/yr | partly: AI summaries and handwriting conversion in Connect | 2024: revenue US$434.3M, net profit US$24.7M, about 791,000 devices, about 568,000 subscribers; gross margin 43.4% in Q1 2025 | Active | https://remarkable.com/store/connect ; https://en.wikipedia.org/wiki/ReMarkable_(manufacturer) ; https://live.euronext.com/en/products/equities/company-news/2025-02-19-remarkable-invest-interim-financial-report-q4-2024 | prices verified; financials snippet only (Euronext PDFs did not parse) |
| Kindle Scribe 3, Scribe Colorsoft | Scribe from $499.99; Colorsoft from $629.99 | none | partly: AI search and summaries, "Send to Alexa+" | not disclosed | Shipping | https://www.aboutamazon.com/news/devices/new-amazon-kindle-scribe-color | verified |
| Nixplay | Classic 10.1in $189.99 list | Plus $29.99/yr | no LLM | "over 4 million customers"; 2023 revenue US$20.0M, loss US$5.0M (SEC) | Active | https://www.nixplay.com/ ; https://www.sec.gov/Archives/edgar/data/1946957/000168316824002773/nixplay_1k-123123.htm | verified |
| Meural Canvas II (Netgear) | no price shown | $8.95/month or $69.95/yr | no | not disclosed | Sales appear ended (ChannelNews), service running | https://www.netgear.com/home/digital-art-canvas/membership ; https://www.channelnews.com.au/exclusivenetgear-kills-off-meural-canvas/ | membership verified; discontinuation snippet only |
| Tidbyt Gen 2 (LED matrix) | $199 | none | no | 100,000 devices shipped | Acquired by Modal (7 Nov 2024); no new hardware, service kept running | https://modal.com/blog/tidbyt-is-joining-modal | verified |
| Daylight DC-1 (10.5in reflective LCD tablet) | $729 | none | no | first run of 5,000 sold out (2024); about $12M to 16M raised | In stock | https://daylightcomputer.com/ ; https://en.wikipedia.org/wiki/Daylight_Computer_Co. | verified (site), funding snippet only |
| InkPoster (PocketBook), Spectra 6 posters | Affresco 13.3in $449 ($499 list) to Duna 40.5in $6,500 | art subscription, price not listed | no (curated art) | not disclosed | Most models sold out | https://inkposter.com/ | verified |
| Visionect Joan (e-paper room signs, B2B) | Joan 6 RE from 349 EUR; Joan 13 Pro 899 EUR | from 49 EUR/month | partly: Teams booking agent | "thousands of workplaces" | Active | https://getjoan.com/pricing/ | verified |
| Fraimic Smart E Ink Canvas (Kickstarter 2025) | $299 pledge, $399 MSRP; large $729 | not found | yes: voice or text prompt generates artwork (ChatGPT images) | $1,120,290, 1,825 backers | shipping planned May 2026 | https://www.kicktraq.com/projects/445470967/fraimic-smart-e-ink-canvas-digital-picture-frame-with-ai/ | snippet only |
| Jitrainno Smart Canvas Echo (Kickstarter autumn 2026, wood frames, Spectra 6) | $289 early, $469 list (Echo-13); Echo-31 $1,499 | not found | yes: text or voice prompts to images | $132,000 at 11 Sept 2026; $286,008 later (BackerKit) | fulfilment from Nov 2026 | https://www.yankodesign.com/2026/09/11/this-color-e-ink-art-frame-lets-you-talk-to-your-wall-and-watch-it-paint-new-art/ | verified (Yanko), totals snippet only |
| BLOOMIN8 Canvas (Arpobot, Kickstarter 2025, IKEA-frame compatible) | not verified | not found | "AI-powered" in title; mechanics unverified | $1.58M to $2.40M, 2,272 backers (trackers disagree) | shipping | https://www.backerkit.com/projects/arpobot/bloomin8-canvas-the-ai-powered-full-color-e-ink-art-frame | snippet only |
| Onyx Boox Note Air 4C, Palma 2 | $529, $299 | none | no (Android) | not disclosed | Active | https://blog.the-ebook-reader.com/2025/03/17/onyxs-ereaders-and-enotes-now-10-40-more-expensive/ | snippet only |
| Dasung Paperlike monitors | $349 to $1,798 | none | no | not found | Active | https://www.tomshardware.com/monitors/portable-monitors/paperlike-color-portable-e-ink-monitor-hits-us-market-for-849-dollars | partly verified |
| Inkplate 6 and 10 (Soldered, dev boards) | not verified (sites blocked) | none | no | Inkplate 10: about $199k raised, 1,062 backers (2021) | Active | https://www.crowdsupply.com/soldered/inkplate-10 | snippet only |
| Waveshare PhotoPainter 7.3in | $88.99 to $90.99 | none | no | not found | original discontinued, (B) current | https://www.waveshare.com/photopainter.htm | verified |
| Divoom Pixoo 64; Pimoroni Inky Frame 7.3; Vobot MiniDock | Vobot about $55 (Kickstarter $187,939, 1,590 backers) | none | no | as stated | Active | https://www.kicktraq.com/projects/vobot/vobot-mini-dock-screen-equipped-dock-portal-to-infomation/ | snippet only; Divoom and Pimoroni prices [placeholder], sites rate-limited |

DIY community size signals (verified, accessed 2026-11-27): esp32-weather-epd 6.4k GitHub stars (https://github.com/lmarzen/esp32-weather-epd); OpenEPaperLink 1.9k stars (https://github.com/OpenEPaperLink/OpenEPaperLink); MagInkDash 178 stars (https://github.com/speedyg0nz/MagInkDash); TRMNL 1,000+ plugins. r/eink subscriber count: [placeholder], Reddit blocked.

### 2.3 The gap, as the record shows it

Facts: the only shipping or funded products configured by natural language today are AI art frames (Fraimic, Jitrainno; BLOOMIN8 unverified): a prompt produces a picture, not a layout, a data feed or a daily paper. TRMNL is the nearest dashboard competitor and has no built-in configurator; owners write plugins with Claude or ChatGPT themselves. reMarkable, Kindle Scribe, Skylight and Joan ship LLM features that are not display configuration. Aura, Nixplay, Meural, InkPoster, Tidbyt, Inkplate, Pimoroni, Waveshare, Divoom and Dasung show no natural-language configuration.

Opinion: no shipping product lets a non-technical owner describe in plain words what a personal e-ink display should show and have the device compose it. The nearest things are prompt-to-picture frames and prompt-to-code dashboards. TRMNL's 14,500 X orders and the $1.1M to $2.4M Spectra 6 frame campaigns show paying demand on both sides of that gap. Whether a premium brand can bridge it is not something these numbers prove.

Positions on the deck's competition map are the author's reading of each product's marketing (opinion), not measured.

---

## 3. Business model benchmarks

### 3.1 Hardware gross margins

| Company | Gross margin | Source | Date | Tag |
|---|---|---|---|---|
| Apple, Products | 36.8% FY2025 (37.2% FY2024); Services 75.4%; total 46.9% | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm | 10-K FY2025 | verified |
| Sonos | 43.7% GAAP FY2025 (45.4% FY2024) | https://investors.sonos.com/news-and-events/investor-news/latest-news/2025/Sonos-Reports-Fourth-Quarter-and-Fiscal-2025-Results/ | 2025-11-05 | verified |
| reMarkable | 43.4% Q1 2025 (42.6% Q1 2024); FY2024 margin up about 2 points "mainly due to higher subscription revenue" | https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2025/04/30/644812_Interim%20Financial%20Report%20-%20%20Q1%202025.pdf | 2025-04-30 | snippet only |
| Peloton, Connected Fitness Products | 13.6% FY2025; subscription 69.1%; total 50.9% | https://www.sec.gov/Archives/edgar/data/0001639825/000163982525000132/q42025shareholderletter.htm | 2025-08-07 | verified |
| GoPro | 33.8% GAAP 2024 | https://www.sec.gov/Archives/edgar/data/1500435/000162828025013046/gpro-20241231.htm | 10-K FY2024 | snippet only |
| Garmin | 58.7% FY2024 (vertically integrated, own factories) | https://www.garmin.com/en-US/newsroom/?p=5476 | Feb 2025 | snippet only |
| Logitech | 43.5% non-GAAP FY2025 | https://ir.logitech.com/press-releases/press-release-details/2025/Logitech-Announces-Q4-and-Full-Fiscal-Year-2025-Results/default.aspx | 2025-04-29 | snippet only |
| Kindle pricing stance | Bezos (2012): "We sell the hardware at our cost ... We want to make money when people use our devices, not when people buy our devices" | https://www.theregister.co.uk/2012/10/12/amazon_ceo_bezos_confirms_content_pays_for_kindle/ | 2012-10-12 | snippet only |

### 3.2 Subscription pricing and attach

| Product | Price | Attach or scale | Source | Tag |
|---|---|---|---|---|
| Plaud Pro, Unlimited | Pro $99.99/yr or $17.99/month; Unlimited $239.99/yr or $29.99/month; free tier 300 min/month | "nearly 50% users upgrading to the Pro plan" (TechCrunch, Aug 2025); software ARR above $100M on 2M+ devices (June 2026) | https://techcrunch.com/2025/08/27/plaud-launches-a-new-ai-hardware-notetaker-the-179-note-pro ; https://eu.36kr.com/en/p/3961453579746437 | attach verified; plan prices snippet only |
| reMarkable Connect | 3.99 EUR/month or 39.90 EUR/yr, 50-day trial | about 568,000 paying subscribers vs about 791,000 devices sold in 2024 (a stock against a flow, not an attach rate) | https://remarkable.com/store/connect ; https://en.wikipedia.org/wiki/ReMarkable_(manufacturer) | price verified; counts snippet only |
| Oura membership | $5.99/month or $69.99/yr; required for most insights | 5.5M rings cumulative; revenue above $1bn expected 2025 (company projection) | https://ouraring.com/membership ; https://techcrunch.com/2025/10/14/smart-ring-maker-oura-raises-900m-from-fidelity | price verified; scale snippet only |
| Whoop | One $199/yr, Peak $239/yr, Life $359/yr; hardware included | 2.5M+ members (third-party estimate, March 2026) | https://whoop.com/membership ; https://sacra.com/c/whoop/ | snippet only (whoop.com 403) |
| Peloton All-Access | price not in the letter [placeholder] | 2.80M paid connected fitness subscriptions; 1.8% average net monthly churn (Q4 FY25) | https://www.sec.gov/Archives/edgar/data/0001639825/000163982525000132/q42025shareholderletter.htm | verified |
| Meural membership | $8.95/month or $69.95/yr (another Netgear page shows $9.99/$99.99) | optional | https://www.netgear.com/home/digital-art-canvas/membership | snippet only, pages conflict |
| Skylight Plus | Frame $39/yr; Calendar $79/yr | optional; 1.7M Calendar households | https://myskylight.com/products/skylight-plus | verified |
| Nixplay Plus | $29.99/yr | subscribers +10,000 (+31%) in 2023, total not disclosed | https://www.sec.gov/Archives/edgar/data/1946957/000168316824002773/nixplay_1k-123123.htm | verified |
| Humane | $24/month required | dead | see 2.1 | snippet only |
| Friend 2.0 | $9.99/month memory | new | https://sfstandard.com/2026/08/02/avi-schiffmann-new-ai-friend-can-talk/ | verified |
| Aura, TRMNL, Tidbyt, Rabbit | no subscription | | see 2.2 | verified (Aura, TRMNL, Tidbyt) |
| Alexa+ | $19.99/month, free with Prime; "over 600 million Alexa devices" | | https://www.aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence | verified, 2025-02-26 |

A general consumer-hardware subscription attach benchmark from an analyst or VC: [placeholder], none found. The Plaud and reMarkable rows are the named datapoints.

### 3.3 Pre-orders, crowdfunding and ads

| Metric | Value | Source | Date | Tag |
|---|---|---|---|---|
| Core Devices (Pebble) pre-orders | 25,000 watch pre-orders and about 5,000 ring pre-orders by Jan 2026; five employees, no outside funding, nothing built before it is sold; Core 2 Duo $149, Time 2 $225 | https://techcrunch.com/2026/01/12/pebble-founder-says-his-new-company-is-not-a-startup | 2026-01-12 | verified (a 50,000 figure in Stark Insider, Aug 2025, conflicts; unresolved) |
| TRMNL X | 14,500 orders in 16 months | https://trmnl.com/blog/on-x | 2026-11-11 | verified |
| Fraimic | $1,120,290, 1,825 backers | kicktraq (above) | 2025 | snippet only |
| BLOOMIN8 | $1.58M to $2.40M, 2,272 backers | backerkit (above) | 2025 | snippet only, trackers disagree |
| Jitrainno | $286,008 (goal $39,181) | backerkit (above) | 2026 | snippet only |
| Daylight DC-1 | all five 2024 Founder's Edition batches sold out, first three within 24 hours | https://bgr.com/tech/daylight-computer-co-ceo-anjan-katta-on-building-a-healthier-computer/ | 2024 | snippet only |
| Kickstarter 2025 | "Design and Technology had the category's biggest year in Kickstarter history"; no totals published | https://updates.kickstarter.com/a-year-in-review-2025-kickstarter-highlights/ | 2025-12-23 | verified |
| Kickstarter Technology success rate | about 20% (secondary, undated) | https://searchlogistics.com/learn/statistics/kickstarter-stats-facts | undated | snippet only |
| Meta ads benchmarks, all industries | 2026: traffic CTR 1.93%, CPC $0.60; lead campaigns CTR 2.70%, CPC $1.80, CVR 8.54%, CPL $27.39 (CVR is form fills, not purchases); no CPM published | https://localiq.com/blog/facebook-advertising-benchmarks/ | updated 2026-09-23 | verified |
| Ad-to-pre-order conversion or CAC for DTC hardware | [placeholder] | | | not found |

### 3.4 Shenzhen ODM and cost benchmarks

| Item | Value | Source | Date | Tag |
|---|---|---|---|---|
| ODM MOQ, consumer electronics | commonly 500 to 5,000 units; Shenzhen "relatively flexible on small batches"; custom moulds raise the first-order MOQ | https://www.cosmosourcing.com/blog/moq-meaning-minimum-order-quantity ; https://www.chinaimportal.com/?p=8724 | undated | snippet only |
| Injection mould tooling | simple two-part single-cavity $2,000 to $5,000; complex $5,000 to $15,000; aluminium soft tooling $1,500 to $4,000 for runs under 5,000 | https://dev.to/china-sourcing-agents/injection-mold-tooling-costs-for-electronics-enclosures-16dl ; https://blog.hackster.io/summary-of-the-costs-to-develop-scale-and-manufacture-a-new-electronic-hardware-product-906311642639 | undated | snippet only; opinion: a wood or lacquer frame may avoid injection tooling entirely |
| 7.5in e-ink panel, 800x480 (Good Display GDEY075T7) | $28.64 single unit (Black Friday; list $34.92); panel only | https://buy-lcd.com/products/gdey075t7 | accessed 2026-11-27 | verified |
| 13.3in e-ink panel with driver HAT, 960x680 (Waveshare) | $144.99 single; $141.59 at 50 to 99 units | https://www.waveshare.com/13.3inch-e-paper-hat-k.htm | accessed 2026-11-27 | verified; retail, not ODM volume pricing |
| 10.3in panel; E Ink Spectra 6 colour panel | [placeholder] | | | no price found |
| ESP32-S3-WROOM-1 module | $4.93 at 1 unit to $3.35 at 1,300+ (LCSC); $3.52 to $3.30 (Future); N16R8 $6.56 (Digi-Key) | https://lcsc.com/product-detail/image/ESP32-S3-WROOM-1-N8R8_C2913201.html ; https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N16R8/16162642 | accessed 2026-11-27 | snippet only |
| Battery and charging board; PCB assembly per unit | [placeholder] | | | not reached |
| COGS-to-retail multiple | 2x to 4x COGS, ideally at least 3x (Predictable Designs); 2.5x to 4x BOM (Bolt); at least 3x, winners 4x to 5x (Sinovation); about 4x (Make) | https://predictabledesigns.com/how-to-price-your-new-electronic-hardware-product/ ; https://blog.bolt.io/?p=112 ; https://www.sinovationventures.com/blog/consumer-iot-start-up-advice | undated | snippet only |
| Certification (CE, RoHS, RED, FCC) for a Wi-Fi device | $3,000 to $8,000 with a pre-certified wireless module; "well over fifty thousand dollars" with a custom radio (Predictable Designs); FCC $4,900 to $10,000 with a pre-certified module (Compliance Testing) | https://predictabledesigns.com/certification-costs-what-it-really-takes/ ; https://compliancetesting.com/fcc-certification-faqs/fcc-certification-cost/ | 2026-01-17; undated | first verified, second snippet only |
| EU 150 EUR customs de minimis | political agreement 13 Nov 2025 to remove it, application in 2026; Council Regulation (EU) 2026/382 and a flat 3 EUR per-item interim duty from 1 Jul 2026 reported | https://taxation-customs.ec.europa.eu/news/e-commerce-150-eur-customs-duty-exemption-threshold-be-removed-2026-2025-11-13_en ; https://eur-lex.europa.eu/eli/reg/2026/382/oj | 2025-11-13 | first verified; regulation and 3 EUR snippet only; relevant only to drop-shipping single units |
| EU duty on heading 8528 52 (monitors), EU VAT rate | [placeholder]; check TARIC for the 10-digit code and China origin; import VAT applies at the destination rate | | | unverified |
| Panel channel for small brands | Good Display (buy-lcd.com) and Waveshare sell single panels and tiered retail to 99 units; Pervasive Displays and E Ink licensing terms [placeholder] | URLs above | accessed 2026-11-27 | verified by the listings |

Hero unit cost and MOQ: **[placeholder]**, by Oscar's instruction; the panel and module prices above are the only sourced inputs so far.

---

## 4. The problem

| Claim | Value | Source | Date | Tag |
|---|---|---|---|---|
| Smart home frustration | 52% of DIY smart home users report setup or connectivity issues; 45% of US internet households own a core smart home device (survey base not stated) | https://www.parksassociates.com/blogs/pr-smart-home/parks-associates-52-of-diy-smart-home-users-report-setup-or-connectivity-issues | 2025-07-09 | verified |
| Returns caused by setup | 36% of US broadband households that returned a CE or smart home device cited setup, installation or usage difficulty | https://www.parksassociates.com/blogs/in-the-news/36--of-ce-and-smart-home-product-returns-due-to-setup--installation-problems9 | undated | snippet only |
| The biggest assistant's economics | Amazon's devices division lost $25bn over 2017 to 2021 (WSJ, via TechCrunch); a former senior employee: "We worried we've hired 10,000 people and we've built a smart timer"; Alexa in 100M homes, 400M devices (2024) | https://techcrunch.com/2024/08/10/as-alexa-turns-10-amazon-looks-to-generative-ai/ | 2024-08-10 | verified (WSJ original paywalled) |
| Alexa+ | $19.99/month, free with Prime; "over 600 million Alexa devices out there today" | https://www.aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence | 2025-02-26 | verified, primary |
| Willingness to pay for bolt-on AI | half of US smartphone owners would not pay extra for AI features (CNET/YouGov, May 2025); about 35% of US consumers do not want AI built into devices at all (Circana) | https://www.emarketer.com/content/consumers-unwilling-pay-ai-features-1 ; https://www.tomshardware.com/tech-industry/artificial-intelligence/one-third-of-consumers-reject-ai-on-their-devices-with-most-saying-they-simply-dont-need-it-latest-report-highlights-privacy-fears-and-potential-costs-among-other-real-world-concerns | 2025 | snippet only; opinion: this supports "AI must be the product, not a feature tax" |
| Paying for generative AI tools | about four in ten surveyed genAI users say they or their household pay for genAI tools or services (Deloitte 2025) | https://www.deloitte.com/us/en/insights/industry/telecommunications/connectivity-mobile-trends-survey.html | 2025 | snippet only |
| Screen time | adult internet users average 6h38m online per day, 3h46m of it on mobile (GWI via DataReportal) | https://datareportal.com/reports/digital-2025-global-overview-report | Feb 2025 | verified |
| Feature phones | about 15% of handsets sold globally in 2024 were feature phones (about 210M units, USD 3.2bn), only 1.7M in North America and 12M in Europe, category "gradually declining" | https://counterpointresearch.com/en/insights/Dumbphones%20are%20getting%20smarter%20and%20more%20premium.%20Are%20they%20the%20solution%20for%20disillusioned%20phone%20addicts | 2025-10-01 | verified; opinion: this does not support a "dumbphone boom" claim, so the deck does not make it |
| E-ink comfort and power (manufacturer claims) | reflective, no backlight; bistable, "no power is required to maintain an image", update power "of the order of microwatts"; users report less eye fatigue than LCD (stated as feedback, not a study) | https://www.eink.com/benefits.html | accessed 2026-11-27 | verified; no peer-reviewed study found; do not use E Ink's blog claim "3x healthier than LCD (Harvard)", no study is cited |
| First-wave AI gadget outcomes | Humane dead (10,000 shipped, $230M+); Rabbit 5% daily use; Friend 3,000 sold | section 2.1 | | verified |
| Matter adoption | no certified-device count found; CSA has 850+ members; Matter 1.5 released Nov 2025; ABI: "limited number of Matter devices relative to total smart home devices" | https://connect.csa-iot.org/alliance-year-in-review-2025-reflections-seasons-greetings ; https://www.abiresearch.com/market-research/insight/7787351-the-release-of-matter-15-specifications-ma | Dec 2025 | snippet only |

Not found: apps per smart home household; IoT or smart speaker abandonment rates; Light Phone, Daylight or reMarkable growth rates; a peer-reviewed e-ink eye-comfort study.

---

## 5. Why now

### 5.1 LLM price curve

Headlines (verified): a16z, "LLMflation": "For an LLM of equivalent performance, the cost is decreasing by 10x every year"; GPT-3 cost $60 per million tokens at launch (Nov 2021), a model matching it cost $0.06 in 2024, a 1,000x drop in three years (https://a16z.com/llmflation-llm-inference-cost/, 2024-11-12). Epoch AI: decline "ranging from 9x to 900x per year" depending on the capability milestone; 40x per year for matching GPT-4 on GPQA Diamond (https://epoch.ai/data-insights/llm-inference-price-trends, 2025-03-12).

Chart series (Epoch AI's lowest price to match a fixed capability tier, USD per million tokens on Epoch's blended metric; all rows https://epoch.ai/data-insights/llm-inference-price-trends, 2025-03-12, verified):

| Tier | Model | Date | USD per 1M tokens |
|---|---|---|---|
| GPT-4 level (MMLU 86) | GPT-4-0314 | 2023-03-14 | 37.50 |
| GPT-4 Turbo level (MMLU 87) | GPT-4 Turbo | 2023-11-06 | 15.00 |
| GPT-4o level | GPT-4o | 2024-05-13 | 7.50 |
| above GPT-4 Turbo (MMLU 88) | Gemini 2.0 Flash | 2025-02-05 | 0.18 |
| GPT-3 level (MMLU 44) | GPT-3 | 2021-11-20 | 60.00 |
| GPT-3.5 level (MMLU 68) | GPT-3.5 Turbo | 2023-03-06 | 2.00 |

My arithmetic: GPT-4-level price fell from 37.50 (Mar 2023) to 0.18 (Feb 2025), about 208x in two years.

Official list prices today, USD per million output tokens (input in brackets), all verified on the providers' pages, accessed 2026-11-27: GPT-5 nano 0.40 (0.05), GPT-5 mini 2 (0.25), GPT-5 10 (1.25) (https://developers.openai.com/api/docs/pricing); Gemini 2.5 Flash-Lite 0.40 (0.10), Gemini 2.5 Flash 2.50 (0.30), Gemini 2.5 Pro 10 (1.25) (https://aistudio.google.com/docs/pricing); Claude Haiku 5.5 0.50 (0.10), Claude Sonnet 5.5 10 (2), Claude Opus 5.5 20 (4), Claude Fable 5.2 40 (8) (https://platform.claude.com/docs/en/about-claude/pricing). Anthropic's Batch API gives 50% off. A daily personalised page on a small model therefore costs a fraction of a cent per edition at list prices; any such number on a slide is an estimate and should carry the token count assumed.

### 5.2 Models, protocols, agents

| Claim | Value | Source | Date | Tag |
|---|---|---|---|---|
| Small models on edge hardware | Gemma 3n: 5B and 8B raw parameters with the memory overhead of 2B and 4B models, "dynamic memory footprint of just 2GB and 3GB", built for phones, tablets and laptops; audio, text and images | https://developers.googleblog.com/en/introducing-gemma-3n/ | 2025-05-20 | verified |
| Model Context Protocol launch | Anthropic: "an open standard that enables developers to build secure, two-way connections" between data sources and AI tools; pre-built servers for Google Drive, Slack, GitHub, Postgres | https://www.anthropic.com/news/model-context-protocol | 2024-11-25 | verified |
| MCP neutral governance and adoption | Linux Foundation forms the Agentic AI Foundation with MCP, goose and AGENTS.md as founding projects; founding contributions from Anthropic, Block and OpenAI; platinum members include AWS, Bloomberg, Cloudflare, Google, Microsoft; "more than 10,000 published MCP servers"; adopted by Claude, Cursor, Microsoft Copilot, Gemini, VS Code, ChatGPT | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | 2025-12-09 | verified |
| Enterprise generative AI spend | USD 37bn in 2025, up from 11.5bn in 2024; 76% of use cases bought rather than built; only 16% of enterprise deployments qualify as true agents | https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/ | 2025-12-09 | verified |
| Microcontroller volume | Espressif: "1.5 Billion+" IoT SoC shipments, "10,000+" customers | https://www.espressif.com/en/company/about-us/who-we-are | accessed 2026-11-27 | verified |
| EU AI Act dates | in force 1 Aug 2024; GPAI obligations from 2 Aug 2025; applicable 2 Aug 2026 with exceptions; Annex III high-risk rules to 2 Dec 2027 and Annex I to 2 Aug 2028 after the AI Omnibus | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | accessed 2026-11-27 | verified; opinion pending a legal read: a consumer e-ink display is not a listed high-risk use; transparency duties apply |

### 5.3 E-paper trend

| Claim | Value | Source | Date | Tag |
|---|---|---|---|---|
| E Ink Holdings revenue 2023 | NT$27.12bn (-9.8% YoY) | https://stockanalysis.com/quote/tpex/8069/revenue/ | updated 2026-11-11 | verified (aggregator of filings) |
| E Ink Holdings revenue 2024 | NT$32.16bn, +19%; net income NT$8.87bn, +14% | https://finance.technews.tw/2025/03/05/e-ink-holdings-2024-q4-earnings/ | 2025-03-05 | verified |
| E Ink Holdings revenue 2025 | NT$36.1bn, +12%, second highest in company history; net income NT$10.5bn, +19%, record; EPS NT$9.14, record | https://quartr.com/events/e-ink-holdings-inc-8069-q4-2025_F92eLSel | 2026-04-13 | verified (earnings-call aggregator); the annual report PDF at eink.com did not parse |
| E Ink 2026 outlook | growth guided 20 to 25%; Spectra 6 colour e-paper the largest shipment area in Q1 2026 | https://quartr.com/events/e-ink-holdings-inc-8069-q1-2026_F92e3b2l | Q1 2026 | snippet only |
| Digitimes on E Ink | "record revenue and operating profit in 2025" | https://www.digitimes.com/news/a20260402PD214.html | 2026-04-02 | verified for that sentence; wording conflicts with "second highest", so the deck says "record profit" |
| Incumbent validation of e-paper frames | Aura Ink, 13.3in Spectra 6, $499, Oct 2025; InkPoster (PocketBook) Spectra 6 posters sold out; three Spectra 6 frame Kickstarters raised $0.3M to $2.4M in 2025 and 2026 | section 2.2 | | verified (Aura, InkPoster); campaign totals snippet only |
| E-paper market CAGR | 11.5% (IMARC) to 17% (GMI) | section 1.3 | | verified |

Not found: Spectra 6, Kaleido 3 and Gallery 3 launch dates from E Ink press releases; an ESP32 price series over time; consumer AI hardware funding totals; a 2024 to 2026 primary statement on Shenzhen access for small brands (HAX material is pre-2024; opinion: Oscar's own supplier quotes will be better evidence).

---

## 6. Placeholders and open items for Oscar

Allowed by Oscar: catalogue renders and prices (Sat 28 Nov), brand name, hero unit cost and MOQ.

Not found in research: a 10.3in and a Spectra 6 colour panel price; battery, charging and PCBA per-unit costs; EU TARIC duty on the hero's heading; ad-to-pre-order conversion for DTC hardware; a consumer-hardware subscription attach benchmark; worldwide e-reader shipments; EU household smart-home share; a dated TWD/USD rate for E Ink revenue; r/eink size; Divoom and Pimoroni prices; reMarkable 2025 full-year results.

Snippet-only figures that carry weight on the slides and should be opened before the coffee: Omdia smart speaker units and ASP (SAM); Eurostat 19% smart speaker use (funnel); reMarkable 2024 financials (ladder, margins); Rabbit price and funding; Plaud plan prices; ODM MOQ and tooling ranges; ESP32 module prices.

The vault notes of the 25 Nov calls and the "existing 9-slide outline" were not reachable from this run (shell search outside the repo is blocked; the two guessed vault paths did not exist). The deck uses the structure in Oscar's payload.
