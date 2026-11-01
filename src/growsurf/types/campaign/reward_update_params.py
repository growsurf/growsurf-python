# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .reward_tax_valuation import RewardTaxValuation
from ..commission_structure import CommissionStructure

__all__ = ["RewardUpdateParams"]


class RewardUpdateParams(TypedDict, total=False):
    id: Required[str]

    commission_structure: Annotated[CommissionStructure, PropertyInfo(alias="commissionStructure")]
    """The affiliate commission structure (AFFILIATE rewards only)."""

    conversions_required: Annotated[int, PropertyInfo(alias="conversionsRequired")]
    """The number of referrals required to earn the reward."""

    coupon_code: Annotated[Optional[str], PropertyInfo(alias="couponCode")]
    """A legacy static coupon code shown to the referrer in the reward-won email and webhook.

    Display text only (GrowSurf does not create or validate it); superseded by a
    connected billing integration's issued coupon when one exists.
    Up to 100 characters.
    """

    description: str
    """The reward description shown to the referrer. Up to 255 characters."""

    event: Literal["LEAD", "CONVERSION"]
    """The event that earns this Campaign Reward.

    `SINGLE_SIDED`, `DOUBLE_SIDED`, and `MILESTONE` rewards support `LEAD` or
    `CONVERSION`. `LEAD` requires `installation.referralTrigger` to be `CUSTOM`.
    When omitted, the Campaign Reward's current event is preserved.
    """

    image_url: Annotated[Optional[str], PropertyInfo(alias="imageUrl")]
    """An image URL for the reward."""

    image_icon_key: Annotated[
        Optional[
            Literal[
                "GIFT_1",
                "GIFT_2",
                "GIFT_3",
                "GIFT_4",
                "GIFT_5",
                "GIFT_6",
                "GIFT_CARD",
                "CASH",
                "COIN",
                "CARD",
                "STAR_1",
                "STAR_2",
                "STAR_3",
                "TROPHY",
                "CROWN",
                "SEAL",
                "HEART_1",
                "HEART_2",
                "TAG",
                "DIAMOND",
                "CONFETTI",
                "ROCKET",
            ]
        ],
        PropertyInfo(alias="imageIconKey"),
    ]
    """The starter icon shown for the reward, or `null` when `imageUrl` is your own image.

    Participant pages draw this icon in your program's accent color. Also set
    `imageUrl` to the icon's image so the iOS and Android SDKs can show it. Sending
    `imageUrl` without `imageIconKey` clears it.
    """

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
    """Custom key/value metadata (single-level; values keep the type you send).

    Each value must be a string, number, or boolean of up to 500 characters. Each key
    must have 1 to 40 characters once camelCased, and two keys that camelCase to the
    same key are rejected. Up to 50 keys. An entry that breaks these rules returns
    `400`.

    For `DOUBLE_SIDED` rewards in referral programs, `rewardAmount` is the referrer’s amount and
    `referredRewardAmount` is the friend’s amount. If `referredRewardAmount` is absent, the friend
    also uses `rewardAmount`, unless the friend’s `referralDescription` is a percent or free offer,
    which stays amount-free. New or changed positive numeric amounts must use whole units for
    currencies without decimals, such as JPY, and no more than two decimal places for other
    currencies, including USD and KWD. Excess precision is rejected rather than rounded, including
    when you clone a program. Existing unchanged amounts and earned rewards keep their saved values.
    """

    next_milestone_prefix: Annotated[Optional[str], PropertyInfo(alias="nextMilestonePrefix")]
    """Text shown before a participant's referral count in milestone progress copy.

    Applies to `MILESTONE` rewards (e.g. "You are only"). Up to 255 characters.
    """

    next_milestone_suffix: Annotated[Optional[str], PropertyInfo(alias="nextMilestoneSuffix")]
    """Text shown after a participant's referral count in milestone progress copy.

    Applies to `MILESTONE` rewards (e.g. "referrals away from your next reward!"). Up to
    255 characters.
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
    Up to 100 characters.
    """

    referral_description: Annotated[Optional[str], PropertyInfo(alias="referralDescription")]
    """The reward description shown to the referred friend (double-sided rewards).

    Up to 255 characters.
    """

    referred_reward_upfront: Annotated[bool, PropertyInfo(alias="referredRewardUpfront")]
    """For double-sided rewards, deliver the referred friend's reward upfront as a discount."""

    referred_value: Annotated[Optional[RewardTaxValuation], PropertyInfo(alias="referredValue")]
    """Tax treatment override for the referred friend's side of a double-sided reward. Null inherits the program's confirmed default.
    """

    title: str
    """The reward title (internal label). Up to 100 characters."""

    value: Optional[RewardTaxValuation]
    """Tax valuation for the reward (the referrer's side of a double-sided reward).

    Used by tax documentation / 1099 reporting.
    """
