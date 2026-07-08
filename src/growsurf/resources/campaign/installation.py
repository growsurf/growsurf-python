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
from ...types.campaign.campaign_installation import CampaignInstallation

__all__ = ["InstallationResource", "AsyncInstallationResource"]


class InstallationResource(SyncAPIResource):
    """Campaign installation (`CampaignInstallation`) configuration — the Program Editor's Installation tab."""

    @cached_property
    def with_raw_response(self) -> InstallationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return InstallationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return InstallationResourceWithStreamingResponse(self)

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
    ) -> CampaignInstallation:
        """
        Retrieves a program's installation configuration — the same surface as the dashboard
        Program Editor's **Installation** tab. This is a large object whose available fields
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
            path_template("/campaign/{id}/installation", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignInstallation,
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
    ) -> CampaignInstallation:
        """
        Updates a program's installation configuration. Only the fields you send are
        changed; omitted fields are left untouched. `referralTrigger` is only available
        for referral programs. `mobile.publicKey` is read-only (server-generated). URLs
        must include an explicit `http://` or `https://` scheme. To see the full
        `CampaignInstallation` object with every field and its current value, `GET` this
        resource first, then `PATCH` back only the fields you want to change.

        Args:
          body: A partial `CampaignInstallation` object — only the fields you send are changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/campaign/{id}/installation", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignInstallation,
        )


class AsyncInstallationResource(AsyncAPIResource):
    """Campaign installation (`CampaignInstallation`) configuration — the Program Editor's Installation tab."""

    @cached_property
    def with_raw_response(self) -> AsyncInstallationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncInstallationResourceWithStreamingResponse(self)

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
    ) -> CampaignInstallation:
        """
        Retrieves a program's installation configuration — the same surface as the dashboard
        Program Editor's **Installation** tab. This is a large object whose available fields
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
            path_template("/campaign/{id}/installation", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignInstallation,
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
    ) -> CampaignInstallation:
        """
        Updates a program's installation configuration. Only the fields you send are
        changed; omitted fields are left untouched. `referralTrigger` is only available
        for referral programs. `mobile.publicKey` is read-only (server-generated). URLs
        must include an explicit `http://` or `https://` scheme. To see the full
        `CampaignInstallation` object with every field and its current value, `GET` this
        resource first, then `PATCH` back only the fields you want to change.

        Args:
          body: A partial `CampaignInstallation` object — only the fields you send are changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/campaign/{id}/installation", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignInstallation,
        )


class InstallationResourceWithRawResponse:
    def __init__(self, installation: InstallationResource) -> None:
        self._installation = installation

        self.retrieve = to_raw_response_wrapper(
            installation.retrieve,
        )
        self.update = to_raw_response_wrapper(
            installation.update,
        )


class AsyncInstallationResourceWithRawResponse:
    def __init__(self, installation: AsyncInstallationResource) -> None:
        self._installation = installation

        self.retrieve = async_to_raw_response_wrapper(
            installation.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            installation.update,
        )


class InstallationResourceWithStreamingResponse:
    def __init__(self, installation: InstallationResource) -> None:
        self._installation = installation

        self.retrieve = to_streamed_response_wrapper(
            installation.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            installation.update,
        )


class AsyncInstallationResourceWithStreamingResponse:
    def __init__(self, installation: AsyncInstallationResource) -> None:
        self._installation = installation

        self.retrieve = async_to_streamed_response_wrapper(
            installation.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            installation.update,
        )
