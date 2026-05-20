# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from .reward import (
    RewardResource,
    AsyncRewardResource,
    RewardResourceWithRawResponse,
    AsyncRewardResourceWithRawResponse,
    RewardResourceWithStreamingResponse,
    AsyncRewardResourceWithStreamingResponse,
)
from ...types import (
    campaign_list_payouts_params,
    campaign_list_referrals_params,
    campaign_list_commissions_params,
    campaign_list_leaderboard_params,
    campaign_list_participants_params,
    campaign_retrieve_analytics_params,
    campaign_create_mobile_participant_token_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .commission import (
    CommissionResource,
    AsyncCommissionResource,
    CommissionResourceWithRawResponse,
    AsyncCommissionResourceWithRawResponse,
    CommissionResourceWithStreamingResponse,
    AsyncCommissionResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .participant import (
    ParticipantResource,
    AsyncParticipantResource,
    ParticipantResourceWithRawResponse,
    AsyncParticipantResourceWithRawResponse,
    ParticipantResourceWithStreamingResponse,
    AsyncParticipantResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.campaign import ReferralStatus
from ...types.referral_list import ReferralList
from ...types.participant_list import ParticipantList
from ...types.campaign.campaign import Campaign
from ...types.campaign_list_response import CampaignListResponse
from ...types.participant_payout_list import ParticipantPayoutList
from ...types.campaign.referral_status import ReferralStatus
from ...types.participant_commission_list import ParticipantCommissionList
from ...types.campaign_retrieve_analytics_response import CampaignRetrieveAnalyticsResponse
from ...types.campaign_create_mobile_participant_token_response import CampaignCreateMobileParticipantTokenResponse

__all__ = ["CampaignResource", "AsyncCampaignResource"]


class CampaignResource(SyncAPIResource):
    @cached_property
    def participant(self) -> ParticipantResource:
        return ParticipantResource(self._client)

    @cached_property
    def reward(self) -> RewardResource:
        """Participant reward retrieval and manual reward operations."""
        return RewardResource(self._client)

    @cached_property
    def commission(self) -> CommissionResource:
        """Affiliate transaction, commission, and payout operations."""
        return CommissionResource(self._client)

    @cached_property
    def with_raw_response(self) -> CampaignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return CampaignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return CampaignResourceWithStreamingResponse(self)

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
    ) -> Campaign:
        """
        Retrieves a program for the given program ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignListResponse:
        """Retrieves a list of your programs. Deleted programs are not returned."""
        return self._get(
            "/campaigns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignListResponse,
        )

    def create_mobile_participant_token(
        self,
        id: str,
        *,
        email: str,
        fingerprint: str | Omit = omit,
        first_name: str | Omit = omit,
        ip_address: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        mobile_instance_id: str | Omit = omit,
        referral_status: Literal["CREDIT_PENDING", "CREDIT_AWARDED"] | Omit = omit,
        referred_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCreateMobileParticipantTokenResponse:
        """
        Creates or returns a participant using the same input behavior as Add
        Participant, then returns a participant-scoped token for GrowSurf mobile SDK
        participant endpoints. Use this endpoint from your backend after your mobile app
        authenticates a signed-in user. The program must have mobile SDK access enabled.

        Args:
          metadata: Shallow custom metadata object.

          mobile_instance_id: Optional app-install scoped identifier for native mobile anti-fraud. Recommended
              for mobile participant creation and mobile participant token flows.

          referred_by: Referrer participant ID or email address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/mobile-participant-token", id=id),
            body=maybe_transform(
                {
                    "email": email,
                    "fingerprint": fingerprint,
                    "first_name": first_name,
                    "ip_address": ip_address,
                    "last_name": last_name,
                    "metadata": metadata,
                    "mobile_instance_id": mobile_instance_id,
                    "referral_status": referral_status,
                    "referred_by": referred_by,
                },
                campaign_create_mobile_participant_token_params.CampaignCreateMobileParticipantTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCreateMobileParticipantTokenResponse,
        )

    def list_commissions(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        status: Literal["PENDING", "APPROVED", "PAID", "REVERSED", "DELETED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantCommissionList:
        """
        Retrieves a paged list of all participant commissions in an affiliate program.

        Args:
          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          status: Participant commission status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/commissions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_id": next_id,
                        "status": status,
                    },
                    campaign_list_commissions_params.CampaignListCommissionsParams,
                ),
            ),
            cast_to=ParticipantCommissionList,
        )

    def list_leaderboard(
        self,
        id: str,
        *,
        is_monthly: bool | Omit = omit,
        leaderboard_type: Literal[
            "ALL_TIME",
            "CURRENT_MONTH",
            "PREV_MONTH",
            "TOTAL_IMPRESSION_COUNT",
            "UNIQUE_IMPRESSION_COUNT",
            "BY_COMMISSIONS",
            "BY_REVENUE",
            "BY_REFERRALS",
            "BY_LEADS",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantList:
        """
        Retrieves participants in leaderboard order for the specified leaderboard type.

        Args:
          is_monthly: Deprecated. Use `leaderboardType=CURRENT_MONTH` instead.

          leaderboard_type: Leaderboard ordering mode.

          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/leaderboard", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_monthly": is_monthly,
                        "leaderboard_type": leaderboard_type,
                        "limit": limit,
                        "next_id": next_id,
                    },
                    campaign_list_leaderboard_params.CampaignListLeaderboardParams,
                ),
            ),
            cast_to=ParticipantList,
        )

    def list_participants(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantList:
        """
        Retrieves a paged list of participants in a program.

        Args:
          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/participants", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_id": next_id,
                    },
                    campaign_list_participants_params.CampaignListParticipantsParams,
                ),
            ),
            cast_to=ParticipantList,
        )

    def list_payouts(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        status: Literal["UPCOMING", "QUEUED", "ISSUED", "FAILED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantPayoutList:
        """
        Retrieves a paged list of all participant payouts in an affiliate program.

        Args:
          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          status: Participant payout status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/payouts", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_id": next_id,
                        "status": status,
                    },
                    campaign_list_payouts_params.CampaignListPayoutsParams,
                ),
            ),
            cast_to=ParticipantPayoutList,
        )

    def list_referrals(
        self,
        id: str,
        *,
        desc: bool | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        offset: int | Omit = omit,
        referral_status: ReferralStatus | Omit = omit,
        sort_by: Literal[
            "updatedAt", "createdAt", "email", "firstName", "lastName", "referralStatus", "referralTriggeredAt"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralList:
        """
        Retrieves a list of all referrals and email invites made by participants in a
        program.

        Args:
          desc: Return results in descending order when true.

          email: URL-encoded email value to filter referral results.

          first_name: First name value to filter results.

          last_name: Last name value to filter results.

          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          offset: Offset number used to skip through a result set.

          sort_by: Field used to sort referral results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/referrals", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "desc": desc,
                        "email": email,
                        "first_name": first_name,
                        "last_name": last_name,
                        "limit": limit,
                        "next_id": next_id,
                        "offset": offset,
                        "referral_status": referral_status,
                        "sort_by": sort_by,
                    },
                    campaign_list_referrals_params.CampaignListReferralsParams,
                ),
            ),
            cast_to=ReferralList,
        )

    def retrieve_analytics(
        self,
        id: str,
        *,
        days: int | Omit = omit,
        end_date: int | Omit = omit,
        start_date: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRetrieveAnalyticsResponse:
        """
        Retrieves analytics for a program.

        Args:
          days: Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825.

          end_date: End date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          start_date: Start date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/analytics", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "days": days,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    campaign_retrieve_analytics_params.CampaignRetrieveAnalyticsParams,
                ),
            ),
            cast_to=CampaignRetrieveAnalyticsResponse,
        )


