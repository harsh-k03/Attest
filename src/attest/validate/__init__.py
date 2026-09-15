"""C5 — Validator: deterministic rule engine. The component that catches the
errors the model is confident about.

Rule categories (declared per-schema in validate/rules/*.yaml so new checks
never require code changes):
  - arithmetic    line items sum to subtotal; subtotal + tax - discount = total
  - type/format   dates parse & not in the future; amounts <= 2 decimals; ...
  - cross-field   due date >= issue date; tax rate in permitted band
  - referential   vendor resolves against the known-vendor table, fuzzily

in  -> ExtractionRecord
out -> validation report: per-rule pass/fail with implicated fields

See docs/ARCHITECTURE.md#c5--validator.
"""
