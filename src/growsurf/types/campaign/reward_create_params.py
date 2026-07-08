# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .reward_tax_valuation import RewardTaxValuation
from ..commission_structure import CommissionStructure

__all__ = ["RewardCreateParams"]


class RewardCreateParams(TypedDict, total=False):
    type: Required[Literal["SINGLE_SIDED", "DOUBLE_SIDED", "MILESTONE", "LEADERBOARD", "AFFILIATE"]]
    """The reward type. Immutable after creation."""

    commission_structure: Annotated[CommissionStructure, PropertyInfo(alias="commissionStructure")]
    """The affiliate commission structure (AFFILIATE rewards only)."""

    conversions_required: Annotated[int, PropertyInfo(alias="conversionsRequired")]
    """The number of referrals required to earn the reward."""

    coupon_code: Annotated[Optional[str], PropertyInfo(alias="couponCode")]
    """A legacy static coupon code shown to the referrer in the reward-won email and webhook.

    Display text only (GrowSurf does not create or validate it); superseded by a
    connected billing integration's issued coupon when one exists.
    """

    description: str
    """The reward description shown to the referrer."""

    image_url: Annotated[Optional[str], PropertyInfo(alias="imageUrl")]
    """An image URL for the reward."""

    is_unlimited: Annotated[bool, PropertyInfo(alias="isUnlimited")]
    """Whether the reward can be earned an unlimited number of times.

    Defaults to `true`, except `MILESTONE` rewards, which can only be earned once.
    """

    is_visible: Annotated[bool, PropertyInfo(alias="isVisible")]
    """Whether the reward is enabled.

    When `false`, the reward is disabled: hidden from participants (including those who
    already earned it) and no longer awarded. Set `true` to make it visible and awardable.
    """

    limit: int
    """The number of times a participant can earn the reward (overridden by `isUnlimited`)."""

    limit_duration: Annotated[Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"], PropertyInfo(alias="limitDuration")]
    """The window over which `limit` applies."""

    metadata: Dict[str, object]
    """Custom key/value metadata (single-level; values are stored as strings)."""

    next_milestone_prefix: Annotated[Optional[str], PropertyInfo(alias="nextMilestonePrefix")]
    """Text shown before a participant's referral count in milestone progress copy.

    Applies to `MILESTONE` rewards (e.g. "You are only").
    """

    next_milestone_suffix: Annotated[Optional[str], PropertyInfo(alias="nextMilestoneSuffix")]
    """Text shown after a participant's referral count in milestone progress copy.

    Applies to `MILESTONE` rewards (e.g. "referrals away from your next reward!").
    """

    number_of_winners: Annotated[int, PropertyInfo(alias="numberOfWinners")]
    """The maximum number of winners. Only applies to `LEADERBOARD` rewards.

    With `limitDuration` `PER_MONTH` this many top referrers win each month; otherwise
    this many win in total. A `LEADERBOARD` reward that omits it defaults to `3`.
    """

    order: int
    """The display order of the reward."""

    referral_coupon_code: Annotated[Optional[str], PropertyInfo(alias="referralCouponCode")]
    """A legacy static coupon code shown to the referred friend in the reward-won email and webhook (double-sided rewards).

    Same caveats as `couponCode`: display text only, superseded by a connected billing
    integration's issued coupon when one exists.
    """

    referral_description: Annotated[Optional[str], PropertyInfo(alias="referralDescription")]
    """The reward description shown to the referred friend (double-sided rewards)."""

    referred_reward_upfront: Annotated[bool, PropertyInfo(alias="referredRewardUpfront")]
    """For double-sided rewards, deliver the referred friend's reward upfront as a discount."""

    referred_value: Annotated[RewardTaxValuation, PropertyInfo(alias="referredValue")]
    """Tax valuation for the referred friend's side of a double-sided reward.

    Defaults to not tax-reportable (a purchase rebate).
    """

    title: str
    """The reward title (internal label)."""

    value: RewardTaxValuation
    """Tax valuation for the reward (the referrer's side of a double-sided reward).

    Used by tax documentation / 1099 reporting.
    """
