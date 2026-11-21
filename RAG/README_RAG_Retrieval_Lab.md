# RAG Retrieval Lab

A concise, API-free Jupyter demo of **BM25**, **dense semantic retrieval**, **hybrid search with RRF**, **cross-encoder reranking**, and **retrieval evaluation**.

## Quick start

1. Open [`RAG_Retrieval_Lab.ipynb`](RAG_Retrieval_Lab.ipynb) in Google Colab or Jupyter.
2. Run the notebook cells top to bottom. The setup cell installs Python packages; the first model load downloads two pretrained Hugging Face models.
3. Compare BM25, Dense, Hybrid/RRF, and Reranked results in the metrics table.
4. **Optional:** change `RUN_LOCAL_GENERATION = True` to run a local `google/flan-t5-small` model for grounded-answer generation. No API key is required.

## Requirements

- Python and Jupyter/Colab, CPU is enough for the toy corpus.
- Internet on the first run for pip packages and pretrained weights. Later runs can reuse cached models.
- No OpenAI, Cohere, Pinecone, or Tavily account required.

## Project structure

```
RAG_Retrieval_Lab.ipynb
README_RAG_Retrieval_Lab.md
```

## What it demonstrates

- Chunking, stable document identifiers and parent-child sections
- Lexical vs semantic retrieval
- RRF rank fusion (no raw-score calibration)
- Query-document cross-encoder reranking
- Recall@3, MRR@3, nDCG@3, and latency comparison
- Grounded prompt with source IDs; optional local LLM generation
- Token-level MaxSim concept for ColBERT

## Evaluation warning

The corpus comprises **18 small explanatory documents** with **10 toy queries** and manually specified relevance judgments. The included metrics are illustrative and must **not** be reported as BEIR results or evidence of production performance. Reranking may or may not improve the ranking on this small corpus.

## For a stronger portfolio

Use a publicly redistributable dataset, establish a held-out set of judged queries, evaluate multiple settings, report hardware/model versions and p50/p95 latency, then add a small `pytest` suite and CI.

## References

- [Sentence Transformers: Usage](https://www.sbert.net/docs/sentence_transformer/usage/usage.html)
- [Sentence Transformers: Cross-Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- [rank-bm25](https://github.com/dorianbrown/rank_bm25)
- [FLAN-T5 model card](https://huggingface.co/google/flan-t5-small)
