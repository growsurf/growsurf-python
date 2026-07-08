# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types import (
    Account,
    RotateApiKeyResponse,
    CreateAccountResponse,
    VerificationEmailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Growsurf) -> None:
        account = client.account.create(
            email="richard@piedpiper.com",
        )
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
        response = client.account.with_raw_response.create(
            email="richard@piedpiper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.create(
            email="richard@piedpiper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(CreateAccountResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Growsurf) -> None:
        account = client.account.retrieve()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Growsurf) -> None:
        response = client.account.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Growsurf) -> None:
        account = client.account.update()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Growsurf) -> None:
        account = client.account.update(
            company="Pied Piper",
            first_name="Richard",
            last_name="Hendricks",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Growsurf) -> None:
        response = client.account.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_api_key(self, client: Growsurf) -> None:
        account = client.account.rotate_api_key()
        assert_matches_type(RotateApiKeyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate_api_key(self, client: Growsurf) -> None:
        response = client.account.with_raw_response.rotate_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(RotateApiKeyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate_api_key(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.rotate_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(RotateApiKeyResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_verification(self, client: Growsurf) -> None:
        account = client.account.request_verification()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_verification(self, client: Growsurf) -> None:
        response = client.account.with_raw_response.request_verification()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_verification(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.request_verification() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resend_verification_email(self, client: Growsurf) -> None:
        account = client.account.resend_verification_email()
        assert_matches_type(VerificationEmailResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resend_verification_email(self, client: Growsurf) -> None:
        response = client.account.with_raw_response.resend_verification_email()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(VerificationEmailResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resend_verification_email(self, client: Growsurf) -> None:
        with client.account.with_streaming_response.resend_verification_email() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(VerificationEmailResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.create(
            email="richard@piedpiper.com",
        )
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
        response = await async_client.account.with_raw_response.create(
            email="richard@piedpiper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(CreateAccountResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.create(
            email="richard@piedpiper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(CreateAccountResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.retrieve()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.account.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.update()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.update(
            company="Pied Piper",
            first_name="Richard",
            last_name="Hendricks",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.account.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_api_key(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.rotate_api_key()
        assert_matches_type(RotateApiKeyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate_api_key(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.account.with_raw_response.rotate_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(RotateApiKeyResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_api_key(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.rotate_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(RotateApiKeyResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_verification(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.request_verification()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_verification(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.account.with_raw_response.request_verification()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_verification(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.request_verification() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resend_verification_email(self, async_client: AsyncGrowsurf) -> None:
        account = await async_client.account.resend_verification_email()
        assert_matches_type(VerificationEmailResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resend_verification_email(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.account.with_raw_response.resend_verification_email()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(VerificationEmailResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resend_verification_email(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.account.with_streaming_response.resend_verification_email() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(VerificationEmailResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
