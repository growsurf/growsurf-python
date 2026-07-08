# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantAnalyticsResponse", "Analytics", "Ranks", "Series"]


class Analytics(BaseModel):
    currency_iso: Optional[str] = FieldInfo(alias="currencyISO", default=None)

    expired_referrals: Optional[int] = FieldInfo(alias="expiredReferrals", default=None)

    impressions: Optional[int] = None

    invites_sent: Optional[int] = FieldInfo(alias="invitesSent", default=None)

    leads: Optional[int] = None

    monthly_referrals: Optional[int] = FieldInfo(alias="monthlyReferrals", default=None)

    pending_rewards: Optional[int] = FieldInfo(alias="pendingRewards", default=None)

    referral_revenue: Optional[int] = FieldInfo(alias="referralRevenue", default=None)
    """Affiliate only.

    Revenue attributed to this participant's referrals, in minor currency units.
    """

    referrals: Optional[int] = None

    rewards_earned: Optional[int] = FieldInfo(alias="rewardsEarned", default=None)

    total_commissions: Optional[int] = FieldInfo(alias="totalCommissions", default=None)
    """Affiliate only. Total commissions earned, in minor currency units."""

    total_paid_out: Optional[int] = FieldInfo(alias="totalPaidOut", default=None)
    """Affiliate only. Total paid out, in minor currency units."""

    unique_impressions: Optional[int] = FieldInfo(alias="uniqueImpressions", default=None)

    upcoming_payout: Optional[int] = FieldInfo(alias="upcomingPayout", default=None)
    """Affiliate only. Approved commissions ready to pay, in minor currency units."""


class Ranks(BaseModel):
    monthly_rank: Optional[int] = FieldInfo(alias="monthlyRank", default=None)

    prev_monthly_rank: Optional[int] = FieldInfo(alias="prevMonthlyRank", default=None)

    rank: Optional[int] = None
    """All-time rank (1-indexed), or null when unranked."""


class Series(BaseModel):
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

    period_start: Optional[int] = FieldInfo(alias="periodStart", default=None)
    """Start of the period, as a Unix timestamp in milliseconds (UTC)."""

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


class ParticipantAnalyticsResponse(BaseModel):
    analytics: Analytics

    ranks: Ranks

    share_count: Dict[str, int] = FieldInfo(alias="shareCount")
    """Per-channel share counts (e.g. `email`, `facebook`, `twitter`, ...)."""

    end_date: Optional[int] = FieldInfo(alias="endDate", default=None)
    """Present only with `include=series`. Window end (Unix ms)."""

    series: Optional[List[Series]] = None
    """Present only when `include=series`.

    This participant's own referral-link activity per period (ascending), windowed by
    `days`/`startDate`/`endDate` and bucketed by `interval`.
    """

    start_date: Optional[int] = FieldInfo(alias="startDate", default=None)
    """Present only with `include=series`. Window start (Unix ms)."""
