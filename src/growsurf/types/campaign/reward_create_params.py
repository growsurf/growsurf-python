# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
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

    description: str
    """The reward description shown to the referrer."""

    image_url: Annotated[Optional[str], PropertyInfo(alias="imageUrl")]
    """An image URL for the reward."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether the reward is active (awardable)."""

    is_unlimited: Annotated[bool, PropertyInfo(alias="isUnlimited")]
    """Whether the reward can be earned an unlimited number of times."""

    is_visible: Annotated[bool, PropertyInfo(alias="isVisible")]
    """Whether the reward is visible."""

    limit: int
    """The number of times a participant can earn the reward (overridden by `isUnlimited`)."""

    limit_duration: Annotated[Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"], PropertyInfo(alias="limitDuration")]
    """The window over which `limit` applies."""

    metadata: Dict[str, object]
    """Custom key/value metadata (single-level; values are stored as strings)."""

    next_milestone_prefix: Annotated[Optional[str], PropertyInfo(alias="nextMilestonePrefix")]

    next_milestone_suffix: Annotated[Optional[str], PropertyInfo(alias="nextMilestoneSuffix")]

    number_of_winners: Annotated[int, PropertyInfo(alias="numberOfWinners")]
    """The maximum number of winners (LEADERBOARD rewards)."""

    order: int
    """The display order of the reward."""

    referral_coupon_code: Annotated[Optional[str], PropertyInfo(alias="referralCouponCode")]

    referral_description: Annotated[Optional[str], PropertyInfo(alias="referralDescription")]
    """The reward description shown to the referred friend (double-sided rewards)."""

    referred_reward_upfront: Annotated[bool, PropertyInfo(alias="referredRewardUpfront")]
    """For double-sided rewards, deliver the referred friend's reward upfront as a discount."""

    title: str
    """The reward title (internal label)."""
