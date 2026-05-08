# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.campaign.commission_delete_response import CommissionDeleteResponse
from ...types.campaign.commission_approve_response import CommissionApproveResponse

__all__ = ["CommissionResource", "AsyncCommissionResource"]


class CommissionResource(SyncAPIResource):
    """Affiliate transaction, commission, and payout operations."""

    @cached_property
    def with_raw_response(self) -> CommissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return CommissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return CommissionResourceWithStreamingResponse(self)

    def delete(
        self,
        commission_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommissionDeleteResponse:
        """
        Removes a pending participant commission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not commission_id:
            raise ValueError(f"Expected a non-empty value for `commission_id` but received {commission_id!r}")
        return self._delete(
            path_template("/campaign/{id}/commission/{commission_id}", id=id, commission_id=commission_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommissionDeleteResponse,
        )

    def approve(
        self,
        commission_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommissionApproveResponse:
        """
        Approves a pending participant commission so it can become eligible for payout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not commission_id:
            raise ValueError(f"Expected a non-empty value for `commission_id` but received {commission_id!r}")
        return self._post(
            path_template("/campaign/{id}/commission/{commission_id}/approve", id=id, commission_id=commission_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommissionApproveResponse,
        )


class AsyncCommissionResource(AsyncAPIResource):
    """Affiliate transaction, commission, and payout operations."""

    @cached_property
    def with_raw_response(self) -> AsyncCommissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncCommissionResourceWithStreamingResponse(self)

    async def delete(
        self,
        commission_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommissionDeleteResponse:
        """
        Removes a pending participant commission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not commission_id:
            raise ValueError(f"Expected a non-empty value for `commission_id` but received {commission_id!r}")
        return await self._delete(
            path_template("/campaign/{id}/commission/{commission_id}", id=id, commission_id=commission_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommissionDeleteResponse,
        )

    async def approve(
        self,
        commission_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommissionApproveResponse:
        """
        Approves a pending participant commission so it can become eligible for payout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not commission_id:
            raise ValueError(f"Expected a non-empty value for `commission_id` but received {commission_id!r}")
        return await self._post(
            path_template("/campaign/{id}/commission/{commission_id}/approve", id=id, commission_id=commission_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommissionApproveResponse,
        )


class CommissionResourceWithRawResponse:
    def __init__(self, commission: CommissionResource) -> None:
        self._commission = commission

        self.delete = to_raw_response_wrapper(
            commission.delete,
        )
        self.approve = to_raw_response_wrapper(
            commission.approve,
        )


class AsyncCommissionResourceWithRawResponse:
    def __init__(self, commission: AsyncCommissionResource) -> None:
        self._commission = commission

        self.delete = async_to_raw_response_wrapper(
            commission.delete,
        )
        self.approve = async_to_raw_response_wrapper(
            commission.approve,
        )


class CommissionResourceWithStreamingResponse:
    def __init__(self, commission: CommissionResource) -> None:
        self._commission = commission

        self.delete = to_streamed_response_wrapper(
            commission.delete,
        )
        self.approve = to_streamed_response_wrapper(
            commission.approve,
        )


class AsyncCommissionResourceWithStreamingResponse:
    def __init__(self, commission: AsyncCommissionResource) -> None:
        self._commission = commission

        self.delete = async_to_streamed_response_wrapper(
            commission.delete,
        )
        self.approve = async_to_streamed_response_wrapper(
            commission.approve,
        )
