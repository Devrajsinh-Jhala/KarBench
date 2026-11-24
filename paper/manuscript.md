# KarBench: Can Language Models Calculate and Cite Indian Income Tax?

**Devraj Jhala** · Software Engineer II, Cisco, India  
24 November 2026 · Preprint draft

## Abstract

Correct tax arithmetic can conceal use of the wrong law. We introduce KarBench, a benchmark for calculating Indian personal income tax and citing the applicable statute across the transition from the Income-tax Act, 1961 to the Income-tax Act, 2025. We evaluate six model configurations from four providers on 100 synthetic salaried profiles paired across three income periods and three access modes, for 5,400 attempts. On the 600 closed-book attempts under the 2025 Act, 303 got both final taxes and the regime choice exactly right within protocol, while zero provided a complete citation set. Giving the applicable rule card improved exact-tax accuracy in every configuration and produced complete citations in 569 of the 600 attempts under the new Act. A separate analysis of saved responses above the benchmark cap finds that Grok 4.7 medium calculated 88 of 100 closed-book new-Act cases exactly, including 80 correct answers above the cap. All 100 named the correct Act and period and abstained on every section field. Tax calculation, statutory citation and completion therefore warrant separate reporting.

## Introduction

Assessment Year (AY) 2026–27 refers to income earned in Financial Year (FY) 2025–26 under the Income-tax Act, 1961. Tax Year (TY) 2026–27 refers to the subsequent income period under the Income-tax Act, 2025 [1, 2]. The same year numbers denote different statutory authorities. In KarBench, 98 of 100 profiles have identical final tax totals under both regimes across these adjacent periods. A grading system that scores only the numbers would miss many errors in the governing Act or section.

KarBench evaluates three outcomes on the same answers: exact tax and regime choice, completeness of the applicable references, and completion under the evaluation protocol. We vary whether the model receives the applicable rules or must obtain them from a bounded tool environment. The repository archives the aggregate tables and reproducibility materials [10].

## Related work

SARA evaluates statutory reasoning using US tax provisions [4]. TaxCalcBench measures exact US tax calculation from structured inputs and documents [5]. LegalBench and IL-TUR cover broader legal reasoning and Indian legal text tasks [6, 7]. Indian legal exam benchmarks and work on legal hallucinations identify problems with authority and citation accuracy [8, 9]. KarBench pairs identical Indian salaried profiles across a statutory transition to measure whether the model’s numbers and legal references change when the applicable law changes.

## Benchmark design

### Cases and reference answers

The development set pairs 100 synthetic profiles across FY 2024–25, FY 2025–26 and TY 2026–27. The first 20 are diagnostic anchors, 40 target thresholds and 40 are general cases. The 60-case pilot is a subset of the 300-case set. Profiles represent resident salaried adults below 60 and cover slabs, salary deductions, house rent allowance (HRA), retirement contributions, eligible interest, rebate and marginal relief, cess and rounding. The benchmark excludes surcharge, special-rate income and business income. Prompt wordings vary how the income period is stated.

A deterministic Decimal engine computes both final taxes and records intermediate steps. It recommends the new regime on an exact tie for scoring consistency. The previous Act and the 2025 Act use different section identifiers for the new regime, rebate, standard deduction and rounding. Rule 279 also changes which cities qualify for the 50% salary term in the HRA formula [1, 3]. As a result, some paired profiles differ numerically even where most do not.

**Expected period labels and principal statutory references. The scorer recognizes applicable aliases.**

| Income period | Label | Act | New regime | Rebate | Deduction | Rounding |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| FY 2024–25 | AY 2025–26 | 1961 | 115BAC | 87A | 16(ia) | 288A and 288B |
| FY 2025–26 | AY 2026–27 | 1961 | 115BAC | 87A | 16(ia) | 288A and 288B |
| TY 2026–27 | Tax Year 2026–27 | 2025 | 202 | 156 | 19 | 516 |

### Evaluation conditions

