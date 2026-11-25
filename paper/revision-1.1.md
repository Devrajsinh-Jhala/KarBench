# KarBench preprint revision 1.1

The revision retains the original dataset and scoring keys. It adds two offline checks on the frozen artifacts and corrects the interpretation, citations, and presentation.

| Point | Change and evidence |
|---|---|
| Provider limits | The primary tables report recorded model and provider configurations. Grok had a 900-second client request timeout and an output cap enforced after receipt. DeepSeek had a 240-second client request timeout and a request-level output cap. Grok's recoverable over-cap responses now appear only as explicitly marked provider-specific sensitivity results. |
| Timeout sensitivity | [Table C5](../results/preprint/table_c5_deadline.csv) filters the existing single-request modes to in-protocol episodes with recorded end-to-end latency at most 240 seconds. For TY 2026–27, the counts remain 303/600 for closed-book exact tax, 0/600 for closed-book complete citations, and 569/600 for rule-assisted complete citations. Across all three periods, two Grok and one Luna-low rule-assisted completions fall outside the window. A controlled provider comparison would need new runs with comparable effective budgets and enforced cutoffs. |
| Reference validation | Exact agreement is defined against the frozen engine key. The 30-case packet yielded qualitative feedback. An independent, case-by-case legal audit of the full reference is outstanding. The added verifier checks arithmetic at the two rounding stages using the saved intermediate values. |
| Scoring | The main configuration table emphasizes final liabilities, citations, and the INR 1 intermediate-tolerance score. Exact full-answer scores remain available as an intermediate-trace diagnostic. For Haiku low and medium with rules in context, the respective tolerance scores were 278/300 and 284/300, compared with 138/300 and 135/300 for exact trace plus citations. |
| Case and tool scope | The cases use synthetic salaried profiles with structured inputs. In the two transition periods the new regime is strictly cheaper for 87 and 86 of 100 profiles. The benchmark also selects it in 12 and 13 ties. The agent can search, read, and calculate through its fixed interface. A code-enabled baseline and real-document cases would test broader workflows. |
| Bibliography | Corrected the author list for [IL-TUR](https://aclanthology.org/2024.acl-long.618/) and cited [LexKairos](https://arxiv.org/abs/2608.09106) with its five authors. |
| Statutory rounding | The methods now specify rounding taxable income before slabs and rounding final liability after applying rebate or marginal relief and cess. The [trace verifier](check_rounding.py) reproduced both stages in all 600 saved regime traces. |
| Ledger | The [cost table](../results/preprint/table_7.csv) now shows saved precision. Recorded usage of USD 55.2172613 plus a reserve of USD 3.3955462 reconciles to USD 58.6128075. The reserve tracks unresolved expenses in the local ledger. |

