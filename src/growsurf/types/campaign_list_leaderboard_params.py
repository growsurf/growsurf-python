# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignListLeaderboardParams"]


class CampaignListLeaderboardParams(TypedDict, total=False):
    is_monthly: Annotated[bool, PropertyInfo(alias="isMonthly")]
    """Deprecated. Use `leaderboardType=CURRENT_MONTH` instead."""

    leaderboard_type: Annotated[
        Literal[
            "ALL_TIME",
            "CURRENT_MONTH",
            "PREV_MONTH",
            "TOTAL_IMPRESSION_COUNT",
            "UNIQUE_IMPRESSION_COUNT",
            "BY_COMMISSIONS",
            "BY_REVENUE",
            "BY_REFERRALS",
            "BY_LEADS",
        ],
        PropertyInfo(alias="leaderboardType"),
    ]
    """Leaderboard ordering mode."""

    limit: int
    """Number of results to return. Maximum 100."""

    next_id: Annotated[str, PropertyInfo(alias="nextId")]
    """ID to start the next paged result set with."""
