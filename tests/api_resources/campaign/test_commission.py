# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types.campaign import CommissionDeleteResponse, CommissionApproveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommission:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Growsurf) -> None:
        commission = client.campaign.commission.delete(
            commission_id="commissionId",
            id="id",
        )
        assert_matches_type(CommissionDeleteResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Growsurf) -> None:
        response = client.campaign.commission.with_raw_response.delete(
            commission_id="commissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commission = response.parse()
        assert_matches_type(CommissionDeleteResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Growsurf) -> None:
        with client.campaign.commission.with_streaming_response.delete(
            commission_id="commissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commission = response.parse()
            assert_matches_type(CommissionDeleteResponse, commission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.commission.with_raw_response.delete(
                commission_id="commissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commission_id` but received ''"):
            client.campaign.commission.with_raw_response.delete(
                commission_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve(self, client: Growsurf) -> None:
        commission = client.campaign.commission.approve(
            commission_id="commissionId",
            id="id",
        )
        assert_matches_type(CommissionApproveResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_approve(self, client: Growsurf) -> None:
        response = client.campaign.commission.with_raw_response.approve(
            commission_id="commissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commission = response.parse()
        assert_matches_type(CommissionApproveResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_approve(self, client: Growsurf) -> None:
        with client.campaign.commission.with_streaming_response.approve(
            commission_id="commissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commission = response.parse()
            assert_matches_type(CommissionApproveResponse, commission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_approve(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.commission.with_raw_response.approve(
                commission_id="commissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commission_id` but received ''"):
            client.campaign.commission.with_raw_response.approve(
                commission_id="",
                id="id",
            )


class TestAsyncCommission:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGrowsurf) -> None:
        commission = await async_client.campaign.commission.delete(
            commission_id="commissionId",
            id="id",
        )
        assert_matches_type(CommissionDeleteResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.commission.with_raw_response.delete(
            commission_id="commissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commission = await response.parse()
        assert_matches_type(CommissionDeleteResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.commission.with_streaming_response.delete(
            commission_id="commissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commission = await response.parse()
            assert_matches_type(CommissionDeleteResponse, commission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.commission.with_raw_response.delete(
                commission_id="commissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commission_id` but received ''"):
            await async_client.campaign.commission.with_raw_response.delete(
                commission_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve(self, async_client: AsyncGrowsurf) -> None:
        commission = await async_client.campaign.commission.approve(
            commission_id="commissionId",
            id="id",
        )
        assert_matches_type(CommissionApproveResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.commission.with_raw_response.approve(
            commission_id="commissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commission = await response.parse()
        assert_matches_type(CommissionApproveResponse, commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.commission.with_streaming_response.approve(
            commission_id="commissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commission = await response.parse()
            assert_matches_type(CommissionApproveResponse, commission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_approve(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.commission.with_raw_response.approve(
                commission_id="commissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `commission_id` but received ''"):
            await async_client.campaign.commission.with_raw_response.approve(
                commission_id="",
                id="id",
            )
