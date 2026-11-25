# KarBench preprint

- [Read the paper](KarBench_Preprint_Devraj_Jhala.pdf)
- [Download the arXiv source archive](KarBench_arXiv_Source.zip)
- [Browse the LaTeX source](main.tex) and [vector figures](figures/)
- [Read the supplement](supplement.md) and [browse the results](../results/preprint/)
- [Revision 1.1 changes and remaining limitations](revision-1.1.md)

To compile the paper with TeX Live, run this command from the paper directory.

    latexmk -pdf -halt-on-error -interaction=nonstopmode main.tex

To reproduce the two-stage rounding check from the released reference traces, run this command from the paper directory.

    python check_rounding.py

[CC BY 4.0 license](LICENSE.md)
