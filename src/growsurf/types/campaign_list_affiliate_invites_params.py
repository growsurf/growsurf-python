# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CampaignListAffiliateInvitesParams"]


class CampaignListAffiliateInvitesParams(TypedDict, total=False):
    limit: int
    """How many invites to return per page (1-100)."""

    offset: int
    """Offset number used to skip through a result set."""

    status: Literal["PENDING", "ACCEPTED", "EXPIRED", "REVOKED"]
    """Only return invites with this status."""
