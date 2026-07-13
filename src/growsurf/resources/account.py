# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import account_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.create_account_response import CreateAccountResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    """Create a GrowSurf account and its initial API key."""

    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """Return the raw response object instead of parsed content."""
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """Stream the response instead of reading it eagerly."""
        return AccountResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        company: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateAccountResponse:
        """Create a GrowSurf account and return its one-time API key.

        The key is locked until the team owner's email address is verified and rotates the
        first time the account owner signs in to the GrowSurf dashboard. Accounts whose
        email is never verified are deleted automatically after 7 days.

        Args:
          email: The email address for the new GrowSurf account. Personal emails and disposable email addresses are not accepted.

          company: Company name for the new account.

          first_name: First name for the new account owner.

          last_name: Last name for the new account owner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "email": email,
                    "company": company,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"api_key_auth": False},
            ),
            cast_to=CreateAccountResponse,
        )


class AsyncAccountResource(AsyncAPIResource):
    """Create a GrowSurf account and its initial API key."""

    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """Return the raw response object instead of parsed content."""
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """Stream the response instead of reading it eagerly."""
        return AsyncAccountResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        company: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateAccountResponse:
        """Create a GrowSurf account and return its one-time API key.

        The key is locked until the team owner's email address is verified and rotates the
        first time the account owner signs in to the GrowSurf dashboard. Accounts whose
        email is never verified are deleted automatically after 7 days.

        Args:
          email: The email address for the new GrowSurf account. Personal emails and disposable email addresses are not accepted.

          company: Company name for the new account.

          first_name: First name for the new account owner.

          last_name: Last name for the new account owner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "company": company,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"api_key_auth": False},
            ),
            cast_to=CreateAccountResponse,
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account
        self.create = to_raw_response_wrapper(account.create)


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account
        self.create = async_to_raw_response_wrapper(account.create)


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account
        self.create = to_streamed_response_wrapper(account.create)


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account
        self.create = async_to_streamed_response_wrapper(account.create)
