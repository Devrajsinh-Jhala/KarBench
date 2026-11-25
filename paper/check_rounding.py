"""Recompute the rounding stages from the frozen JSONL traces."""

from decimal import Decimal
import json
from pathlib import Path


def rupees_to_tens(amount):
    if amount < 0:
        raise ValueError("Expected a non-negative liability or taxable amount")
    whole_rupees = int(amount)
    return ((whole_rupees + 5) // 10) * 10


def main():
    dataset = Path(__file__).resolve().parents[1] / "data/gold_v1.jsonl"
    case_ids = set()
    regime_count = 0
    for line in dataset.read_text(encoding="utf-8").splitlines():
        case = json.loads(line, parse_float=Decimal)
        case_id = case["id"]
        if case_id in case_ids:
            raise ValueError(f"Duplicate reference case {case_id}")
        case_ids.add(case_id)
        for regime in ("old_regime", "new_regime"):
            trace = {row["field"]: Decimal(row["amount"]) for row in case["trace"][regime]["trace"]}
            answer = case["answer"][regime]
            taxable = rupees_to_tens(trace["gross_total_income"] - trace["deductions_applied"])
            final_tax = rupees_to_tens(trace["tax_after_rebate"] + trace["cess"])
            if taxable != trace["taxable_income"] or taxable != answer["taxable_income"]:
                raise ValueError(f"Taxable income differs for {case_id} ({regime})")
            if final_tax != trace["total_tax"] or final_tax != answer["total_tax"]:
                raise ValueError(f"Final liability differs for {case_id} ({regime})")
            regime_count += 1
    print(f"Verified both rounding stages in {regime_count} regime traces for {len(case_ids)} cases.")


if __name__ == "__main__":
    main()
