"""Document-type classifier: receipt | invoice | unsupported.

Deliberately cheap relative to the extractor VLM — this only needs to pick
which schema/prompt to use downstream, not extract anything itself.

TODO(week 1-2): linear probe on frozen CLIP features as the first cut;
promote to a fine-tuned ViT only if accuracy demands it.
"""

from enum import Enum


class DocType(str, Enum):
    RECEIPT = "receipt"
    INVOICE = "invoice"
    UNSUPPORTED = "unsupported"


def classify(page_image) -> DocType:
    raise NotImplementedError("C2 router: classify() — see docs/ARCHITECTURE.md §3, §11 Week 1")
