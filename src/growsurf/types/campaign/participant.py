# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .referral_source import ReferralSource
from .referral_status import ReferralStatus
from .fraud_risk_level import FraudRiskLevel
from .participant_reward import ParticipantReward

__all__ = ["Participant", "Referrer"]


class Referrer(BaseModel):
    id: Optional[str] = None

    created_at: Optional[int] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    fingerprint: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    fraud_reason_code: Optional[str] = FieldInfo(alias="fraudReasonCode", default=None)

    fraud_risk_level: Optional[FraudRiskLevel] = FieldInfo(alias="fraudRiskLevel", default=None)

    impression_count: Optional[int] = FieldInfo(alias="impressionCount", default=None)

    invite_count: Optional[int] = FieldInfo(alias="inviteCount", default=None)

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Shallow custom metadata object."""

    monthly_rank: Optional[int] = FieldInfo(alias="monthlyRank", default=None)

    monthly_referral_count: Optional[int] = FieldInfo(alias="monthlyReferralCount", default=None)

    monthly_referrals: Optional[List[str]] = FieldInfo(alias="monthlyReferrals", default=None)

    prev_monthly_rank: Optional[int] = FieldInfo(alias="prevMonthlyRank", default=None)

    prev_monthly_referral_count: Optional[int] = FieldInfo(alias="prevMonthlyReferralCount", default=None)

    rank: Optional[int] = None

    referral_count: Optional[int] = FieldInfo(alias="referralCount", default=None)

    referrals: Optional[List[str]] = None

    referral_source: Optional[ReferralSource] = FieldInfo(alias="referralSource", default=None)

    referral_status: Optional[ReferralStatus] = FieldInfo(alias="referralStatus", default=None)

    share_count: Optional[Dict[str, int]] = FieldInfo(alias="shareCount", default=None)

    share_url: Optional[str] = FieldInfo(alias="shareUrl", default=None)

    unique_impression_count: Optional[int] = FieldInfo(alias="uniqueImpressionCount", default=None)

    unsubscribed: Optional[bool] = None


class Participant(BaseModel):
    id: str

    email: str

    monthly_rank: int = FieldInfo(alias="monthlyRank")

    monthly_referral_count: int = FieldInfo(alias="monthlyReferralCount")

    rank: int

    referral_count: int = FieldInfo(alias="referralCount")

    rewards: List[ParticipantReward]

    share_url: str = FieldInfo(alias="shareUrl")

    all_matching_fraudsters: Optional[List[Dict[str, object]]] = FieldInfo(alias="allMatchingFraudsters", default=None)

    created_at: Optional[int] = FieldInfo(alias="createdAt", default=None)

    fingerprint: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    fraud_reason_code: Optional[str] = FieldInfo(alias="fraudReasonCode", default=None)

    fraud_risk_level: Optional[FraudRiskLevel] = FieldInfo(alias="fraudRiskLevel", default=None)

    impression_count: Optional[int] = FieldInfo(alias="impressionCount", default=None)

    invite_count: Optional[int] = FieldInfo(alias="inviteCount", default=None)

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)

    is_new: Optional[bool] = FieldInfo(alias="isNew", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Shallow custom metadata object."""

    mobile_instance_id: Optional[str] = FieldInfo(alias="mobileInstanceId", default=None)
    """
    App-install scoped mobile identifier used for anti-fraud matching when provided
    by native mobile apps. The official mobile SDKs generate this as a lowercase
    UUID. Not stored when strict GDPR/CCPA mode is enabled.
    """

    monthly_referrals: Optional[List[str]] = FieldInfo(alias="monthlyReferrals", default=None)

    notes: Optional[str] = None

    paypal_email_address: Optional[str] = FieldInfo(alias="paypalEmailAddress", default=None)

    prev_monthly_rank: Optional[int] = FieldInfo(alias="prevMonthlyRank", default=None)

    prev_monthly_referral_count: Optional[int] = FieldInfo(alias="prevMonthlyReferralCount", default=None)

    referrals: Optional[List[str]] = None

    referral_source: Optional[ReferralSource] = FieldInfo(alias="referralSource", default=None)

    referral_status: Optional[ReferralStatus] = FieldInfo(alias="referralStatus", default=None)

    referred_by: Optional[str] = FieldInfo(alias="referredBy", default=None)

    referrer: Optional[Referrer] = None

    share_count: Optional[Dict[str, int]] = FieldInfo(alias="shareCount", default=None)

    unique_impression_count: Optional[int] = FieldInfo(alias="uniqueImpressionCount", default=None)

    unread_commissions_count: Optional[int] = FieldInfo(alias="unreadCommissionsCount", default=None)

    unread_payouts_count: Optional[int] = FieldInfo(alias="unreadPayoutsCount", default=None)

    unsubscribed: Optional[bool] = None

    vanity_keys: Optional[List[str]] = FieldInfo(alias="vanityKeys", default=None)