class AsyncCampaignResource(AsyncAPIResource):
    @cached_property
    def participant(self) -> AsyncParticipantResource:
        return AsyncParticipantResource(self._client)

    @cached_property
    def reward(self) -> AsyncRewardResource:
        """Participant reward retrieval and manual reward operations."""
        return AsyncRewardResource(self._client)

    @cached_property
    def commission(self) -> AsyncCommissionResource:
        """Affiliate transaction, commission, and payout operations."""
        return AsyncCommissionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCampaignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncCampaignResourceWithStreamingResponse(self)

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
    ) -> Campaign:
        """
        Retrieves a program for the given program ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignListResponse:
        """Retrieves a list of your programs. Deleted programs are not returned."""
        return await self._get(
            "/campaigns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignListResponse,
        )

    async def create_mobile_participant_token(
        self,
        id: str,
        *,
        email: str,
        fingerprint: str | Omit = omit,
        first_name: str | Omit = omit,
        ip_address: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        mobile_instance_id: str | Omit = omit,
        referral_status: Literal["CREDIT_PENDING", "CREDIT_AWARDED"] | Omit = omit,
        referred_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignCreateMobileParticipantTokenResponse:
        """
        Creates or returns a participant using the same input behavior as Add
        Participant, then returns a participant-scoped token for GrowSurf mobile SDK
        participant endpoints. Use this endpoint from your backend after your mobile app
        authenticates a signed-in user. The program must have mobile SDK access enabled.

        Args:
          metadata: Shallow custom metadata object.

          mobile_instance_id: Optional app-install scoped identifier for native mobile anti-fraud. Recommended
              for mobile participant creation and mobile participant token flows.

          referred_by: Referrer participant ID or email address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/mobile-participant-token", id=id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "fingerprint": fingerprint,
                    "first_name": first_name,
                    "ip_address": ip_address,
                    "last_name": last_name,
                    "metadata": metadata,
                    "mobile_instance_id": mobile_instance_id,
                    "referral_status": referral_status,
                    "referred_by": referred_by,
                },
                campaign_create_mobile_participant_token_params.CampaignCreateMobileParticipantTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignCreateMobileParticipantTokenResponse,
        )

    async def list_commissions(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        status: Literal["PENDING", "APPROVED", "PAID", "REVERSED", "DELETED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantCommissionList:
        """
        Retrieves a paged list of all participant commissions in an affiliate program.

        Args:
          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          status: Participant commission status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/commissions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_id": next_id,
                        "status": status,
                    },
                    campaign_list_commissions_params.CampaignListCommissionsParams,
                ),
            ),
            cast_to=ParticipantCommissionList,
        )

    async def list_leaderboard(
        self,
        id: str,
        *,
        is_monthly: bool | Omit = omit,
        leaderboard_type: Literal[
            "ALL_TIME",
            "CURRENT_MONTH",
            "PREV_MONTH",
            "TOTAL_IMPRESSION_COUNT",
            "UNIQUE_IMPRESSION_COUNT",
            "BY_COMMISSIONS",
            "BY_REVENUE",
            "BY_REFERRALS",
            "BY_LEADS",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantList:
        """
        Retrieves participants in leaderboard order for the specified leaderboard type.

        Args:
          is_monthly: Deprecated. Use `leaderboardType=CURRENT_MONTH` instead.

          leaderboard_type: Leaderboard ordering mode.

          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/leaderboard", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_monthly": is_monthly,
                        "leaderboard_type": leaderboard_type,
                        "limit": limit,
                        "next_id": next_id,
                    },
                    campaign_list_leaderboard_params.CampaignListLeaderboardParams,
                ),
            ),
            cast_to=ParticipantList,
        )

    async def list_participants(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantList:
        """
        Retrieves a paged list of participants in a program.

        Args:
          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/participants", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_id": next_id,
                    },
                    campaign_list_participants_params.CampaignListParticipantsParams,
                ),
            ),
            cast_to=ParticipantList,
        )

    async def list_payouts(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        status: Literal["UPCOMING", "QUEUED", "ISSUED", "FAILED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantPayoutList:
        """
        Retrieves a paged list of all participant payouts in an affiliate program.

        Args:
          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          status: Participant payout status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/payouts", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_id": next_id,
                        "status": status,
                    },
                    campaign_list_payouts_params.CampaignListPayoutsParams,
                ),
            ),
            cast_to=ParticipantPayoutList,
        )

    async def list_referrals(
        self,
        id: str,
        *,
        desc: bool | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        offset: int | Omit = omit,
        referral_status: ReferralStatus | Omit = omit,
        sort_by: Literal[
            "updatedAt", "createdAt", "email", "firstName", "lastName", "referralStatus", "referralTriggeredAt"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralList:
        """
        Retrieves a list of all referrals and email invites made by participants in a
        program.

        Args:
          desc: Return results in descending order when true.

          email: URL-encoded email value to filter referral results.

          first_name: First name value to filter results.

          last_name: Last name value to filter results.

          limit: Number of results to return. Maximum 100.

          next_id: ID to start the next paged result set with.

          offset: Offset number used to skip through a result set.

          sort_by: Field used to sort referral results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/referrals", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "desc": desc,
                        "email": email,
                        "first_name": first_name,
                        "last_name": last_name,
                        "limit": limit,
                        "next_id": next_id,
                        "offset": offset,
                        "referral_status": referral_status,
                        "sort_by": sort_by,
                    },
                    campaign_list_referrals_params.CampaignListReferralsParams,
                ),
            ),
            cast_to=ReferralList,
        )

    async def retrieve_analytics(
        self,
        id: str,
        *,
        days: int | Omit = omit,
        end_date: int | Omit = omit,
        start_date: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRetrieveAnalyticsResponse:
        """
        Retrieves analytics for a program.

        Args:
          days: Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825.

          end_date: End date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          start_date: Start date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/analytics", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "days": days,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    campaign_retrieve_analytics_params.CampaignRetrieveAnalyticsParams,
                ),
            ),
            cast_to=CampaignRetrieveAnalyticsResponse,
        )


