# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import account_create_params, account_update_params
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
from ..types.account import Account
from ..types.create_account_response import CreateAccountResponse
from ..types.rotate_api_key_response import RotateApiKeyResponse
from ..types.verification_email_response import VerificationEmailResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    """Account operations for the account that owns the API key."""

    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        company: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateAccountResponse:
        """
        Creates a new GrowSurf account. This is the only endpoint that does not require
        an API key, so you can call it on a client constructed with any placeholder
        `api_key`.

        The response includes an API key for the new account, but the key is locked
        until the account's email address is verified: authenticated endpoints outside
        the Accounts group return a `403` with error code `EMAIL_NOT_VERIFIED_ERROR`
        until then (resend the email via the resend-verification-email endpoint, then
        retry). A welcome email is sent to the address with the verification link and a
        set-password link for dashboard access. Accounts whose email is never verified
        are deleted automatically after 7 days. For security, the API key is rotated
        the first time the account owner signs in to the GrowSurf dashboard. Some
        actions (such as emailing participants) additionally require the GrowSurf team
        to verify the account first. By creating an account you agree, on behalf of the
        account holder, to GrowSurf's [Terms of Service](https://growsurf.com/terms) and
        [Privacy Policy](https://growsurf.com/privacy).

        Args:
          email: The email address for the new account. Personal emails and disposable email addresses are not accepted.

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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAccountResponse,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves your GrowSurf account — profile and GrowSurf-team verification state.
        `verificationStatus` is `VERIFIED` once the GrowSurf team has verified the
        account — this is required before you can send participant emails from a program.
        """
        return self._get(
            "/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def update(
        self,
        *,
        company: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Updates your own account profile (`first_name`, `last_name`, `company`). Any
        other property is rejected with a `400` — in particular, the account `email`
        cannot be changed via the API, and billing/subscription is not editable here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/account",
            body=maybe_transform(
                {
                    "company": company,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def rotate_api_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotateApiKeyResponse:
        """
        Generates a new API key and immediately revokes the old one.

        The key used to make this request stops working as soon as the response is
        returned — update every integration that used the old key with the new one. The
        account owner is notified by email whenever the key is rotated.
        """
        return self._post(
            "/account/api-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RotateApiKeyResponse,
        )

    def request_verification(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Requests GrowSurf-team verification of your account (required before a program can
        email its participants). Idempotent — calling it again while a request is pending
        does not create a duplicate. Returns the account with its updated
        `verificationStatus`.
        """
        return self._post(
            "/account/verification-request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def resend_verification_email(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationEmailResponse:
        """
        Resends the email-verification email to the account's email address.

        A `200` with `status: 'SENT'` is only returned when an email was actually
        dispatched. Returns a `400` if the email is already verified, or a `429` if a
        verification email was sent too recently — wait a moment, then retry.
        """
        return self._post(
            "/account/verification-email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationEmailResponse,
        )


class AsyncAccountResource(AsyncAPIResource):
    """Account operations for the account that owns the API key."""

    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        company: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateAccountResponse:
        """
        Creates a new GrowSurf account. This is the only endpoint that does not require
        an API key, so you can call it on a client constructed with any placeholder
        `api_key`.

        The response includes an API key for the new account, but the key is locked
        until the account's email address is verified: authenticated endpoints outside
        the Accounts group return a `403` with error code `EMAIL_NOT_VERIFIED_ERROR`
        until then (resend the email via the resend-verification-email endpoint, then
        retry). A welcome email is sent to the address with the verification link and a
        set-password link for dashboard access. Accounts whose email is never verified
        are deleted automatically after 7 days. For security, the API key is rotated
        the first time the account owner signs in to the GrowSurf dashboard. Some
        actions (such as emailing participants) additionally require the GrowSurf team
        to verify the account first. By creating an account you agree, on behalf of the
        account holder, to GrowSurf's [Terms of Service](https://growsurf.com/terms) and
        [Privacy Policy](https://growsurf.com/privacy).

        Args:
          email: The email address for the new account. Personal emails and disposable email addresses are not accepted.

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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAccountResponse,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Retrieves your GrowSurf account — profile and GrowSurf-team verification state.
        `verificationStatus` is `VERIFIED` once the GrowSurf team has verified the
        account — this is required before you can send participant emails from a program.
        """
        return await self._get(
            "/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def update(
        self,
        *,
        company: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Updates your own account profile (`first_name`, `last_name`, `company`). Any
        other property is rejected with a `400` — in particular, the account `email`
        cannot be changed via the API, and billing/subscription is not editable here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/account",
            body=await async_maybe_transform(
                {
                    "company": company,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def rotate_api_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotateApiKeyResponse:
        """
        Generates a new API key and immediately revokes the old one.

        The key used to make this request stops working as soon as the response is
        returned — update every integration that used the old key with the new one. The
        account owner is notified by email whenever the key is rotated.
        """
        return await self._post(
            "/account/api-key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RotateApiKeyResponse,
        )

    async def request_verification(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Account:
        """
        Requests GrowSurf-team verification of your account (required before a program can
        email its participants). Idempotent — calling it again while a request is pending
        does not create a duplicate. Returns the account with its updated
        `verificationStatus`.
        """
        return await self._post(
            "/account/verification-request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def resend_verification_email(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationEmailResponse:
        """
        Resends the email-verification email to the account's email address.

        A `200` with `status: 'SENT'` is only returned when an email was actually
        dispatched. Returns a `400` if the email is already verified, or a `429` if a
        verification email was sent too recently — wait a moment, then retry.
        """
        return await self._post(
            "/account/verification-email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationEmailResponse,
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.create = to_raw_response_wrapper(
            account.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account.retrieve,
        )
        self.update = to_raw_response_wrapper(
            account.update,
        )
        self.rotate_api_key = to_raw_response_wrapper(
            account.rotate_api_key,
        )
        self.request_verification = to_raw_response_wrapper(
            account.request_verification,
        )
        self.resend_verification_email = to_raw_response_wrapper(
            account.resend_verification_email,
        )


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.create = async_to_raw_response_wrapper(
            account.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            account.update,
        )
        self.rotate_api_key = async_to_raw_response_wrapper(
            account.rotate_api_key,
        )
        self.request_verification = async_to_raw_response_wrapper(
            account.request_verification,
        )
        self.resend_verification_email = async_to_raw_response_wrapper(
            account.resend_verification_email,
        )


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.create = to_streamed_response_wrapper(
            account.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            account.update,
        )
        self.rotate_api_key = to_streamed_response_wrapper(
            account.rotate_api_key,
        )
        self.request_verification = to_streamed_response_wrapper(
            account.request_verification,
        )
        self.resend_verification_email = to_streamed_response_wrapper(
            account.resend_verification_email,
        )


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.create = async_to_streamed_response_wrapper(
            account.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            account.update,
        )
        self.rotate_api_key = async_to_streamed_response_wrapper(
            account.rotate_api_key,
        )
        self.request_verification = async_to_streamed_response_wrapper(
            account.request_verification,
        )
        self.resend_verification_email = async_to_streamed_response_wrapper(
            account.resend_verification_email,
        )