Closed book supplies the profile and answer schema. Rules in context adds the applicable dated rule card. Agent mode allows rule search and lookup across all three periods and access to a calculator. The six model configurations each evaluate 300 cases once in each of the three modes. The requested endpoints were deepseek-flash (thinking enabled, low), gpt-6-luna (low and medium), claude-haiku-5-5 (adaptive, low and medium) and grok-4.7 (medium). Provider effort levels are API settings and do not imply equal compute.

The protocol sets 8,192 metered output tokens per request, 16,384 per agent episode, six agent turns and four tool calls per turn. The standard timeout was 240 seconds and Grok’s was 900. DeepSeek, Luna and Haiku used provider request controls. Grok responses were scored against the cap after receipt. We retain cutoff rows in the planned-attempt denominator and examine their parseable answers in a separate sensitivity analysis.

## Scoring

Exact tax requires exact rounded final liabilities in both regimes and the correct regime recommendation. Complete citation requires the governing Act, income-period label and all applicable section fields. The comparison rubric accepts a blank rebate section if both predicted and reference rebate or relief are zero in both regimes. Full-answer accuracy also checks intermediate amounts. The INR 1 variant tolerates up to one rupee per intermediate amount, with final totals still exact.

Protocol-level rates use all planned attempts and require a completed outcome. Finished-answer rates use only completed rows. We also rescore parseable saved answers from output-limit rows offline and add them to the numerator of a separate all-attempt sensitivity analysis. The paired profile bootstrap uses 10,000 draws over the 100 profiles and keeps all three periods together. Its exploratory percentile intervals reflect variation over profiles, with one inference attempt per identity.

## Results

### Supplying rules improves exact tax

Rules in context improved exact-tax rates in every configuration. Gains ranged from 18.0 to 49.3 percentage points. DeepSeek increased from 227/300 (75.7%) to 288/300 (96.0%). Grok’s largest gain includes a substantial change in completion. With its usable over-cap outputs included, the Grok gain shrinks from 49.3 to 4.7 percentage points (280/300 to 294/300).

**Finished and exact-tax results across access modes and exact-tax change with rules. Each configuration has 900 total attempts and 300 attempts per mode.**

