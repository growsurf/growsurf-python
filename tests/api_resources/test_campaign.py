# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types import (
    ReferralList,
    ParticipantList,
    CampaignListResponse,
    ParticipantPayoutList,
    ParticipantCommissionList,
    CampaignRetrieveAnalyticsResponse,
)
from growsurf.types.campaign import Campaign

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCampaign:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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


class TestAsyncCampaign:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

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
