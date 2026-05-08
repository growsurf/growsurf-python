# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.campaign import reward_approve_params
from ...types.campaign.reward_delete_response import RewardDeleteResponse
from ...types.campaign.reward_approve_response import RewardApproveResponse
from ...types.campaign.reward_fulfill_response import RewardFulfillResponse

__all__ = ["RewardResource", "AsyncRewardResource"]


class RewardResource(SyncAPIResource):
    """Participant reward retrieval and manual reward operations."""

    @cached_property
    def with_raw_response(self) -> RewardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return RewardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RewardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/growsurf-python#with_streaming_response
        """
        return RewardResourceWithStreamingResponse(self)

    def delete(
        self,
        reward_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardDeleteResponse:
        """
        Removes a manually approved participant reward that has not already been
        approved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not reward_id:
            raise ValueError(f"Expected a non-empty value for `reward_id` but received {reward_id!r}")
        return self._delete(
            path_template("/campaign/{id}/reward/{reward_id}", id=id, reward_id=reward_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardDeleteResponse,
        )

    def approve(
        self,
        reward_id: str,
        *,
        id: str,
        fulfill: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardApproveResponse:
        """
        Approves a manually approved reward earned by a participant.

        Args:
          fulfill: Set true to mark the reward as fulfilled after approval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not reward_id:
            raise ValueError(f"Expected a non-empty value for `reward_id` but received {reward_id!r}")
        return self._post(
            path_template("/campaign/{id}/reward/{reward_id}/approve", id=id, reward_id=reward_id),
            body=maybe_transform({"fulfill": fulfill}, reward_approve_params.RewardApproveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardApproveResponse,
        )

    def fulfill(
        self,
        reward_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardFulfillResponse:
        """
        Marks an approved participant reward as fulfilled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not reward_id:
            raise ValueError(f"Expected a non-empty value for `reward_id` but received {reward_id!r}")
        return self._post(
            path_template("/campaign/{id}/reward/{reward_id}/fulfill", id=id, reward_id=reward_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardFulfillResponse,
        )


class AsyncRewardResource(AsyncAPIResource):
    """Participant reward retrieval and manual reward operations."""

    @cached_property
    def with_raw_response(self) -> AsyncRewardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRewardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRewardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/growsurf-python#with_streaming_response
        """
        return AsyncRewardResourceWithStreamingResponse(self)

    async def delete(
        self,
        reward_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardDeleteResponse:
        """
        Removes a manually approved participant reward that has not already been
        approved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not reward_id:
            raise ValueError(f"Expected a non-empty value for `reward_id` but received {reward_id!r}")
        return await self._delete(
            path_template("/campaign/{id}/reward/{reward_id}", id=id, reward_id=reward_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardDeleteResponse,
        )

    async def approve(
        self,
        reward_id: str,
        *,
        id: str,
        fulfill: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardApproveResponse:
        """
        Approves a manually approved reward earned by a participant.

        Args:
          fulfill: Set true to mark the reward as fulfilled after approval.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not reward_id:
            raise ValueError(f"Expected a non-empty value for `reward_id` but received {reward_id!r}")
        return await self._post(
            path_template("/campaign/{id}/reward/{reward_id}/approve", id=id, reward_id=reward_id),
            body=await async_maybe_transform({"fulfill": fulfill}, reward_approve_params.RewardApproveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardApproveResponse,
        )

    async def fulfill(
        self,
        reward_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardFulfillResponse:
        """
        Marks an approved participant reward as fulfilled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not reward_id:
            raise ValueError(f"Expected a non-empty value for `reward_id` but received {reward_id!r}")
        return await self._post(
            path_template("/campaign/{id}/reward/{reward_id}/fulfill", id=id, reward_id=reward_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardFulfillResponse,
        )


class RewardResourceWithRawResponse:
    def __init__(self, reward: RewardResource) -> None:
        self._reward = reward

        self.delete = to_raw_response_wrapper(
            reward.delete,
        )
        self.approve = to_raw_response_wrapper(
            reward.approve,
        )
        self.fulfill = to_raw_response_wrapper(
            reward.fulfill,
        )


class AsyncRewardResourceWithRawResponse:
    def __init__(self, reward: AsyncRewardResource) -> None:
        self._reward = reward

        self.delete = async_to_raw_response_wrapper(
            reward.delete,
        )
        self.approve = async_to_raw_response_wrapper(
            reward.approve,
        )
        self.fulfill = async_to_raw_response_wrapper(
            reward.fulfill,
        )


class RewardResourceWithStreamingResponse:
    def __init__(self, reward: RewardResource) -> None:
        self._reward = reward

        self.delete = to_streamed_response_wrapper(
            reward.delete,
        )
        self.approve = to_streamed_response_wrapper(
            reward.approve,
        )
        self.fulfill = to_streamed_response_wrapper(
            reward.fulfill,
        )


class AsyncRewardResourceWithStreamingResponse:
    def __init__(self, reward: AsyncRewardResource) -> None:
        self._reward = reward

        self.delete = async_to_streamed_response_wrapper(
            reward.delete,
        )
        self.approve = async_to_streamed_response_wrapper(
            reward.approve,
        )
        self.fulfill = async_to_streamed_response_wrapper(
            reward.fulfill,
        )
