# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignListPayoutsParams"]


class CampaignListPayoutsParams(TypedDict, total=False):
    limit: int
    """Number of results to return. Maximum 100."""

    next_id: Annotated[str, PropertyInfo(alias="nextId")]
    """ID to start the next paged result set with."""

    status: Literal["UPCOMING", "QUEUED", "ISSUED", "FAILED"]
    """Participant payout status."""
