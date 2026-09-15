"""Metrics defined in docs/ARCHITECTURE.md §8:

  - field-level F1 (exact match after normalisation)
  - document accuracy (all fields correct)
  - expected calibration error
  - automation rate @ fixed precision (default 99%)
  - escalation rate
  - latency p50 / p95

Normalisation (documented, not just applied): currency symbols stripped,
whitespace collapsed, dates to ISO 8601, amounts to two decimals. Always
report whether a comparison is exact or normalised.
"""


def normalize(value, field_type: str):
    raise NotImplementedError("eval/metrics.py: normalize() — see docs/ARCHITECTURE.md §8")


def field_f1(predictions, ground_truth) -> dict:
    raise NotImplementedError("eval/metrics.py: field_f1()")


def document_accuracy(predictions, ground_truth) -> float:
    raise NotImplementedError("eval/metrics.py: document_accuracy()")


def automation_rate_at_precision(confidences, correctness, target_precision: float = 0.99) -> float:
    raise NotImplementedError("eval/metrics.py: automation_rate_at_precision()")
