"""C1 — Ingest: normalise arbitrary input into page images + optional text layer.

in  -> PDF, PNG, JPEG
out -> page images (fixed resolution) + text layer when the source is a
       digital PDF
tech -> pypdfium2 for PDF rasterisation, OpenCV for deskew/normalise

See docs/ARCHITECTURE.md#c1--ingest.
"""
