"""The three repair strategies (docs/ARCHITECTURE.md §4):

  1. re-crop the implicated region and re-extract just that region
     (e.g. line-item table, totals block)
  2. targeted re-prompt for a single field
  3. OCR fallback + regex parsing over the full page text

Strategy selection is driven by failure type, not chosen at random — see the
failure/cause/strategy table in docs/ARCHITECTURE.md §4.
"""

from enum import Enum


class Strategy(str, Enum):
    RECROP = "recrop"
    TARGETED_REPROMPT = "targeted_reprompt"
    OCR_FALLBACK = "ocr_fallback"


def select_strategy(validation_report: dict) -> Strategy:
    raise NotImplementedError("C6 agent: select_strategy() — see docs/ARCHITECTURE.md §11 Week 4")
