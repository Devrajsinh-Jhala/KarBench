# KarBench

**Can language models calculate and cite Indian income tax?**

KarBench evaluates language models on exact personal income tax, regime choice and statutory citation. It uses 100 synthetic salaried profiles paired across FY 2024–25, FY 2025–26 and TY 2026–27. The paper compares closed-book, rules-in-context and tool-assisted evaluation across 5,400 attempts.

| Resource | Contents |
|---|---|
| [Preprint](paper/manuscript.md) | Design, scoring and headline results |
| [LaTeX source](paper/main.tex) | Times-style typesetting and chart source |
| [Supplement](paper/supplement.md) | Per-period outcomes, cutoff sensitivity, costs and run provenance |
| [Aggregate results](results/preprint/) | CSV tables used in the preprint |
| [Citation](CITATION.cff) | Citation metadata |

## Main result

On the TY 2026–27 closed-book attempts, 303 of 600 got both taxes and the regime recommendation exactly right within protocol and zero provided a complete citation set. Providing the applicable rule card restored complete citations in 569 of 600 attempts.

The results use synthetic cases and the benchmark’s frozen engine reference. Case-level outcomes for the independent 30-case review are pending documentation. The released aggregate tables can be inspected directly. Exact row-by-row rescoring requires the original response and runner snapshots described in the supplement.
