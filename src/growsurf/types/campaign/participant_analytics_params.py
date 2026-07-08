# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantAnalyticsParams"]


class ParticipantAnalyticsParams(TypedDict, total=False):
    id: Required[str]

    days: int
    """Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825."""

    end_date: Annotated[int, PropertyInfo(alias="endDate")]
    """End date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """

    include: Literal["series"]
    """Set to `series` to also return this participant's own activity per period."""

    interval: Literal["day", "week", "month"]
    """Bucket size for the `series` (only used with `include=series`).

    Defaults to `day`.
    """

    start_date: Annotated[int, PropertyInfo(alias="startDate")]
    """Start date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """
