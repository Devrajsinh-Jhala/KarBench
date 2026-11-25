# KarBench supplementary material

These tables and protocol records accompany the [preprint](manuscript.md). The run digests identify the underlying artifacts and do not by themselves provide the raw data.

Revision 1.1 adds [Table C5](../results/preprint/table_c5_deadline.csv), the retrospective 240-second elapsed-time filter on the single-request modes. The [revision notes](revision-1.1.md) explain its scope and document the reference rounding check, scoring interpretation, and full-precision ledger.

## A. Scores and scoring sensitivities

| Configuration | Mode | Finished | Exact tax | All citations | ₹1 full | Exact full |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek Flash | Closed book | 239 | 227 (75.7%) | 155 (51.7%) | 148 (49.3%) | 145 (48.3%) |
| DeepSeek Flash | Rules in context | 289 | 288 (96.0%) | 287 (95.7%) | 283 (94.3%) | 274 (91.3%) |
| DeepSeek Flash | Agent | 209 | 203 (67.7%) | 207 (69.0%) | 200 (66.7%) | 192 (64.0%) |
| Luna low | Closed book | 300 | 149 (49.7%) | 185 (61.7%) | 77 (25.7%) | 65 (21.7%) |
| Luna low | Rules in context | 263 | 203 (67.7%) | 260 (86.7%) | 177 (59.0%) | 125 (41.7%) |
| Luna low | Agent | 266 | 170 (56.7%) | 264 (88.0%) | 129 (43.0%) | 98 (32.7%) |
| Luna medium | Closed book | 299 | 196 (65.3%) | 191 (63.7%) | 116 (38.7%) | 112 (37.3%) |
| Luna medium | Rules in context | 289 | 255 (85.0%) | 289 (96.3%) | 247 (82.3%) | 227 (75.7%) |
| Luna medium | Agent | 251 | 216 (72.0%) | 250 (83.3%) | 204 (68.0%) | 192 (64.0%) |
| Haiku low | Closed book | 300 | 183 (61.0%) | 121 (40.3%) | 61 (20.3%) | 47 (15.7%) |
| Haiku low | Rules in context | 300 | 279 (93.0%) | 300 (100.0%) | 278 (92.7%) | 138 (46.0%) |
| Haiku low | Agent | 298 | 249 (83.0%) | 293 (97.7%) | 230 (76.7%) | 149 (49.7%) |
| Haiku medium | Closed book | 300 | 210 (70.0%) | 136 (45.3%) | 77 (25.7%) | 61 (20.3%) |
| Haiku medium | Rules in context | 300 | 286 (95.3%) | 300 (100.0%) | 284 (94.7%) | 135 (45.0%) |
| Haiku medium | Agent | 268 | 239 (79.7%) | 268 (89.3%) | 229 (76.3%) | 134 (44.7%) |
| Grok medium | Closed book | 84 | 82 (27.3%) | 74 (24.7%) | 73 (24.3%) | 68 (22.7%) |
| Grok medium | Rules in context | 236 | 230 (76.7%) | 236 (78.7%) | 225 (75.0%) | 212 (70.7%) |
| Grok medium | Agent | 143 | 140 (46.7%) | 143 (47.7%) | 139 (46.3%) | 138 (46.0%) |

**Table A1.** All-attempt results within each mode. Rates use 300 attempts. The finish count gives the denominator for any finished-only rate.