| Configuration | Finished /900 | Exact tax /900 | Closed book /300 | With rules /300 | Gain (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek Flash | 737 | 718 | 227 | 288 | 20.3 |
| Luna low | 829 | 522 | 149 | 203 | 18.0 |
| Luna medium | 839 | 667 | 196 | 255 | 19.7 |
| Haiku low | 898 | 711 | 183 | 279 | 32.0 |
| Haiku medium | 868 | 735 | 210 | 286 | 25.3 |
| Grok medium | 463 | 452 | 82 | 230 | 49.3 |

### Under the 2025 Act, exact tax and correct citations diverge

Models got both taxes and the regime correct on 303/600 closed-book attempts under the 2025 Act within protocol. Complete citations were 0/600 closed book, 569/600 with rules in context and 480/600 with tools. The citation errors differed by model. DeepSeek named the previous Act on 43 of 54 finished closed-book answers. Both Haiku configurations used a stale period label on 91 of 100. Luna medium named the new-regime section correctly on 78 of 99 finished answers and left the rounding field empty on 96.

**TY 2026–27. Each configuration has 100 planned attempts in each mode. Tax counts include the correct regime choice. Citation completeness applies the rebate-blank rule.**

| Configuration | Closed-book exact tax | Closed-book citations | With-rules citations | Agent citations |
| --- | ---: | ---: | ---: | ---: |
| DeepSeek Flash | 51 | 0 | 96 | 70 |
| Luna low | 50 | 0 | 94 | 89 |
| Luna medium | 62 | 0 | 95 | 88 |
| Haiku low | 61 | 0 | 100 | 99 |
| Haiku medium | 71 | 0 | 100 | 97 |
| Grok medium | 8 | 0 | 84 | 37 |

### Output limits hide usable answers

Grok finished 463 of 900 attempts, with 280 output-limit, 122 tool-call-limit and 35 turn-limit outcomes. All 280 output-limit rows contained parseable final JSON. Reported reasoning tokens accounted for 98.6% of their metered output. By comparison, 71 of 72 DeepSeek output-limit rows had empty final text and the remaining row failed parsing. The same nominal cap thus corresponds to different observed failure modes.

In TY 2026–27 closed book, Grok got exact tax and regime choice on 8 of 9 finished answers and 80 of 91 parseable over-cap answers. All 100 named the correct Act and period and left all four section fields blank. The prompt permits blanks for unknown identifiers. These data show abstention in the task context and cannot establish whether the model would retrieve the sections in a direct citation-only task.

## Limitations

The profiles and prompts are synthetic, English-language and restricted to a salaried population. Benchmark rates describe this set and the tested model configurations. Provider token accounting, request limits and effort settings differ, and cap sensitivity is specific to saved usable responses. No repeated inference trials estimate model stochasticity. The 30-case independent review packet is available, with case-level reviewer calculations and dispositions pending documentation. The presented scores use the frozen diagnostic engine reference.

## Conclusion

KarBench shows that a model can calculate the right tax while omitting or misidentifying the applicable statutory references. Supplying dated rules improves both outcomes, and completion constraints can hide otherwise usable outputs. Reporting these measures individually makes the difference visible.

## Data and code availability

The KarBench repository contains the study’s aggregate results and supplementary analyses [10]. The supplement records case and run identifiers, protocol hashes, coverage, costs and sensitivity tables. Row-by-row reproduction of the reported live scores needs the original provider responses and the corresponding run snapshots.

## Use of generative AI

Anthropic Claude [11] suggested the initial idea for KarBench and was used in early project development. OpenAI ChatGPT [12] assisted with manuscript drafting and revision and with preparing figures from the benchmark results. Model use in the experiments is described separately in Benchmark design.

## References

1. Government of India. *Income-tax Act, 2025, as amended by the Finance Act, 2026*. §§ 1, 3, 19, 156, 202, 516 and 536. [Official text](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf)
2. Income Tax Department. *General Questions FAQs*. Transition between AY 2026–27 and TY 2026–27. [Department guidance](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/General%20Questions-faqs)
3. Central Board of Direct Taxes. *Income-tax Rules, 2026*, Notification 22/2026, G.S.R. 198(E), 20 March 2026, Rule 279. [Notified text](https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf)
4. Holzenberger, N., Blair-Stanek, A., and Van Durme, B. *A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering*. 2020. [Paper](https://arxiv.org/abs/2005.05257)
5. Bock, M. R., Molisee, K., Ozer, Z., and Shah, S. *TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task*. 2025. [Paper](https://arxiv.org/abs/2507.16126) · [Benchmark repository](https://github.com/column-tax/tax-calc-bench)
6. Guha, N., et al. *LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models*. NeurIPS, 2023. [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/89e44582fd28ddfea1ea4dcb0ebbf4b0-Abstract-Datasets_and_Benchmarks.html)
7. Kalamkar, P., et al. *IL-TUR: Benchmark for Indian Legal Text Understanding and Reasoning*. ACL, 2024. [Paper](https://aclanthology.org/2024.acl-long.618/)
8. Juvekar, K., Bhattacharya, A., Khadloya, S., and Saxena, U. *Are LLMs Court-Ready? Evaluating Frontier Models on Indian Legal Reasoning*. Natural Legal Language Processing Workshop, 2025. [Paper](https://aclanthology.org/2025.nllp-1.26/)
9. Dahl, M., Magesh, V., Suzgun, M., and Ho, D. E. *Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models*. 2024. [Paper](https://arxiv.org/abs/2401.01301)
10. Jhala, D. *KarBench research artifacts*. [https://github.com/Devrajsinh-Jhala/KarBench](https://github.com/Devrajsinh-Jhala/KarBench).
11. Anthropic. *Claude*. [Product documentation](https://claude.com/product/overview).
12. OpenAI. *ChatGPT*. [Product documentation](https://chatgpt.com/overview/).
