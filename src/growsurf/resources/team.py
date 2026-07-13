# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import team_update_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.team import Team
from .._base_client import make_request_options
from ..types.rotate_api_key_response import RotateApiKeyResponse
from ..types.verification_email_response import VerificationEmailResponse

__all__ = ["TeamResource", "AsyncTeamResource"]


class TeamResource(SyncAPIResource):
    """Operations for the team bound to the API key or OAuth connection."""

    @cached_property
    def with_raw_response(self) -> TeamResourceWithRawResponse:
        """Return the raw response object instead of parsed content."""
        return TeamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamResourceWithStreamingResponse:
        """Stream the response instead of reading it eagerly."""
        return TeamResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """Retrieve the team bound to the API key or OAuth connection."""
        return self._get(
            "/team",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def update(
        self,
        *,
        name: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """Update the bound team's display name.

        Any other property is rejected with a `400`.

        Args:
          name: The team's display name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/team",
            body=maybe_transform({"name": name}, team_update_params.TeamUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def rotate_api_key(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotateApiKeyResponse:
        """Rotate the API key used for this request.

        The SDK sends a retry-safe `Idempotency-Key`, so automatic retries return the
        same replacement. Store the new key, then update every integration that used the
        old key. This operation is unavailable through MCP.
        """
        return self._post(
            "/api-key/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RotateApiKeyResponse,
        )

    def request_verification(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """Request GrowSurf verification for the bound team.

        Calling this again while a request is pending does not create a duplicate.
        """
        return self._post(
            "/team/verification-request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def resend_owner_verification_email(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationEmailResponse:
        """Resend the email-verification message to the bound team's owner.

        The response never reveals the owner's email address.
        """
        return self._post(
            "/team/owner/verification-email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationEmailResponse,
        )


class AsyncTeamResource(AsyncAPIResource):
    """Operations for the team bound to the API key or OAuth connection."""

    @cached_property
    def with_raw_response(self) -> AsyncTeamResourceWithRawResponse:
        """Return the raw response object instead of parsed content."""
        return AsyncTeamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamResourceWithStreamingResponse:
        """Stream the response instead of reading it eagerly."""
        return AsyncTeamResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """Retrieve the team bound to the API key or OAuth connection."""
        return await self._get(
            "/team",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    async def update(
        self,
        *,
        name: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """Update the bound team's display name.

        Any other property is rejected with a `400`.

        Args:
          name: The team's display name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/team",
            body=await async_maybe_transform({"name": name}, team_update_params.TeamUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    async def rotate_api_key(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotateApiKeyResponse:
        """Rotate the API key used for this request.

        The SDK sends a retry-safe `Idempotency-Key`, so automatic retries return the
        same replacement. Store the new key, then update every integration that used the
        old key. This operation is unavailable through MCP.
        """
        return await self._post(
            "/api-key/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RotateApiKeyResponse,
        )

    async def request_verification(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Team:
        """Request GrowSurf verification for the bound team.

        Calling this again while a request is pending does not create a duplicate.
        """
        return await self._post(
            "/team/verification-request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    async def resend_owner_verification_email(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationEmailResponse:
        """Resend the email-verification message to the bound team's owner.

        The response never reveals the owner's email address.
        """
        return await self._post(
            "/team/owner/verification-email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationEmailResponse,
        )


class TeamResourceWithRawResponse:
    def __init__(self, team: TeamResource) -> None:
        self._team = team
        self.retrieve = to_raw_response_wrapper(team.retrieve)
        self.update = to_raw_response_wrapper(team.update)
        self.rotate_api_key = to_raw_response_wrapper(team.rotate_api_key)
        self.request_verification = to_raw_response_wrapper(team.request_verification)
        self.resend_owner_verification_email = to_raw_response_wrapper(team.resend_owner_verification_email)


class AsyncTeamResourceWithRawResponse:
    def __init__(self, team: AsyncTeamResource) -> None:
        self._team = team
        self.retrieve = async_to_raw_response_wrapper(team.retrieve)
        self.update = async_to_raw_response_wrapper(team.update)
        self.rotate_api_key = async_to_raw_response_wrapper(team.rotate_api_key)
        self.request_verification = async_to_raw_response_wrapper(team.request_verification)
        self.resend_owner_verification_email = async_to_raw_response_wrapper(team.resend_owner_verification_email)


class TeamResourceWithStreamingResponse:
    def __init__(self, team: TeamResource) -> None:
        self._team = team
        self.retrieve = to_streamed_response_wrapper(team.retrieve)
        self.update = to_streamed_response_wrapper(team.update)
        self.rotate_api_key = to_streamed_response_wrapper(team.rotate_api_key)
        self.request_verification = to_streamed_response_wrapper(team.request_verification)
        self.resend_owner_verification_email = to_streamed_response_wrapper(team.resend_owner_verification_email)


class AsyncTeamResourceWithStreamingResponse:
    def __init__(self, team: AsyncTeamResource) -> None:
        self._team = team
        self.retrieve = async_to_streamed_response_wrapper(team.retrieve)
        self.update = async_to_streamed_response_wrapper(team.update)
        self.rotate_api_key = async_to_streamed_response_wrapper(team.rotate_api_key)
        self.request_verification = async_to_streamed_response_wrapper(team.request_verification)
        self.resend_owner_verification_email = async_to_streamed_response_wrapper(team.resend_owner_verification_email)
