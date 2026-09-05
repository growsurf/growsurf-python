# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import json
from typing import Any, cast

import httpx
import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types import (
    ReferralList,
    AffiliateInvite,
    ParticipantList,
    AffiliateApplication,
    CampaignListResponse,
    ParticipantPayoutList,
    ParticipantCommissionList,
    AffiliateInviteListResponse,
    AffiliateApplicationListResponse,
    CampaignRetrieveAnalyticsResponse,
    CampaignCreateMobileParticipantTokenResponse,
)
from growsurf.types.campaign import Campaign

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

CAMPAIGN_RESPONSE: dict[str, object] = {
    "id": "campaign-id",
    "impressionCount": 0,
    "inviteCount": 0,
    "name": "Pied Piper",
    "participantCount": 0,
    "referralCount": 0,
    "rewards": [],
    "status": "DRAFT",
    "type": "REFERRAL",
    "winnerCount": 0,
}

MOBILE_PARTICIPANT_TOKEN_RESPONSE: dict[str, object] = {
    "expiresIn": 31536000,
    "isNew": True,
    "participantToken": "participant-token",
    "participant": {
        "id": "participant-id",
        "email": "gavin@hooli.com",
        "monthlyRank": 0,
        "monthlyReferralCount": 0,
        "rank": 0,
        "referralCount": 0,
        "rewards": [],
    },
}


