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

    status: Literal["PENDING", "FULFILLED"]

    approved: Optional[bool] = None

    approved_at: Optional[int] = FieldInfo(alias="approvedAt", default=None)

    commission_structure: Optional[CommissionStructure] = FieldInfo(alias="commissionStructure", default=None)

    fulfilled_at: Optional[int] = FieldInfo(alias="fulfilledAt", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    is_fulfilled: Optional[bool] = FieldInfo(alias="isFulfilled", default=None)

    is_referrer: Optional[bool] = FieldInfo(alias="isReferrer", default=None)

    referred_id: Optional[str] = FieldInfo(alias="referredId", default=None)

    referrer_id: Optional[str] = FieldInfo(alias="referrerId", default=None)

    unread: Optional[bool] = None
