from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from growsurf import Growsurf
from growsurf.types import (
    CampaignEngagementAnalytics,
    CampaignActivationAnalyticsResponse,
    CampaignRetrieveActivationAnalyticsParams,
)
from growsurf._compat import get_model_fields
from growsurf.types.campaign import ParticipantAnalyticsResponse, ParticipantActivationAnalytics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def test_analytics_models_preserve_covered_and_unavailable_values() -> None:
    unavailable_metric = {
        "state": "UNAVAILABLE",
        "value": None,
        "reason": "COVERAGE_UNAVAILABLE",
    }
    engagement = CampaignEngagementAnalytics(
        **cast(
            Any,
            {
                "coverageStartAt": None,
                "metricContractVersion": 1,
                "programType": "REFERRAL",
                "timezone": "UTC",
                "interval": "day",
                "platform": {"requested": "ALL", "applied": "ALL", "state": "UNAVAILABLE"},
                "period": {
                    "from": 1754006400000,
                    "to": 1756684800000,
                    "effectiveFrom": None,
                    "previousFrom": 1751328000000,
                    "previousTo": 1754006400000,
                },
                "state": "UNAVAILABLE",
                "reason": "COVERAGE_UNAVAILABLE",
                "totals": {
                    "activeParticipants": unavailable_metric,
                    "sharingParticipants": unavailable_metric,
                    "sharingRate": unavailable_metric,
                    "repeatActiveParticipants": unavailable_metric,
                    "repeatSharingParticipants": unavailable_metric,
                    "retainedActiveParticipants": unavailable_metric,
                    "portalViews": unavailable_metric,
                    "shareActions": unavailable_metric,
                },
                "previousPeriod": {"state": "UNAVAILABLE", "reason": "COVERAGE_UNAVAILABLE", "totals": None},
                "comparison": {"state": "UNAVAILABLE", "reason": "COVERAGE_UNAVAILABLE", "metrics": None},
                "series": [],
                "breakdowns": {
                    "platforms": [],
                    "portalViewSources": [],
                    "shareChannels": [],
                    "firstShareChannels": [],
                },
            },
        )
    )
    campaign_activation = CampaignActivationAnalyticsResponse(
        **cast(
            Any,
            {
                "coverageStartAt": None,
                "metricContractVersion": 1,
                "programType": "AFFILIATE",
                "timezone": "UTC",
                "cohortInterval": "week",
                "observationWindowDays": 30,
                "portalViewedLabel": "Affiliate portal viewed",
                "portalViewedHelperText": "The affiliate viewed the affiliate portal.",
                "aggregate": {
                    "state": "UNAVAILABLE",
                    "reason": "COVERAGE_UNAVAILABLE",
                    "cohort": {
                        "from": 1754006400000,
                        "to": 1756684800000,
                        "effectiveFrom": None,
                        "maturedAt": 1759276800000,
                        "asOf": 1756684800000,
                        "anchorField": "approvedAsAffiliateAt",
                    },
                    "strictStages": None,
                    "rawStageCounts": None,
                    "stalledSegments": None,
                    "outcomes": None,
                    "largestDrop": None,
                },
                "cohorts": [],
            },
        )
    )
    participant_activation = ParticipantActivationAnalytics(
        **cast(
            Any,
            {
                "coverageStartAt": 1754006400000,
                "metricContractVersion": 1,
                "programType": "AFFILIATE",
                "state": "AVAILABLE",
                "reason": None,
                "cohort": {"anchorField": "approvedAsAffiliateAt", "anchorAt": 1754006400000},
                "enrolledAsAdvocateAt": None,
                "milestones": {
                    "firstPortalViewedAt": 1754092800000,
                    "firstReferralLinkCopiedAt": 1754096400000,
                    "firstShareAt": 1754100000000,
                    "firstShareChannel": "linkedin",
                    "firstUniqueClickAt": 1754186400000,
                    "firstLeadAt": 1754272800000,
                    "firstReferralAt": 1754359200000,
                    "firstRewardAt": None,
                    "firstCommissionAt": 1754445600000,
                    "payoutSetupCompletedAt": None,
                },
            },
        )
    )
    participant_response = ParticipantAnalyticsResponse(
        **cast(
            Any,
            {
                "analytics": {},
                "ranks": {},
                "shareCount": {},
                "activation": participant_activation,
                "series": [{"periodStart": 1754006400000, "portalViews": None, "shareActions": 2}],
            },
        )
    )
    activation_params: CampaignRetrieveActivationAnalyticsParams = {
        "cohort_from": 1754006400000,
        "cohort_to": 1756684800000,
        "cohort_interval": "week",
        "observation_window_days": 30,
        "timezone": "UTC",
    }

    assert engagement.totals.portal_views.value is None
    assert campaign_activation.aggregate.strict_stages is None
    assert participant_response.activation is not None
    assert participant_response.activation.milestones.first_share_channel == "linkedin"
    assert participant_response.series is not None
    assert participant_response.series[0].portal_views is None
    assert activation_params["observation_window_days"] == 30
    milestone_fields = get_model_fields(type(participant_activation.milestones))
    assert "portal_opened_at" not in milestone_fields
    assert "first_window_opened_at" not in milestone_fields


