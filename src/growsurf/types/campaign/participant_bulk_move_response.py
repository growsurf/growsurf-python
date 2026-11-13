# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantBulkMoveResponse", "Result", "Summary"]


class Result(BaseModel):
    identifier: str
    """The submitted participant ID or email address, echoed back as received."""

    index: int
    """Zero-based position of this entry in the submitted `participants` array."""

    status: Literal["MOVED", "NOT_FOUND", "DUPLICATE", "ERROR"]
    """Per-row outcome.

    `MOVED` — the participant was resolved and is now in the target group.
    `NOT_FOUND` — no participant matches the ID or email. `DUPLICATE` — the entry
    resolves to the same participant as an earlier entry in the same request.
    `ERROR` — the lookup failed for this row.
    """

    email: Optional[str] = None
    """The resolved participant's email address. Present on `MOVED` rows."""

    message: Optional[str] = None
    """Human-readable detail for `NOT_FOUND`, `DUPLICATE`, and `ERROR` rows."""

    participant_id: Optional[str] = FieldInfo(alias="participantId", default=None)
    """The resolved GrowSurf participant ID.

    Present when the entry resolved to a participant.
    """


class Summary(BaseModel):
    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Entries that resolved to the same participant as an earlier entry."""

    error_count: int = FieldInfo(alias="errorCount")
    """Entries that failed to look up."""

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)
    """The target group, or `None` for Default."""

    moved_count: int = FieldInfo(alias="movedCount")
    """Entries that resolved to a participant and were moved."""

    not_found_count: int = FieldInfo(alias="notFoundCount")
    """Entries that did not match any participant."""

    total: int
    """Number of entries submitted in this request."""


class ParticipantBulkMoveResponse(BaseModel):
    results: List[Result]
    """One entry per submitted identifier, in the same order as the request."""

    summary: Summary
    """Counts of submitted, moved, not-found, duplicate, and failed entries."""
