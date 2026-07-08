# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantBulkDeleteResponse", "Result", "Summary"]


class Result(BaseModel):
    identifier: str
    """The submitted participant ID or email address, echoed back as received."""

    index: int
    """Zero-based position of this entry in the submitted `participants` array."""

    status: Literal["DELETED", "NOT_FOUND", "DUPLICATE", "ERROR"]
    """Per-row outcome.

    `DELETED` — the participant was resolved and removed. `NOT_FOUND` — no
    participant matches the ID or email. `DUPLICATE` — the entry resolves to the
    same participant as an earlier entry in the same request. `ERROR` — the lookup
    or deletion failed for this row.
    """

    email: Optional[str] = None
    """The resolved participant's email address. Present on `DELETED` rows."""

    message: Optional[str] = None
    """Human-readable detail for `NOT_FOUND`, `DUPLICATE`, and `ERROR` rows."""

    participant_id: Optional[str] = FieldInfo(alias="participantId", default=None)
    """The resolved GrowSurf participant ID.

    Present when the entry resolved to a participant.
    """


class Summary(BaseModel):
    deleted_count: int = FieldInfo(alias="deletedCount")
    """Entries that resolved to a participant and were deleted."""

    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Entries that resolved to the same participant as an earlier entry."""

    error_count: int = FieldInfo(alias="errorCount")
    """Entries that failed to look up or delete."""

    not_found_count: int = FieldInfo(alias="notFoundCount")
    """Entries that did not match any participant."""

    total: int
    """Number of entries submitted in this request."""


class ParticipantBulkDeleteResponse(BaseModel):
    results: List[Result]
    """One entry per submitted identifier, in the same order as the request."""

    summary: Summary
