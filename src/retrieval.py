from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievedChunk:
    source: str
    section: str
    text: str
    score: float
    metadata: dict[str, str]


def merge_hybrid_results(bm25_hits: list[RetrievedChunk], vector_hits: list[RetrievedChunk]) -> list[RetrievedChunk]:
    """Deduplicate and merge BM25 + vector candidates by source/section."""
    merged: dict[tuple[str, str], RetrievedChunk] = {}
    for hit in bm25_hits + vector_hits:
        key = (hit.source, hit.section)
        current = merged.get(key)
        if current is None or hit.score > current.score:
            merged[key] = hit
    return sorted(merged.values(), key=lambda item: item.score, reverse=True)
