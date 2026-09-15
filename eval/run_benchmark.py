"""Runs all four systems (B0 OCR+rules, B1 zero-shot VLM, B2 fine-tuned VLM
no agent, Attest full system) against all four datasets (CORD-v2, DocILE,
SROIE, FUNSD) and writes results to eval/results/.

See docs/ARCHITECTURE.md §8 for the baseline definitions and metric set, and
§11 for which week each baseline/system becomes available.

Also the harness for the with/without-repair-loop ablation described in
§4 — "the single most persuasive number in the repository".
"""


def main():
    raise NotImplementedError("eval/run_benchmark.py — see docs/ARCHITECTURE.md §11 Week 1")


if __name__ == "__main__":
    main()
