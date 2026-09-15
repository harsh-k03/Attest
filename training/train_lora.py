"""QLoRA fine-tune of Qwen2.5-VL-3B-Instruct on the prepared CORD-v2 set.

Intended to run on a single 16 GB T4 (e.g. Kaggle) — see docs/ARCHITECTURE.md
§9 (technology stack) and §12 (VRAM risk + mitigation: capped image long
edge, gradient checkpointing, batch size 1 with accumulation, fallback to a
2B model if forced).

TODO(week 2): PEFT/TRL training loop; log runs to Weights & Biases so public
run links can go in the README (docs/ARCHITECTURE.md §9).
"""


def main():
    raise NotImplementedError("training/train_lora.py — see docs/ARCHITECTURE.md §11 Week 2")


if __name__ == "__main__":
    main()
