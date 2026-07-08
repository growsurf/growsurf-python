# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .reward_tax_valuation import RewardTaxValuation
from ..commission_structure import CommissionStructure

__all__ = ["Reward"]


class Reward(BaseModel):
    id: str
    """The unique identifier of the campaign reward."""

    is_unlimited: bool = FieldInfo(alias="isUnlimited")
    """`true` if this reward can be earned by a single participant an unlimited number of times."""

    metadata: Dict[str, object]
    """The reward metadata."""

    type: Literal["SINGLE_SIDED", "DOUBLE_SIDED", "MILESTONE", "LEADERBOARD", "AFFILIATE"]
    """The reward type."""

    commission_structure: Optional[CommissionStructure] = FieldInfo(alias="commissionStructure", default=None)
    """The reward commission structure. Present only for affiliate programs."""

    conversions_required: Optional[int] = FieldInfo(alias="conversionsRequired", default=None)
    """The number of referrals a participant must make to earn this reward."""

    coupon_code: Optional[str] = FieldInfo(alias="couponCode", default=None)
    """A legacy static coupon code shown to the referrer in the reward-won email and webhook.

    Display text only (GrowSurf does not create or validate it); superseded by a
    connected billing integration's issued coupon when one exists.
    """

    description: Optional[str] = None
    """The reward description shown to the referrer."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """The reward image URL."""

    limit: Optional[int] = None
    """The number of times a participant can earn this reward (overridden when `isUnlimited` is `true`).

    `-1` represents an unlimited reward in REST responses.
    """

    limit_duration: Optional[Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"]] = FieldInfo(
        alias="limitDuration", default=None
    )
    """Whether the reward can be earned in total, on a monthly basis, or on a yearly basis."""

    next_milestone_prefix: Optional[str] = FieldInfo(alias="nextMilestonePrefix", default=None)
    """Text displayed in front of a participant's referral count for UI purposes.

    Applicable for milestone rewards (when `type` is `MILESTONE`).
    """

    next_milestone_suffix: Optional[str] = FieldInfo(alias="nextMilestoneSuffix", default=None)
    """Text displayed after a participant's referral count for UI purposes.

    Applicable for milestone rewards (when `type` is `MILESTONE`).
    """

    number_of_winners: Optional[int] = FieldInfo(alias="numberOfWinners", default=None)
    """The maximum number of winners. Only applies to `LEADERBOARD` rewards.

    With `limitDuration` `PER_MONTH` this many top referrers win each month; otherwise
    this many win in total.
    """

    order: Optional[int] = None
    """If there are multiple rewards, the order in which the reward should be displayed."""

    referral_coupon_code: Optional[str] = FieldInfo(alias="referralCouponCode", default=None)
    """A legacy static coupon code shown to the referred friend in the reward-won email and webhook (double-sided rewards).

    Same caveats as `couponCode`: display text only, superseded by a connected billing
    integration's issued coupon when one exists.
    """

    referral_description: Optional[str] = FieldInfo(alias="referralDescription", default=None)
    """The reward description shown to the referred friend (only applicable for double-sided reward types)."""

    referred_reward_upfront: Optional[bool] = FieldInfo(alias="referredRewardUpfront", default=None)
    """Only applies to double-sided rewards.

    When `true`, the referred friend's reward is delivered upfront as a discount and
    no `ParticipantReward` is created for them when the referral triggers.
    """

    referred_value: Optional[RewardTaxValuation] = FieldInfo(alias="referredValue", default=None)
    """Tax valuation for the referred friend's side of a double-sided reward.

    Defaults to not tax-reportable (a purchase rebate).
    """

    value: Optional[RewardTaxValuation] = None
    """Tax valuation for the reward (the referrer's side of a double-sided reward).

    Used by tax documentation / 1099 reporting.
    """