| Configuration | TY 2026–27 mode | Finished | Exact tax | All citations | ₹1 full | Exact full |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek Flash | Closed book | 54 | 51 | 0 | 0 | 0 |
| DeepSeek Flash | Rules in context | 96 | 96 | 96 | 94 | 92 |
| DeepSeek Flash | Agent | 70 | 67 | 70 | 67 | 65 |
| Luna low | Closed book | 100 | 50 | 0 | 0 | 0 |
| Luna low | Rules in context | 94 | 65 | 94 | 50 | 35 |
| Luna low | Agent | 91 | 53 | 89 | 37 | 31 |
| Luna medium | Closed book | 99 | 62 | 0 | 0 | 0 |
| Luna medium | Rules in context | 95 | 81 | 95 | 78 | 71 |
| Luna medium | Agent | 88 | 74 | 88 | 69 | 64 |
| Haiku low | Closed book | 100 | 61 | 0 | 0 | 0 |
| Haiku low | Rules in context | 100 | 92 | 100 | 92 | 46 |
| Haiku low | Agent | 99 | 85 | 99 | 81 | 54 |
| Haiku medium | Closed book | 100 | 71 | 0 | 0 | 0 |
| Haiku medium | Rules in context | 100 | 94 | 100 | 93 | 45 |
| Haiku medium | Agent | 97 | 87 | 97 | 84 | 55 |
| Grok medium | Closed book | 9 | 8 | 0 | 0 | 0 |
| Grok medium | Rules in context | 84 | 82 | 84 | 80 | 75 |
| Grok medium | Agent | 37 | 37 | 37 | 36 | 35 |

**Table A2.** TY 2026–27 outcomes within protocol, out of 100 per cell. For Grok’s sensitivity analysis, rules in context adds 16 exact-tax, 16 complete-citation, 16 ₹1 full and 13 exact-full answers. Closed book adds 80 exact-tax, zero complete-citation and zero full answers. Agents add zero answers.

| Configuration | Closed book exact | Rules exact | Agent exact | Overall exact |
| --- | ---: | ---: | ---: | ---: |
| DeepSeek Flash | 42 → 145 | 261 → 274 | 189 → 192 | 492 → 611 |
| Luna low | 23 → 65 | 81 → 125 | 70 → 98 | 174 → 288 |
| Luna medium | 33 → 112 | 126 → 227 | 124 → 192 | 283 → 531 |
| Haiku low | 44 → 47 | 134 → 138 | 149 → 149 | 327 → 334 |
| Haiku medium | 56 → 61 | 135 → 135 | 134 → 134 | 325 → 330 |
| Grok medium | 24 → 68 | 167 → 212 | 101 → 138 | 292 → 418 |

**Table A3.** Exact full-answer counts per mode before and after the uniform rebate-blank rule. All rows use 300 attempts per mode and 900 attempts per configuration. For DeepSeek closed book, the original 42/300 (14.0%) becomes 145/300 (48.3%) under the shared exact rubric and 148/300 (49.3%) within ₹1.

## B. Citations and period signatures