class CampaignResourceWithRawResponse:
    def __init__(self, campaign: CampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = to_raw_response_wrapper(
            campaign.retrieve,
        )
        self.list = to_raw_response_wrapper(
            campaign.list,
        )
        self.create_mobile_participant_token = to_raw_response_wrapper(
            campaign.create_mobile_participant_token,
        )
        self.list_commissions = to_raw_response_wrapper(
            campaign.list_commissions,
        )
        self.list_leaderboard = to_raw_response_wrapper(
            campaign.list_leaderboard,
        )
        self.list_participants = to_raw_response_wrapper(
            campaign.list_participants,
        )
        self.list_payouts = to_raw_response_wrapper(
            campaign.list_payouts,
        )
        self.list_referrals = to_raw_response_wrapper(
            campaign.list_referrals,
        )
        self.retrieve_analytics = to_raw_response_wrapper(
            campaign.retrieve_analytics,
        )

    @cached_property
    def participant(self) -> ParticipantResourceWithRawResponse:
        return ParticipantResourceWithRawResponse(self._campaign.participant)

    @cached_property
    def reward(self) -> RewardResourceWithRawResponse:
        """Participant reward retrieval and manual reward operations."""
        return RewardResourceWithRawResponse(self._campaign.reward)

    @cached_property
    def commission(self) -> CommissionResourceWithRawResponse:
        """Affiliate transaction, commission, and payout operations."""
        return CommissionResourceWithRawResponse(self._campaign.commission)


class AsyncCampaignResourceWithRawResponse:
    def __init__(self, campaign: AsyncCampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = async_to_raw_response_wrapper(
            campaign.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            campaign.list,
        )
        self.create_mobile_participant_token = async_to_raw_response_wrapper(
            campaign.create_mobile_participant_token,
        )
        self.list_commissions = async_to_raw_response_wrapper(
            campaign.list_commissions,
        )
        self.list_leaderboard = async_to_raw_response_wrapper(
            campaign.list_leaderboard,
        )
        self.list_participants = async_to_raw_response_wrapper(
            campaign.list_participants,
        )
        self.list_payouts = async_to_raw_response_wrapper(
            campaign.list_payouts,
        )
        self.list_referrals = async_to_raw_response_wrapper(
            campaign.list_referrals,
        )
        self.retrieve_analytics = async_to_raw_response_wrapper(
            campaign.retrieve_analytics,
        )

    @cached_property
    def participant(self) -> AsyncParticipantResourceWithRawResponse:
        return AsyncParticipantResourceWithRawResponse(self._campaign.participant)

    @cached_property
    def reward(self) -> AsyncRewardResourceWithRawResponse:
        """Participant reward retrieval and manual reward operations."""
        return AsyncRewardResourceWithRawResponse(self._campaign.reward)

    @cached_property
    def commission(self) -> AsyncCommissionResourceWithRawResponse:
        """Affiliate transaction, commission, and payout operations."""
        return AsyncCommissionResourceWithRawResponse(self._campaign.commission)


class CampaignResourceWithStreamingResponse:
    def __init__(self, campaign: CampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = to_streamed_response_wrapper(
            campaign.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            campaign.list,
        )
        self.create_mobile_participant_token = to_streamed_response_wrapper(
            campaign.create_mobile_participant_token,
        )
        self.list_commissions = to_streamed_response_wrapper(
            campaign.list_commissions,
        )
        self.list_leaderboard = to_streamed_response_wrapper(
            campaign.list_leaderboard,
        )
        self.list_participants = to_streamed_response_wrapper(
            campaign.list_participants,
        )
        self.list_payouts = to_streamed_response_wrapper(
            campaign.list_payouts,
        )
        self.list_referrals = to_streamed_response_wrapper(
            campaign.list_referrals,
        )
        self.retrieve_analytics = to_streamed_response_wrapper(
            campaign.retrieve_analytics,
        )

    @cached_property
    def participant(self) -> ParticipantResourceWithStreamingResponse:
        return ParticipantResourceWithStreamingResponse(self._campaign.participant)

    @cached_property
    def reward(self) -> RewardResourceWithStreamingResponse:
        """Participant reward retrieval and manual reward operations."""
        return RewardResourceWithStreamingResponse(self._campaign.reward)

    @cached_property
    def commission(self) -> CommissionResourceWithStreamingResponse:
        """Affiliate transaction, commission, and payout operations."""
        return CommissionResourceWithStreamingResponse(self._campaign.commission)


class AsyncCampaignResourceWithStreamingResponse:
    def __init__(self, campaign: AsyncCampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = async_to_streamed_response_wrapper(
            campaign.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            campaign.list,
        )
        self.create_mobile_participant_token = async_to_streamed_response_wrapper(
            campaign.create_mobile_participant_token,
        )
        self.list_commissions = async_to_streamed_response_wrapper(
            campaign.list_commissions,
        )
        self.list_leaderboard = async_to_streamed_response_wrapper(
            campaign.list_leaderboard,
        )
        self.list_participants = async_to_streamed_response_wrapper(
            campaign.list_participants,
        )
        self.list_payouts = async_to_streamed_response_wrapper(
            campaign.list_payouts,
        )
        self.list_referrals = async_to_streamed_response_wrapper(
            campaign.list_referrals,
        )
        self.retrieve_analytics = async_to_streamed_response_wrapper(
            campaign.retrieve_analytics,
        )

    @cached_property
    def participant(self) -> AsyncParticipantResourceWithStreamingResponse:
        return AsyncParticipantResourceWithStreamingResponse(self._campaign.participant)

    @cached_property
    def reward(self) -> AsyncRewardResourceWithStreamingResponse:
        """Participant reward retrieval and manual reward operations."""
        return AsyncRewardResourceWithStreamingResponse(self._campaign.reward)

    @cached_property
    def commission(self) -> AsyncCommissionResourceWithStreamingResponse:
        """Affiliate transaction, commission, and payout operations."""
        return AsyncCommissionResourceWithStreamingResponse(self._campaign.commission)
