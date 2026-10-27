# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .campaign.language import Language

__all__ = ["CampaignCreateMobileParticipantTokenParams"]


class CampaignCreateMobileParticipantTokenParams(TypedDict, total=False):
    email: Required[str]

    fingerprint: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    ip_address: Annotated[str, PropertyInfo(alias="ipAddress")]

    is_affiliate: Annotated[bool, PropertyInfo(alias="isAffiliate")]
    """Affiliate programs only. Controls affiliate enrollment for a new participant.

    `true` enrolls the participant with `affiliateStatus: APPROVED`; `false` creates a
    non-affiliate without `affiliateStatus`. Existing participants are returned
    unchanged.
    """

    language: Language
    """The language of the participant's portal and program emails.

    Stored when it is one of the program's languages. A regional tag maps to its
    language (for example, `es-MX` is stored as `es`). Any other value is ignored and
    the program's base language applies. Applied only when this request creates the
    participant.
    """

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    metadata: Dict[str, object]
    """Shallow custom metadata object."""

    mobile_instance_id: Annotated[str, PropertyInfo(alias="mobileInstanceId")]
    """Optional app-install scoped identifier for native mobile anti-fraud.

    Recommended for mobile participant creation and mobile participant token flows.
    The official mobile SDKs generate this as a lowercase UUID.
    """

    referral_status: Annotated[Literal["CREDIT_PENDING", "CREDIT_AWARDED"], PropertyInfo(alias="referralStatus")]

    referred_at: Annotated[Optional[int], PropertyInfo(alias="referredAt")]
    """When the participant was referred, in Unix milliseconds.

    Used only with a valid `referredBy`. If you omit `referralStatus`, GrowSurf
    compares this time with the program's referral credit window to set it. Defaults
    to the time of the request.
    """

    referred_by: Annotated[str, PropertyInfo(alias="referredBy")]
    """Referrer participant ID or email address."""
