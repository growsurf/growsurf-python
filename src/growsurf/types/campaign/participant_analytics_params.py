# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantAnalyticsParams"]


class ParticipantAnalyticsParams(TypedDict, total=False):
    id: Required[str]

    days: int
    """Last number of days for optional `series` and `email` analytics.

    Defaults to 365. Maximum 1825. Does not filter the top-level all-time totals.
    """

    end_date: Annotated[int, PropertyInfo(alias="endDate")]
    """End of a custom `series` and `email` analytics window as a Unix timestamp.

    Expressed in milliseconds. Set it together with `startDate`. Does not filter the
    top-level all-time totals.
    """

    include: str
    """Comma-separated optional data.

    `series` returns this participant's own activity per period; `email` returns
    `sent`, `delivered`, `opened`, `clicked`, `bounced`, `spamComplaints`, and
    per-email-type metrics attributed to the participant for the requested analytics
    window (including invitations they sent); `activation` returns the cohort anchor
    and covered first milestones. Request `activation,series` to add covered
    portal-view and share-action counts to every series item. Only documented tokens
    are accepted; an unknown token returns `400`.
    """

    interval: Literal["day", "week", "month"]
    """Bucket size for the `series` (only used when `include` contains `series`).

    Defaults to `day`.
    """

    start_date: Annotated[int, PropertyInfo(alias="startDate")]
    """Start of a custom `series` and `email` analytics window as a Unix timestamp.

    Expressed in milliseconds. Set it together with `endDate`. Does not filter the
    top-level all-time totals.
    """
