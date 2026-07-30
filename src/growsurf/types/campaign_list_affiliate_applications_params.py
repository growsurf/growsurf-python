# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CampaignListAffiliateApplicationsParams"]


class CampaignListAffiliateApplicationsParams(TypedDict, total=False):
    limit: int
    """How many applications to return per page (1-100)."""

    offset: int
    """Offset number used to skip through a result set."""

    status: Literal["PENDING", "APPROVED", "DENIED"]
    """Only return applications with this status."""