| Configuration | Field | Correct | Accepted blank | Required blank | Stale | Other |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek Flash | Governing Act | 11 | 0 | 0 | 43 | 0 |
| DeepSeek Flash | Period label | 11 | 0 | 0 | 40 | 3 |
| DeepSeek Flash | New-regime section | 7 | 0 | 4 | 43 | 0 |
| DeepSeek Flash | Rebate section | 5 | 31 | 1 | 16 | 1 |
| DeepSeek Flash | Standard deduction | 4 | 0 | 5 | 43 | 2 |
| DeepSeek Flash | Rounding | 0 | 0 | 6 | 43 | 5 |
| Luna low | Governing Act | 99 | 0 | 0 | 0 | 1 |
| Luna low | Period label | 100 | 0 | 0 | 0 | 0 |
| Luna low | New-regime section | 12 | 0 | 86 | 0 | 2 |
| Luna low | Rebate section | 8 | 61 | 29 | 0 | 2 |
| Luna low | Standard deduction | 2 | 0 | 87 | 2 | 9 |
| Luna low | Rounding | 0 | 0 | 98 | 0 | 2 |
| Luna medium | Governing Act | 98 | 0 | 0 | 0 | 1 |
| Luna medium | Period label | 98 | 0 | 0 | 1 | 0 |
| Luna medium | New-regime section | 78 | 0 | 20 | 0 | 1 |
| Luna medium | Rebate section | 26 | 61 | 8 | 0 | 4 |
| Luna medium | Standard deduction | 4 | 0 | 38 | 15 | 42 |
| Luna medium | Rounding | 0 | 0 | 96 | 0 | 3 |
| Haiku low | Governing Act | 100 | 0 | 0 | 0 | 0 |
| Haiku low | Period label | 2 | 0 | 0 | 91 | 7 |
| Haiku low | New-regime section | 15 | 0 | 77 | 7 | 1 |
| Haiku low | Rebate section | 17 | 50 | 23 | 10 | 0 |
| Haiku low | Standard deduction | 0 | 0 | 74 | 26 | 0 |
| Haiku low | Rounding | 0 | 0 | 93 | 7 | 0 |
| Haiku medium | Governing Act | 99 | 0 | 0 | 1 | 0 |
| Haiku medium | Period label | 2 | 0 | 0 | 91 | 7 |
| Haiku medium | New-regime section | 25 | 0 | 73 | 2 | 0 |
| Haiku medium | Rebate section | 29 | 48 | 21 | 2 | 0 |
| Haiku medium | Standard deduction | 0 | 0 | 67 | 33 | 0 |
| Haiku medium | Rounding | 0 | 0 | 99 | 1 | 0 |
| Grok medium | Governing Act | 100 | 0 | 0 | 0 | 0 |
| Grok medium | Period label | 100 | 0 | 0 | 0 | 0 |
| Grok medium | New-regime section | 0 | 0 | 100 | 0 | 0 |
| Grok medium | Rebate section | 0 | 63 | 37 | 0 | 0 |
| Grok medium | Standard deduction | 0 | 0 | 100 | 0 | 0 |
| Grok medium | Rounding | 0 | 0 | 100 | 0 | 0 |

**Table B1.** Five citation buckets for all parseable closed-book TY 2026–27 answers, including Grok’s over-cap answers. Each row counts one field per answer. A single answer may contribute to multiple fields.

| Grok cohort | Field | Correct | Accepted blank | Required blank | Stale | Other |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Finished closed book (9) | Governing Act | 9 | 0 | 0 | 0 | 0 |
| Finished closed book (9) | Period label | 9 | 0 | 0 | 0 | 0 |
| Finished closed book (9) | New-regime section | 0 | 0 | 9 | 0 | 0 |
| Finished closed book (9) | Rebate section | 0 | 6 | 3 | 0 | 0 |
| Finished closed book (9) | Standard deduction | 0 | 0 | 9 | 0 | 0 |
| Finished closed book (9) | Rounding | 0 | 0 | 9 | 0 | 0 |
| Over-cap closed book (91) | Governing Act | 91 | 0 | 0 | 0 | 0 |
| Over-cap closed book (91) | Period label | 91 | 0 | 0 | 0 | 0 |
| Over-cap closed book (91) | New-regime section | 0 | 0 | 91 | 0 | 0 |
| Over-cap closed book (91) | Rebate section | 0 | 57 | 34 | 0 | 0 |
| Over-cap closed book (91) | Standard deduction | 0 | 0 | 91 | 0 | 0 |
| Over-cap closed book (91) | Rounding | 0 | 0 | 91 | 0 | 0 |
| Finished rules (84) | Governing Act | 84 | 0 | 0 | 0 | 0 |
| Finished rules (84) | Period label | 84 | 0 | 0 | 0 | 0 |
| Finished rules (84) | New-regime section | 84 | 0 | 0 | 0 | 0 |
| Finished rules (84) | Rebate section | 65 | 19 | 0 | 0 | 0 |
| Finished rules (84) | Standard deduction | 84 | 0 | 0 | 0 | 0 |
| Finished rules (84) | Rounding | 84 | 0 | 0 | 0 | 0 |
| Finished agent (37) | Governing Act | 37 | 0 | 0 | 0 | 0 |
| Finished agent (37) | Period label | 37 | 0 | 0 | 0 | 0 |
| Finished agent (37) | New-regime section | 37 | 0 | 0 | 0 | 0 |
| Finished agent (37) | Rebate section | 24 | 13 | 0 | 0 | 0 |
| Finished agent (37) | Standard deduction | 37 | 0 | 0 | 0 | 0 |
| Finished agent (37) | Rounding | 37 | 0 | 0 | 0 | 0 |

