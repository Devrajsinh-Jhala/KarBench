# Frozen dataset

KarBench v0.1.0 contains 300 questions derived from 100 synthetic profiles evaluated across three periods. The [dataset card](../DATASET_CARD.md) describes the population, generation, and limits.

| File | Contents |
|---|---|
| [cases_v1.jsonl](cases_v1.jsonl) | Full prompts, profile inputs, period labels, and case IDs |
| [gold_v1.jsonl](gold_v1.jsonl) | Reference answers, calculation traces, and counterfactual answers keyed by case ID |
| [pilot_cases.jsonl](pilot_cases.jsonl) | The 60-case pilot subset of the 300 cases |
| [rule_archive.jsonl](rule_archive.jsonl) | Source-linked rule cards used in the benchmark |
| [rules/](rules/) | Period-specific structured rule files pinned in the manifest |
| [manifest.json](manifest.json) | Frozen counts, version, seed, and integrity hashes |

Join cases and references on the id field. The cases and reference answer JSONL files preserve the evaluated version, including the original common HRA wording. See the [paper](../paper/KarBench_Preprint_Devraj_Jhala.pdf) for the clarification.

[CC BY 4.0 license](../LICENSE-DATA.md)
