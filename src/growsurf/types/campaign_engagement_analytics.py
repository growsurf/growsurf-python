# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .analytics_availability import AnalyticsAvailability
from .analytics_unavailable_reason import AnalyticsUnavailableReason

__all__ = [
    "CampaignEngagementAnalytics",
    "ParticipantEngagementMetric",
    "ParticipantEngagementTotals",
    "ParticipantEngagementPeriod",
    "ParticipantEngagementPlatformFilter",
    "ParticipantEngagementPreviousPeriod",
    "ParticipantEngagementComparisonMetrics",
    "ParticipantEngagementComparison",
    "ParticipantEngagementSeriesPoint",
    "ParticipantEngagementPlatformBreakdown",
    "ParticipantEngagementPortalSourceBreakdown",
    "ParticipantEngagementShareChannelBreakdown",
    "ParticipantEngagementFirstShareChannelBreakdown",
    "ParticipantEngagementBreakdowns",
]


class ParticipantEngagementMetric(BaseModel):
    state: AnalyticsAvailability

    value: Optional[float]

    reason: Optional[AnalyticsUnavailableReason]

    delta: Optional[float] = None


class ParticipantEngagementTotals(BaseModel):
    active_participants: ParticipantEngagementMetric = FieldInfo(alias="activeParticipants")

    sharing_participants: ParticipantEngagementMetric = FieldInfo(alias="sharingParticipants")

    sharing_rate: ParticipantEngagementMetric = FieldInfo(alias="sharingRate")

    repeat_active_participants: ParticipantEngagementMetric = FieldInfo(alias="repeatActiveParticipants")

    repeat_sharing_participants: ParticipantEngagementMetric = FieldInfo(alias="repeatSharingParticipants")

    retained_active_participants: ParticipantEngagementMetric = FieldInfo(alias="retainedActiveParticipants")

    portal_views: ParticipantEngagementMetric = FieldInfo(alias="portalViews")

    share_actions: ParticipantEngagementMetric = FieldInfo(alias="shareActions")


class ParticipantEngagementPeriod(BaseModel):
    from_: int = FieldInfo(alias="from")

    to: int

    effective_from: Optional[int] = FieldInfo(alias="effectiveFrom")

    previous_from: int = FieldInfo(alias="previousFrom")

    previous_to: int = FieldInfo(alias="previousTo")


class ParticipantEngagementPlatformFilter(BaseModel):
    requested: Literal["ALL", "WEB", "IOS", "ANDROID"]

    applied: Literal["ALL", "WEB", "IOS", "ANDROID"]

    state: AnalyticsAvailability


class ParticipantEngagementPreviousPeriod(BaseModel):
    state: AnalyticsAvailability

    reason: Optional[AnalyticsUnavailableReason]

    totals: Optional[ParticipantEngagementTotals]


class ParticipantEngagementComparisonMetrics(BaseModel):
    active_participants: Optional[ParticipantEngagementMetric] = FieldInfo(alias="activeParticipants", default=None)

    sharing_participants: Optional[ParticipantEngagementMetric] = FieldInfo(alias="sharingParticipants", default=None)

    repeat_active_participants: Optional[ParticipantEngagementMetric] = FieldInfo(
        alias="repeatActiveParticipants", default=None
    )

    repeat_sharing_participants: Optional[ParticipantEngagementMetric] = FieldInfo(
        alias="repeatSharingParticipants", default=None
    )

    portal_views: Optional[ParticipantEngagementMetric] = FieldInfo(alias="portalViews", default=None)

    share_actions: Optional[ParticipantEngagementMetric] = FieldInfo(alias="shareActions", default=None)


class ParticipantEngagementComparison(BaseModel):
    state: AnalyticsAvailability

    reason: Optional[AnalyticsUnavailableReason]

    metrics: Optional[ParticipantEngagementComparisonMetrics]


class ParticipantEngagementSeriesPoint(BaseModel):
    from_: int = FieldInfo(alias="from")

    to: int

    active_participants: int = FieldInfo(alias="activeParticipants")

    sharing_participants: int = FieldInfo(alias="sharingParticipants")

    portal_views: int = FieldInfo(alias="portalViews")

    share_actions: int = FieldInfo(alias="shareActions")


class ParticipantEngagementPlatformBreakdown(BaseModel):
    key: Literal["WEB", "IOS", "ANDROID"]

    active_participants: int = FieldInfo(alias="activeParticipants")

    sharing_participants: int = FieldInfo(alias="sharingParticipants")

    portal_views: int = FieldInfo(alias="portalViews")

    share_actions: int = FieldInfo(alias="shareActions")


class ParticipantEngagementPortalSourceBreakdown(BaseModel):
    key: Literal[
        "DEFAULT_LAUNCHER", "SDK_OPEN", "CSS_CLASS", "EMBEDDABLE_ELEMENT", "HOSTED_PORTAL", "NATIVE_WINDOW", "UNKNOWN"
    ]

    active_participants: int = FieldInfo(alias="activeParticipants")

    portal_views: int = FieldInfo(alias="portalViews")


class ParticipantEngagementShareChannelBreakdown(BaseModel):
    key: str

    sharing_participants: int = FieldInfo(alias="sharingParticipants")

    share_actions: int = FieldInfo(alias="shareActions")


class ParticipantEngagementFirstShareChannelBreakdown(BaseModel):
    key: str

    sharing_participants: int = FieldInfo(alias="sharingParticipants")


class ParticipantEngagementBreakdowns(BaseModel):
    platforms: List[ParticipantEngagementPlatformBreakdown]

    portal_view_sources: List[ParticipantEngagementPortalSourceBreakdown] = FieldInfo(alias="portalViewSources")

    share_channels: List[ParticipantEngagementShareChannelBreakdown] = FieldInfo(alias="shareChannels")

    first_share_channels: List[ParticipantEngagementFirstShareChannelBreakdown] = FieldInfo(alias="firstShareChannels")


class CampaignEngagementAnalytics(BaseModel):
    """Current participant engagement for the selected program, period, and platform."""

    coverage_start_at: Optional[int] = FieldInfo(alias="coverageStartAt")

    metric_contract_version: int = FieldInfo(alias="metricContractVersion")

    program_type: Literal["REFERRAL", "AFFILIATE"] = FieldInfo(alias="programType")

    timezone: str

    interval: Literal["day", "week", "month"]

    platform: ParticipantEngagementPlatformFilter

    period: ParticipantEngagementPeriod

    state: AnalyticsAvailability

    reason: Optional[AnalyticsUnavailableReason]

    totals: ParticipantEngagementTotals

    previous_period: ParticipantEngagementPreviousPeriod = FieldInfo(alias="previousPeriod")

    comparison: ParticipantEngagementComparison

    series: List[ParticipantEngagementSeriesPoint]

    breakdowns: ParticipantEngagementBreakdowns