**Table B2.** TY 2026–27 Grok counts for the finished and over-cap cohorts. Stale and other wrong citation counts are zero in these four cohorts. All 16 parseable over-cap rules-in-context answers also passed every citation field.

| Configuration | Finished within cap | Usable exact tax | Complete citations |
| --- | ---: | ---: | ---: |
| DeepSeek Flash | 47/91 | 44/91 (48.4%) | 0/91 |
| Luna low | 91/91 | 42/91 (46.2%) | 0/91 |
| Luna medium | 90/91 | 54/91 (59.3%) | 0/91 |
| Haiku low | 91/91 | 54/91 (59.3%) | 0/91 |
| Haiku medium | 91/91 | 62/91 (68.1%) | 0/91 |
| Grok medium | 0/91 | 80/91 (87.9%) | 0/91 |

**Table B3.** The same 91 closed-book TY 2026–27 profiles where Grok went over cap. This is an exploratory outcome-defined subset. Haiku low and medium completed all 91 and left all four section fields empty on 61 and 59, respectively.

### Earlier-period citation audit

Each cell in Tables B4 and B5 gives correct or accepted / blank / stale / other among valid answers. These two tables reproduce the archived four-configuration audit, which pooled modes and folded permitted rebate blanks into the first bucket.

| Field | DeepSeek | Luna low | Luna medium | Haiku low |
| --- | ---: | ---: | ---: | ---: |
| Governing Act | 255 / 0 / 0 / 0 | 273 / 0 / 0 / 2 | 274 / 0 / 0 / 3 | 300 / 0 / 0 / 0 |
| New regime | 255 / 0 / 0 / 0 | 275 / 0 / 0 / 0 | 277 / 0 / 0 / 0 | 300 / 0 / 0 / 0 |
| Rebate or relief | 252 / 2 / 0 / 1 | 273 / 2 / 0 / 0 | 277 / 0 / 0 / 0 | 297 / 0 / 0 / 3 |
| Standard deduction | 255 / 0 / 0 / 0 | 275 / 0 / 0 / 0 | 277 / 0 / 0 / 0 | 300 / 0 / 0 / 0 |
| Rounding | 251 / 0 / 0 / 4 | 275 / 0 / 0 / 0 | 277 / 0 / 0 / 0 | 272 / 0 / 0 / 28 |
| Period label | 251 / 0 / 0 / 4 | 275 / 0 / 0 / 0 | 277 / 0 / 0 / 0 | 281 / 0 / 0 / 19 |

**Table B4.** FY 2024–25 citation audit across modes. Denominators by column are 255, 275, 277 and 300.

| Field | DeepSeek | Luna low | Luna medium | Haiku low |
| --- | ---: | ---: | ---: | ---: |
| Governing Act | 261 / 0 / 0 / 1 | 260 / 0 / 0 / 9 | 277 / 0 / 0 / 3 | 299 / 0 / 0 / 0 |
| New regime | 262 / 0 / 0 / 0 | 269 / 0 / 0 / 0 | 280 / 0 / 0 / 0 | 299 / 0 / 0 / 0 |
| Rebate or relief | 254 / 0 / 0 / 8 | 264 / 5 / 0 / 0 | 277 / 3 / 0 / 0 | 299 / 0 / 0 / 0 |
| Standard deduction | 262 / 0 / 0 / 0 | 269 / 0 / 0 / 0 | 280 / 0 / 0 / 0 | 299 / 0 / 0 / 0 |
| Rounding | 256 / 0 / 0 / 6 | 269 / 0 / 0 / 0 | 280 / 0 / 0 / 0 | 277 / 0 / 0 / 22 |
| Period label | 254 / 0 / 0 / 8 | 269 / 0 / 0 / 0 | 279 / 0 / 0 / 1 | 275 / 0 / 0 / 24 |

