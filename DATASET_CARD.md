# Dataset card

Version: 0.1.0 public development set. Owner: Devraj Jhala. Created 9 November 2026.

## Intended use

Research on exact personal-income-tax calculation, temporal applicability, and tool-assisted retrieval using synthetic Indian salaried profiles. The reference answers use the frozen benchmark engine. This dataset is intended for research and evaluation.

## Population and inputs

- Resident individuals aged 18–59; adult age fixed at 35 unless stated.
- Annual cash gross salary includes HRA, excludes employer NPS. Add employer NPS to gross salary once before its permitted deduction.
- Basic+DA includes retirement-benefit DA only; no turnover commission or other perquisites.
- Full-year constant employment/accommodation city, salary, HRA and rent. The city represents both employment and accommodation. Any positive rent amount shown was actually paid for accommodation the employee does not own. In the frozen prompt, the rent clause was unqualified. The 210 cases with zero rent and zero HRA have zero HRA exemption under both regimes.
- Old-regime eligible 80C-equivalent payments, non-cash self/family health premiums, additional employee NPS without double claims, savings-bank interest, professional tax, and one completed self-occupied property's current-year interest.
- The higher home-loan cap's acquisition/construction, completion and interest-certificate conditions are explicit. Older-period loan-date requirements are also explicit. No pre-construction interest or carry-forward loss is included.
- Employer NPS allowed in both regimes, subject to private/government caps. No other employer retirement contributions; NPS capped below the aggregate employer contribution perquisite threshold.
- Gross income is kept at or below INR 50 lakh, excluding surcharge cases by construction.
- Other exemptions/deductions, business, capital gains, NRIs, senior citizens, agricultural income, special-rate income, pensions, arrears, TDS credits, interest, penalties and filing-timing eligibility issues are excluded.

Inputs called `eligible_*` establish payment eligibility; the engine still applies monetary caps and the gross-total-income limitation. This benchmark does not infer eligibility from insurance documents or investment receipts.

## Construction and splits

100 deterministic profiles × 3 periods = 300 cases. First 20 profiles × 3 periods = 60 pilot cases. About half of the additional profiles target slab/rebate neighborhoods; realistic deduction bundles occur roughly every third generated profile. The first 20 are deliberately selected diagnostic anchors, not a random sample of Indian taxpayers.

The pilot is a subset of the full public development set, not a held-out test split. Each profile has a shared ID across periods. Dates are rendered as income intervals, year ends, or FY/AY labels. Repeated runs, paired years and paraphrases must not be counted as independent taxpayer samples.

Synthetic generation uses seed 20261109. Prompts have no computed tax answers. Gold records include both regimes' values, traces and counterfactual results under every period. SHA-256 digests lock cases, gold, rule files and rule archive.

## Legal time

FY 2024–25 → AY 2025–26 under the 1961 Act.
FY 2025–26 → AY 2026–27 under the 1961 Act, even if filing after April 2026.
TY 2026–27 → 2025 Act, sections 202 / 156 / 19 / 516.

New-regime amounts can agree across the second and third periods for this scope. Old-regime HRA amounts can differ because rule 279 expands the 50% city list to eight. The case generator contains binding examples of that change.

## Reference answers and review

The frozen reference answers were produced by a Decimal engine and include intermediate steps. A CA student provided qualitative feedback on a 30-case packet and flagged the HRA prompt wording. The preprint describes the reference checks and review scope.

The tie policy recommends the new regime on equal final rounded tax. This is a benchmark convention, not a claim that only one tied choice is legally valid.

## Limitations and licensing

The results describe tested model configurations on the released synthetic cases. The benchmark does not cover actual taxpayer documents, full tax law, open-web retrieval, or multilingual prompts. Original cases, prompts, reference answers, and rule cards are released under [CC BY 4.0](LICENSE-DATA.md).
