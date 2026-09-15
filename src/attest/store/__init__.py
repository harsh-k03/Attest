"""Persistence layer: SQLAlchemy models + queries over the MySQL 8 schema
defined in docs/ARCHITECTURE.md §6 (documents, extractions, reviews, vendors).

Two properties the schema is designed to preserve:
  - attempts are append-only (extractions.attempt) — the repair history is
    never overwritten, so the audit trail is real rather than claimed
  - reviews.was_correct closes the loop: it is simultaneously the human
    correction, the calibration measurement, and next round's training label
"""
