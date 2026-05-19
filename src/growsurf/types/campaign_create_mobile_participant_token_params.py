# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignCreateMobileParticipantTokenParams"]


class CampaignCreateMobileParticipantTokenParams(TypedDict, total=False):
    email: Required[str]

    fingerprint: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    ip_address: Annotated[str, PropertyInfo(alias="ipAddress")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    metadata: Dict[str, object]
    """Shallow custom metadata object."""

    referral_status: Annotated[Literal["CREDIT_PENDING", "CREDIT_AWARDED"], PropertyInfo(alias="referralStatus")]

    referred_by: Annotated[str, PropertyInfo(alias="referredBy")]
    """Referrer participant ID or email address."""
