"""Tests for the C5 rule engine (attest.validate.engine).

Start here once engine.py is implemented (Week 3): each rule in
validate/rules/*.yaml should have at least one passing and one failing
fixture, especially the arithmetic rules (items-sum-to-subtotal,
total-reconciles) since those are what the repair-loop ablation depends on.
"""

import pytest


@pytest.mark.skip(reason="C5 validator not yet implemented — see docs/ARCHITECTURE.md §11 Week 3")
def test_items_sum_to_subtotal_passes_on_valid_receipt():
    ...


@pytest.mark.skip(reason="C5 validator not yet implemented — see docs/ARCHITECTURE.md §11 Week 3")
def test_total_reconciles_fails_on_arithmetic_mismatch():
    ...
