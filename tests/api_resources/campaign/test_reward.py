# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types.campaign import (
    RewardDeleteResponse,
    RewardApproveResponse,
    RewardFulfillResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReward:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Growsurf) -> None:
        reward = client.campaign.reward.delete(
            reward_id="rewardId",
            id="id",
        )
        assert_matches_type(RewardDeleteResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Growsurf) -> None:
        response = client.campaign.reward.with_raw_response.delete(
            reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(RewardDeleteResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Growsurf) -> None:
        with client.campaign.reward.with_streaming_response.delete(
            reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(RewardDeleteResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.reward.with_raw_response.delete(
                reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reward_id` but received ''"):
            client.campaign.reward.with_raw_response.delete(
                reward_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve(self, client: Growsurf) -> None:
        reward = client.campaign.reward.approve(
            reward_id="rewardId",
            id="id",
        )
        assert_matches_type(RewardApproveResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve_with_all_params(self, client: Growsurf) -> None:
        reward = client.campaign.reward.approve(
            reward_id="rewardId",
            id="id",
            fulfill=True,
        )
        assert_matches_type(RewardApproveResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_approve(self, client: Growsurf) -> None:
        response = client.campaign.reward.with_raw_response.approve(
            reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(RewardApproveResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_approve(self, client: Growsurf) -> None:
        with client.campaign.reward.with_streaming_response.approve(
            reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(RewardApproveResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_approve(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.reward.with_raw_response.approve(
                reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reward_id` but received ''"):
            client.campaign.reward.with_raw_response.approve(
                reward_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fulfill(self, client: Growsurf) -> None:
        reward = client.campaign.reward.fulfill(
            reward_id="rewardId",
            id="id",
        )
        assert_matches_type(RewardFulfillResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fulfill(self, client: Growsurf) -> None:
        response = client.campaign.reward.with_raw_response.fulfill(
            reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = response.parse()
        assert_matches_type(RewardFulfillResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fulfill(self, client: Growsurf) -> None:
        with client.campaign.reward.with_streaming_response.fulfill(
            reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = response.parse()
            assert_matches_type(RewardFulfillResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fulfill(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.reward.with_raw_response.fulfill(
                reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reward_id` but received ''"):
            client.campaign.reward.with_raw_response.fulfill(
                reward_id="",
                id="id",
            )


class TestAsyncReward:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.reward.delete(
            reward_id="rewardId",
            id="id",
        )
        assert_matches_type(RewardDeleteResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.reward.with_raw_response.delete(
            reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(RewardDeleteResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.reward.with_streaming_response.delete(
            reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(RewardDeleteResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.reward.with_raw_response.delete(
                reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reward_id` but received ''"):
            await async_client.campaign.reward.with_raw_response.delete(
                reward_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.reward.approve(
            reward_id="rewardId",
            id="id",
        )
        assert_matches_type(RewardApproveResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.reward.approve(
            reward_id="rewardId",
            id="id",
            fulfill=True,
        )
        assert_matches_type(RewardApproveResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.reward.with_raw_response.approve(
            reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(RewardApproveResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.reward.with_streaming_response.approve(
            reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(RewardApproveResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_approve(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.reward.with_raw_response.approve(
                reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reward_id` but received ''"):
            await async_client.campaign.reward.with_raw_response.approve(
                reward_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fulfill(self, async_client: AsyncGrowsurf) -> None:
        reward = await async_client.campaign.reward.fulfill(
            reward_id="rewardId",
            id="id",
        )
        assert_matches_type(RewardFulfillResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fulfill(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.reward.with_raw_response.fulfill(
            reward_id="rewardId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward = await response.parse()
        assert_matches_type(RewardFulfillResponse, reward, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fulfill(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.reward.with_streaming_response.fulfill(
            reward_id="rewardId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward = await response.parse()
            assert_matches_type(RewardFulfillResponse, reward, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fulfill(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.reward.with_raw_response.fulfill(
                reward_id="rewardId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reward_id` but received ''"):
            await async_client.campaign.reward.with_raw_response.fulfill(
                reward_id="",
                id="id",
            )
