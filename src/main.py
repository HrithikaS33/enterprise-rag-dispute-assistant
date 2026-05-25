from fastapi import FastAPI

from .schemas import DraftRequest, DraftResponse

app = FastAPI(title="Enterprise RAG Dispute Assistant")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/draft", response_model=DraftResponse)
def draft_response(request: DraftRequest) -> DraftResponse:
    """Reference endpoint showing the production contract shape."""
    return DraftResponse(
        case_id=request.case_id,
        answer="Draft generation placeholder. Connect retriever and LLM chain here.",
        citations=[],
        latency_ms=0,
        evaluation={"faithfulness": None, "citation_coverage": None},
    )
