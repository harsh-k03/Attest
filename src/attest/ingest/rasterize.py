"""Rasterise PDFs/images into normalised page images.

Target: 200 DPI, deskewed, long edge capped so extractor token budgets are
predictable across documents. Digital PDFs also yield a text layer that the
router/extractor may use alongside the image.

TODO(week 1-2): implement with pypdfium2 (PDF -> page images) and OpenCV
(deskew via minAreaRect on text-mask contours; long-edge cap + letterbox).
"""

from pathlib import Path


def rasterize(path: Path, dpi: int = 200, max_long_edge: int = 1600):
    """Return a list of normalised page images (and text layer, if any) for `path`.

    Raises NotImplementedError until Week 1 of the build plan.
    """
    raise NotImplementedError("C1 ingest: rasterize() — see docs/ARCHITECTURE.md §3, §11 Week 1")
