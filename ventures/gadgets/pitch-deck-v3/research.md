# Gadgets pitch deck v3: research and sources

Written 2026-11-27 for Oscar's edit. **v3 (same day) adds section 7**, the global market by region and the worldwide funnel, after Oscar's ask: "in the market, get claude to research for the whole world, give me a market size by region overall, then break up the total market like you did in the bottom up". Sections 1 to 6 are v2's, unchanged except for slide numbers (the market is now slides 5 and 6, so competition is slide 7, business model slide 8). Section 1.4 still holds the Spain, France, Germany inputs that section 7 reuses as the beachhead. v2 replaced v1 after Oscar's correction (decision of 27 Nov 09:57): the flagship is the concept itself, one premium brand with a multi-category collection of decorations, gadgets and other objects for the home. The personal digest (PersonalPress) is not part of the collection and is not in the deck (it is named here only to say so). Gadgets is Oscar's solo project: no one else appears as team. No valuation, round size or equity appears anywhere.

Method: three parallel research passes (market sizing; competition; business model, problem and why-now), each with WebSearch and WebFetch, merged here. Problem and why-now items that did not change from v1 are carried over from `../pitch-deck-v1/research.md` (sections 5.1 and 5.2) with their original tags.

How to read the tags:
- **verified**: the page was opened and the figure read on it.
- **snippet only**: the figure came from a search result; the page was blocked, paywalled or not opened. Unverified: treat as "reported". The deck marks these sources with a star.
- **my arithmetic**: derived from sourced inputs; the formula is shown.
- **assumption**: a number chosen by the author, labelled as such, to be replaced with pilot data.
- **opinion**: the author's reading.
- **[placeholder]** and **[not found]**: not available. Placeholders also mark inputs Oscar owns: brand name, renders and prices (due Sat 28 Nov), unit cost and MOQ.

Scoping note: the research briefs used a working price range of 30 to 400 EUR per object to choose comparables. That range is not Oscar's and does not appear in the deck. Prices per object are placeholders.

---

## 1. Market

### 1.1 Method

Two views that should land in the same order of magnitude, each from different kinds of source:
1. **Top-down**: global decor market, narrowed to Europe plus the US, to online sales, then to the premium tier. Every narrowing step applies a ratio from one publisher to a different geography; those steps are assumptions and are labelled.
2. **Bottom-up**: households in Spain, France and Germany, to online buyers, to buyers of home items online, to premium design-object buyers, to customers of the brand. The last two ratios are assumptions with no source; they are placeholders to replace with a pilot conversion rate or a survey.

Publishers disagree widely on decor (1.5x on the same year) because scopes differ. The deck uses the lowest, narrowest base (GMI) and removes furniture.

### 1.2 Top-down inputs

| Metric | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| Global home decor 2025 (GMI) | US$680.6bn; 2026 US$702.3bn; 2035 US$950.8bn; CAGR 3.4%. Furniture US$391.5bn, so non-furniture US$289.1bn (680.6 minus 391.5) | https://www.gminsights.com/industry-analysis/home-decor-market | Aug 2026 | verified; 289.1 my arithmetic |
| Global home decor 2025 (Fortune Business Insights) | US$802.26bn; 2034 US$1,299.88bn; includes furniture, textiles, flooring, lighting, accessories | https://www.fortunebusinessinsights.com/home-d-cor-market-109906 | page updated 9 Nov 2026 | verified |
| Global home decor (Grand View Research) | US$1,037.14bn (page labels it 2025 and 2026 in different places); 2030 US$1,622.9bn; furniture 50.7% of revenue | https://www.grandviewresearch.com/industry-analysis/home-decor-market | published Dec 2024, updated May 2026 | verified; internally inconsistent year labels |
| Global home decor (Mordor) | 2026 US$716.5bn; 2032 US$955.3bn; 2025 US$681.05bn only in a snippet | https://www.mordorintelligence.com/industry-reports/home-decor-market | updated 22 Oct 2026 | verified (2026); snippet only (2025) |
| IMARC global; Statista narrow "Home Decor" | IMARC US$810.5bn 2025 (snippet); Statista US$133.6bn 2024 (narrow B2C segment, page 403) | https://www.statista.com/outlook/cmo/furniture/home-decor/worldwide | 2024 | snippet only |
| Europe home decor 2025 (GMI) | US$188.5bn; 2035 US$250.1bn; CAGR 2.9%; includes furniture | https://www.gminsights.com/industry-analysis/home-decor-market | Aug 2026 | verified |
| Europe home decor 2025 (Fortune BI) | US$124.99bn (15.6% of global) | https://www.fortunebusinessinsights.com/home-d-cor-market-109906 | 9 Nov 2026 | verified |
| Europe mid-to-high-range decor (GMI) | US$55bn 2025, 2035 US$83.18bn, CAGR 4.34%. Tiers: medium US$50 to 200, high US$200 to 1,000, premium above US$1,000. Germany US$11.0bn, Spain US$4.4bn, France 13.45% share (about US$7.4bn, my arithmetic) | https://www.gminsights.com/industry-analysis/europe-mid-to-high-range-home-decor-market | Oct 2026 | verified |
| Eurostat, EU27 household consumption, COICOP CP05 (furnishings, household equipment, maintenance), 2022 | EUR 471,052.5M; CP051 furniture, carpets EUR 160,165.6M; CP052 household textiles EUR 34,964.3M; CP054 glassware, tableware, utensils EUR 44,550.7M. Germany CP05 EUR 130,085M, France EUR 62,731M, Spain EUR 34,928M. No data after 2022. CP05 includes appliances and maintenance: not decor-only | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_co3_p3?format=JSON&geo=ES&geo=FR&geo=DE&geo=EU27_2020&coicop=CP05&coicop=TOTAL&unit=CP_MEUR&sinceTimePeriod=2020 | 2022 data | verified (fetched from the API) |
| US home decor 2025 (IMARC) | US$191.5bn; 2034 US$257.0bn; CAGR 3.23%; includes furniture | https://www.imarcgroup.com/united-states-home-decor-market-statistics | 2026-02-10 | verified |
| US furniture and home furnishings stores (Census NAICS 442, via FRED) | 2025 US$127,347M; 2024 US$125,026M (+1.9%); store sales only | https://fred.stlouisfed.org/data/MRTSSM442USN | series to Sep 2026 | verified; growth my arithmetic |
| US household furnishings and equipment per consumer unit (BLS CES) | US$2,355 in 2025 (US$2,414 in 2024); 137,994 thousand consumer units; implied total about US$325bn (my arithmetic); includes appliances | https://www.bls.gov/news.release/cesan.nr0.htm | 2026-10-29 | verified |
| Luxury home decor (Custom Market Insights) | US$151.82bn 2025; no definition of "luxury"; 22% of GMI's global total, which looks too high (opinion, report mill) | https://www.custommarketinsights.com/report/luxury-home-decor-market | updated Jan 2026 | verified; not used |
| Smart lighting 2025 (MarketsandMarkets) | US$9.86bn; 2032 US$20.5bn; includes commercial, industrial and street lighting; GMI gives US$18bn (snippet) | https://www.marketsandmarkets.com/Market-Reports/smart-lighting-market-985.html | Oct 2026 | verified |
| Portable Bluetooth speakers 2025 (Fortune BI) | US$16.29bn; CAGR 11.86%; other publishers US$6.75bn to 19.5bn (3x spread, snippets) | https://www.fortunebusinessinsights.com/smart-home-market-105011 (the URL serves the Bluetooth speaker report) | 9 Nov 2026 | verified |
| Consumer electronics accessories (Persistence) | US$187.8bn 2026; scope includes phone cases and chargers | https://www.persistencemarketresearch.com/mediarelease/consumer-electronic-accessories-market.asp | Aug 2026 | verified; not used (scope too broad) |
| Online share of decor, global (GMI) | 41.5% (US$282.4bn) in 2025, 46% by 2035 | https://www.gminsights.com/industry-analysis/home-decor-market | Aug 2026 | verified |
| Online share, Europe mid-to-high (GMI) | about 38% in 2025 (1 minus 34.10/55) | https://www.gminsights.com/industry-analysis/europe-mid-to-high-range-home-decor-market | Oct 2026 | my arithmetic |
| Online share of European DIY, home and garden | 17% in 2025, 13.7% in 2022, 8.9% in 2019; online market EUR 66bn of EUR 388bn | https://www.diyinternational.com/content/news/2026/03/24/plus/e-commerce-share-in-the-diy-sector-is-growing.html | 2026-03-24 | verified |

### 1.3 Top-down ladder (the figures on the slide)