**Table B5.** FY 2025–26 citation audit across modes. Denominators by column are 262, 269, 280 and 299.

| Configuration | Matches current only | Matches current and another | Matches another only | Matches none |
| --- | ---: | ---: | ---: | ---: |
| DeepSeek Flash | 66 | 161 | 1 | 11 |
| Luna low | 27 | 122 | 3 | 148 |
| Luna medium | 52 | 144 | 2 | 101 |
| Haiku low | 44 | 139 | 2 | 115 |
| Haiku medium | 49 | 161 | 4 | 86 |
| Grok medium | 32 | 50 | 0 | 2 |

**Table B6.** Whether both reported rounded tax amounts match counterfactual reference values, among finished closed-book episodes across periods. A match on several years is ambiguous. Regime choice and citation validity are independent of this attribution diagnostic.

## C. Completion, output and tool use

| Configuration | Mode | FY 2024–25 | FY 2025–26 | TY 2026–27 |
| --- | ---: | ---: | ---: | ---: |
| DeepSeek Flash | Closed book | 89 / 11 / 0 / 0 / 0 / 0 | 96 / 4 / 0 / 0 / 0 / 0 | 54 / 46 / 0 / 0 / 0 / 0 |
| DeepSeek Flash | Rules in context | 94 / 6 / 0 / 0 / 0 / 0 | 99 / 1 / 0 / 0 / 0 / 0 | 96 / 4 / 0 / 0 / 0 / 0 |
| DeepSeek Flash | Agent | 72 / 0 / 25 / 3 / 0 / 0 | 67 / 0 / 30 / 3 / 0 / 0 | 70 / 0 / 25 / 5 / 0 / 0 |
| Luna low | Closed book | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 |
| Luna low | Rules in context | 85 / 0 / 0 / 0 / 15 / 0 | 84 / 0 / 0 / 0 / 16 / 0 | 94 / 0 / 0 / 0 / 6 / 0 |
| Luna low | Agent | 90 / 0 / 8 / 0 / 2 / 0 | 85 / 0 / 13 / 0 / 2 / 0 | 91 / 0 / 8 / 0 / 1 / 0 |
| Luna medium | Closed book | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 | 99 / 0 / 0 / 0 / 0 / 1 |
| Luna medium | Rules in context | 99 / 0 / 0 / 0 / 1 / 0 | 95 / 0 / 0 / 0 / 5 / 0 | 95 / 0 / 0 / 0 / 5 / 0 |
| Luna medium | Agent | 78 / 0 / 15 / 5 / 2 / 0 | 85 / 0 / 8 / 7 / 0 / 0 | 88 / 0 / 5 / 6 / 1 / 0 |
| Haiku low | Closed book | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 |
| Haiku low | Rules in context | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 |
| Haiku low | Agent | 100 / 0 / 0 / 0 / 0 / 0 | 99 / 0 / 1 / 0 / 0 / 0 | 99 / 0 / 1 / 0 / 0 / 0 |
| Haiku medium | Closed book | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 |
| Haiku medium | Rules in context | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 | 100 / 0 / 0 / 0 / 0 / 0 |
| Haiku medium | Agent | 91 / 0 / 9 / 0 / 0 / 0 | 80 / 0 / 20 / 0 / 0 / 0 | 97 / 0 / 3 / 0 / 0 / 0 |
| Grok medium | Closed book | 46 / 54 / 0 / 0 / 0 / 0 | 29 / 71 / 0 / 0 / 0 / 0 | 9 / 91 / 0 / 0 / 0 / 0 |
| Grok medium | Rules in context | 76 / 24 / 0 / 0 / 0 / 0 | 76 / 24 / 0 / 0 / 0 / 0 | 84 / 16 / 0 / 0 / 0 / 0 |
| Grok medium | Agent | 49 / 0 / 41 / 10 / 0 / 0 | 57 / 0 / 32 / 11 / 0 / 0 | 37 / 0 / 49 / 14 / 0 / 0 |

