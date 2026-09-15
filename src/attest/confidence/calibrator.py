"""Fits/applies the confidence calibrator.

TODO(week 3): mean token logprob per field span as the base signal;
temperature-scaled logistic regression fitted on the validation split as the
primary calibrator, isotonic regression as a documented fallback if ECE stays
high after temperature scaling (see docs/ARCHITECTURE.md §12 risks).
"""


def calibrate(field_logprobs: dict[str, float]) -> dict[str, float]:
    """Return {field: calibrated p(correct)}."""
    raise NotImplementedError("C4 confidence: calibrate() — see docs/ARCHITECTURE.md §11 Week 3")


def expected_calibration_error(confidences, correctness) -> float:
    """ECE over a validation set: gap between stated confidence and observed
    correctness rate, bucketed. Target: < 0.05 (Week 3 gate)."""
    raise NotImplementedError("C4 confidence: expected_calibration_error()")