class TestCampaign:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_create_sends_goal(self, client: Growsurf, respx_mock: Any) -> None:
        route = respx_mock.post(f"{base_url}/campaigns").mock(return_value=httpx.Response(200, json=CAMPAIGN_RESPONSE))

        client.campaign.create(type="REFERRAL", goal="B2B_SAAS_SELF_SERVICE")

        assert json.loads(route.calls.last.request.content) == {
            "type": "REFERRAL",
            "goal": "B2B_SAAS_SELF_SERVICE",
        }

    def test_mobile_participant_token_sends_affiliate_choice(self, client: Growsurf, respx_mock: Any) -> None:
        route = respx_mock.post(f"{base_url}/campaign/campaign-id/mobile-participant-token").mock(
            return_value=httpx.Response(200, json=MOBILE_PARTICIPANT_TOKEN_RESPONSE)
        )

        client.campaign.create_mobile_participant_token(
            "campaign-id",
            email="gavin@hooli.com",
            is_affiliate=False,
        )

        assert json.loads(route.calls.last.request.content) == {
            "email": "gavin@hooli.com",
            "isAffiliate": False,
        }

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Growsurf) -> None:
        campaign = client.campaign.create(
            type="REFERRAL",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.create(
            type="REFERRAL",
            company_logo_image_url="companyLogoImageUrl",
            company_name="companyName",
            currency_iso="currencyISO",
            name="name",
            rewards=[{"type": "SINGLE_SIDED"}],
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.create(
            type="REFERRAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.create(
            type="REFERRAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Growsurf) -> None:
        campaign = client.campaign.retrieve(
            "id",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Growsurf) -> None:
        campaign = client.campaign.update(
            id="id",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.update(
            id="id",
            company_logo_image_url="companyLogoImageUrl",
            company_name="companyName",
            name="name",
            status="IN_PROGRESS",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Growsurf) -> None:
        campaign = client.campaign.list()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Growsurf) -> None:
        campaign = client.campaign.clone(
            "id",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.clone(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.clone(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.clone(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mobile_participant_token(self, client: Growsurf) -> None:
        campaign = client.campaign.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
        )
        assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mobile_participant_token_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
            fingerprint="fingerprint",
            first_name="firstName",
            ip_address="ipAddress",
            last_name="lastName",
            metadata={"foo": "bar"},
            mobile_instance_id="mobileInstanceId",
            referral_status="CREDIT_PENDING",
            referred_by="referredBy",
        )
        assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_mobile_participant_token(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_mobile_participant_token(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_mobile_participant_token(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.create_mobile_participant_token(
                id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_commissions(self, client: Growsurf) -> None:
        campaign = client.campaign.list_commissions(
            id="id",
        )
        assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_commissions_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_commissions(
            id="id",
            limit=1,
            next_id="nextId",
            status="PENDING",
        )
        assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_commissions(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_commissions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_commissions(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_commissions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_commissions(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_commissions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_leaderboard(self, client: Growsurf) -> None:
        campaign = client.campaign.list_leaderboard(
            id="id",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_leaderboard_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_leaderboard(
            id="id",
            is_monthly=True,
            leaderboard_type="ALL_TIME",
            limit=1,
            next_id="nextId",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_leaderboard(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_leaderboard(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_leaderboard(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_leaderboard(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(ParticipantList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_leaderboard(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_leaderboard(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_participants(self, client: Growsurf) -> None:
        campaign = client.campaign.list_participants(
            id="id",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_participants_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_participants(
            id="id",
            limit=1,
            next_id="nextId",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_participants(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_participants(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_participants(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_participants(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(ParticipantList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_participants(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_participants(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payouts(self, client: Growsurf) -> None:
        campaign = client.campaign.list_payouts(
            id="id",
        )
        assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payouts_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_payouts(
            id="id",
            limit=1,
            next_id="nextId",
            status="UPCOMING",
        )
        assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_payouts(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_payouts(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_payouts(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_payouts(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_payouts(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_payouts(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_referrals(self, client: Growsurf) -> None:
        campaign = client.campaign.list_referrals(
            id="id",
        )
        assert_matches_type(ReferralList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_referrals_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_referrals(
            id="id",
            desc=True,
            email="email",
            first_name="firstName",
            last_name="lastName",
            limit=1,
            next_id="nextId",
            offset=0,
            referral_status="CREDIT_PENDING",
            sort_by="updatedAt",
        )
        assert_matches_type(ReferralList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_referrals(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_referrals(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(ReferralList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_referrals(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_referrals(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(ReferralList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_referrals(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_referrals(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_analytics(self, client: Growsurf) -> None:
        campaign = client.campaign.retrieve_analytics(
            id="id",
        )
        assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_analytics_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.retrieve_analytics(
            id="id",
            days=1,
            end_date=0,
            include="previousPeriod,statusCounts,rates",
            interval="day",
            start_date=0,
        )
        assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_analytics(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.retrieve_analytics(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_analytics(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.retrieve_analytics(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_analytics(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.retrieve_analytics(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_affiliate_applications(self, client: Growsurf) -> None:
        campaign = client.campaign.list_affiliate_applications(
            id="id",
        )
        assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_affiliate_applications_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_affiliate_applications(
            id="id",
            limit=1,
            offset=0,
            status="PENDING",
        )
        assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_affiliate_applications(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_affiliate_applications(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_affiliate_applications(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_affiliate_applications(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_affiliate_applications(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_affiliate_applications(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_affiliate_application(self, client: Growsurf) -> None:
        campaign = client.campaign.retrieve_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_affiliate_application(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.retrieve_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_affiliate_application(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.retrieve_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateApplication, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_affiliate_application(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.retrieve_affiliate_application(
                application_id="applicationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.campaign.with_raw_response.retrieve_affiliate_application(
                application_id="",
                id="campaignId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_review_affiliate_application(self, client: Growsurf) -> None:
        campaign = client.campaign.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_review_affiliate_application_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
            allow_immediate_reapply=True,
            reapply_allowed_at=0,
            rejection_reason="rejectionReason",
            review_note="reviewNote",
            status="APPROVED",
        )
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_review_affiliate_application(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_review_affiliate_application(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateApplication, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_review_affiliate_application(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.review_affiliate_application(
                application_id="applicationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.campaign.with_raw_response.review_affiliate_application(
                application_id="",
                id="campaignId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_affiliate_invites(self, client: Growsurf) -> None:
        campaign = client.campaign.list_affiliate_invites(
            id="id",
        )
        assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_affiliate_invites_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.list_affiliate_invites(
            id="id",
            limit=1,
            offset=0,
            status="PENDING",
        )
        assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_affiliate_invites(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.list_affiliate_invites(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_affiliate_invites(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.list_affiliate_invites(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_affiliate_invites(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.list_affiliate_invites(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_affiliate_invite(self, client: Growsurf) -> None:
        campaign = client.campaign.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_affiliate_invite_with_all_params(self, client: Growsurf) -> None:
        campaign = client.campaign.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
            first_name="firstName",
            last_name="lastName",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_affiliate_invite(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_affiliate_invite(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateInvite, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_affiliate_invite(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.create_affiliate_invite(
                id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_affiliate_invite(self, client: Growsurf) -> None:
        campaign = client.campaign.revoke_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke_affiliate_invite(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.revoke_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke_affiliate_invite(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.revoke_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateInvite, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke_affiliate_invite(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.revoke_affiliate_invite(
                invite_id="inviteId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.campaign.with_raw_response.revoke_affiliate_invite(
                invite_id="",
                id="campaignId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resend_affiliate_invite(self, client: Growsurf) -> None:
        campaign = client.campaign.resend_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resend_affiliate_invite(self, client: Growsurf) -> None:
        response = client.campaign.with_raw_response.resend_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resend_affiliate_invite(self, client: Growsurf) -> None:
        with client.campaign.with_streaming_response.resend_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(AffiliateInvite, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_resend_affiliate_invite(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.with_raw_response.resend_affiliate_invite(
                invite_id="inviteId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.campaign.with_raw_response.resend_affiliate_invite(
                invite_id="",
                id="campaignId",
            )


class TestAsyncCampaign:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    async def test_create_sends_goal(self, async_client: AsyncGrowsurf, respx_mock: Any) -> None:
        route = respx_mock.post(f"{base_url}/campaigns").mock(return_value=httpx.Response(200, json=CAMPAIGN_RESPONSE))

        await async_client.campaign.create(type="REFERRAL", goal="B2B_SAAS_SELF_SERVICE")

        assert json.loads(route.calls.last.request.content) == {
            "type": "REFERRAL",
            "goal": "B2B_SAAS_SELF_SERVICE",
        }

    async def test_mobile_participant_token_sends_affiliate_choice(
        self, async_client: AsyncGrowsurf, respx_mock: Any
    ) -> None:
        route = respx_mock.post(f"{base_url}/campaign/campaign-id/mobile-participant-token").mock(
            return_value=httpx.Response(200, json=MOBILE_PARTICIPANT_TOKEN_RESPONSE)
        )

        await async_client.campaign.create_mobile_participant_token(
            "campaign-id",
            email="gavin@hooli.com",
            is_affiliate=False,
        )

        assert json.loads(route.calls.last.request.content) == {
            "email": "gavin@hooli.com",
            "isAffiliate": False,
        }

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.create(
            type="REFERRAL",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.create(
            type="REFERRAL",
            company_logo_image_url="companyLogoImageUrl",
            company_name="companyName",
            currency_iso="currencyISO",
            name="name",
            rewards=[{"type": "SINGLE_SIDED"}],
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.create(
            type="REFERRAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.create(
            type="REFERRAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.retrieve(
            "id",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.update(
            id="id",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.update(
            id="id",
            company_logo_image_url="companyLogoImageUrl",
            company_name="companyName",
            name="name",
            status="IN_PROGRESS",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.clone(
            "id",
        )
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.clone(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(Campaign, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.clone(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(Campaign, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.clone(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mobile_participant_token(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
        )
        assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mobile_participant_token_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
            fingerprint="fingerprint",
            first_name="firstName",
            ip_address="ipAddress",
            last_name="lastName",
            metadata={"foo": "bar"},
            mobile_instance_id="mobileInstanceId",
            referral_status="CREDIT_PENDING",
            referred_by="referredBy",
        )
        assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_mobile_participant_token(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_mobile_participant_token(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.create_mobile_participant_token(
            id="id",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignCreateMobileParticipantTokenResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_mobile_participant_token(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.create_mobile_participant_token(
                id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_commissions(
            id="id",
        )
        assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_commissions_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_commissions(
            id="id",
            limit=1,
            next_id="nextId",
            status="PENDING",
        )
        assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_commissions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_commissions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(ParticipantCommissionList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_commissions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_leaderboard(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_leaderboard(
            id="id",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_leaderboard_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_leaderboard(
            id="id",
            is_monthly=True,
            leaderboard_type="ALL_TIME",
            limit=1,
            next_id="nextId",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_leaderboard(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_leaderboard(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_leaderboard(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_leaderboard(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(ParticipantList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_leaderboard(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_leaderboard(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_participants(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_participants(
            id="id",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_participants_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_participants(
            id="id",
            limit=1,
            next_id="nextId",
        )
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_participants(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_participants(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(ParticipantList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_participants(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_participants(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(ParticipantList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_participants(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_participants(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_payouts(
            id="id",
        )
        assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payouts_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_payouts(
            id="id",
            limit=1,
            next_id="nextId",
            status="UPCOMING",
        )
        assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_payouts(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_payouts(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(ParticipantPayoutList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_payouts(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_referrals(
            id="id",
        )
        assert_matches_type(ReferralList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_referrals_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_referrals(
            id="id",
            desc=True,
            email="email",
            first_name="firstName",
            last_name="lastName",
            limit=1,
            next_id="nextId",
            offset=0,
            referral_status="CREDIT_PENDING",
            sort_by="updatedAt",
        )
        assert_matches_type(ReferralList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_referrals(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(ReferralList, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_referrals(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(ReferralList, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_referrals(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_analytics(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.retrieve_analytics(
            id="id",
        )
        assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_analytics_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.retrieve_analytics(
            id="id",
            days=1,
            end_date=0,
            include="previousPeriod,statusCounts,rates",
            interval="day",
            start_date=0,
        )
        assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_analytics(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.retrieve_analytics(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_analytics(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.retrieve_analytics(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignRetrieveAnalyticsResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_analytics(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.retrieve_analytics(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_affiliate_applications(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_affiliate_applications(
            id="id",
        )
        assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_affiliate_applications_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_affiliate_applications(
            id="id",
            limit=1,
            offset=0,
            status="PENDING",
        )
        assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_affiliate_applications(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_affiliate_applications(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_affiliate_applications(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_affiliate_applications(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateApplicationListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_affiliate_applications(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_affiliate_applications(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.retrieve_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.retrieve_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.retrieve_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateApplication, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.retrieve_affiliate_application(
                application_id="applicationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.campaign.with_raw_response.retrieve_affiliate_application(
                application_id="",
                id="campaignId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_review_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_review_affiliate_application_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
            allow_immediate_reapply=True,
            reapply_allowed_at=0,
            rejection_reason="rejectionReason",
            review_note="reviewNote",
            status="APPROVED",
        )
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_review_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateApplication, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_review_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.review_affiliate_application(
            application_id="applicationId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateApplication, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_review_affiliate_application(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.review_affiliate_application(
                application_id="applicationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.campaign.with_raw_response.review_affiliate_application(
                application_id="",
                id="campaignId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_affiliate_invites(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_affiliate_invites(
            id="id",
        )
        assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_affiliate_invites_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.list_affiliate_invites(
            id="id",
            limit=1,
            offset=0,
            status="PENDING",
        )
        assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_affiliate_invites(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.list_affiliate_invites(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_affiliate_invites(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.list_affiliate_invites(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateInviteListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_affiliate_invites(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.list_affiliate_invites(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_affiliate_invite_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
            first_name="firstName",
            last_name="lastName",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.create_affiliate_invite(
            id="id",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateInvite, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.create_affiliate_invite(
                id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.revoke_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.revoke_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.revoke_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateInvite, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.revoke_affiliate_invite(
                invite_id="inviteId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.campaign.with_raw_response.revoke_affiliate_invite(
                invite_id="",
                id="campaignId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resend_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        campaign = await async_client.campaign.resend_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resend_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.with_raw_response.resend_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(AffiliateInvite, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resend_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.with_streaming_response.resend_affiliate_invite(
            invite_id="inviteId",
            id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(AffiliateInvite, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_resend_affiliate_invite(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.with_raw_response.resend_affiliate_invite(
                invite_id="inviteId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.campaign.with_raw_response.resend_affiliate_invite(
                invite_id="",
                id="campaignId",
            )
