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

Under the Income-tax Act, 2025, the models got both tax amounts and the regime recommendation right on 303 of 600 closed-book attempts. None supplied a complete set of statutory citations. Supplying the applicable rule card raised the number of complete citation sets to 569 of 600.

The cases are synthetic and scored against a frozen reference engine. The 30-case review provided qualitative feedback. The original provider responses and matching experiment snapshots are required for exact row-level reproduction of the reported runs.

## Licensing

The [synthetic dataset and original rule cards](LICENSE-DATA.md) and the [preprint and its source](paper/LICENSE.md) are available under CC BY 4.0.