**Table C1.** Counts by mode and period, in order completed / output limit / tool-call limit / turn limit / invalid answer / provider error. Denominator is 100 in each cell. Overall there are 4,634 completed, 352 output-limit, 293 tool-call-limit, 64 turn-limit, 56 invalid-answer and one provider-error outcome.

| Group | Capped | Reasoning | Other output | Median reasoning | Median other | Reasoning > cap | Parseable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek, all | 72 | 589,720 | 104 | 8,192 | 0 | 0 | 0 |
| Grok, all | 280 | 3,191,275 | 45,288 | 10,729 | 165 | 270 | 280 |
| Grok, closed book | 216 | 2,548,129 | 34,666 | 11,188.5 | 165 | 211 | 216 |
| Grok, rules | 64 | 643,146 | 10,622 | 9,560 | 167 | 59 | 64 |
| Grok, TY26–27 closed book | 91 | 1,144,085 | 13,727 | 11,976 | 150 | 90 | 91 |

**Table C2.** Provider-reported reasoning and other output on capped rows. 71/72 DeepSeek rows used the entire 8,192 tokens for reasoning. The median of each component is computed separately. Luna and Haiku have zero capped rows.

| Configuration | Metered responses | Input tokens | Output tokens | Reasoning tokens | Mean seconds | Median seconds | P90 seconds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek Flash | 1,823 | 5,975,035 | 3,926,099 | 3,676,572 | 28.11 | 25.87 | 46.41 |
| Luna low | 1,485 | 2,930,977 | 596,928 | 408,765 | 17.11 | 9.78 | 13.95 |
| Luna medium | 1,601 | 3,584,683 | 1,363,120 | 1,167,083 | 19.28 | 16.21 | 36.22 |
| Haiku low | 1,466 | 4,606,847 | 1,742,573 | Unreported | 10.38 | 10.08 | 14.21 |
| Haiku medium | 1,483 | 5,050,600 | 2,039,769 | Unreported | 12.40 | 12.22 | 17.30 |
| Grok medium | 1,873 | 7,103,011 | 5,988,319 | 5,810,484 | 85.37 | 71.35 | 161.63 |

**Table C3.** Token totals and episode latency from the final saved 900 rows per configuration. Reasoning tokens are part of output tokens where separately reported. Counts describe metered responses linked to the final episodes. The USD ledger additionally captures some recovery attempts and reserves.

| Configuration | Successful agent episodes | Executions | Median tools | Reached 4 tools in one turn | Completed on turn 6 |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek Flash | 209 | 1549 | 7 | 121 | 31 |
| Luna low | 266 | 1120 | 4 | 75 | 1 |
| Luna medium | 251 | 1070 | 4 | 73 | 13 |
| Haiku low | 298 | 935 | 3 | 3 | 0 |
| Haiku medium | 268 | 1139 | 4 | 35 | 0 |
| Grok medium | 143 | 999 | 6 | 79 | 27 |

**Table C4.** Tools used by successful agent episodes. A run-wide tool count may exceed four because the ceiling applies to each turn.

## D. Reproducibility and frozen provenance

The dataset is version 0.1.0. The digest of its canonical manifest is `5cac1b8304abb5ced20cfaa964cea501ad53a5ffde4cae3bed11c77489a98cb1`. The manifest pins cases, reference answers, rule cards, the archive and engine. `deepseek-v1-frozen` points to `b5c2761ed37525dd640781dd7fd49d414645c5cc`. `grok-47-medium-v1-frozen` points to `121f9fa042110bf8bd5febb540c0c614cd103b79`. These are local tags. Case-level data from the independent 30-case review are pending documentation.

**Shared protocol digests (SHA-256)**

- Prompt `6a518b811433fca04ccbdcadfd26dd1679f4a0b6b1f4f5ec56e133680d7b6875`

