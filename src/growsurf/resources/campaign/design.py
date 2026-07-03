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
from ...types.campaign.campaign_design import CampaignDesign

__all__ = ["DesignResource", "AsyncDesignResource"]


class DesignResource(SyncAPIResource):
    """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""

    @cached_property
    def with_raw_response(self) -> DesignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return DesignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DesignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return DesignResourceWithStreamingResponse(self)

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
    ) -> CampaignDesign:
        """
        Retrieves a program's design configuration — the same surface as the dashboard
        Program Editor's **Design** tab. This is a large object whose available fields
        depend on the program type; see the API reference for the full field list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/design", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDesign,
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
    ) -> CampaignDesign:
        """
        Updates a program's design configuration. Only the fields you send are changed (a
        surgical merge; arrays such as `signup.fields` replace wholesale). Unknown
        fields, fields not available for the program type, and invalid values return a
        `400`. The request body is a partial `CampaignDesign` object; see the API
        reference for the full field list.

        Args:
          body: A partial `CampaignDesign` object — only the fields you send are changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/campaign/{id}/design", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDesign,
        )


class AsyncDesignResource(AsyncAPIResource):
    """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""

    @cached_property
    def with_raw_response(self) -> AsyncDesignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDesignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDesignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncDesignResourceWithStreamingResponse(self)

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
    ) -> CampaignDesign:
        """
        Retrieves a program's design configuration — the same surface as the dashboard
        Program Editor's **Design** tab. This is a large object whose available fields
        depend on the program type; see the API reference for the full field list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/design", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDesign,
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
    ) -> CampaignDesign:
        """
        Updates a program's design configuration. Only the fields you send are changed (a
        surgical merge; arrays such as `signup.fields` replace wholesale). Unknown
        fields, fields not available for the program type, and invalid values return a
        `400`. The request body is a partial `CampaignDesign` object; see the API
        reference for the full field list.

        Args:
          body: A partial `CampaignDesign` object — only the fields you send are changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/campaign/{id}/design", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDesign,
        )


class DesignResourceWithRawResponse:
    def __init__(self, design: DesignResource) -> None:
        self._design = design

        self.retrieve = to_raw_response_wrapper(
            design.retrieve,
        )
        self.update = to_raw_response_wrapper(
            design.update,
        )


class AsyncDesignResourceWithRawResponse:
    def __init__(self, design: AsyncDesignResource) -> None:
        self._design = design

        self.retrieve = async_to_raw_response_wrapper(
            design.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            design.update,
        )


class DesignResourceWithStreamingResponse:
    def __init__(self, design: DesignResource) -> None:
        self._design = design

        self.retrieve = to_streamed_response_wrapper(
            design.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            design.update,
        )


class AsyncDesignResourceWithStreamingResponse:
    def __init__(self, design: AsyncDesignResource) -> None:
        self._design = design

        self.retrieve = async_to_streamed_response_wrapper(
            design.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            design.update,
        )
