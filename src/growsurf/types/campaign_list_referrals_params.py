# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .campaign.referral_status import ReferralStatus

__all__ = ["CampaignListReferralsParams"]


class CampaignListReferralsParams(TypedDict, total=False):
    desc: bool
    """Return results in descending order when true."""

    email: str
    """URL-encoded email value to filter referral results."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name value to filter results."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name value to filter results."""

    limit: int
    """Number of results to return. Maximum 100."""

    next_id: Annotated[str, PropertyInfo(alias="nextId")]
    """ID to start the next paged result set with."""

    offset: int
    """Offset number used to skip through a result set."""

    referral_status: Annotated[ReferralStatus, PropertyInfo(alias="referralStatus")]

    sort_by: Annotated[
        Literal["updatedAt", "createdAt", "email", "firstName", "lastName", "referralStatus", "referralTriggeredAt"],
        PropertyInfo(alias="sortBy"),
    ]
    """Field used to sort referral results."""
