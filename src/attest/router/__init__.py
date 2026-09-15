"""C2 — Router: classify a document as receipt / invoice / unsupported.

in  -> page images
out -> doc type + schema id (unsupported documents skip extraction entirely
       and go straight to the human review queue)
tech -> fine-tuned ViT, or a linear probe on CLIP features

See docs/ARCHITECTURE.md#c2--router.
"""
