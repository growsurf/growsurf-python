# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantTriggerReferralParams"]


class ParticipantTriggerReferralParams(TypedDict, total=False):
    id: Required[str]

    delay_in_days: Annotated[int, PropertyInfo(alias="delayInDays")]
    """Number of whole days to hold referral credit before it is awarded.

    Useful for honoring a refund window before crediting a referrer. Omit this field
    to award credit immediately. The credit is awarded automatically once the delay
    elapses, and can be cancelled before then with the Cancel delayed referral
    trigger request.
    """
