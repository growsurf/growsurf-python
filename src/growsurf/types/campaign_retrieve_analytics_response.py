# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CampaignRetrieveAnalyticsResponse",
    "Analytics",
    "Series",
    "PreviousPeriod",
    "StatusCounts",
    "StatusCountsRewardStatus",
    "StatusCountsCommissionStatus",
    "StatusCountsCommissionStatusMetric",
    "StatusCountsPayoutStatus",
    "StatusCountsPayoutStatusMetric",
    "Rates",
]


class Analytics(BaseModel):
    android_native_shares: Optional[int] = FieldInfo(alias="androidNativeShares", default=None)

    bluesky_shares: Optional[int] = FieldInfo(alias="blueskyShares", default=None)

    copy_ref_link_shares: Optional[int] = FieldInfo(alias="copyRefLinkShares", default=None)

    email_shares: Optional[int] = FieldInfo(alias="emailShares", default=None)

    facebook_shares: Optional[int] = FieldInfo(alias="facebookShares", default=None)

    impressions: Optional[int] = None

    invites: Optional[int] = None

    ios_native_shares: Optional[int] = FieldInfo(alias="iosNativeShares", default=None)

    linked_in_shares: Optional[int] = FieldInfo(alias="linkedInShares", default=None)

    messenger_shares: Optional[int] = FieldInfo(alias="messengerShares", default=None)

    participants: Optional[int] = None

    pinterest_shares: Optional[int] = FieldInfo(alias="pinterestShares", default=None)

    qrcode_shares: Optional[int] = FieldInfo(alias="qrcodeShares", default=None)

    reddit_shares: Optional[int] = FieldInfo(alias="redditShares", default=None)

    referral_credit_expireds: Optional[int] = FieldInfo(alias="referralCreditExpireds", default=None)

    referral_credit_pendings: Optional[int] = FieldInfo(alias="referralCreditPendings", default=None)

    referrals: Optional[int] = None

    sms_shares: Optional[int] = FieldInfo(alias="smsShares", default=None)

    telegram_shares: Optional[int] = FieldInfo(alias="telegramShares", default=None)

    threads_shares: Optional[int] = FieldInfo(alias="threadsShares", default=None)

    total_commission_count: Optional[int] = FieldInfo(alias="totalCommissionCount", default=None)
    """Affiliate programs only. Number of commission records."""

    total_commissions: Optional[int] = FieldInfo(alias="totalCommissions", default=None)
    """Affiliate programs only.

    Commissions in the smallest unit of the program currency.
    """

    total_revenue: Optional[int] = FieldInfo(alias="totalRevenue", default=None)
    """Affiliate programs only. Revenue in the smallest unit of the program currency."""

    tumblr_shares: Optional[int] = FieldInfo(alias="tumblrShares", default=None)

    twitter_shares: Optional[int] = FieldInfo(alias="twitterShares", default=None)

    unique_impressions: Optional[int] = FieldInfo(alias="uniqueImpressions", default=None)

    wechat_shares: Optional[int] = FieldInfo(alias="wechatShares", default=None)

    whats_app_shares: Optional[int] = FieldInfo(alias="whatsAppShares", default=None)


class Series(Analytics):
    period_start: Optional[int] = FieldInfo(alias="periodStart", default=None)
    """Start of the period, as a Unix timestamp in milliseconds (UTC)."""


class PreviousPeriod(BaseModel):
    """Totals for the equal-length window immediately preceding the requested one."""

    analytics: Optional[Analytics] = None

    end_date: Optional[int] = FieldInfo(alias="endDate", default=None)

    start_date: Optional[int] = FieldInfo(alias="startDate", default=None)


class StatusCountsRewardStatus(BaseModel):
    approved: Optional[int] = None

    pending: Optional[int] = None
    """Unapproved rewards awaiting fulfillment."""


class StatusCountsCommissionStatusMetric(BaseModel):
    count: Optional[int] = None

    total_amount: Optional[int] = FieldInfo(alias="totalAmount", default=None)
    """Total commission amount in minor currency units."""

    total_revenue: Optional[int] = FieldInfo(alias="totalRevenue", default=None)
    """Total attributed revenue in minor currency units."""


class StatusCountsCommissionStatus(BaseModel):
    """Affiliate only. Commission counts and amounts by status."""

    approved: Optional[StatusCountsCommissionStatusMetric] = None

    paid: Optional[StatusCountsCommissionStatusMetric] = None

    pending: Optional[StatusCountsCommissionStatusMetric] = None

    reversed: Optional[StatusCountsCommissionStatusMetric] = None


class StatusCountsPayoutStatusMetric(BaseModel):
    count: Optional[int] = None

    total_amount: Optional[int] = FieldInfo(alias="totalAmount", default=None)
    """Total payout amount in minor currency units."""


class StatusCountsPayoutStatus(BaseModel):
    """Affiliate only. Payout counts and amounts by status."""

    failed: Optional[StatusCountsPayoutStatusMetric] = None

    issued: Optional[StatusCountsPayoutStatusMetric] = None

    queued: Optional[StatusCountsPayoutStatusMetric] = None

    upcoming: Optional[StatusCountsPayoutStatusMetric] = None


class StatusCounts(BaseModel):
    """Status-count breakdowns.

    `rewardStatus` is present for every program; `affiliateStatus`,
    `commissionStatus`, and `payoutStatus` are present only for affiliate programs.
    Money amounts are in minor units of `currencyISO`.
    """

    affiliate_status: Optional[Dict[str, int]] = FieldInfo(alias="affiliateStatus", default=None)
    """Affiliate only. Participant counts keyed by affiliate status."""

    commission_status: Optional[StatusCountsCommissionStatus] = FieldInfo(alias="commissionStatus", default=None)
    """Affiliate only. Commission counts and amounts by status."""

    currency_iso: Optional[str] = FieldInfo(alias="currencyISO", default=None)

    payout_status: Optional[StatusCountsPayoutStatus] = FieldInfo(alias="payoutStatus", default=None)
    """Affiliate only. Payout counts and amounts by status."""

    reward_status: Optional[StatusCountsRewardStatus] = FieldInfo(alias="rewardStatus", default=None)


class Rates(BaseModel):
    """Derived referral rates, each a ratio in the range 0-1 (0 when its denominator is 0)."""

    participation_rate: Optional[float] = FieldInfo(alias="participationRate", default=None)
    """`participants` divided by `uniqueImpressions`."""

    referral_conversion_rate: Optional[float] = FieldInfo(alias="referralConversionRate", default=None)
    """`referrals` divided by `uniqueImpressions`."""

    shares_per_participant: Optional[float] = FieldInfo(alias="sharesPerParticipant", default=None)
    """Total shares across all channels divided by `participants`."""


class CampaignRetrieveAnalyticsResponse(BaseModel):
    analytics: Analytics

    end_date: int = FieldInfo(alias="endDate")

    start_date: int = FieldInfo(alias="startDate")

    previous_period: Optional[PreviousPeriod] = FieldInfo(alias="previousPeriod", default=None)
    """Present only when `include` contains `previousPeriod`."""

    rates: Optional[Rates] = None
    """Present only when `include` contains `rates`."""

    series: Optional[List[Series]] = None
    """Present only when `interval` is `day`, `week`, or `month`.

    Per-period totals, ascending.
    """

    status_counts: Optional[StatusCounts] = FieldInfo(alias="statusCounts", default=None)
    """Present only when `include` contains `statusCounts`."""
