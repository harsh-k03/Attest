"""C4 — Confidence estimator: raw token logprobs -> calibrated p(correct) per field.

in  -> field spans + logprobs
out -> p(correct) per field
tech -> temperature scaling (primary), isotonic regression (fallback)

Reliability is reported as expected calibration error (ECE), not accuracy —
a confident-and-wrong model is the failure mode this component exists to
catch. See docs/ARCHITECTURE.md#c4--confidence-estimator and §5.
"""
