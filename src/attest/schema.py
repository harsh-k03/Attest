"""The target schema: what Attest extracts from a document.

Every component (extractor, validator, repair agent, store, metrics) reads or
writes these models, so this file is the contract between them. Any breaking
change here must bump SCHEMA_VERSION.

Design decisions:
  - Money is Decimal, never float. The validator checks sums exactly, and in
    floating point 0.1 + 0.2 != 0.3.
  - Every field is optional. A missing value means "the extractor could not
    find it", which is information, not an error. (CORD-v2 has no vendor or
    date labels at all.)
  - Types are checked here (is it a number? a date?). Value checks (at most
    2 decimals, date not in the future, items sum to subtotal) belong to the
    validator, so they become failed rules the repair loop can act on.
  - extra="forbid": if the model invents a key, it is rejected at the
    boundary instead of being silently stored.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

SCHEMA_VERSION = "1.0"


class DocType(StrEnum):
    RECEIPT = "receipt"
    INVOICE = "invoice"
    UNSUPPORTED = "unsupported"


class _Model(BaseModel):
    """Base for every schema model: unknown keys are an error."""

    model_config = ConfigDict(extra="forbid")


class LineItem(_Model):
    description: str | None = None
    quantity: Decimal | None = None
    unit_price: Decimal | None = None
    amount: Decimal | None = None


class ReceiptFields(_Model):
    doc_type: Literal["receipt"] = "receipt"
    vendor_name: str | None = None
    transaction_date: date | None = None
    currency: str | None = None
    line_items: list[LineItem] = Field(default_factory=list)
    subtotal: Decimal | None = None
    service_charge: Decimal | None = None
    tax: Decimal | None = None
    discount: Decimal | None = None
    total: Decimal | None = None


class InvoiceFields(_Model):
    doc_type: Literal["invoice"] = "invoice"
    vendor_name: str | None = None
    customer_name: str | None = None
    invoice_number: str | None = None
    issue_date: date | None = None
    due_date: date | None = None
    currency: str | None = None
    line_items: list[LineItem] = Field(default_factory=list)
    subtotal: Decimal | None = None
    tax: Decimal | None = None
    discount: Decimal | None = None
    total: Decimal | None = None


def flatten(fields: ReceiptFields | InvoiceFields) -> dict[str, object]:
    """Flatten a field set into {field_path: value}.

    Paths look like "total" or "line_items[2].amount". Confidences, validation
    reports and metrics all use these same paths, so this function is the one
    place that defines them.
    """
    flat: dict[str, object] = {}
    for name, value in fields:
        if name == "doc_type":
            continue
        if isinstance(value, list):
            for i, item in enumerate(value):
                for sub_name, sub_value in item:
                    flat[f"{name}[{i}].{sub_name}"] = sub_value
        else:
            flat[name] = value
    return flat