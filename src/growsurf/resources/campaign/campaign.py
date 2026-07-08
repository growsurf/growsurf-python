# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from .design import (
    DesignResource,
    AsyncDesignResource,
    DesignResourceWithRawResponse,
    AsyncDesignResourceWithRawResponse,
    DesignResourceWithStreamingResponse,
    AsyncDesignResourceWithStreamingResponse,
)
from .emails import (
    EmailsResource,
    AsyncEmailsResource,
    EmailsResourceWithRawResponse,
    AsyncEmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
    AsyncEmailsResourceWithStreamingResponse,
)
from .reward import (
    RewardResource,
    AsyncRewardResource,
    RewardResourceWithRawResponse,
    AsyncRewardResourceWithRawResponse,
    RewardResourceWithStreamingResponse,
    AsyncRewardResourceWithStreamingResponse,
)
from ...types import (
    campaign_create_params,
    campaign_update_params,
    campaign_list_payouts_params,
    campaign_list_referrals_params,
    campaign_list_commissions_params,
    campaign_list_leaderboard_params,
    campaign_list_participants_params,
    campaign_retrieve_analytics_params,
    campaign_create_mobile_participant_token_params,
)
from .options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from .rewards import (
    RewardsResource,
    AsyncRewardsResource,
    RewardsResourceWithRawResponse,
    AsyncRewardsResourceWithRawResponse,
    RewardsResourceWithStreamingResponse,
    AsyncRewardsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
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
from .installation import (
    InstallationResource,
    AsyncInstallationResource,
    InstallationResourceWithRawResponse,
    AsyncInstallationResourceWithRawResponse,
    InstallationResourceWithStreamingResponse,
    AsyncInstallationResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.campaign import ReferralStatus, reward_create_params
from ...types.referral_list import ReferralList
from ...types.participant_list import ParticipantList
from ...types.campaign.campaign import Campaign
from ...types.campaign_list_response import CampaignListResponse
from ...types.participant_payout_list import ParticipantPayoutList
from ...types.campaign.referral_status import ReferralStatus
from ...types.participant_commission_list import ParticipantCommissionList
from ...types.referral_flow_screenshots_response import ReferralFlowScreenshotsResponse
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
    def rewards(self) -> RewardsResource:
        """Campaign reward (`CampaignReward`) configuration operations."""
        return RewardsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Campaign webhook (`Webhook`) configuration operations."""
        return WebhooksResource(self._client)

    @cached_property
    def design(self) -> DesignResource:
        """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""
        return DesignResource(self._client)

    @cached_property
    def emails(self) -> EmailsResource:
        """Campaign emails (`CampaignEmails`) configuration — the Program Editor's Emails tab."""
        return EmailsResource(self._client)

    @cached_property
    def options(self) -> OptionsResource:
        """Campaign options (`CampaignOptions`) — the Program Editor's Options tab."""
        return OptionsResource(self._client)

    @cached_property
    def installation(self) -> InstallationResource:
        """Campaign installation (`CampaignInstallation`) — the Program Editor's Installation tab."""
        return InstallationResource(self._client)

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

    def create(
        self,
        *,
        type: Literal["REFERRAL", "AFFILIATE"],
        company_logo_image_url: str | Omit = omit,
        company_name: str | Omit = omit,
        currency_iso: str | Omit = omit,
        name: str | Omit = omit,
        rewards: Iterable[reward_create_params.RewardCreateParams] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Creates a new program pre-populated with type-appropriate defaults, plus any
        optional inline rewards. The new program is created in `DRAFT` status and owned
        by the API key's account. Requires a verified account email.

        Args:
          type: The program type. Immutable after creation.

          currency_iso: ISO 4217 currency code. Defaults to USD. Chosen when the program is
              created and immutable afterward — it cannot be changed on update.

          name: The program name. Defaults to "Untitled Program".

          rewards: Optional inline rewards to create with the program.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/campaigns",
            body=maybe_transform(
                {
                    "type": type,
                    "company_logo_image_url": company_logo_image_url,
                    "company_name": company_name,
                    "currency_iso": currency_iso,
                    "name": name,
                    "rewards": rewards,
                },
                campaign_create_params.CampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

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

    def update(
        self,
        id: str,
        *,
        company_logo_image_url: str | Omit = omit,
        company_name: str | Omit = omit,
        name: str | Omit = omit,
        status: Literal["IN_PROGRESS", "COMPLETE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Updates a program's identity and lifecycle. Only the fields you send are
        changed. `type`, `urlId`, and `currencyISO` are immutable. Editor-tab
        configuration (design, emails, options, installation) is edited via the
        dedicated config sub-resources, not here. The program cannot be deleted via
        this endpoint.

        Args:
          status: The requested program status. `IN_PROGRESS` publishes or resumes the program;
              `COMPLETE` ends it. Any other value returns a `400`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/campaign/{id}", id=id),
            body=maybe_transform(
                {
                    "company_logo_image_url": company_logo_image_url,
                    "company_name": company_name,
                    "name": name,
                    "status": status,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
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

    def clone(
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
        Clones an existing program into a new `DRAFT` program. Integrations and
        credentials are not copied; active rewards are cloned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/clone", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

    def get_referral_flow_screenshots(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralFlowScreenshotsResponse:
        """
        Captures two preview screenshots for the program: the authenticated referrer
        view and the referred-friend view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/referral-flow-screenshots", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferralFlowScreenshotsResponse,
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
              for mobile participant creation and mobile participant token flows. The official
              mobile SDKs generate this as a lowercase UUID.

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
        include: str | Omit = omit,
        interval: Literal["day", "week", "month", "total"] | Omit = omit,
        start_date: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRetrieveAnalyticsResponse:
        """
        Retrieves analytics for a program. Pass ``interval`` to also get a time-series
        (``series``) alongside the totals, and ``include`` to add previous-period
        totals, status breakdowns, or derived rates — useful for detecting trends over
        time.

        Args:
          days: Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825.

          end_date: End date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          include: Comma-separated list of optional enrichments (opt-in to keep the default
              response lean). Any of `previousPeriod` (totals for the equal-length window
              immediately before the requested one), `statusCounts` (reward and, for affiliate
              programs, affiliate/commission/payout status breakdowns), and `rates` (derived
              referral rates).

          interval: When set to `day`, `week`, or `month`, the response also includes a `series`
              array with per-period totals. Defaults to `total` (no series).

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
                        "include": include,
                        "interval": interval,
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
    def rewards(self) -> AsyncRewardsResource:
        """Campaign reward (`CampaignReward`) configuration operations."""
        return AsyncRewardsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Campaign webhook (`Webhook`) configuration operations."""
        return AsyncWebhooksResource(self._client)

    @cached_property
    def design(self) -> AsyncDesignResource:
        """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""
        return AsyncDesignResource(self._client)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        """Campaign emails (`CampaignEmails`) configuration — the Program Editor's Emails tab."""
        return AsyncEmailsResource(self._client)

    @cached_property
    def options(self) -> AsyncOptionsResource:
        """Campaign options (`CampaignOptions`) — the Program Editor's Options tab."""
        return AsyncOptionsResource(self._client)

    @cached_property
    def installation(self) -> AsyncInstallationResource:
        """Campaign installation (`CampaignInstallation`) — the Program Editor's Installation tab."""
        return AsyncInstallationResource(self._client)

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

    async def create(
        self,
        *,
        type: Literal["REFERRAL", "AFFILIATE"],
        company_logo_image_url: str | Omit = omit,
        company_name: str | Omit = omit,
        currency_iso: str | Omit = omit,
        name: str | Omit = omit,
        rewards: Iterable[reward_create_params.RewardCreateParams] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Creates a new program pre-populated with type-appropriate defaults, plus any
        optional inline rewards. The new program is created in `DRAFT` status and owned
        by the API key's account. Requires a verified account email.

        Args:
          type: The program type. Immutable after creation.

          currency_iso: ISO 4217 currency code. Defaults to USD. Chosen when the program is
              created and immutable afterward — it cannot be changed on update.

          name: The program name. Defaults to "Untitled Program".

          rewards: Optional inline rewards to create with the program.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/campaigns",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "company_logo_image_url": company_logo_image_url,
                    "company_name": company_name,
                    "currency_iso": currency_iso,
                    "name": name,
                    "rewards": rewards,
                },
                campaign_create_params.CampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

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

    async def update(
        self,
        id: str,
        *,
        company_logo_image_url: str | Omit = omit,
        company_name: str | Omit = omit,
        name: str | Omit = omit,
        status: Literal["IN_PROGRESS", "COMPLETE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Updates a program's identity and lifecycle. Only the fields you send are
        changed. `type`, `urlId`, and `currencyISO` are immutable. Editor-tab
        configuration (design, emails, options, installation) is edited via the
        dedicated config sub-resources, not here. The program cannot be deleted via
        this endpoint.

        Args:
          status: The requested program status. `IN_PROGRESS` publishes or resumes the program;
              `COMPLETE` ends it. Any other value returns a `400`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/campaign/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "company_logo_image_url": company_logo_image_url,
                    "company_name": company_name,
                    "name": name,
                    "status": status,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
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

    async def clone(
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
        Clones an existing program into a new `DRAFT` program. Integrations and
        credentials are not copied; active rewards are cloned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/clone", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

    async def get_referral_flow_screenshots(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralFlowScreenshotsResponse:
        """
        Captures two preview screenshots for the program: the authenticated referrer
        view and the referred-friend view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/referral-flow-screenshots", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferralFlowScreenshotsResponse,
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
              for mobile participant creation and mobile participant token flows. The official
              mobile SDKs generate this as a lowercase UUID.

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
        include: str | Omit = omit,
        interval: Literal["day", "week", "month", "total"] | Omit = omit,
        start_date: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRetrieveAnalyticsResponse:
        """
        Retrieves analytics for a program. Pass ``interval`` to also get a time-series
        (``series``) alongside the totals, and ``include`` to add previous-period
        totals, status breakdowns, or derived rates — useful for detecting trends over
        time.

        Args:
          days: Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825.

          end_date: End date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          include: Comma-separated list of optional enrichments (opt-in to keep the default
              response lean). Any of `previousPeriod` (totals for the equal-length window
              immediately before the requested one), `statusCounts` (reward and, for affiliate
              programs, affiliate/commission/payout status breakdowns), and `rates` (derived
              referral rates).

          interval: When set to `day`, `week`, or `month`, the response also includes a `series`
              array with per-period totals. Defaults to `total` (no series).

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
                        "include": include,
                        "interval": interval,
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

        self.create = to_raw_response_wrapper(
            campaign.create,
        )
        self.retrieve = to_raw_response_wrapper(
            campaign.retrieve,
        )
        self.update = to_raw_response_wrapper(
            campaign.update,
        )
        self.list = to_raw_response_wrapper(
            campaign.list,
        )
        self.clone = to_raw_response_wrapper(
            campaign.clone,
        )
        self.get_referral_flow_screenshots = to_raw_response_wrapper(
            campaign.get_referral_flow_screenshots,
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

    @cached_property
    def rewards(self) -> RewardsResourceWithRawResponse:
        """Campaign reward (`CampaignReward`) configuration operations."""
        return RewardsResourceWithRawResponse(self._campaign.rewards)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        """Campaign webhook (`Webhook`) configuration operations."""
        return WebhooksResourceWithRawResponse(self._campaign.webhooks)

    @cached_property
    def design(self) -> DesignResourceWithRawResponse:
        """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""
        return DesignResourceWithRawResponse(self._campaign.design)

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        """Campaign emails (`CampaignEmails`) configuration — the Program Editor's Emails tab."""
        return EmailsResourceWithRawResponse(self._campaign.emails)

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        """Campaign options (`CampaignOptions`) — the Program Editor's Options tab."""
        return OptionsResourceWithRawResponse(self._campaign.options)

    @cached_property
    def installation(self) -> InstallationResourceWithRawResponse:
        """Campaign installation (`CampaignInstallation`) — the Program Editor's Installation tab."""
        return InstallationResourceWithRawResponse(self._campaign.installation)


class AsyncCampaignResourceWithRawResponse:
    def __init__(self, campaign: AsyncCampaignResource) -> None:
        self._campaign = campaign

        self.create = async_to_raw_response_wrapper(
            campaign.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            campaign.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            campaign.update,
        )
        self.list = async_to_raw_response_wrapper(
            campaign.list,
        )
        self.clone = async_to_raw_response_wrapper(
            campaign.clone,
        )
        self.get_referral_flow_screenshots = async_to_raw_response_wrapper(
            campaign.get_referral_flow_screenshots,
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

    @cached_property
    def rewards(self) -> AsyncRewardsResourceWithRawResponse:
        """Campaign reward (`CampaignReward`) configuration operations."""
        return AsyncRewardsResourceWithRawResponse(self._campaign.rewards)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        """Campaign webhook (`Webhook`) configuration operations."""
        return AsyncWebhooksResourceWithRawResponse(self._campaign.webhooks)

    @cached_property
    def design(self) -> AsyncDesignResourceWithRawResponse:
        """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""
        return AsyncDesignResourceWithRawResponse(self._campaign.design)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        """Campaign emails (`CampaignEmails`) configuration — the Program Editor's Emails tab."""
        return AsyncEmailsResourceWithRawResponse(self._campaign.emails)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        """Campaign options (`CampaignOptions`) — the Program Editor's Options tab."""
        return AsyncOptionsResourceWithRawResponse(self._campaign.options)

    @cached_property
    def installation(self) -> AsyncInstallationResourceWithRawResponse:
        """Campaign installation (`CampaignInstallation`) — the Program Editor's Installation tab."""
        return AsyncInstallationResourceWithRawResponse(self._campaign.installation)


class CampaignResourceWithStreamingResponse:
    def __init__(self, campaign: CampaignResource) -> None:
        self._campaign = campaign

        self.create = to_streamed_response_wrapper(
            campaign.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            campaign.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            campaign.update,
        )
        self.list = to_streamed_response_wrapper(
            campaign.list,
        )
        self.clone = to_streamed_response_wrapper(
            campaign.clone,
        )
        self.get_referral_flow_screenshots = to_streamed_response_wrapper(
            campaign.get_referral_flow_screenshots,
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

    @cached_property
    def rewards(self) -> RewardsResourceWithStreamingResponse:
        """Campaign reward (`CampaignReward`) configuration operations."""
        return RewardsResourceWithStreamingResponse(self._campaign.rewards)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        """Campaign webhook (`Webhook`) configuration operations."""
        return WebhooksResourceWithStreamingResponse(self._campaign.webhooks)

    @cached_property
    def design(self) -> DesignResourceWithStreamingResponse:
        """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""
        return DesignResourceWithStreamingResponse(self._campaign.design)

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        """Campaign emails (`CampaignEmails`) configuration — the Program Editor's Emails tab."""
        return EmailsResourceWithStreamingResponse(self._campaign.emails)

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        """Campaign options (`CampaignOptions`) — the Program Editor's Options tab."""
        return OptionsResourceWithStreamingResponse(self._campaign.options)

    @cached_property
    def installation(self) -> InstallationResourceWithStreamingResponse:
        """Campaign installation (`CampaignInstallation`) — the Program Editor's Installation tab."""
        return InstallationResourceWithStreamingResponse(self._campaign.installation)


class AsyncCampaignResourceWithStreamingResponse:
    def __init__(self, campaign: AsyncCampaignResource) -> None:
        self._campaign = campaign

        self.create = async_to_streamed_response_wrapper(
            campaign.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            campaign.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            campaign.update,
        )
        self.list = async_to_streamed_response_wrapper(
            campaign.list,
        )
        self.clone = async_to_streamed_response_wrapper(
            campaign.clone,
        )
        self.get_referral_flow_screenshots = async_to_streamed_response_wrapper(
            campaign.get_referral_flow_screenshots,
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

    @cached_property
    def rewards(self) -> AsyncRewardsResourceWithStreamingResponse:
        """Campaign reward (`CampaignReward`) configuration operations."""
        return AsyncRewardsResourceWithStreamingResponse(self._campaign.rewards)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """Campaign webhook (`Webhook`) configuration operations."""
        return AsyncWebhooksResourceWithStreamingResponse(self._campaign.webhooks)

    @cached_property
    def design(self) -> AsyncDesignResourceWithStreamingResponse:
        """Campaign design (`CampaignDesign`) configuration — the Program Editor's Design tab."""
        return AsyncDesignResourceWithStreamingResponse(self._campaign.design)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        """Campaign emails (`CampaignEmails`) configuration — the Program Editor's Emails tab."""
        return AsyncEmailsResourceWithStreamingResponse(self._campaign.emails)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        """Campaign options (`CampaignOptions`) — the Program Editor's Options tab."""
        return AsyncOptionsResourceWithStreamingResponse(self._campaign.options)

    @cached_property
    def installation(self) -> AsyncInstallationResourceWithStreamingResponse:
        """Campaign installation (`CampaignInstallation`) — the Program Editor's Installation tab."""
        return AsyncInstallationResourceWithStreamingResponse(self._campaign.installation)
