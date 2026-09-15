"""C3 — Extractor: the core model. LoRA-adapted Qwen2.5-VL-3B-Instruct that
emits the flat target schema as constrained (grammar-guided) JSON.

in  -> page image + schema prompt
out -> JSON fields + per-token logprobs (retained for C4 confidence estimator)
tech -> Qwen2.5-VL-3B + PEFT/LoRA, served on vLLM with guided decoding

Malformed JSON is treated as an engineering failure, not a model failure —
generation must be grammar-constrained so it never happens.

See docs/ARCHITECTURE.md#c3--extractor.
"""
