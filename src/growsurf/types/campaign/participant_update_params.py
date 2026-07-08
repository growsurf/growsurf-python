# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ParticipantUpdateParams"]


class ParticipantUpdateParams(TypedDict, total=False):
    id: Required[str]

    email: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    metadata: Dict[str, object]
    """Shallow custom metadata object."""

    notes: str
    """Freeform internal notes about the participant (internal only, never exposed to
    participants)."""

    paypal_email: Annotated[str, PropertyInfo(alias="paypalEmail")]
    """The participant's PayPal email address, used for affiliate payouts."""

    referral_status: Annotated[
        Literal["CREDIT_PENDING", "CREDIT_AWARDED", "CREDIT_EXPIRED"], PropertyInfo(alias="referralStatus")
    ]

    referred_by: Annotated[str, PropertyInfo(alias="referredBy")]

    unsubscribed: bool

    vanity_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="vanityKeys")]
