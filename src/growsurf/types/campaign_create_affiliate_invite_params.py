# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignCreateAffiliateInviteParams"]


class CampaignCreateAffiliateInviteParams(TypedDict, total=False):
    email: Required[str]
    """Valid email address to invite. Maximum 255 characters."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """Invitee first name, used in the invite email. Maximum 255 characters."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Invitee last name. Maximum 255 characters."""
