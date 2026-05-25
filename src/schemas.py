from pydantic import BaseModel, Field


class DraftRequest(BaseModel):
    case_id: str = Field(..., examples=["CASE-10291"])
    question: str
    jurisdiction: str | None = None
    effective_date: str | None = None


class Citation(BaseModel):
    source: str
    section: str
    effective_date: str | None = None
    snippet: str


class DraftResponse(BaseModel):
    case_id: str
    answer: str
    citations: list[Citation]
    latency_ms: int
    evaluation: dict[str, float | None]
