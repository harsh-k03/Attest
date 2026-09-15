"""Convert CORD-v2's nested JSON ground truth into Attest's flat target schema.

Data source: HF naver-clova-ix/cord-v2 (see docs/ARCHITECTURE.md §7 Datasets).

TODO(week 1): freeze the flat target schema (receipt fields: vendor_name,
transaction_date, line_items[], subtotal, tax, discount, total, ...) and
write the CORD -> schema mapping here. This runs before train_lora.py and
before the eval harness, per the Week-1 gate in docs/ARCHITECTURE.md §11.
"""


def main():
    raise NotImplementedError("training/prepare_cord.py — see docs/ARCHITECTURE.md §11 Week 1")


if __name__ == "__main__":
    main()
