# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..analytics_availability import AnalyticsAvailability
from ..analytics_unavailable_reason import AnalyticsUnavailableReason

__all__ = ["ParticipantActivationAnalytics", "ParticipantActivationCohort", "ParticipantActivationMilestones"]


class ParticipantActivationCohort(BaseModel):
    anchor_field: Literal["enrolledAsAdvocateAt", "approvedAsAffiliateAt"] = FieldInfo(alias="anchorField")

    anchor_at: Optional[int] = FieldInfo(alias="anchorAt")


class ParticipantActivationMilestones(BaseModel):
    first_portal_viewed_at: Optional[int] = FieldInfo(alias="firstPortalViewedAt")

    first_referral_link_copied_at: Optional[int] = FieldInfo(alias="firstReferralLinkCopiedAt")

    first_share_at: Optional[int] = FieldInfo(alias="firstShareAt")

    first_share_channel: Optional[
        Literal[
            "email",
            "facebook",
            "twitter",
            "linkedin",
            "pinterest",
            "threads",
            "bluesky",
            "sms",
            "messenger",
            "whatsapp",
            "wechat",
            "telegram",
            "reddit",
            "tumblr",
            "qrcode",
            "copyRefLink",
            "iosNativeShare",
            "androidNativeShare",
        ]
    ] = FieldInfo(alias="firstShareChannel")

    first_unique_click_at: Optional[int] = FieldInfo(alias="firstUniqueClickAt")

    first_lead_at: Optional[int] = FieldInfo(alias="firstLeadAt")

    first_referral_at: Optional[int] = FieldInfo(alias="firstReferralAt")

    first_reward_at: Optional[int] = FieldInfo(alias="firstRewardAt")

    first_commission_at: Optional[int] = FieldInfo(alias="firstCommissionAt")

    payout_setup_completed_at: Optional[int] = FieldInfo(alias="payoutSetupCompletedAt")


class ParticipantActivationAnalytics(BaseModel):
    """Covered first milestones for one participant.

    Unknown history remains `null` and is paired with an explicit state and reason.
    """

    coverage_start_at: Optional[int] = FieldInfo(alias="coverageStartAt")

    metric_contract_version: int = FieldInfo(alias="metricContractVersion")

    program_type: Literal["REFERRAL", "AFFILIATE"] = FieldInfo(alias="programType")

    state: AnalyticsAvailability

    reason: Optional[AnalyticsUnavailableReason]

    cohort: ParticipantActivationCohort

    enrolled_as_advocate_at: Optional[int] = FieldInfo(alias="enrolledAsAdvocateAt")

    milestones: ParticipantActivationMilestones
