# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..commission_structure import CommissionStructure

__all__ = ["Campaign", "Reward"]


class Reward(BaseModel):
    id: str

    is_unlimited: bool = FieldInfo(alias="isUnlimited")

    metadata: Dict[str, object]
    """Shallow custom metadata object."""

    type: Literal["SINGLE_SIDED", "DOUBLE_SIDED", "MILESTONE", "LEADERBOARD", "AFFILIATE"]

    commission_structure: Optional[CommissionStructure] = FieldInfo(alias="commissionStructure", default=None)

    conversions_required: Optional[int] = FieldInfo(alias="conversionsRequired", default=None)

    coupon_code: Optional[str] = FieldInfo(alias="couponCode", default=None)

    description: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    limit: Optional[int] = None
    """`-1` represents an unlimited reward in REST responses."""

    limit_duration: Optional[Literal["IN_TOTAL", "PER_MONTH"]] = FieldInfo(alias="limitDuration", default=None)

    next_milestone_prefix: Optional[str] = FieldInfo(alias="nextMilestonePrefix", default=None)

    next_milestone_suffix: Optional[str] = FieldInfo(alias="nextMilestoneSuffix", default=None)

    number_of_winners: Optional[int] = FieldInfo(alias="numberOfWinners", default=None)

    order: Optional[int] = None

    referral_description: Optional[str] = FieldInfo(alias="referralDescription", default=None)

    referred_reward_upfront: Optional[bool] = FieldInfo(alias="referredRewardUpfront", default=None)


class Campaign(BaseModel):
    id: str

    impression_count: int = FieldInfo(alias="impressionCount")

    invite_count: int = FieldInfo(alias="inviteCount")

    name: str

    participant_count: int = FieldInfo(alias="participantCount")

    referral_count: int = FieldInfo(alias="referralCount")

    rewards: List[Reward]

    status: Literal["DRAFT", "IN_PROGRESS", "COMPLETE", "DELETED"]

    type: Literal["REFERRAL", "AFFILIATE"]

    winner_count: int = FieldInfo(alias="winnerCount")

    currency_iso: Optional[str] = FieldInfo(alias="currencyISO", default=None)
