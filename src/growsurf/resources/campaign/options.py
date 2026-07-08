# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign.campaign_options import CampaignOptions

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    """Campaign options (`CampaignOptions`) configuration — the Program Editor's Options tab."""

    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignOptions:
        """
        Retrieves a program's options configuration — the same surface as the dashboard
        Program Editor's **Options** tab. This is a large object whose available fields
        depend on the program type; the response includes every field and its current
        value, which is the same shape you send back on `PATCH`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/options", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignOptions,
        )

    def update(
        self,
        id: str,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignOptions:
        """
        Updates a program's options. Only the fields you send are changed. Some fields are
        program-type specific (`requireManualRewardApproval`/`autoFulfillRewards` are
        referral-only; `payoutThreshold`/`taxDocumentation` are affiliate-only, and
        affiliate programs require `requireParticipantAuth: true`).
        `fraud.recaptcha.secretKey` is write-only. `referralCreditWindowDays: null` means
        "never expires". To see the full `CampaignOptions` object with every field and its
        current value, `GET` this resource first, then `PATCH` back only the fields you
        want to change.

        Args:
          body: A partial `CampaignOptions` object — only the fields you send are changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/campaign/{id}/options", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignOptions,
        )


class AsyncOptionsResource(AsyncAPIResource):
    """Campaign options (`CampaignOptions`) configuration — the Program Editor's Options tab."""

    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignOptions:
        """
        Retrieves a program's options configuration — the same surface as the dashboard
        Program Editor's **Options** tab. This is a large object whose available fields
        depend on the program type; the response includes every field and its current
        value, which is the same shape you send back on `PATCH`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/options", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignOptions,
        )

    async def update(
        self,
        id: str,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignOptions:
        """
        Updates a program's options. Only the fields you send are changed. Some fields are
        program-type specific (`requireManualRewardApproval`/`autoFulfillRewards` are
        referral-only; `payoutThreshold`/`taxDocumentation` are affiliate-only, and
        affiliate programs require `requireParticipantAuth: true`).
        `fraud.recaptcha.secretKey` is write-only. `referralCreditWindowDays: null` means
        "never expires". To see the full `CampaignOptions` object with every field and its
        current value, `GET` this resource first, then `PATCH` back only the fields you
        want to change.

        Args:
          body: A partial `CampaignOptions` object — only the fields you send are changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/campaign/{id}/options", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignOptions,
        )


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.retrieve = to_raw_response_wrapper(
            options.retrieve,
        )
        self.update = to_raw_response_wrapper(
            options.update,
        )


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.retrieve = async_to_raw_response_wrapper(
            options.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            options.update,
        )


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.retrieve = to_streamed_response_wrapper(
            options.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            options.update,
        )


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.retrieve = async_to_streamed_response_wrapper(
            options.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            options.update,
        )
