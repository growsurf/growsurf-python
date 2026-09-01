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
    """Comma-separated list of optional data to include: `previousPeriod` adds totals
    for the equal-length window immediately before the requested one; `statusCounts`
    adds reward (and, for affiliate programs, affiliate/commission/payout) status
    breakdowns; `rates` adds derived referral rates; `email` adds `sent`, `delivered`,
    `opened`, `clicked`, `bounced`, `spamComplaints`, and per-email-type metrics.

    When `email` and an interval are both requested, each `series` item also contains
    counts for emails sent during that period. Combine `email` with `previousPeriod`
    to include the same email metrics in both windows.
    `engagement` adds covered participant activity totals, comparisons, series, and
    breakdowns.
    """

    interval: Literal["day", "week", "month", "total"]
    """When set to `day`, `week`, or `month`, the response also includes a `series`
    array with per-period totals and uses the same bucket size for `engagement.series`.

    Defaults to `total` (no legacy series); `engagement.series` uses daily buckets when
    `interval` is `total` or omitted.
    """

    platform: Literal["ALL", "WEB", "IOS", "ANDROID"]
    """Participant platform used for `engagement`. Defaults to `ALL`."""

    start_date: Annotated[int, PropertyInfo(alias="startDate")]
    """Start date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """

    timezone: str
    """IANA timezone used for engagement periods and buckets. Defaults to `UTC`."""
