"""Tests for the target schema (attest.schema)."""

from datetime import date
from decimal import Decimal

import pytest
from pydantic import ValidationError

from attest.schema import InvoiceFields, ReceiptFields, flatten


def make_receipt(**overrides) -> ReceiptFields:
    data = {
        "line_items": [
            {"description": "Nasi Goreng", "quantity": "1", "amount": "25000"},
            {"description": "Es Teh", "quantity": "2", "amount": "10000"},
        ],
        "subtotal": "35000",
        "total": "35000",
    }
    data.update(overrides)
    return ReceiptFields.model_validate(data)


def test_amounts_are_exact_decimals():
    receipt = make_receipt()
    assert isinstance(receipt.total, Decimal)
    assert sum(item.amount for item in receipt.line_items) == receipt.subtotal


def test_float_arithmetic_would_have_failed():
    # The reason money is Decimal: this is False with floats.
    assert 0.1 + 0.2 != 0.3
    assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")


def test_missing_fields_are_allowed():
    receipt = ReceiptFields()
    assert receipt.total is None
    assert receipt.line_items == []


def test_dates_are_parsed():
    invoice = InvoiceFields(issue_date="2026-10-01")
    assert invoice.issue_date == date(2026, 10, 1)


def test_unparseable_date_is_rejected():
    with pytest.raises(ValidationError):
        InvoiceFields(issue_date="not a date")


def test_invented_field_is_rejected():
    with pytest.raises(ValidationError):
        make_receipt(tip_jar="500")


def test_flatten_produces_stable_paths():
    flat = flatten(make_receipt())
    assert flat["total"] == Decimal(35000)
    assert flat["line_items[1].description"] == "Es Teh"
    assert "doc_type" not in flat