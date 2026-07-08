# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignRetrieveAnalyticsParams"]


class CampaignRetrieveAnalyticsParams(TypedDict, total=False):
    days: int
    """Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825."""

    end_date: Annotated[int, PropertyInfo(alias="endDate")]
    """End date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """

    include: str
    """Comma-separated list of optional enrichments (opt-in to keep the default
    response lean).

    Any of `previousPeriod` (totals for the equal-length window immediately before
    the requested one), `statusCounts` (reward and, for affiliate programs,
    affiliate/commission/payout status breakdowns), and `rates` (derived referral
    rates).
    """

    interval: Literal["day", "week", "month", "total"]
    """When set to `day`, `week`, or `month`, the response also includes a `series`
    array with per-period totals.

    Defaults to `total` (no series).
    """

    start_date: Annotated[int, PropertyInfo(alias="startDate")]
    """Start date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """
