# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types import CreateAccountResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.parametrize("configured_api_key", [None, "My API Key"], ids=["keyless", "configured-key"])
    def test_create_never_sends_authorization(
        self,
        monkeypatch: pytest.MonkeyPatch,
        configured_api_key: str | None,
    ) -> None:
        monkeypatch.delenv("GROWSURF_API_KEY", raising=False)
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(
                200,
                json={
                    "email": "richard@piedpiper.com",
                    "apiKey": "new_key",
                    "verificationStatus": "NOT_REQUESTED",
                },
            )

        with httpx.Client(transport=httpx.MockTransport(handler)) as http_client:
            with Growsurf(
                api_key=configured_api_key,
                base_url="http://localhost:4010",
                http_client=http_client,
            ) as account_client:
                account_client.account.create(email="richard@piedpiper.com")

        assert len(requests) == 1
        assert "Authorization" not in requests[0].headers

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Growsurf) -> None:
        account = client.account.create(email="richard@piedpiper.com")
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Growsurf) -> None:
        account = client.account.create(
            email="richard@piedpiper.com",
            company="Pied Piper",
            first_name="Richard",
            last_name="Hendricks",
        )
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Growsurf) -> None:
        response = client.account.with_raw_response.create(email="richard@piedpiper.com")
        assert response.is_closed is True
        account = response.parse()
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.create(email="richard@piedpiper.com") as response:
            assert not response.is_closed
            account = response.parse()
            assert_matches_type(CreateAccountResponse, account, path=["response"])
        assert cast(Any, response.is_closed) is True


class TestAsyncAccount:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.parametrize("configured_api_key", [None, "My API Key"], ids=["keyless", "configured-key"])
    async def test_create_never_sends_authorization(
        self,
        monkeypatch: pytest.MonkeyPatch,
        configured_api_key: str | None,
    ) -> None:
        monkeypatch.delenv("GROWSURF_API_KEY", raising=False)
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(
                200,
                json={
                    "email": "richard@piedpiper.com",
                    "apiKey": "new_key",
                    "verificationStatus": "NOT_REQUESTED",
                },
            )

        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http_client:
            async with AsyncGrowsurf(
                api_key=configured_api_key,
                base_url="http://localhost:4010",
                http_client=http_client,
            ) as account_client:
                await account_client.account.create(email="richard@piedpiper.com")

        assert len(requests) == 1
        assert "Authorization" not in requests[0].headers

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.create(email="richard@piedpiper.com")
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.create(
            email="richard@piedpiper.com",
            company="Pied Piper",
            first_name="Richard",
            last_name="Hendricks",
        )
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.account.with_raw_response.create(email="richard@piedpiper.com")
        assert response.is_closed is True
        account = await response.parse()
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.create(email="richard@piedpiper.com") as response:
            assert not response.is_closed
            account = await response.parse()
            assert_matches_type(CreateAccountResponse, account, path=["response"])
        assert cast(Any, response.is_closed) is True