| Step | Arithmetic | Result | Tag |
|---|---|---|---|
| Global decor without furniture | 680.6 minus 391.5 (GMI 2025) | US$289.1bn | my arithmetic |
| Adjacent gadget categories, upper bound | smart lighting 9.86 + Bluetooth speakers 16.29; scope broader than home, overlap unknown | US$26.2bn | my arithmetic; additivity is an assumption |
| **TAM** | 289.1 + 26.2 | **about US$315bn** | my arithmetic |
| EU plus US decor without furniture | (188.5 + 191.5) x 42.5%; 42.5% = 289.1/680.6, the global non-furniture share applied to Europe and the US | US$161.5bn | assumption |
| Of which online | 161.5 x 41.5% (GMI global online share applied to EU and US) | US$67.0bn | assumption |
| **SAM**: premium tier | 67.0 x 29%; 29% = 55/188.5, GMI's European mid-to-high share applied to EU and US | **about US$19bn** | assumption |

Caveats: the GMI Europe figure includes the UK and non-EU countries; inputs come from three reports; the three narrowing ratios each rest on one publisher. The SAM excludes gadgets (not sized for EU and US).

### 1.4 Bottom-up funnel, Spain, France, Germany

| Step | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| Households, Spain | 19,746,638 on 1 Jan 2026 | https://ine.es/dyngs/Prensa/en/ECP4T25.htm?print=1 | 2026-02-12 | verified |
| Households, Germany | 41.8M in 2024 | https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/11/PD26_386_122.html | 2026-11-05 | verified |
| Households, France | about 30.9M on 1 Jan 2022; no later figure found | https://www.insee.fr/fr/statistiques/8612510 | 2025-11-18 | verified |
| Households, three countries | 19.75 + 30.9 + 41.8 = 92.5M | derived | | my arithmetic; mixed years |
| Individuals who bought online in the last 12 months, 2025 | DE 81.38%, FR 80.15%, ES 70.77%, EU 73.56% | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_ec_ib20?format=JSON&geo=ES&geo=FR&geo=DE&geo=EU27_2020&ind_type=IND_TOTAL&unit=PC_IND&sinceTimePeriod=2024 | 2025 | verified (fetched from the API) |
| Online-buying households | 41.8 x 0.8138 + 30.9 x 0.8015 + 19.75 x 0.7077 = 34.0 + 24.8 + 14.0 = 72.8M; individuals' rate used as a household proxy | derived | | assumption |
| EU individuals buying furniture, home accessories or garden items online in the last 3 months | 19% (2024), EU-wide, base: internet users | https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250220-3 | 2025-02-20 | verified |
| Bought home items online | 72.8M x 19% = 13.8M; the 3-month rate applied to all three countries as a conservative floor for annual buyers | derived | | assumption |
| Premium design-object buyers | 13.8M x 10% = 1.38M. **ASSUMPTION**, no source; range 5% to 15% | | | assumption |
| Customers of the brand, year 3 | 1.38M x 1% to 3% = 13,830 to 41,490. **ASSUMPTION** | | | assumption |
| Revenue illustration | 13,830 x EUR 120 = EUR 1.66M; 41,490 x EUR 120 = EUR 4.98M. EUR 120 a year per customer is an **assumption** | | | assumption; not a forecast |
| Cross-check | EUR 1.66M is 0.009% of the roughly US$19bn SAM (different geographies, so plausibility only) | | | my arithmetic |

The most fragile inputs are the 10% premium share, the 1% to 3% capture rate and the EUR 120 spend. Replace them with a pilot result.

