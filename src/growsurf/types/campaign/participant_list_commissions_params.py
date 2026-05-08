# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantListCommissionsParams"]


class ParticipantListCommissionsParams(TypedDict, total=False):
    id: Required[str]

    limit: int
    """Number of results to return. Maximum 100."""

    next_id: Annotated[str, PropertyInfo(alias="nextId")]
    """ID to start the next paged result set with."""

    status: Literal["PENDING", "APPROVED", "PAID", "REVERSED", "DELETED"]
    """Participant commission status."""
