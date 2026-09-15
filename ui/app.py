"""C7 — Review queue: Gradio interface for human review.

Presents only what a reviewer needs: the page image with the implicated
region highlighted, the model's proposed value, and the failed rule stated
in plain language. Corrections write back to `reviews` (docs/ARCHITECTURE.md
§6) and become gold-standard labels for the next fine-tuning round.

in  -> escalated records (from the attest.agent repair loop, or router
       `unsupported` classifications)
out -> verified records + new labels

TODO(week 5): build against the FastAPI backend (attest.api.main).
"""

import gradio as gr


def build_ui() -> "gr.Blocks":
    raise NotImplementedError("ui/app.py: build_ui() — see docs/ARCHITECTURE.md §11 Week 5")


if __name__ == "__main__":
    build_ui().launch()
