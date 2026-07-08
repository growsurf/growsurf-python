# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types.campaign import (
    Reward,
    DeleteRewardResponse,
    CampaignRewardListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRewards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Growsurf) -> None:
        reward = client.campaign.rewards.create(
            id="id",
            type="SINGLE_SIDED",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Growsurf) -> None:
        reward = client.campaign.rewards.create(
            id="id",
            type="SINGLE_SIDED",
            conversions_required=1,
            coupon_code="couponCode",
            description="description",
            image_url="imageUrl",
            is_unlimited=True,
            is_visible=True,
            limit=0,
            limit_duration="IN_TOTAL",
            metadata={"foo": "bar"},
            next_milestone_prefix="nextMilestonePrefix",
            next_milestone_suffix="nextMilestoneSuffix",
            number_of_winners=0,
            order=0,
            referral_coupon_code="referralCouponCode",
            referral_description="referralDescription",
            referred_reward_upfront=True,
            title="title",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Growsurf) -> None:
        response = client.campaign.rewards.with_raw_response.create(
            id="id",
            type="SINGLE_SIDED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Growsurf) -> None:
        with client.campaign.rewards.with_streaming_response.create(
            id="id",
            type="SINGLE_SIDED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(Reward, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.rewards.with_raw_response.create(
                id="",
                type="SINGLE_SIDED",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Growsurf) -> None:
        reward = client.campaign.rewards.update(
            campaign_reward_id="rewardId",
            id="id",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Growsurf) -> None:
        reward = client.campaign.rewards.update(
            campaign_reward_id="rewardId",
            id="id",
            conversions_required=1,
            coupon_code="couponCode",
            description="description",
            image_url="imageUrl",
            is_unlimited=True,
            is_visible=True,
            limit=0,
            limit_duration="IN_TOTAL",
            metadata={"foo": "bar"},
            next_milestone_prefix="nextMilestonePrefix",
            next_milestone_suffix="nextMilestoneSuffix",
            number_of_winners=0,
            order=0,
            referral_coupon_code="referralCouponCode",
            referral_description="referralDescription",
            referred_reward_upfront=True,
            title="title",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Growsurf) -> None:
        response = client.campaign.rewards.with_raw_response.update(
            campaign_reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Growsurf) -> None:
        with client.campaign.rewards.with_streaming_response.update(
            campaign_reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(Reward, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.rewards.with_raw_response.update(
                campaign_reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_reward_id` but received ''"):
            client.campaign.rewards.with_raw_response.update(
                campaign_reward_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Growsurf) -> None:
        reward = client.campaign.rewards.list(
            "id",
        )
        assert_matches_type(CampaignRewardListResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Growsurf) -> None:
        response = client.campaign.rewards.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(CampaignRewardListResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Growsurf) -> None:
        with client.campaign.rewards.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(CampaignRewardListResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.rewards.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Growsurf) -> None:
        reward = client.campaign.rewards.delete(
            campaign_reward_id="rewardId",
            id="id",
        )
        assert_matches_type(DeleteRewardResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Growsurf) -> None:
        response = client.campaign.rewards.with_raw_response.delete(
            campaign_reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(DeleteRewardResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Growsurf) -> None:
        with client.campaign.rewards.with_streaming_response.delete(
            campaign_reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(DeleteRewardResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.rewards.with_raw_response.delete(
                campaign_reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_reward_id` but received ''"):
            client.campaign.rewards.with_raw_response.delete(
                campaign_reward_id="",
                id="id",
            )


class TestAsyncRewards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.rewards.create(
            id="id",
            type="SINGLE_SIDED",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.rewards.create(
            id="id",
            type="SINGLE_SIDED",
            conversions_required=1,
            coupon_code="couponCode",
            description="description",
            image_url="imageUrl",
            is_unlimited=True,
            is_visible=True,
            limit=0,
            limit_duration="IN_TOTAL",
            metadata={"foo": "bar"},
            next_milestone_prefix="nextMilestonePrefix",
            next_milestone_suffix="nextMilestoneSuffix",
            number_of_winners=0,
            order=0,
            referral_coupon_code="referralCouponCode",
            referral_description="referralDescription",
            referred_reward_upfront=True,
            title="title",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.rewards.with_raw_response.create(
            id="id",
            type="SINGLE_SIDED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.rewards.with_streaming_response.create(
            id="id",
            type="SINGLE_SIDED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(Reward, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.rewards.with_raw_response.create(
                id="",
                type="SINGLE_SIDED",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.rewards.update(
            campaign_reward_id="rewardId",
            id="id",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.rewards.update(
            campaign_reward_id="rewardId",
            id="id",
            conversions_required=1,
            coupon_code="couponCode",
            description="description",
            image_url="imageUrl",
            is_unlimited=True,
            is_visible=True,
            limit=0,
            limit_duration="IN_TOTAL",
            metadata={"foo": "bar"},
            next_milestone_prefix="nextMilestonePrefix",
            next_milestone_suffix="nextMilestoneSuffix",
            number_of_winners=0,
            order=0,
            referral_coupon_code="referralCouponCode",
            referral_description="referralDescription",
            referred_reward_upfront=True,
            title="title",
        )
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.rewards.with_raw_response.update(
            campaign_reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(Reward, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.rewards.with_streaming_response.update(
            campaign_reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(Reward, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.rewards.with_raw_response.update(
                campaign_reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_reward_id` but received ''"):
            await async_client.campaign.rewards.with_raw_response.update(
                campaign_reward_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.rewards.list(
            "id",
        )
        assert_matches_type(CampaignRewardListResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.rewards.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(CampaignRewardListResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.rewards.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(CampaignRewardListResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.rewards.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.rewards.delete(
            campaign_reward_id="rewardId",
            id="id",
        )
        assert_matches_type(DeleteRewardResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.rewards.with_raw_response.delete(
            campaign_reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(DeleteRewardResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.rewards.with_streaming_response.delete(
            campaign_reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(DeleteRewardResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.rewards.with_raw_response.delete(
                campaign_reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_reward_id` but received ''"):
            await async_client.campaign.rewards.with_raw_response.delete(
                campaign_reward_id="",
                id="id",
            )
