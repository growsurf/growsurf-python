# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .campaign.referral_status import ReferralStatus

__all__ = ["ReferralList", "Referral"]


class Referral(BaseModel):
    id: str

    created_at: int = FieldInfo(alias="createdAt")

    email: str

    referral_status: ReferralStatus = FieldInfo(alias="referralStatus")

    referred_by: str = FieldInfo(alias="referredBy")

    updated_at: int = FieldInfo(alias="updatedAt")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)


class ReferralList(BaseModel):
    limit: int

    more: bool

    referrals: List[Referral]

    next_id: Optional[str] = FieldInfo(alias="nextId", default=None)

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
