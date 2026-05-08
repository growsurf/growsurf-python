# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CampaignRetrieveAnalyticsResponse", "Analytics"]


class Analytics(BaseModel):
    bluesky_shares: Optional[int] = FieldInfo(alias="blueskyShares", default=None)

    email_shares: Optional[int] = FieldInfo(alias="emailShares", default=None)

    facebook_shares: Optional[int] = FieldInfo(alias="facebookShares", default=None)

    impressions: Optional[int] = None

    invites: Optional[int] = None

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


class CampaignRetrieveAnalyticsResponse(BaseModel):
    analytics: Analytics

    end_date: int = FieldInfo(alias="endDate")

    start_date: int = FieldInfo(alias="startDate")
