# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types.campaign import (
    Webhook,
    WebhookListResponse,
    WebhookTestResponse,
    DeleteWebhookResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
            events=["NEW_PARTICIPANT_ADDED", "PARTICIPANT_REACHED_A_GOAL"],
            is_enabled=True,
            secret="whsec_middleout",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Growsurf) -> None:
        response = client.campaign.webhooks.with_raw_response.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Growsurf) -> None:
        with client.campaign.webhooks.with_streaming_response.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.webhooks.with_raw_response.create(
                id="",
                payload_url="https://piedpiper.com/growsurf/webhook",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.update(
            webhook_id="webhookId",
            id="id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.update(
            webhook_id="webhookId",
            id="id",
            events=["NEW_PARTICIPANT_ADDED"],
            is_enabled=False,
            payload_url="https://piedpiper.com/growsurf/webhook",
            secret="whsec_middleout",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Growsurf) -> None:
        response = client.campaign.webhooks.with_raw_response.update(
            webhook_id="webhookId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Growsurf) -> None:
        with client.campaign.webhooks.with_streaming_response.update(
            webhook_id="webhookId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.webhooks.with_raw_response.update(
                webhook_id="webhookId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.campaign.webhooks.with_raw_response.update(
                webhook_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.list(
            "id",
        )
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Growsurf) -> None:
        response = client.campaign.webhooks.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Growsurf) -> None:
        with client.campaign.webhooks.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.webhooks.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.delete(
            webhook_id="webhookId",
            id="id",
        )
        assert_matches_type(DeleteWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Growsurf) -> None:
        response = client.campaign.webhooks.with_raw_response.delete(
            webhook_id="webhookId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(DeleteWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Growsurf) -> None:
        with client.campaign.webhooks.with_streaming_response.delete(
            webhook_id="webhookId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(DeleteWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.webhooks.with_raw_response.delete(
                webhook_id="webhookId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.campaign.webhooks.with_raw_response.delete(
                webhook_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.test(
            webhook_id="webhookId",
            id="id",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Growsurf) -> None:
        webhook = client.campaign.webhooks.test(
            webhook_id="webhookId",
            id="id",
            event="NEW_PARTICIPANT_ADDED",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Growsurf) -> None:
        response = client.campaign.webhooks.with_raw_response.test(
            webhook_id="webhookId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Growsurf) -> None:
        with client.campaign.webhooks.with_streaming_response.test(
            webhook_id="webhookId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.webhooks.with_raw_response.test(
                webhook_id="webhookId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.campaign.webhooks.with_raw_response.test(
                webhook_id="",
                id="id",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
            events=["NEW_PARTICIPANT_ADDED", "PARTICIPANT_REACHED_A_GOAL"],
            is_enabled=True,
            secret="whsec_middleout",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.webhooks.with_raw_response.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.webhooks.with_streaming_response.create(
            id="id",
            payload_url="https://piedpiper.com/growsurf/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.create(
                id="",
                payload_url="https://piedpiper.com/growsurf/webhook",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.update(
            webhook_id="webhookId",
            id="id",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.update(
            webhook_id="webhookId",
            id="id",
            events=["NEW_PARTICIPANT_ADDED"],
            is_enabled=False,
            payload_url="https://piedpiper.com/growsurf/webhook",
            secret="whsec_middleout",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.webhooks.with_raw_response.update(
            webhook_id="webhookId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.webhooks.with_streaming_response.update(
            webhook_id="webhookId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.update(
                webhook_id="webhookId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.update(
                webhook_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.list(
            "id",
        )
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.webhooks.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.webhooks.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.delete(
            webhook_id="webhookId",
            id="id",
        )
        assert_matches_type(DeleteWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.webhooks.with_raw_response.delete(
            webhook_id="webhookId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(DeleteWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.webhooks.with_streaming_response.delete(
            webhook_id="webhookId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(DeleteWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.delete(
                webhook_id="webhookId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.delete(
                webhook_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.test(
            webhook_id="webhookId",
            id="id",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        webhook = await async_client.campaign.webhooks.test(
            webhook_id="webhookId",
            id="id",
            event="NEW_PARTICIPANT_ADDED",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.webhooks.with_raw_response.test(
            webhook_id="webhookId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.webhooks.with_streaming_response.test(
            webhook_id="webhookId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.test(
                webhook_id="webhookId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.campaign.webhooks.with_raw_response.test(
                webhook_id="",
                id="id",
            )
