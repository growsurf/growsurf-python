# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignRetrieveAnalyticsParams"]


class CampaignRetrieveAnalyticsParams(TypedDict, total=False):
    days: int
    """Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825."""

    end_date: Annotated[int, PropertyInfo(alias="endDate")]
    """End date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """

    start_date: Annotated[int, PropertyInfo(alias="startDate")]
    """Start date of the analytics timeframe as a Unix timestamp in milliseconds.

    Required if `days` is not set.
    """
