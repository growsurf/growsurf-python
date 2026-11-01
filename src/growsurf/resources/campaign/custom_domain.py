# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.campaign import custom_domain_set_params
from ...types.campaign.campaign_custom_domain import CampaignCustomDomain
from ...types.campaign.delete_campaign_custom_domain_response import DeleteCampaignCustomDomainResponse

__all__ = ["CustomDomainResource", "AsyncCustomDomainResource"]


class CustomDomainResource(SyncAPIResource):
    """Campaign custom domain (`CampaignCustomDomain`) — the domain that serves a program's landing pages."""

    @cached_property
    def with_raw_response(self) -> CustomDomainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return CustomDomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomDomainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return CustomDomainResourceWithStreamingResponse(self)

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
    ) -> CampaignCustomDomain:
        """
        Retrieves the custom domain that serves a program's landing pages, and whether
        its DNS is verified. When no custom domain is set, `domain` is `null`. This
        call does not check DNS; use `verify` for a live check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/custom-domain", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCustomDomain,
        )

    def set(
        self,
        id: str,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCustomDomain:
        """
        Sets the custom domain for a program's landing pages, or replaces the current
        one. Send a hostname such as `refer.piedpiper.com`; `https://` is added if you
        leave it out. Paths, ports, queries and `http://` return a `400`.

        Replacing a domain removes the old one right away, and its pages stop loading
        there. Sending the current domain again changes nothing. A domain used by
        another program returns a `409`.

        A new domain starts unverified. Point a `CNAME` record from the hostname to the
        `dnsRecord.value` in the response, then call `verify`.

        Args:
          domain: The hostname to serve the program's landing pages from, with or without
              `https://`. Up to 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/campaign/{id}/custom-domain", id=id),
            body=maybe_transform({"domain": domain}, custom_domain_set_params.CustomDomainSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCustomDomain,
        )

    def verify(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCustomDomain:
        """
        Checks the custom domain's DNS now and returns the result in `isVerified`. The
        first time the check passes, GrowSurf sets up the domain's SSL certificate;
        pages can take a few minutes to load over `https://` after that. If the record
        is wrong or has not propagated yet, `isVerified` stays `false`; call again
        later. More than one `CNAME` record on the hostname returns a `400`. Returns a
        `404` when no custom domain is set.
        A domain that is already verified is returned as is, without a new check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/custom-domain/verify", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCustomDomain,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteCampaignCustomDomainResponse:
        """
        Removes a program's custom domain. Its landing pages go back to their GrowSurf
        URL. Returns a `404` when no custom domain is set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/campaign/{id}/custom-domain", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteCampaignCustomDomainResponse,
        )


class AsyncCustomDomainResource(AsyncAPIResource):
    """Campaign custom domain (`CampaignCustomDomain`) — the domain that serves a program's landing pages."""

    @cached_property
    def with_raw_response(self) -> AsyncCustomDomainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomDomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomDomainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncCustomDomainResourceWithStreamingResponse(self)

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
    ) -> CampaignCustomDomain:
        """
        Retrieves the custom domain that serves a program's landing pages, and whether
        its DNS is verified. When no custom domain is set, `domain` is `null`. This
        call does not check DNS; use `verify` for a live check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/custom-domain", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCustomDomain,
        )

    async def set(
        self,
        id: str,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCustomDomain:
        """
        Sets the custom domain for a program's landing pages, or replaces the current
        one. Send a hostname such as `refer.piedpiper.com`; `https://` is added if you
        leave it out. Paths, ports, queries and `http://` return a `400`.

        Replacing a domain removes the old one right away, and its pages stop loading
        there. Sending the current domain again changes nothing. A domain used by
        another program returns a `409`.

        A new domain starts unverified. Point a `CNAME` record from the hostname to the
        `dnsRecord.value` in the response, then call `verify`.

        Args:
          domain: The hostname to serve the program's landing pages from, with or without
              `https://`. Up to 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/campaign/{id}/custom-domain", id=id),
            body=await async_maybe_transform({"domain": domain}, custom_domain_set_params.CustomDomainSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCustomDomain,
        )

    async def verify(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCustomDomain:
        """
        Checks the custom domain's DNS now and returns the result in `isVerified`. The
        first time the check passes, GrowSurf sets up the domain's SSL certificate;
        pages can take a few minutes to load over `https://` after that. If the record
        is wrong or has not propagated yet, `isVerified` stays `false`; call again
        later. More than one `CNAME` record on the hostname returns a `400`. Returns a
        `404` when no custom domain is set.
        A domain that is already verified is returned as is, without a new check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/custom-domain/verify", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCustomDomain,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteCampaignCustomDomainResponse:
        """
        Removes a program's custom domain. Its landing pages go back to their GrowSurf
        URL. Returns a `404` when no custom domain is set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/campaign/{id}/custom-domain", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteCampaignCustomDomainResponse,
        )


class CustomDomainResourceWithRawResponse:
    def __init__(self, custom_domain: CustomDomainResource) -> None:
        self._custom_domain = custom_domain

        self.retrieve = to_raw_response_wrapper(
            custom_domain.retrieve,
        )
        self.set = to_raw_response_wrapper(
            custom_domain.set,
        )
        self.verify = to_raw_response_wrapper(
            custom_domain.verify,
        )
        self.delete = to_raw_response_wrapper(
            custom_domain.delete,
        )


class AsyncCustomDomainResourceWithRawResponse:
    def __init__(self, custom_domain: AsyncCustomDomainResource) -> None:
        self._custom_domain = custom_domain

        self.retrieve = async_to_raw_response_wrapper(
            custom_domain.retrieve,
        )
        self.set = async_to_raw_response_wrapper(
            custom_domain.set,
        )
        self.verify = async_to_raw_response_wrapper(
            custom_domain.verify,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_domain.delete,
        )


class CustomDomainResourceWithStreamingResponse:
    def __init__(self, custom_domain: CustomDomainResource) -> None:
        self._custom_domain = custom_domain

        self.retrieve = to_streamed_response_wrapper(
            custom_domain.retrieve,
        )
        self.set = to_streamed_response_wrapper(
            custom_domain.set,
        )
        self.verify = to_streamed_response_wrapper(
            custom_domain.verify,
        )
        self.delete = to_streamed_response_wrapper(
            custom_domain.delete,
        )


class AsyncCustomDomainResourceWithStreamingResponse:
    def __init__(self, custom_domain: AsyncCustomDomainResource) -> None:
        self._custom_domain = custom_domain

        self.retrieve = async_to_streamed_response_wrapper(
            custom_domain.retrieve,
        )
        self.set = async_to_streamed_response_wrapper(
            custom_domain.set,
        )
        self.verify = async_to_streamed_response_wrapper(
            custom_domain.verify,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_domain.delete,
        )
