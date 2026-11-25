# KarBench

KarBench tests whether language models can calculate Indian personal income tax and cite the law governing the income period. It follows 100 synthetic salaried profiles across FY 2024–25, FY 2025–26, and TY 2026–27. The preprint reports 5,400 evaluations across six model configurations and three settings with different access to dated rules.

| Resource | Contents |
|---|---|
| [Preprint PDF](paper/KarBench_Preprint_Devraj_Jhala.pdf) | Study design, findings, five figures, and eight tables |
| [LaTeX source](paper/main.tex) and [figure files](paper/figures/) | Manuscript source and vector figures |
| [arXiv source archive](paper/KarBench_arXiv_Source.zip) | Packaged manuscript and figures |
| [Frozen dataset](data/) and [dataset card](DATASET_CARD.md) | Cases, reference answers, rule cards, and integrity hashes |
| [Aggregate results](results/preprint/) and [supplement](paper/supplement.md) | Scores, protocol details, cutoff sensitivity, and run provenance |
| [Citation metadata](CITATION.cff) | Author and project information |

## Main result

Under the Income-tax Act, 2025, 303 of 600 closed-book attempts matched both rounded engine liabilities and the benchmark-designated regime. None supplied a complete set of statutory citations. Supplying the applicable rule card raised the number of complete citation sets to 569 of 600.

In a separate analysis of Grok's 100 usable closed-book answers for TY 2026-27, including 91 above the scoring cutoff, 88 matched both liabilities and the designated regime. All 100 left the section identifiers blank. Across periods, [12 of 475 incorrect closed-book liability pairs](results/preprint/table_b7.csv) matched another period's reference pair.

The cases are synthetic and scored against a frozen reference engine. The 30-case review provided qualitative feedback. The scores describe the recorded provider configurations, whose deadlines and cutoff enforcement differed. See [revision 1.1](paper/revision-1.1.md) for the corrections and added checks. Reproducing the reported runs row by row requires the original provider responses and matching experiment snapshots.

## Licensing

The [synthetic dataset and original rule cards](LICENSE-DATA.md) and the [preprint and its source](paper/LICENSE.md) are available under CC BY 4.0.
