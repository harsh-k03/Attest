"""Extractor model wrapper: prompt construction, guided decoding, logprob capture.

TODO(week 2): wire to a vLLM server running the LoRA-adapted
Qwen2.5-VL-3B-Instruct checkpoint produced by training/train_lora.py, with a
JSON grammar matching the flat target schema.
"""


def extract(page_image, schema_prompt: str, fields: list[str] | None = None):
    """Run extraction, optionally narrowed to `fields` (used by the repair loop's
    targeted re-prompt strategy — see docs/ARCHITECTURE.md §4).

    Returns (json_fields, token_logprobs).
    """
    raise NotImplementedError("C3 extract: extract() — see docs/ARCHITECTURE.md §3, §11 Week 2")