Spend per household for context (not used in the funnel): Spain EUR 1,248 in 2025, 3.6% of EUR 35,101 total (INE, https://ine.es/dyngs/Prensa/en/EPF2025.htm, 2026-06-25, verified); Germany EUR 148 a month for interior decoration, appliances and articles in 2024, so EUR 1,776 a year (Destatis, https://www.destatis.de/EN/Themes/Society-Environment/Income-Consumption-Living-Conditions/Consumption-Expenditure/Tables/liste-germany.html, 2024, verified; annual figure my arithmetic); US US$2,355 per consumer unit in 2025 (BLS, above). Eurostat national accounts give higher figures (Germany about EUR 3,110, Spain about EUR 1,770 per household, my arithmetic on 2022 spend over current household counts); the gap suggests national accounts include more than direct household spending.

### 1.5 Other context found (not on the slide)

| Metric | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| US e-commerce share of total retail | 16.4% (Q3 2025); all retail, not decor | https://www.census.gov/retail/ecommerce.html | Dec 2025 | snippet only |
| Q4 share of US furniture and home furnishings store sales | 25.7% in 2025, 27.2% in 2024; November and December 2025 17.5% | https://fred.stlouisfed.org/data/MRTSSM442USN | 2024 and 2025 | my arithmetic; store sales only |
| Deloitte holiday 2025 | about US$181 planned for home items, furnishings and decorations, up 22% | https://www.deloitte.com/content/dam/insights/articles/2025/us188488_cic-holiday-retail/pdf/DI_2025-Holiday-Survey.pdf | 2025 | snippet only |
| Morning Consult: consideration of a home or housewares gift | engagement 42%, baby shower 43%, wedding "organization and home decor" 34%; consideration, not sales share | https://housewares.org/press-releases/consumers-plans-for-entertaining-and-celebrating-moments-in-2026/ | 2025-12-18 | verified |
| US internet households owning a smart home device | 49% (Parks Associates). The press release found in this pass is dated 22 Jan 2026, v1 cited a post dated 2026-04-23: check which release is meant before using | https://www.parksassociates.com/blogs/home-systems-and-controls/smart-home-growth-continues-as-matter-and-ai-drive-ease-of-use | v1: 2026-04-23 | verified in v1; not used in v2 |

Not found: share of households buying premium or design-brand home objects; share of decor and gadgets bought as gifts; INSEE per-household spend; European smart home ownership from a primary source; decor online share for Spain, France and Germany separately; EU27 CP05 after 2022; US online-buyer rate and decor 3-month rate (needed to extend the funnel to the US).

---

## 2. Competition

The set: premium design-object and design-led gadget brands, plus design furnishing brands and channels. E-readers, e-ink tablets, AI wearables and photo frames (the v1 competition set) are out of scope in v2.

### 2.1 Design-led electronics and lighting

| Brand | Hero price | Scale and margin | Funding, ownership | Smart layer | Status Nov 2026 | Source URLs and date | Tag |
|---|---|---|---|---|---|---|---|
| Teenage Engineering | EP-133 K.O. II £299 at launch (EUR 313 to 372 at retailers); OB-4 EUR 535 to 599 | SEK 361.2M, FY2025; EBITDA SEK 7.7M; net profit SEK 2.4M; 84 staff. FY2024 about SEK 438M, so about -18% (my arithmetic) | Founding partner of Nothing since 2021 | light, no shared app found | Stalled; founder says it will stop making synthesizers | https://allabolag.se/5567183719/teenage-engineering-ab (FY2025); https://mezha.ua/news/teenage-engineering-to-stop-making-synths-315968/ (Oct, year not on page); https://www.musicradar.com/news/teenage-engineering-ep-133-ko-2 (2023-11-22) | verified (FY2025 figures, £299); snippet only (EUR prices, FY2024, synth news year). A second pass saw 2024 turnover as SEK 437.9M (Allabolag) or SEK 427.2M (Syna) and net profit SEK 42.6M: snippet only |
| Nothing | CMF Watch Pro 2 EUR 69; Ear (3) about EUR 142 | 2024 revenue "over US$500M" (Bloomberg via 9to5Google), about 7M devices | US$200M Series C, Sept 2025 | strong (Nothing OS) | Growing | https://9to5google.com/2025/01/16/nothing-expansion-funding-successful-2024-report/ ; https://techcrunch.com/2025/09/15/nothing-closes-200m-series-c-led-by-tiger-global-plans-ai-first-device-launch/ | verified (revenue as press-reported); snippet only (prices). 2024 accounts overdue at Companies House (https://sacra.com/research/nothing, snippet only) |
| Marshall Group | Emberton III US$179.99 | MSEK 4,007 FY2023; adjusted operating profit MSEK 757 (19%); 9M 2024 MSEK 3,194, +15% (snippet) | Brands: Marshall, Natal, Urbanears, adidas headphones | light | Growing | https://group.marshall.com/2024/02/15/a-record-breaking-2023-and-a-new-era-for-marshall/ (2024-02-15); https://marshall.com/us/en/product/emberton-iii?pid=1009767 (2026-11-27) | verified |
| Bang & Olufsen | not found | DKK 2,553M FY2024/25 (prior DKK 2,588M); gross margin 55.0%; EBIT before special items DKK 26M (1.0%); 346 mono-brand stores, net -41 | listed | medium | Stalled, thin profit | https://www.inderes.dk/releases/annual-report-202425-bang-and-olufsen-reports-a-year-of-transition-achieving-record-high-gross-margin-positive-operating-profit-and-strengthened-branded-channel-performance (2025-07-03) | verified. Another source says 53.3% gross margin; a Q4 figure of 55.8% was the source of an earlier mix-up |
| Sonos | | US$1,443.3M FY2025 (US$1,518.1M FY2024, snippet); GAAP gross margin 43.7%; GAAP net loss US$61.1M | listed | very high | Stalled, recovering | https://investors.sonos.com/news-and-events/investor-news/latest-news/2025/Sonos-Reports-Fourth-Quarter-and-Fiscal-2025-Results/ (2025-11-05); 10-K https://www.sec.gov/Archives/edgar/data/1314727/000131472725000090/sono-20250927.htm | verified |
| Devialet | Phantom historically EUR 1,490 to 2,590 | revenue down about 20% in a year (Oct 2024) | conciliation procedure at the Paris commercial court | medium | Distressed; 2026 status not found | https://mac4ever.com/audio/184613-devialet-va-mal-mais-a-quel-point (2024-10-09) | verified (drop, procedure); snippet only (the rest) |
| Samsung The Frame | 43in US$899.99; 55in US$1,299.99 (snippet) | n/a | Samsung Electronics | high | Growing | https://samsung.com/us/lifestyle-tvs/the-frame/43-inch-the-frame-qled-4k-tv-ls03fa-sku-qn43ls03fafxza (2026-11-27) | verified (43in) |
| Nanoleaf | Shapes Hexagons Smarter Kit 5 panels US$119.99 list | about US$30.9M 2025 (US$29.7M 2024); net loss about US$1.7M (US$6.4M in 2024) | acquired by OneRobotics (SwitchBot parent) for about US$40.5M in four closings, announced 2026-05-15; about 1.3x revenue (my arithmetic) | high | Acquired | https://inside.lighting/news/26-06/nanoleaf-acquired-40-million-deal (2026-06-04); https://www.heise.de/-11316733 (2026-06-03) | verified (deal, revenue, loss); snippet only (prices) |
| Govee | | RMB 4.705bn (about US$693M) 2025; smart ambiance lighting 88.5% | ChiNext IPO application accepted 2026-06-24 | very high | Growing, IPO pending | https://matteralpha.com/industry-news/govee-ipo-prospectus-smart-home-strategy | snippet only |
| Philips Hue / Signify | Hue Go lamp £149.99 | Signify EUR 5,765M 2025, comparable sales -3.4%; adjusted EBITA 8.9%; Hue not broken out | listed; strategic review | very high | Stalled | https://signify.com/en-us/our-company/news/press-releases/2026/20260130-signify-fourth-quarter-and-full-year-results-2025 (2026-01-30) | snippet only (group); verified (Hue Go price, https://philips-hue.com/en-gb/p/hue-white-and-colour-ambiance-hue-go-portable-table-lamp/8719514404571, 2026-11-27) |
| Xiaomi ecosystem | | IoT and lifestyle products RMB 123.2bn 2025 (+18.3%); segment gross margin 23.1%; 1.079bn connected devices | listed | very high | Growing | https://hkexnews.hk/listedco/listconews/sehk/2026/0324/2026032400608.pdf (not opened) | snippet only |
| Ember, Fellow, Dyson, Smeg, Loewe | Ember Mug 2 about US$150 (Target); Fellow Stagg EKG Pro US$195 (2022) | Dyson GBP 6.13bn 2025, pre-tax profit GBP 511M (snippet; 2025 page 403); Smeg UK arm GBP 73.7M 2025; Ember, Fellow, Loewe not found | Loewe: Skytec Group since Dec 2019 (snippet); the earlier assumption that Hisense owns it is unsupported | | | https://target.com/p/ember-14oz-mug-2-white/-/A-81529010 ; https://techcrunch.com/2022/10/05/fellow-stagg-ekg ; https://kbbreview.com/?p=85611 | snippet only |

### 2.2 Design furnishing and object brands

| Brand | Hero price | Scale | Ownership | Status | Source URLs and date | Tag |
|---|---|---|---|---|---|---|
| Muji (Ryohin Keikaku) | Railway Station Alarm Clock EUR 39.95; Digital Clock small EUR 59.95 | JPY 784.6bn FY Aug 2025 (+18.6%); operating profit JPY 73.8bn (9.4%); 1,412 stores, 729 overseas | listed | Growing | https://ng.investing.com/news/company-news/ryohin-keikaku-fy258-presentation-record-profits-as-china-sales-surge-93CH-2139136 (2025-10-10); https://muji.eu/products/railway-station-alarm-clock-5685 | verified (financials); snippet only (prices) |
| Lexon (BOW Group) | Oblio charger US$79.90 (sold out online) | revenue not found | acquired by BOW Group in 2018; BOW also owns MyKronoz, Musart, Legacy, Leblon Delienne | Growing (acquisitive) | https://lexon-design.com/us/product/oblio/ (2026-11-27); https://venturebeat.com/business/lexon-writes-a-new-chapter-in-its-history-by-joining-bow-group | verified (price, stock); snippet only (ownership) |
| HAY | PC Portable lamp US$99 to 115 (sources conflict) | DKK 1,219M FY to 31 May 2025 (DKK 1,215.6M the year before; DKK 1,477.7M in 2022); net profit DKK 112.9M | MillerKnoll majority (bought 33% in June 2018 for US$65.5M and 34% in Dec 2019 for US$79.0M); founders hold the remaining 33%. No evidence of Kirk Kapital or Lego-family ownership: an earlier assumption in the brief was wrong | Growing | https://www.sec.gov/Archives/edgar/data/66382/000006638221000009/mlhr-20210227.htm ; https://companydata.dk/en/virksomhed/26799945-hay-aps (403 when opened) | snippet only |
| Muuto | not found | DKK 843.3M 2024 (snippet) | Knoll (now MillerKnoll) bought it for US$311.3M, closed 2018-01-25; not Mohawk | Growing | https://cfn.news/news/2018/1/25/knoll-completes-acquisition-of-muuto | snippet only |
| Flos (B&B Italia Group) | not found | Flos EUR 222M 2024 (EUR 242.7M 2023) | Investindustrial and Carlyle; Louis Poulsen sale reported at EUR 470M, June 2026 | Restructuring | Radiocor via borsaitaliana.it, 2026-06-11 (item not found on the page when opened) | snippet only |
| Ferm Living | not found | DKK 360.8M 2024 (DKK 335.5M 2023); net result DKK 41.3M | Maj Invest probable (opinion) | Growing | https://companydata.dk/en/claim/30070186 | snippet only |
| Alessi, Vitra, Tom Dixon, Normann Copenhagen, Design Letters | Anna G corkscrew US$110 | Vitra UK arm GBP 16.1M 2024 (-23%); Design Letters 2024 gross profit DKK 10.9M, net loss DKK 1.8M; others not found | Tom Dixon: sold to Neo Investment Partners (date not found) | mixed | https://us.alessi.com/products/anna-g-corkscrew ; https://bigfurnituregroup.com/?p=37162 ; https://estatistik.dk/virksomhed/design-letters-aps/32284698 | snippet only |
| Zara Home | not found | not separated; 374 stores (391 a year earlier) | Inditex | Stalled | https://fashionunited.com/news/business/inditex-posts-6-22-billion-euro-profit-in-2025-and-3-19-percent-sales-growth/2026031171084 | snippet only |
| Maisons du Monde | n/a | EUR 947.3M 2025 (-5.4%; 2024 EUR 1,001.9M); net loss EUR 405.9M including about EUR 296M non-cash impairment; 328 stores in 9 countries | rescue protocol signed 2026-06-18 with Alteri and Eicos; creditors convert debt and hold about 95.2% | Distressed | https://lexpress-franchise.com/actualites/maisons-du-monde-annonce-perte-406-m-euros-en-2025-et-signature-protocole-sauvetage/ (2026-06-19) | verified (a second pass read gross margin 63.1%, revenue -8.0%: snippet only, conflicting) |

Not found despite searching: Native Union, Twelve South, Courant, Ugmonk, Areaware, Kikkerland, Hands/Loft/Tokyu Hands, Daiso premium lines, Habitat, Conran Shop, Hubsch, Bloomingville, Marset, Nordic Nest (only an unreliable third-party band).

### 2.3 Channels and failures

| Item | What the record shows | Source URL | Date | Tag |
|---|---|---|---|---|
| Etsy | Revenue US$2,883.5M 2025; GMS about US$11.92bn; take rate 24.2% (my arithmetic); GMS -5.3% reported | https://seekingalpha.com/pr/20405358 | Q4 2025 release | snippet only |
| Made.com | Administration 2022-11-09; Next paid GBP 3.4M for brand and IP against a GBP 775M float valuation in 2021 | https://techcrunch.com/2022/11/09/next-acquires-made-coms-brand-and-ip-as-the-online-furniture-retailer-enters-administration | 2022-11-09 | snippet only |
| IKEA x Sonos Symfonisk | Partnership ended; range stops selling January 2026; on sale since Aug 2019, table lamp speaker EUR 179 | https://techradar.com/audio/speakers/sonos-and-ikea-just-ended-their-unlikely-symfonisk-audio-duet-and-thats-a-real-shame | 2025-05-06 | snippet only |
| Anki, Jibo, Kuri | Cloud-dependent home robots that shut down or were cancelled, 2018 to 2019; Anki after raising over US$200M | https://spectrum.ieee.org/consumer-robotics-company-anki-abruptly-shuts-down | 2019 | snippet only |
| Kickstarter design and technology | "Biggest year in Kickstarter history" for the category in 2025; no totals published | https://updates.kickstarter.com/a-year-in-review-2025-kickstarter-highlights/ | 2025-12-23 | verified |
| MoMA Design Store | sells the Lumio Book Lamp (Kickstarter about US$580k, snippet) | https://store.moma.org/products/lumio-book-lamp | | snippet only |

### 2.4 Price points shown on the slide 4 ladder (list prices, own currency, not converted)

| Product | Price | Source | Date | Tag |
|---|---|---|---|---|
| Emberton III (Marshall) | US$179.99 | https://marshall.com/us/en/product/emberton-iii?pid=1009767 | 2026-11-27 | verified |
| The Frame 43in (Samsung) | US$899.99 | https://samsung.com/us/lifestyle-tvs/the-frame/43-inch-the-frame-qled-4k-tv-ls03fa-sku-qn43ls03fafxza | 2026-11-27 | verified |
| Oblio charger (Lexon) | US$79.90 | https://lexon-design.com/us/product/oblio/ | 2026-11-27 | verified |
| PC Portable lamp (HAY) | US$99 to 115 | https://us.hay.com/lighting/pc-portable-lamp/2516116.html (now redirects to dwr.com) | undated | snippet only |
| Anna G corkscrew (Alessi) | US$110 (variants US$155 to 190) | https://us.alessi.com/products/anna-g-corkscrew | undated | snippet only |
| Shapes Hexagons Smarter Kit (Nanoleaf) | US$119.99 list, US$99.99 sale | https://us-shop.nanoleaf.me/products/shapes-hexagon-smarter-kit-5pk | undated | snippet only (429) |
| Mug 2, 14 oz (Ember) | about US$150 | https://target.com/p/ember-14oz-mug-2-white/-/A-81529010 | undated | snippet only |
| Railway Station Alarm Clock; Digital Clock small (Muji) | EUR 39.95; EUR 59.95 | https://muji.eu/products/railway-station-alarm-clock-5685 ; https://muji.eu/products/digital-clock-with-alarm-small-white-7756 | undated | snippet only |
| CMF Watch Pro 2; Ear (3) (Nothing) | EUR 69; about EUR 142 | https://be.nothing.tech/pages/cmf-store ; https://galaxus.de/en/s1/product/nothing-ear-3-anc-550-h-wireless-headphones-62018402 | undated | snippet only |
| EP-133 K.O. II; OB-4 (Teenage Engineering) | EUR 313 to 372; EUR 535 to 599 | https://galaxus.de/en/s1/product/teenage-engineering-ep133-ko-ii-sampler-midi-controllers-43127332 ; https://thomann.nl/teenage_engineering_ob_4_black_reviews.htm | undated | snippet only |

Left off the ladder: Stagg EKG Pro US$195 (2022, snippet only), Hue Go £149.99 (verified, GBP lane dropped for space).

### 2.5 The gap, as the record shows it

Facts: none of the brands above was found presenting decorations, gadgets and interior oddities under one brand with a shared design language and a shared software layer. Nothing's OS spans phones, audio and the CMF line but stays in electronics. Teenage Engineering has a strong shared design language and no shared app layer. Xiaomi has the shared app and ecosystem (1.079bn connected devices, snippet only) but is mass-utility. Lexon's parent BOW is a multi-brand group. HAY, Muuto, Alessi, Flos, Vitra and Tom Dixon show no software layer in the evidence.

Opinion: absence is a reading, not a proof; not every brand could be searched. Closest on range: Muji. Closest on gadgets plus gifts in one design language: Lexon. Closest on shared design language with software: Nothing and Teenage Engineering. Closest on a shared app layer: the Xiaomi ecosystem. The single-object route (Lumio) shows demand for one beautiful gadget, not for a family.

Map scores on slide 7 (x: 0 fixed object, 1 shaped by software; y: 0 mass utility, 1 museum-grade design) are opinion and drawn from the competition pass: Teenage Engineering .55/.85, B&O .45/.92, Devialet .50/.78, Nothing .80/.70, Marshall .30/.60, Lexon .35/.66, Samsung Frame .75/.55, Sonos .80/.49, Ember .60/.50, Nanoleaf .92/.40, Philips Hue .85/.45, Xiaomi .90/.30, Govee .92/.22, Vitra .02/.95, Alessi .02/.85, Flos .16/.90, HAY and Muuto .05/.75, Muji .15/.65, Ferm Living .02/.57, Zara Home .02/.36, Maisons du Monde .02/.28, MoMA Design Store .03/.80, Etsy .03/.44. The venture's own position is an aim, drawn as a span from fixed decor to smart objects.

---

## 3. Business model

### 3.1 Gross margins, latest fiscal year (slide 8 benchmark strip)

| Company | Gross margin | Source URL | Date | Tag |
|---|---|---|---|---|
| Williams-Sonoma | 46.2% on US$7.81bn | https://www.sec.gov/Archives/edgar/data/719955/000071995526000030/exhibit991fy2025q4earnings.htm | FY ended 1 Feb 2026, released 2026-03-18 | verified |
| Arhaus | 38.9% on US$1,379.2M (39.4% in 2024) | https://www.sec.gov/Archives/edgar/data/1875444/000187544426000010/arhs-20251231.htm | FY2025 10-K | verified |
| RH | 44.1% on US$3,440M | https://www.sec.gov/Archives/edgar/data/1528849/000110465926037992/rh-20260131x10k.htm | FY ended 31 Jan 2026 | snippet only |
| Lovesac | 56.4% on US$697.1M; internet US$192.3M = 27.6% of sales (my arithmetic) | https://www.sec.gov/Archives/edgar/data/1701758/000162828026021185/q4fy26pressrelease.htm | FY ended 1 Feb 2026 | snippet only |
| Sonos | 43.7% GAAP (45.4% prior year) | https://investors.sonos.com/news-and-events/investor-news/latest-news/2025/Sonos-Reports-Fourth-Quarter-and-Fiscal-2025-Results/ | 2025-11-05 | verified |
| Bang & Olufsen | 55.0% | see 2.1 | 2025-07-03 | verified |
| Tonies | 62.8% (EUR 395.9M gross profit on EUR 630.3M) | https://www.mynewsdesk.com/uk/tonies/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442747 | 2026-04-14 | verified |
| Peloton, connected fitness products | 13.6% (subscription 69.1%) | https://www.sec.gov/Archives/edgar/data/0001639825/000163982525000132/q42025shareholderletter.htm | 2025-08-07 | verified (v1) |
| Marshall | adjusted operating margin 23.6% for Jan to Sep 2024; gross margin not found | https://group.marshall.com/2024/11/13/marshall-group-reports-strong-profitable-growth-in-the-third-quarter/ | Nov 2024 | snippet only |
| Teenage Engineering, Nothing | gross profit not found | | | |
| Apple Products 36.8% FY2025 | carried from v1 | https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm | 10-K FY2025 | verified (v1) |

Opinion: home-furnishing retailers sit at about 39% to 63%, connected-audio brands lower at about 44% to 55%.

### 3.2 Unit cost rule of thumb

Retail price at 2x to 4x cost, ideally at least 3x (Predictable Designs https://predictabledesigns.com/how-to-price-your-new-electronic-hardware-product/ ; Bolt https://blog.bolt.io/?p=112 ; Sinovation https://www.sinovationventures.com/blog/consumer-iot-start-up-advice; undated; snippet only, carried from v1). The deck draws one third as structure, not a forecast. Hero unit cost and MOQ stay placeholders until a quote exists.

### 3.3 Direct versus wholesale, and the cost of an order

| Metric | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| Keystone convention | retail price is twice wholesale (a 50% retailer margin); some categories use 3x | https://faire.com/blog/selling/wholesale-basics-for-brands-makers-and-artists | undated | snippet only |
| EUR 100 shelf price, Spain | VAT 21% (https://www.europa.eu/youreurope/business/taxation/vat/vat-rules-rates, checked 2026-07-13, verified): direct net EUR 82.6 (100/1.21); wholesale at keystone EUR 41.3 (half of 82.6). An earlier pass showed EUR 50 for wholesale, taking half of the VAT-inclusive price; the VAT-exclusive base used here is the correct one | derived | | my arithmetic |
| Home and furniture conversion | 1.29% (Dynamic Yield, cited by Shopify); global average 2.66% | https://www.shopify.com/blog/ecommerce-conversion-rate | 2026-08-22 | verified |
| Meta ads, all industries, traffic campaigns | CTR 1.93%, CPC US$0.60 | https://localiq.com/blog/facebook-advertising-benchmarks/ | 2026-09-23 | verified (v1) |
| Ad spend per order | 0.60 / 0.0129 = about US$47 (mixed industries and category; not converted to euros) | derived | | my arithmetic |
| Other CAC figures | home and furniture about US$77 and about US$98 (two blogs); furniture CPA US$156.72 and home and garden US$36.28 (eMarketer); Meta cost per purchase about US$38.99; definitions differ | https://loyaltylion.com/blog/blog-average-cac-ecommerce ; https://www.triplewhale.com/blog/facebook-ads-benchmarks | 2024 to 2026 | snippet only |
| Online return rate | 19.3% of online sales (15.8% overall) | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 | 2025-10-15 | verified |
| Return rate by category | electronics about 8% to 15%, home goods about 15% to 20% (blog estimates; NRF does not publish by category) | https://www.corso.com/post-purchase-resource-center/ecommerce-return-rate-benchmarks-by-industry | undated | snippet only |
| Average order value, furniture and homeware | US$252.3 (ECDB) | https://ecommercedb.com/insights/understanding-the-cvr-and-aov-correlation-across-product-types/5031 | undated | snippet only |
| Sonos channel reliance | "a vast majority" of product sales through partners; Best Buy 14% of revenue; DTC share not read | https://www.sec.gov/Archives/edgar/data/1314727/000131472725000090/sono-20250927.htm | FY2025 | verified (partial read) |

Not found: HAY, Muuto and Marshall DTC shares; Littledata and Klaviyo benchmarks; Nanoleaf's DTC share (only "most profitable channel" in vendor marketing).

### 3.4 Pre-orders and crowdfunding

| Metric | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| Peak Design Roller Pro | US$12,940,078 from 23,461 backers on a US$100k goal; over US$13M with late pledges | https://updates.kickstarter.com/peak-design-raises-13m-with-their-biggest-kickstarter-ever/ | 2025-04-24 | verified |
| Kickstarter all-time | US$8.51bn pledged, 272,205 funded projects, 39.11% success rate; Design US$1.78bn and Technology US$1.65bn (third-party compilation) | https://searchlogistics.com/learn/statistics/kickstarter-stats-facts | updated 2026-04-13 | verified (secondary source) |
| Hardware delays | most founders deliver, but more than three quarters ship late (Mollick, 48,500 projects) | https://papers.ssrn.com/abstract=2088298 | 2014 | snippet only |
| TRMNL X (carried from v1) | 14,500 orders in 16 months | https://trmnl.com/blog/on-x | 2026-11-11 | verified (v1) |

### 3.5 Software tiers and content attach

| Metric | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| Tonies FY2025 | revenue EUR 630.3M (+31.2%); Toniebox EUR 161.2M; figurines (content) EUR 447.2M = 71.0% of revenue (my arithmetic); gross margin 62.8% | mynewsdesk URL in 3.1 | 2026-04-14 | verified |
| Tonies units | 2.6M Tonieboxes and 43.3M figurines in FY2025 (annual report PDF encrypted); 10M Tonieboxes by Sep 2025 | https://www.hauptversammlung.de/fileadmin/public/user_upload/tonies_GB25.pdf ; https://www.mynewsdesk.com/uk/tonies/pressreleases/tonies-r-celebrates-milestone-with-10-million-tonieboxes-sold-worldwide-3406049 | 2025 to 2026 | snippet only |
| Skylight Plus | US$79 a year for Calendar (optional). A figure of US$39 a year in v1 was for the Frame plan | https://skylight.zendesk.com/hc/en-us/articles/35984779668379-What-does-a-Skylight-Calendar-cost | undated | verified |
| reMarkable Connect | EUR 39.90 a year | https://remarkable.com/store/connect | accessed 2026-11-27 | verified (v1) |
| Philips Hue Secure | Basic US$39.99 per camera a year; Plus US$99.99 a year for up to 10 cameras (UK page, currency symbol ambiguous) | https://www.philips-hue.com/en-gb/explore-hue/propositions/smart-home-security/subscription-plans | Nov 2026 | verified |
| Yoto | revenue GBP 94.8M 2024 (+86%); Explorer membership GBP 29.99 a year | https://routenote.com/radar/yoto-revenue-jumps-43-as-screen-free-kids-audio-continues-to-boom/ | 2025 | snippet only |

Opinion: Tonies is the best-fit comparable: a design-led object whose cheaper add-ons carry most of the revenue. Here the add-on is the next object in the family; the optional software tier is a smaller line on the smart objects only.

### 3.6 Collaborations and limited editions

IKEA x Teenage Engineering FREKVENS was announced 2017-06-07 for stores from February 2019 and launched February 2020 as a 26-piece limited collection (announcement verified, https://www.ikea.com/global/en/newsroom/collaborations/make-some-noise-and-get-the-party-started-with-upcoming-collection-frekvens--ikea-and-teenage-engineering-in-collaboration-170607 ; launch details snippet only, https://www.ikea.com/es/en/new/frekvens-limited-collection-pubcd6f39e0). IKEA x Swedish House Mafia OBEGRÄNSAD launched October 2022 (snippet only, https://about.ikea.com/en/newsroom/2022/09/08/ikea-to-launch-the-obegransad-collection-in-collaboration-with-swedish-house-mafia). No sales or volume data found for FREKVENS, SYMFONISK or OBEGRÄNSAD, so the deck makes no claim that drops or collaborations lift sales. The brief's description of FREKVENS as a 2021 Swedish House Mafia project was wrong and is not used.

### 3.7 Shenzhen build and EU import

| Item | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| ODM MOQ | commonly 500 to 5,000 units; custom moulds raise the first order | https://www.cosmosourcing.com/blog/moq-meaning-minimum-order-quantity ; https://www.chinaimportal.com/?p=8724 | undated | snippet only (v1) |
| Injection tooling | simple US$2,000 to 5,000; complex US$5,000 to 15,000; aluminium soft tooling US$1,500 to 4,000 | https://dev.to/china-sourcing-agents/injection-mold-tooling-costs-for-electronics-enclosures-16dl | undated | snippet only (v1) |
| Certification (CE, RED, FCC) with a pre-certified Wi-Fi module | US$3,000 to 8,000 | https://predictabledesigns.com/certification-costs-what-it-really-takes/ | 2026-01-17 | verified (v1) |
| EU customs | Regulation (EU) 2026/382 ends the EUR 150 exemption on 1 Jul 2026 and applies a flat EUR 3 duty per item to consignments of EUR 150 or less until 1 Jul 2028; "item" means goods sharing a tariff classification, description and origin; the declarant pays; Product Identifiers mandatory from 1 Nov 2026 | https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en ; https://trade.ec.europa.eu/access-to-markets/en/news/eu-applies-eu3-customs-duty-item-low-value-e-commerce-consignments | 2026-06-08; 2026 | verified (EUR-Lex text returned empty) |
| VAT | Spain 21%, France 20%, Germany 19% | https://www.europa.eu/youreurope/business/taxation/vat/vat-rules-rates | checked 2026-07-13 | verified |
| Duty rates | speakers CN 8518 22: 0% (https://celna24.pl/customs-tariff/851822, secondary); alarm clocks 9105 11: 4.70% (https://custom-tariffs-seo.pages.dev/en/codes/9105-11-alarm-clocks, secondary, accessed 2026-02-23); lamps 9405, glassware 7013, festive and decorative 9505, plastics 3926: not found, check TARIC | https://taxation-customs.ec.europa.eu/customs-4/calculation-customs-duties/customs-tariff/eu-customs-tariff-taric_sl | 2026 | verified on page, secondary sources |
| Sea freight Asia to North Europe | about US$2,589 per 40ft container (early May 2026); Drewry index US$3,549 (11 Jun 2026); full-container rates only | https://www.chemorbis.com/en/premium-plastics-news/Asia-Europe-freight-rates-largely-erase-war-driven-gains-supporting-China-Europe-polymer-arbitrage/2026/05/07/971091 | May to Jun 2026 | snippet only |
| Freight per boxed unit | 67 m3 usable / 0.01 m3 per box = 6,700 units; US$2,589 / 6,700 = about US$0.39. Box size and container fill are assumptions; a small brand shipping LCL or air pays far more | derived | | my arithmetic on assumptions |

Opinion: the EUR 3 duty hurts cheap parcels shipped from China more than it hurts a brand importing in bulk and shipping from an EU warehouse; on a EUR 30 object EUR 3 is 10% of the price. No source makes this argument.

---

## 4. The problem

| Claim | Value | Source URL | Date | Tag |
|---|---|---|---|---|
| Smart home setup frustration | 52% of DIY smart home users report setup or connectivity issues | https://www.parksassociates.com/blogs/pr-smart-home/parks-associates-52-of-diy-smart-home-users-report-setup-or-connectivity-issues | 2025-07-09 | verified (v1) |
| Unused devices | 55% of Brits have at least three unused devices; 37.9% keep old tech in a drawer or box (Back Market) | https://www.backmarket.co.uk/en-gb/c/technology/unused-tech-survey | 2025 | snippet only |
| E-waste | 62 million tonnes in 2022, 22.3% documented as properly collected and recycled; documented recycling projected to fall to 20% by 2030 (snippet) | https://www.itu.int/en/mediacentre/pages/pr-2024-03-20-e-waste-recycling.aspx | 2024-03-20 | verified |
| Design as a purchase driver (counter-evidence) | consumers ranked aesthetic design the least important smart-home feature ("neither important nor unimportant"); quality materials, energy efficiency and security updates ranked highest (4.1 of 5); sample size and countries not stated | https://www.futuresource-consulting.com/insights/what-consumers-want-from-the-smart-home-sophie-harding-s-post-survey-findings-2023 | 2023-11-01 | verified |
| McKinsey Design Index | top-quartile design scorers grew revenue 32 points and shareholder returns 56 points faster than peers over five years; about 300 listed companies in medtech, consumer goods and retail banking; 2018; no home goods | https://www.mckinsey.com/capabilities/mckinsey-design/our-insights/the-business-value-of-design | Oct 2018 | snippet only; not used on the slide. No "219%" figure was found |
| "Gadgets feel cheap", smart-device abandonment | not found | | | |

Honest framing used on slide 2: design is not shown to drive smart-home purchases, so the deck does not claim it. The bet is that design wins where people shop for decor and the smart layer is optional.

---

## 5. Why now

Carried from v1 (`../pitch-deck-v1/research.md` section 5), tags unchanged:
- LLM price curve: Epoch AI, lowest price to match GPT-4-level capability fell from US$37.50 per million tokens (Mar 2023) to US$0.18 (Feb 2025), about 208x (my arithmetic). https://epoch.ai/data-insights/llm-inference-price-trends, 2025-03-12, verified. a16z: about 10x a year at equal capability, https://a16z.com/llmflation-llm-inference-cost/, 2024-11-12, verified.
- Small models on edge hardware: Gemma 3n with a 2 to 3 GB memory footprint, https://developers.googleblog.com/en/introducing-gemma-3n/, 2025-05-20, verified.
- Open tool protocol: more than 10,000 published MCP servers under Linux Foundation governance, https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation, 2025-12-09, verified.
- Commodity radios: Espressif "1.5 Billion+" IoT SoC shipments, https://www.espressif.com/en/company/about-us/who-we-are, accessed 2026-11-27, verified.

New in v2:
- Online share of European DIY, home and garden rose from 8.9% (2019) to 13.7% (2022) to 17% (2025); online market EUR 66bn of EUR 388bn. https://www.diyinternational.com/content/news/2026/03/24/plus/e-commerce-share-in-the-diy-sector-is-growing.html, 2026-03-24, verified.
- Pre-orders for design objects: Peak Design Roller Pro, US$12.9M from 23,461 backers; Kickstarter reports 2025 as its biggest year for Design and Technology (section 3.4), verified.
- EU import rules changed on 1 Jul 2026 (section 3.7), verified.
- Shopify 2025 GMV US$378.4bn (+29%), https://www.shopify.com/news/shopify-q4-2025-financial-results, 2026-02-11, snippet only; not used on the slide.
- Alibaba and 1688 lowering the sourcing barrier: not found.

---

## 6. Placeholders and open items for Oscar

Owned by Oscar: brand name; catalogue renders and prices (Sat 28 Nov); the choice of launch objects; unit cost and MOQ (need an ODM quote); founder surname, photo, education, languages; team plan; any plan date after December.

Invented for the deck and flagged as such: the two decor objects in the collection ("Shelf object", "Wall piece"; the other seven come from the 26 Nov catalogue decision); the three brand rules on slide 3; the plan rows after December; the bottom-up funnel's 10% premium share, 1% to 3% capture rate and EUR 120 annual spend.

Snippet-only figures that carry weight on the slides and are worth opening before the coffee: HAY, Muuto and Flos ownership and revenue (register pages blocked); Lexon ownership; Teenage Engineering FY2024 revenue and the synth news year; retail prices for HAY, Alessi, Nanoleaf, Ember, Muji, Nothing and Teenage Engineering in EUR; Mollick's late-shipping finding; the keystone convention; ODM MOQ; the Asia to Europe container rate; Back Market's unused-device survey.

Not found: premium design-object buyer share; gift share of decor; Marshall, Teenage Engineering and Nothing gross margins; lamp (9405), glassware (7013) and decorative (9505) duty rates; sales lift from limited editions; sourcing-marketplace evidence; a smart-device abandonment study.

Corrections to earlier assumptions: HAY is majority-owned by MillerKnoll, not Kirk Kapital or the Lego family; Muuto is owned by MillerKnoll (via Knoll), not Mohawk; Loewe is not owned by Hisense on the evidence found; Skylight Plus for the Calendar is US$79 a year; the FREKVENS collaboration was not a 2021 Swedish House Mafia project.

v3 additions (27 Nov): open items and snippet-only figures for the world market are in section 7.5 (Not found) and 7.6. Snippet-only figures that now carry weight on slides 5 and 6: Statista's narrow US$133.6bn segment (the low end of the range), DataReportal's 56.2% weekly online buyers, and the 2.2 billion world households (a secondary page). Worth opening before the coffee: the UN DESA household file, and one primary source for online buyers outside the EU. Invented for the deck in v3 and flagged on the slides: the six assumptions A1 to A6 (7.1), including the 42.5%, 41.5% and 29.2% ratios applied to every region.

---

## 7. v3: the world market by region, and the worldwide funnel (slides 5 and 6)

Added 2026-11-27 for Oscar's ask (quoted at the top). Every figure was read on the page on 2026-11-27 unless the tag says snippet only. Arithmetic can be re-run: `build_deck.py` holds the inputs and formulas in one block ("v3 market data") and generates every number on slides 5 and 6 from it; the tables below show the same numbers.

### 7.1 Method and rules

- **Scope of "the market"**: the brand's scope is home decor without furniture plus the adjacent design gadgets (smart lighting, speakers). This is the same scope as v2's TAM (US$315bn).
- **One base year and one currency**: 2025 and US$. Where a publisher gives only 2026 (Persistence, Mordor, Fortune BI country values) the figure is shown with its year and is never mixed into 2025 arithmetic. Euro figures (the beachhead's national statistics, the EUR 120 spend) are converted at **EUR 1 = US$ 1.0975**, the ECB reference rate for 26 November 2026 (https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html, page read 2026-11-27; the page showed no rate yet for 27 Nov; verified). A search snippet for the same page said 1.1150 for 27 Nov; the page itself contradicts it, so the page is used. FX moves: at 1.10 the revenue figures change by 0.2%.
- **Base publisher**: Global Market Insights (GMI), because it is the lowest full base with a regional split, and because v2 already used it. Other publishers are shown as ranges, never averaged.
- **Where the publishers disagree**: on the global total (US$681bn to 1,037bn, 1.5x), and far more on the regional split (see 7.3). Region definitions differ (Fortune BI's "Latin America" is South America only; GMI's Asia-Pacific includes India and Oceania; GMI's North America is the US, Canada and Mexico on its own definition, which I could not confirm). The deck says so.
- **Assumptions** (labelled on the slides): (A1) GMI's global non-furniture share, 42.5%, applies to every region; (A2) the global online share, 41.5%, applies to every region; (A3) GMI's European mid-to-high share, 29.2% (55 / 188.5), applies to every region; (A4) the regional shares of smart lighting and speakers come from Fortune BI and are applied to MarketsandMarkets' smaller smart-lighting total; (A5) "rest of world" in the gadget sources splits into Latin America and Middle East and Africa in GMI's decor proportions (58.3% and 41.7%); (A6) the funnel ratios in 7.5.

### 7.2 Regional inputs: home decor including furniture

| Publisher | Base year | Global | North America | Europe | Asia-Pacific | Latin America | Middle East and Africa | Other | URL, page date | Tag |
|---|---|---|---|---|---|---|---|---|---|---|
| **GMI** (base) | 2025 | US$680.6bn (furniture 391.5; online 41.5%, US$282.4bn) | 195.3 (28.7%) | 188.5 (27.7%) | 215.1 (31.6%) | 47.6 (7.0%) | 34.0 (5.0%) | China 82.8 (12.2%), Japan 38.7 (5.7%), India 26.9, US 162.1 (all inside their regions); regions sum to 680.5 (rounding); CAGR 3.4% to 2035; shares my arithmetic | https://www.gminsights.com/industry-analysis/home-decor-market , Aug 2026 | verified; shares my arithmetic |
| **Fortune Business Insights** | 2025 | US$802.26bn | 273.09 (stated 34.27%; values give 34.04%) | 124.99 (15.60%) | 369.44 (stated 45.75%; values give 46.05%) | 10.27 (South America only; 1.34%) | 24.47 (3.04%) | 2026 values: China 226.63, Japan 56.47, US 228.44, Germany 27.11, UK 16.34. The five regions sum to the global total. The page's stated shares do not match its own values and it labels the forecast window two ways (2025-2032, 2026-2034) | https://www.fortunebusinessinsights.com/home-d-cor-market-109906 , updated 9 Nov 2026 | verified; inconsistencies noted |
| **Persistence Market Research** | 2026 | US$859.9bn (2033: 1,284.5) | 31% (about 266.6, my arithmetic) | 27% (about 232.2) | 39% (about 335.4) | not stated | not stated | no 2025 base on the page; base year not explicit | https://www.persistencemarketresearch.com/market-research/home-decor-market.asp , Aug 2026 | verified (2026 only); values my arithmetic. A snippet of another Persistence listing gave North America 38% (2025) and a later release 39.8%: contradictory, snippet only, not used |
| **Mordor Intelligence** | 2026 | US$716.5bn (2025: 681.05, snippet) | 41.81% (about 299.6, my arithmetic) | not stated | not stated; fastest growing, 7.1% CAGR 2027-2032 | not stated | not stated | no regional US$ values; no furniture share | https://www.mordorintelligence.com/industry-reports/home-decor-market , 2026-10-22 | verified (2026); snippet only (2025 total) |
| **Grand View Research** | 2024 | US$960.14bn (page also gives 1,037.14 as 2025 and as 2026); furniture 50.7% | 36.7% (about 352.4, my arithmetic) | not stated | not stated; fastest growing; China the largest country | not stated | not stated | the page labels two different years for 1,037.14 | https://www.grandviewresearch.com/industry-analysis/home-decor-market , updated May 2026 | verified; values my arithmetic |
| IMARC (global) | 2025 | US$810.5bn (2034: 1,128.1; CAGR 3.70%) | n/a | n/a | n/a | n/a | n/a | regional chart exists in the report, numbers not on the page. IMARC US: US$191.5bn 2025 (see 1.2) vs GMI US 162.1: a 1.2x gap on the same year | https://www.imarcgroup.com/home-decorative-materials-market and https://www.imarcgroup.com/united-states-home-decor-market-statistics | snippet only (global); verified (US, section 1.2) |
| Statista Market Insights | 2024-2025 | worldwide narrow segment US$133.6bn (2024) | US "home decor" US$37.1bn (2025) | n/a | Eastern Asia US$31.2bn (2025); China "decorations" US$9.9bn (2025) | n/a | n/a | far narrower definition than the others (a B2C decorations segment). Used only as the low end of the range | https://www.statista.com/outlook/cmo/furniture/home-decor/worldwide (page returned 403) | snippet only |
| Barchart (publisher not named) | 2025 | n/a | "largest share, 44.89%" | n/a | n/a | n/a | n/a | https://www.barchart.com/story/news/2366934/global-home-decor-market-set-for-steady-growth-expected-to-hit-us-1-19-trillion-by-2035-amid-shift-toward-home-centric-lifestyles | snippet only; not used (no publisher, no total) |

How far the publishers disagree on the same region and year (2025, GMI against Fortune BI): North America 195 vs 273 (1.4x), Europe 188 vs 125 (1.5x the other way), Asia-Pacific 215 vs 369 (1.7x), Latin America 48 vs 10 (4.6x, but Fortune BI is South America only), Middle East and Africa 34 vs 24 (1.4x). The shown range on slide 5 is these two. Which region is the largest depends on the publisher: Asia-Pacific (GMI, Fortune BI, Persistence), North America (Mordor, Grand View, Barchart).

**Honest reading (opinion)**: the world total is known to within about 1.5x, the split by region only to within about 1.5x to 2x per region, and Latin America and Middle East and Africa are the weakest. No publisher's number should be quoted to a decimal.

### 7.3 The brand's scope by region (arithmetic)

Non-furniture share: (680.6 - 391.5) / 680.6 = 289.1 / 680.6 = **42.48%** (GMI's own totals). Applied to each GMI region (A1).

Gadgets, 2025:
- Smart lighting: MarketsandMarkets US$9.86bn (includes commercial, industrial and street lighting; https://www.marketsandmarkets.com/Market-Reports/smart-lighting-market-985.html , Oct 2026, verified). It has its own regional claim (Europe about 39.3%, a figure the page contradicts elsewhere; not used). Fortune BI gives a US$27.98bn market (2.8x larger) with regional shares North America 38%, Europe 29%, Asia-Pacific 25%, rest of world 8% (https://www.fortunebusinessinsights.com/smart-lighting-market-117284 , updated 9 Nov 2026, verified). The shares are applied to the smaller total (A4): 3.75, 2.86, 2.47, 0.79.
- Portable Bluetooth speakers: Fortune BI US$16.29bn (https://www.fortunebusinessinsights.com/smart-home-market-105011 , updated 9 Nov 2026, verified). Stated shares North America 34%, Europe 29%, Asia-Pacific 27%, rest of world "nearly 4%"; the four add to 94% and the page does not explain the gap. Normalised to 100% (A4): 36.2%, 30.9%, 28.7%, 4.3%, giving 5.89, 5.03, 4.68, 0.69.
- Total gadgets: 9.86 + 16.29 = US$26.15bn. Range: US$26.2bn (this) to US$44.3bn (both from Fortune BI, 27.98 + 16.29). Overlap between the two categories, and between smart lighting and decor lighting, is unknown. China and Japan gadget values: not found.
- Rest of world split (A5): 1.48bn x 58.3% = 0.86 (Latin America), x 41.7% = 0.62 (Middle East and Africa).

| Region | GMI incl. furniture | x 42.48% = decor without furniture | Smart lighting | Speakers | Gadgets | **Brand scope** | Sold online (x 41.5%) | Premium tier (x 29.18%) |
|---|---|---|---|---|---|---|---|---|
| North America | 195.3 | 82.96 | 3.75 | 5.89 | 9.64 | **92.6** | 34.43 | 10.05 |
| Europe | 188.5 | 80.07 | 2.86 | 5.03 | 7.89 | **88.0** | 33.23 | 9.70 |
| Asia-Pacific | 215.1 | 91.37 | 2.47 | 4.68 | 7.14 | **98.5** | 37.92 | 11.06 |
| Latin America | 47.6 | 20.22 | (0.79 x 58.3%) 0.46 | (0.69 x 58.3%) 0.40 | 0.86 | **21.1** | 8.39 | 2.45 |
| Middle East and Africa | 34.0 | 14.44 | 0.33 | 0.29 | 0.62 | **15.1** | 5.99 | 1.75 |
| Sum of regions | 680.5 | 289.06 | 9.86 | 16.29 | 26.15 | 315.2 | 119.98 | 35.0 |
| **World, from GMI totals** | 680.6 | 289.1 | | | 26.15 | **315.25 (about US$315bn)** | 289.1 x 0.415 = 119.98 (about 120.0) | 119.98 x 0.2918 = 35.0 |
| China (in Asia-Pacific) | 82.8 | 35.17 | not found | not found | | decor only | | |
| Japan (in Asia-Pacific) | 38.7 | 16.44 | not found | not found | | decor only | | |

The 29.18% is 55 / 188.5 (GMI Europe mid-to-high US$55bn over its US$188.5bn European total; https://www.gminsights.com/industry-analysis/europe-mid-to-high-range-home-decor-market , Oct 2026, verified; the tier is US$50 to 1,000 an item). Applying a European ratio to every region (A3) is an assumption; the premium column excludes gadgets.

**Range of the brand's decor-without-furniture base** (my arithmetic, assumption A1 applied to each base): Statista narrow segment 133.6 (2024, snippet only); GMI 289.1; Fortune BI 802.26 x 42.48% = 340.8; IMARC 810.5 x 42.48% = 344.3; Grand View 1,037.14 x 42.48% = **440.5**. So **US$134bn to 441bn**, and the TAM with gadgets is US$160bn to 485bn on the same logic (134 + 26 = 160; 441 + 44 = 485). Caveat (opinion): the non-furniture 42.5% includes textiles, flooring, lighting and kitchenware, so the part that is "objects like ours" is smaller than US$289bn; the narrow Statista figure shows how much smaller it could be.

### 7.4 What a household spends, as a plausibility anchor

Section 1.4 holds the national spend figures (Spain EUR 1,248 a household a year for furnishings and household equipment, Germany EUR 1,776, US US$2,355). The world funnel in 7.5 implies US$672 a year of online decor-without-furniture spend per household that bought home items online (119.98bn / 178.5M, my arithmetic): lower than those totals, which include furniture and appliances. Plausible, not proof.

### 7.5 Worldwide funnel, households to customers (slide 6)

Every step labelled as on the slide. SOURCED means a published figure measured on that population; ASSUMPTION means our choice, or a published rate applied to a population it was not measured on.

| Step | World | Spain, France, Germany (beachhead) | Label | Source and tag |
|---|---|---|---|---|
| Households | **2.2 billion** | **92.5M** (19.75M ES + 30.9M FR + 41.8M DE; mixed years) | SOURCED (world: unverified) | World: worldpopulationclock.net, "approximately 2.2 billion as of 2025" (an average household size of 3.5 and a table with 3.75 appear on the same site, so the count is 2.2 to 2.3 billion; page says it cites UN DESA, the UN file was not retrieved), https://worldpopulationclock.net/average-household-size-worldwide/ , accessed 2026-11-27: **snippet-level (secondary page), starred**. Cross-check: World Bank world population 2024 = 8,140,897,523 (https://api.worldbank.org/v2/country/WLD/indicator/SP.POP.TOTL?format=json&date=2024, verified) / 2.2bn = 3.7 people a household: consistent. Beachhead: INE https://ine.es/dyngs/Prensa/en/ECP4T25.htm?print=1 (2026-02-12), INSEE https://www.insee.fr/fr/statistiques/8612510 (2025-11-18, 30.9M is for 1 Jan 2022), Destatis https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/11/PD26_386_122.html (2026-11-05): verified |
| Households that buy online | 2.2bn x 76% x 56.2% = **939.7M** (42.7% of households) | 72.8M (78.7%): 41.8 x 81.38% + 30.9 x 80.15% + 19.75 x 70.77% | SOURCED rates; people's rates used as a household proxy (assumption within the step) | World: ITU, "6.3 billion people, or 76 per cent of the world's population, are using the Internet" (https://www.itu.int/en/ITU-D/Statistics/Pages/facts/default.aspx , release 2026-11-03, page read 2026-11-27, verified). DataReportal, 56.2% of internet users aged 16+ buy something online every week (GWI) (https://datareportal.com/global-digital-overview?country=82 , 2026, **snippet only, starred**; weekly is stricter than yearly, so conservative; another blog says 2.8bn online shoppers, about 44% of 6.3bn: unsourced, not used). Beachhead: Eurostat isoc_ec_ib20, 2025 (verified, see 1.4) |
| Bought home items online | 939.7M x 19% = **178.5M** | 72.8M x 19% = **13.8M** | ASSUMPTION (the EU rate applied outside its measured population; for the three countries a conservative floor, as in v2) | Eurostat news, 19% of EU individuals bought furniture, home accessories or garden items online in 3 months (2024): https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250220-3 , 2025-02-20, verified. Likely too high outside Europe and North America |
| Premium design-object buyers | 178.5M x 10% = **17.85M** (5% to 15%: 8.9M to 26.8M) | 13.8M x 10% = **1.38M** | ASSUMPTION | No source found (same as v2) |
| Customers of the brand, year 3 | 17.85M x 1% to 3% = **178.5k to 535.6k** (a ceiling if the brand reached everyone, not a plan) | 1.383M x 1% to 3% = **13,832 to 41,496** (v2: 13,830 to 41,490) | ASSUMPTION | v2 assumption, no source |
| Yearly revenue, year 3 | 178.5k x EUR 120 x 1.0975 = **US$23.5M**; 535.6k: **US$70.5M** | 13,832 x 131.7 = **US$1.82M**; 41,496: **US$5.47M** (EUR 1.66M to 4.98M, as v2) | ASSUMPTION (EUR 120 a customer a year) | EUR 120 from v2; FX is the ECB rate in 7.1 |

Checks (my arithmetic):
- The three countries hold 92.5M / 2,200M = **4.2%** of world households and 1.383M / 17.85M = **7.7%** of the funnel's premium buyers, because their online rates are higher than the world's.
- World revenue ceiling against the premium online pool: US$23.5M to 70.5M is 0.07% to 0.20% of US$35.0bn. The beachhead's US$1.8M to 5.5M is 0.005% to 0.016% of the same pool.
- Beachhead in dollars, sourced: GMI Europe mid-to-high decor, Germany US$11.0bn, Spain US$4.4bn, France 13.45% of 55 = US$7.4bn (my arithmetic): **US$22.8bn**, all channels, furniture included (https://www.gminsights.com/industry-analysis/europe-mid-to-high-range-home-decor-market , Oct 2026, verified). That is 12.1% of GMI's European total.
- Sensitivity: the premium share (5% to 15%) and the capture rate (1% to 3%) together move the customer count 9x between the lowest and highest corner: 5% x 1% = 0.05% of home-item buyers, 15% x 3% = 0.45%. Replace both with a pilot result.

Not found: household counts by region from a primary source (the UN DESA Household Size and Composition 2026 file, UNDESA_PD_2026_hh-size-composition.xlsx on https://population.un.org/Household/index.html , was not retrievable), online-shopper rates by region outside the EU (UNCTAD and Statista regional figures are behind paywalls or were not in the snippets), a premium design-object buyer share, home-item online purchase rates outside the EU, gadget market sizes for China and Japan, regional splits for IMARC and Statista. For these reasons the funnel is run for the world and for the beachhead, and regional detail on slide 6 is in dollars (7.3), not households.

### 7.6 v3 tags summary (new figures only)

- **Verified** (page opened and the figure read): GMI regional values and totals; Fortune BI decor, smart lighting and speaker totals and shares; Persistence 2026 total and shares; Mordor 2026 total and North America share; Grand View 2024 total and North America share; MarketsandMarkets smart lighting total; ITU 6.3bn and 76%; ECB 1.0975; World Bank population.
- **Snippet only (starred on the slides)**: Statista narrow segment US$133.6bn; DataReportal 56.2%; world households 2.2 billion (secondary page); IMARC global US$810.5bn; Mordor's 2025 total; Barchart.
- **My arithmetic**: every share converted to dollars, the 289.1, 315.25, 119.98, 35.0 figures, the gadget splits, the funnel multiplications, FX conversions, the ranges.
- **Assumptions**: A1 to A6 in 7.1 and the funnel's 19%, 10%, 1% to 3% and EUR 120.
- **Opinion**: the honest-reading paragraph under 7.2 and the caveat on the non-furniture share in 7.3.
- **Placeholders**: none new.

### 7.7 Changes from v2 on the slides

- The v2 market slide (top-down ladder EU plus US, bottom-up three-country funnel, spend tiles) is replaced by slide 5 (world by region) and slide 6 (worldwide funnel with the three-country funnel as the beachhead). The v2 top-down figures (US$161.5bn EU plus US, US$67.0bn online, US$19.4bn premium) are no longer on a slide; the world premium online pool is now US$35.0bn on the same logic (A1 to A3) and Europe's is US$9.7bn. The v2 spend-per-household tiles (INE, Destatis, BLS) are no longer on a slide and remain in section 1.4.
- One number moved because the base changed: v2 used IMARC's US figure (US$191.5bn) for the United States; v3 uses GMI's regions throughout (US 162.1 inside North America 195.3) and shows IMARC's figure beside it.
