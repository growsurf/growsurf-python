# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign import webhook_test_params, webhook_create_params, webhook_update_params
from ...types.campaign.webhook import Webhook
from ...types.campaign.webhook_event import WebhookEvent
from ...types.campaign.webhook_list_response import WebhookListResponse
from ...types.campaign.webhook_test_response import WebhookTestResponse
from ...types.campaign.delete_webhook_response import DeleteWebhookResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    """Campaign webhook (`Webhook`) configuration operations."""

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        payload_url: str,
        events: List[WebhookEvent] | Omit = omit,
        is_enabled: bool | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Adds a webhook to the program.

        Args:
          payload_url: The URL that receives webhook deliveries.

          events: The events this webhook is subscribed to. When omitted, it is subscribed to no
              events.

          secret: Write-only. Used to sign deliveries (the `GrowSurf-Signature` HMAC header). Never
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/webhooks", id=id),
            body=maybe_transform(
                {
                    "payload_url": payload_url,
                    "events": events,
                    "is_enabled": is_enabled,
                    "secret": secret,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def update(
        self,
        webhook_id: str,
        *,
        id: str,
        events: List[WebhookEvent] | Omit = omit,
        is_enabled: bool | Omit = omit,
        payload_url: str | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Updates a webhook by id.

        Args:
          secret: Write-only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._patch(
            path_template("/campaign/{id}/webhooks/{webhook_id}", id=id, webhook_id=webhook_id),
            body=maybe_transform(
                {
                    "events": events,
                    "is_enabled": is_enabled,
                    "payload_url": payload_url,
                    "secret": secret,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        Lists a program's webhooks (secrets are never returned).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/webhooks", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    def delete(
        self,
        webhook_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteWebhookResponse:
        """
        Removes a webhook by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._delete(
            path_template("/campaign/{id}/webhooks/{webhook_id}", id=id, webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteWebhookResponse,
        )

    def test(
        self,
        webhook_id: str,
        *,
        id: str,
        event: WebhookEvent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTestResponse:
        """
        Sends a live test event to a webhook using its stored URL and secret.

        Args:
          event: The event to simulate. When omitted, the webhook's first enabled event is used
              (`400` if it has none).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._post(
            path_template("/campaign/{id}/webhooks/{webhook_id}/test", id=id, webhook_id=webhook_id),
            body=maybe_transform({"event": event}, webhook_test_params.WebhookTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookTestResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    """Campaign webhook (`Webhook`) configuration operations."""

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        payload_url: str,
        events: List[WebhookEvent] | Omit = omit,
        is_enabled: bool | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Adds a webhook to the program.

        Args:
          payload_url: The URL that receives webhook deliveries.

          events: The events this webhook is subscribed to. When omitted, it is subscribed to no
              events.

          secret: Write-only. Used to sign deliveries (the `GrowSurf-Signature` HMAC header). Never
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/webhooks", id=id),
            body=await async_maybe_transform(
                {
                    "payload_url": payload_url,
                    "events": events,
                    "is_enabled": is_enabled,
                    "secret": secret,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def update(
        self,
        webhook_id: str,
        *,
        id: str,
        events: List[WebhookEvent] | Omit = omit,
        is_enabled: bool | Omit = omit,
        payload_url: str | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Updates a webhook by id.

        Args:
          secret: Write-only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._patch(
            path_template("/campaign/{id}/webhooks/{webhook_id}", id=id, webhook_id=webhook_id),
            body=await async_maybe_transform(
                {
                    "events": events,
                    "is_enabled": is_enabled,
                    "payload_url": payload_url,
                    "secret": secret,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        Lists a program's webhooks (secrets are never returned).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/webhooks", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    async def delete(
        self,
        webhook_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteWebhookResponse:
        """
        Removes a webhook by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._delete(
            path_template("/campaign/{id}/webhooks/{webhook_id}", id=id, webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteWebhookResponse,
        )

    async def test(
        self,
        webhook_id: str,
        *,
        id: str,
        event: WebhookEvent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTestResponse:
        """
        Sends a live test event to a webhook using its stored URL and secret.

        Args:
          event: The event to simulate. When omitted, the webhook's first enabled event is used
              (`400` if it has none).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._post(
            path_template("/campaign/{id}/webhooks/{webhook_id}/test", id=id, webhook_id=webhook_id),
            body=await async_maybe_transform({"event": event}, webhook_test_params.WebhookTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookTestResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.test = to_raw_response_wrapper(
            webhooks.test,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.test = async_to_raw_response_wrapper(
            webhooks.test,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.test = to_streamed_response_wrapper(
            webhooks.test,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.test = async_to_streamed_response_wrapper(
            webhooks.test,
        )
