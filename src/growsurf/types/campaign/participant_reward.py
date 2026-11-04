# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..commission_structure import CommissionStructure

__all__ = ["ParticipantReward"]


class ParticipantReward(BaseModel):
    id: str

    reward_id: str = FieldInfo(alias="rewardId")

    status: Literal["PENDING", "FULFILLED", "CANCELLED"]

    approved: Optional[bool] = None

    approved_at: Optional[int] = FieldInfo(alias="approvedAt", default=None)

    amount: Optional[float] = None
    """What the reward is worth in major units of `currency_iso`.

    `None` for a percent-off coupon or when no amount is available.
    """

    amount_source: Optional[
        Literal[
            "STRIPE",
            "CHARGEBEE",
            "RECURLY",
            "CHARGIFY",
            "PAYPAL",
            "VENMO",
            "TANGO_CARD",
            "TREMENDOUS",
            "XTRM",
            "METADATA",
        ]
    ] = FieldInfo(alias="amountSource", default=None)
    """Where `amount` or `percent_off` comes from.

    `METADATA` means the amount saved when the reward was earned.
    """

    commission_structure: Optional[CommissionStructure] = FieldInfo(alias="commissionStructure", default=None)

    currency_iso: Optional[str] = FieldInfo(alias="currencyISO", default=None)

    fulfilled_at: Optional[int] = FieldInfo(alias="fulfilledAt", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    is_fulfilled: Optional[bool] = FieldInfo(alias="isFulfilled", default=None)

    is_referrer: Optional[bool] = FieldInfo(alias="isReferrer", default=None)

    percent_off: Optional[float] = FieldInfo(alias="percentOff", default=None)
    """Discount of a percent-off coupon (`20` = 20% off); `None` for every other reward."""

    referred_id: Optional[str] = FieldInfo(alias="referredId", default=None)

    referrer_id: Optional[str] = FieldInfo(alias="referrerId", default=None)

    unread: Optional[bool] = None