- Tool schema `6b38d40a99b2a4f20be62fb0785499b29ef57ca6e80da4420bc7130337988b8c`

- Base scoring code `5f89b93385daf7f2fce43c9585e046e32d8c5ba184b0ff7e9b87b2f7c1ef319f`

- Shared comparison scorer `fdd7e4d6ca6eff97e8eca8ba5244949151c3589948ec087de5363176764fbe34`

- Frozen Grok analysis script `12e44d8888021553297b05f380afecc57d1140be163cf1227f7d4a224185eb3d`

- Protocol and citation policy version `2026-11-10.2`

**DeepSeek Flash**  
Run ID `76e333bf0f7858f8c6d654a343a17388d0e29a1e513e958e315e22a57bba1797`  
Raw SHA-256 `cfea0b6864c952b67bd13fb4c428e7864013666b084ebd47fc65c7b4c0b40461`  
Manifest file SHA-256 `e8deb867df7a9937ef45629caac4395610b78db047f76bcfa373cdffab6911e9`

**Luna low**  
Run ID `1a3b85e930d73bcdb85006963c2b4dc01138b28207333a0ae07f97f8741cfb72`  
Raw SHA-256 `3fafb933c9d014b3dd73ee57d29aad640ca411907a85bd72923140fea299574b`  
Manifest file SHA-256 `14f58d4918a6558d6490401da442ac1853423bf82d8723006607fe769d1c8de2`

**Luna medium**  
Run ID `0004e1181dd98be2f0d8577e8eec340e70df945c749f715ed19fb9021b3d4c31`  
Raw SHA-256 `6084a7c16a591a205ed496f58f12958ab36450b5b2078809b9e090b6ce33d45c`  
Manifest file SHA-256 `f2233a5e19c891922d8d16c25f6f777c486ce2a0ff537fb06e3565addda94d45`

**Haiku low**  
Run ID `1d1daf29c4d4664fc6d1769b4cbea350f082a6ae60f6c3278e28dca15e8a14df`  
Raw SHA-256 `b9dc8dc0526b5270227226b323deab800ca424f4cd08820f4509fa2641e36258`  
Manifest file SHA-256 `0ff0709ae9f811b715e8bd304aaced115329fa9dc9c2768a1da47cb9ccb197bd`

**Haiku medium**  
Run ID `3949cc168eff05ca0ee969938ab9e6bc3cae63db7dd24fdd26a3b55ee28b9dc4`  
Raw SHA-256 `f3d6dc6da242003194b237695d91a396690775c7eba50b3a596a09acabf42cd8`  
Manifest file SHA-256 `00b4eb4ba1f05e58403b86d9fccebff6ce134d99026644bd12f02e3435d7e9ad`

**Grok medium**  
Run ID `de7122106bb61df68cd0e504880b1ebe4f24b8911ae4f34f18640b5b028afb96`  
Raw SHA-256 `f27d829e890e52ac1ac6aed41d8fbe8ec1c86b7d4c8b822466cd65b92d291112`  
Manifest file SHA-256 `6d734baae8a8ec277d5aeec54799b2ce67b8ebcb50ce3280314faae94293f2c7`

The experiment generated cases, gold answers, tool schemas, code, raw responses, usage and failure flags. Raw digests identify the frozen snapshots. The aggregate tables here preserve the measurements reported in the study. The cited tags and raw digests identify the evaluated snapshots. The shared base files are `data/cases_v1.jsonl`, `data/gold_v1.jsonl`, `data/manifest.json` and the dated rule archive. The offline scorer is `scripts/run_openai_comparison.py` at the Grok tag. To reproduce cap sensitivity, parse only stored `truncated` records, apply the same rubric to parseable final JSON and add passing rows to a secondary numerator. Use the full planned denominator and preserve the original outcome.

The comparison includes the six complete 900-row configurations. Preliminary smoke tests, the superseded partial OpenAI run, and the partial Gemini attempt belong to the experimental record. They are outside this completed-run analysis. Pilot rows included in a full run are counted once.