@pytest.mark.respx(base_url=base_url)
def test_analytics_request_paths_and_query_names_remain_compatible(client: Growsurf, respx_mock: MockRouter) -> None:
    analytics_requests: list[httpx.Request] = []
    activation_requests: list[httpx.Request] = []
    participant_requests: list[httpx.Request] = []

    def analytics_handler(request: httpx.Request) -> httpx.Response:
        analytics_requests.append(request)
        return httpx.Response(200, json={"analytics": {}, "startDate": 1, "endDate": 2})

    def activation_handler(request: httpx.Request) -> httpx.Response:
        activation_requests.append(request)
        return httpx.Response(
            200,
            json={
                "coverageStartAt": None,
                "metricContractVersion": 1,
                "programType": "REFERRAL",
                "timezone": "UTC",
                "cohortInterval": "day",
                "observationWindowDays": 30,
                "portalViewedLabel": "Referral portal viewed",
                "portalViewedHelperText": "The participant viewed the referral portal.",
                "aggregate": {
                    "state": "UNAVAILABLE",
                    "reason": "COVERAGE_UNAVAILABLE",
                    "cohort": {
                        "from": 1,
                        "to": 2,
                        "effectiveFrom": None,
                        "maturedAt": 3,
                        "asOf": 2,
                        "anchorField": "enrolledAsAdvocateAt",
                    },
                    "strictStages": None,
                    "rawStageCounts": None,
                    "stalledSegments": None,
                    "outcomes": None,
                    "largestDrop": None,
                },
                "cohorts": [],
            },
        )

    def participant_handler(request: httpx.Request) -> httpx.Response:
        participant_requests.append(request)
        return httpx.Response(200, json={"analytics": {}, "ranks": {}, "shareCount": {}})

    respx_mock.get("/campaign/campaign_123/analytics").mock(side_effect=analytics_handler)
    respx_mock.get("/campaign/campaign_123/analytics/activation").mock(side_effect=activation_handler)
    respx_mock.get("/campaign/campaign_123/participant/participant_123/analytics").mock(side_effect=participant_handler)

    client.campaign.retrieve_analytics(id="campaign_123")
    client.campaign.retrieve_analytics(
        id="campaign_123",
        include="engagement",
        timezone="America/Los_Angeles",
        platform="WEB",
    )
    client.campaign.retrieve_activation_analytics(
        id="campaign_123",
        cohort_from=1754006400000,
        cohort_to=1756684800000,
        cohort_interval="week",
        observation_window_days=30,
        timezone="America/Los_Angeles",
    )
    client.campaign.participant.retrieve_analytics(
        participant_id_or_email="participant_123",
        id="campaign_123",
        include="activation,series",
    )

    assert len(analytics_requests) == 2
    assert dict(analytics_requests[0].url.params) == {}
    assert dict(analytics_requests[1].url.params) == {
        "include": "engagement",
        "timezone": "America/Los_Angeles",
        "platform": "WEB",
    }
    assert dict(activation_requests[0].url.params) == {
        "cohortFrom": "1754006400000",
        "cohortTo": "1756684800000",
        "cohortInterval": "week",
        "observationWindowDays": "30",
        "timezone": "America/Los_Angeles",
    }
    assert dict(participant_requests[0].url.params) == {"include": "activation,series"}
