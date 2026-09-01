# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .analytics_availability import AnalyticsAvailability
from .analytics_unavailable_reason import AnalyticsUnavailableReason

__all__ = [
    "CampaignActivationAnalyticsResponse",
    "ActivationStage",
    "ActivationStageCounts",
    "ActivationStalledSegment",
    "ActivationOutcomeCount",
    "ActivationOutcomes",
    "ActivationLargestDrop",
    "ActivationCohortBounds",
    "CampaignActivationCohortResult",
]


class ActivationStage(BaseModel):
    key: Literal["ELIGIBLE", "PORTAL_VIEWED", "SHARE_ACTION", "UNIQUE_REFERRAL_VISIT", "LEAD", "CREDITED_REFERRAL"]

    count: int

    conversion_rate_from_prior: Optional[float] = FieldInfo(alias="conversionRateFromPrior")

    conversion_rate_from_eligible: Optional[float] = FieldInfo(alias="conversionRateFromEligible")

    drop_off_count: Optional[int] = FieldInfo(alias="dropOffCount")

    drop_off_rate: Optional[float] = FieldInfo(alias="dropOffRate")

    median_time_to_stage_ms: Optional[float] = FieldInfo(alias="medianTimeToStageMs")

    stalled_segment_key: Optional[
        Literal[
            "ELIGIBLE_NO_PORTAL_VIEW",
            "PORTAL_VIEWED_NO_SHARE_ACTION",
            "SHARED_NO_UNIQUE_REFERRAL_VISIT",
            "UNIQUE_VISIT_NO_LEAD",
            "LEAD_NO_CREDITED_REFERRAL",
        ]
    ] = FieldInfo(alias="stalledSegmentKey")


class ActivationStageCounts(BaseModel):
    eligible: int = FieldInfo(alias="ELIGIBLE")

    portal_viewed: int = FieldInfo(alias="PORTAL_VIEWED")

    share_action: int = FieldInfo(alias="SHARE_ACTION")

    unique_referral_visit: int = FieldInfo(alias="UNIQUE_REFERRAL_VISIT")

    lead: int = FieldInfo(alias="LEAD")

    credited_referral: int = FieldInfo(alias="CREDITED_REFERRAL")


class ActivationStalledSegment(BaseModel):
    key: Literal[
        "ELIGIBLE_NO_PORTAL_VIEW",
        "PORTAL_VIEWED_NO_SHARE_ACTION",
        "SHARED_NO_UNIQUE_REFERRAL_VISIT",
        "UNIQUE_VISIT_NO_LEAD",
        "LEAD_NO_CREDITED_REFERRAL",
    ]

    from_stage: Literal["ELIGIBLE", "PORTAL_VIEWED", "SHARE_ACTION", "UNIQUE_REFERRAL_VISIT", "LEAD"] = FieldInfo(
        alias="fromStage"
    )

    to_stage: Literal["PORTAL_VIEWED", "SHARE_ACTION", "UNIQUE_REFERRAL_VISIT", "LEAD", "CREDITED_REFERRAL"] = (
        FieldInfo(alias="toStage")
    )

    count: int


class ActivationOutcomeCount(BaseModel):
    count: int


class ActivationOutcomes(BaseModel):
    first_reward: Optional[ActivationOutcomeCount] = FieldInfo(alias="FIRST_REWARD", default=None)

    first_commission: Optional[ActivationOutcomeCount] = FieldInfo(alias="FIRST_COMMISSION", default=None)

    payout_setup_completed: Optional[ActivationOutcomeCount] = FieldInfo(alias="PAYOUT_SETUP_COMPLETED", default=None)


class ActivationLargestDrop(BaseModel):
    from_stage: str = FieldInfo(alias="fromStage")

    to_stage: str = FieldInfo(alias="toStage")

    count: int

    rate: float

    stalled_segment_key: str = FieldInfo(alias="stalledSegmentKey")

    improvement_area_key: Literal[
        "PORTAL_ACCESS",
        "SHARING_EXPERIENCE",
        "SHARE_EFFECTIVENESS",
        "VISITOR_SIGNUP",
        "ATTRIBUTION_AND_QUALIFICATION",
    ] = FieldInfo(alias="improvementAreaKey")

    improvement_area: str = FieldInfo(alias="improvementArea")


class ActivationCohortBounds(BaseModel):
    from_: int = FieldInfo(alias="from")

    to: int

    effective_from: Optional[int] = FieldInfo(alias="effectiveFrom")

    matured_at: int = FieldInfo(alias="maturedAt")

    as_of: int = FieldInfo(alias="asOf")

    anchor_field: Literal["enrolledAsAdvocateAt", "approvedAsAffiliateAt"] = FieldInfo(alias="anchorField")


class CampaignActivationCohortResult(BaseModel):
    state: AnalyticsAvailability

    reason: Optional[AnalyticsUnavailableReason]

    cohort: ActivationCohortBounds

    strict_stages: Optional[List[ActivationStage]] = FieldInfo(alias="strictStages")

    raw_stage_counts: Optional[ActivationStageCounts] = FieldInfo(alias="rawStageCounts")

    stalled_segments: Optional[List[ActivationStalledSegment]] = FieldInfo(alias="stalledSegments")

    outcomes: Optional[ActivationOutcomes]

    largest_drop: Optional[ActivationLargestDrop] = FieldInfo(alias="largestDrop")


class CampaignActivationAnalyticsResponse(BaseModel):
    """Activation cohorts for eligible participants in a referral or affiliate program."""

    coverage_start_at: Optional[int] = FieldInfo(alias="coverageStartAt")

    metric_contract_version: int = FieldInfo(alias="metricContractVersion")

    program_type: Literal["REFERRAL", "AFFILIATE"] = FieldInfo(alias="programType")

    timezone: str

    cohort_interval: Literal["day", "week", "month"] = FieldInfo(alias="cohortInterval")

    observation_window_days: Literal[7, 30] = FieldInfo(alias="observationWindowDays")

    portal_viewed_label: Literal["Referral portal viewed", "Affiliate portal viewed"] = FieldInfo(
        alias="portalViewedLabel"
    )

    portal_viewed_helper_text: str = FieldInfo(alias="portalViewedHelperText")

    aggregate: CampaignActivationCohortResult

    cohorts: List[CampaignActivationCohortResult]
