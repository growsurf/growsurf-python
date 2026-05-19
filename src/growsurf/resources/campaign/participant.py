# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterable, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.campaign import (
    ReferralStatus,
    participant_add_params,
    participant_update_params,
    participant_list_payouts_params,
    participant_list_rewards_params,
    participant_send_invites_params,
    participant_list_referrals_params,
    participant_list_commissions_params,
    participant_record_transaction_params,
)
from ...types.referral_list import ReferralList
from ...types.campaign.participant import Participant
from ...types.participant_payout_list import ParticipantPayoutList
from ...types.campaign.referral_status import ReferralStatus
from ...types.participant_commission_list import ParticipantCommissionList
from ...types.campaign.participant_delete_response import ParticipantDeleteResponse
from ...types.campaign.participant_list_rewards_response import ParticipantListRewardsResponse
from ...types.campaign.participant_send_invites_response import ParticipantSendInvitesResponse
from ...types.campaign.participant_trigger_referral_response import ParticipantTriggerReferralResponse
from ...types.campaign.participant_record_transaction_response import ParticipantRecordTransactionResponse

__all__ = ["ParticipantResource", "AsyncParticipantResource"]


class ParticipantResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParticipantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return ParticipantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParticipantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return ParticipantResourceWithStreamingResponse(self)

    def retrieve(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Participant:
        """
        Retrieves a single participant by GrowSurf participant ID or email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Participant,
        )

    def update(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        referral_status: Literal["CREDIT_PENDING", "CREDIT_AWARDED", "CREDIT_EXPIRED"] | Omit = omit,
        referred_by: str | Omit = omit,
        unsubscribed: bool | Omit = omit,
        vanity_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Participant:
        """
        Updates a participant by GrowSurf participant ID or email address.

        Args:
          metadata: Shallow custom metadata object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._post(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "referral_status": referral_status,
                    "referred_by": referred_by,
                    "unsubscribed": unsubscribed,
                    "vanity_keys": vanity_keys,
                },
                participant_update_params.ParticipantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Participant,
        )

    def delete(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantDeleteResponse:
        """
        Removes a participant by GrowSurf participant ID or email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._delete(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantDeleteResponse,
        )

    def add(
        self,
        id: str,
        *,
        email: str,
        fingerprint: str | Omit = omit,
        first_name: str | Omit = omit,
        ip_address: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        referral_status: Literal["CREDIT_PENDING", "CREDIT_AWARDED"] | Omit = omit,
        referred_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Participant:
        """Adds a new participant to the program.

        If the email already exists, the existing
        participant is returned.

        Args:
          metadata: Shallow custom metadata object.

          referred_by: Referrer participant ID or email address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/participant", id=id),
            body=maybe_transform(
                {
                    "email": email,
                    "fingerprint": fingerprint,
                    "first_name": first_name,
                    "ip_address": ip_address,
                    "last_name": last_name,
                    "metadata": metadata,
                    "referral_status": referral_status,
                    "referred_by": referred_by,
                },
                participant_add_params.ParticipantAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Participant,
        )

    def list_commissions(
        self,
        participant_id_or_email: str,
        *,
        id: str,
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
        Retrieves a paged list of commissions earned by a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/commissions",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_commissions_params.ParticipantListCommissionsParams,
                ),
            ),
            cast_to=ParticipantCommissionList,
        )

    def list_payouts(
        self,
        participant_id_or_email: str,
        *,
        id: str,
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
        Retrieves a paged list of payouts that belong to a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/payouts",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_payouts_params.ParticipantListPayoutsParams,
                ),
            ),
            cast_to=ParticipantPayoutList,
        )

    def list_referrals(
        self,
        participant_id_or_email: str,
        *,
        id: str,
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
        Retrieves referrals and email invites made by a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/referrals",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_referrals_params.ParticipantListReferralsParams,
                ),
            ),
            cast_to=ReferralList,
        )

    def list_rewards(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantListRewardsResponse:
        """
        Retrieves a paged list of rewards earned by a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/rewards",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_rewards_params.ParticipantListRewardsParams,
                ),
            ),
            cast_to=ParticipantListRewardsResponse,
        )

    def record_transaction(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        currency: str,
        gross_amount: int,
        amount_cash_net: int | Omit = omit,
        amount_paid: int | Omit = omit,
        charge_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        invoice_id: str | Omit = omit,
        invoice_subtotal_excluding_tax: int | Omit = omit,
        invoice_total: int | Omit = omit,
        invoice_total_excluding_tax: int | Omit = omit,
        net_amount: int | Omit = omit,
        order_id: str | Omit = omit,
        paid_at: int | Omit = omit,
        payment_id: str | Omit = omit,
        payment_intent_id: str | Omit = omit,
        subscription_id: str | Omit = omit,
        tax_amount: int | Omit = omit,
        total_tax_amount: int | Omit = omit,
        total_tax_amounts: Iterable[Dict[str, object]] | Omit = omit,
        total_taxes: Iterable[Dict[str, object]] | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantRecordTransactionResponse:
        """
        Records a sale made by a referred customer and generates affiliate commissions
        for their referrer when applicable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return cast(
            ParticipantRecordTransactionResponse,
            self._post(
                path_template(
                    "/campaign/{id}/participant/{participant_id_or_email}/transaction",
                    id=id,
                    participant_id_or_email=participant_id_or_email,
                ),
                body=maybe_transform(
                    {
                        "currency": currency,
                        "gross_amount": gross_amount,
                        "amount_cash_net": amount_cash_net,
                        "amount_paid": amount_paid,
                        "charge_id": charge_id,
                        "customer_id": customer_id,
                        "description": description,
                        "external_id": external_id,
                        "invoice_id": invoice_id,
                        "invoice_subtotal_excluding_tax": invoice_subtotal_excluding_tax,
                        "invoice_total": invoice_total,
                        "invoice_total_excluding_tax": invoice_total_excluding_tax,
                        "net_amount": net_amount,
                        "order_id": order_id,
                        "paid_at": paid_at,
                        "payment_id": payment_id,
                        "payment_intent_id": payment_intent_id,
                        "subscription_id": subscription_id,
                        "tax_amount": tax_amount,
                        "total_tax_amount": total_tax_amount,
                        "total_tax_amounts": total_tax_amounts,
                        "total_taxes": total_taxes,
                        "transaction_id": transaction_id,
                    },
                    participant_record_transaction_params.ParticipantRecordTransactionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParticipantRecordTransactionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def send_invites(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        email_addresses: SequenceNotStr[str],
        message_text: str,
        subject_text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantSendInvitesResponse:
        """
        Sends email invites on behalf of a participant to a list of email addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._post(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/invites",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=maybe_transform(
                {
                    "email_addresses": email_addresses,
                    "message_text": message_text,
                    "subject_text": subject_text,
                },
                participant_send_invites_params.ParticipantSendInvitesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantSendInvitesResponse,
        )

    def trigger_referral(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantTriggerReferralResponse:
        """
        Triggers referral credit for an existing referred participant by GrowSurf
        participant ID or email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return self._post(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/ref",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantTriggerReferralResponse,
        )


class AsyncParticipantResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParticipantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParticipantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParticipantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncParticipantResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Participant:
        """
        Retrieves a single participant by GrowSurf participant ID or email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Participant,
        )

    async def update(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        referral_status: Literal["CREDIT_PENDING", "CREDIT_AWARDED", "CREDIT_EXPIRED"] | Omit = omit,
        referred_by: str | Omit = omit,
        unsubscribed: bool | Omit = omit,
        vanity_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Participant:
        """
        Updates a participant by GrowSurf participant ID or email address.

        Args:
          metadata: Shallow custom metadata object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._post(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "referral_status": referral_status,
                    "referred_by": referred_by,
                    "unsubscribed": unsubscribed,
                    "vanity_keys": vanity_keys,
                },
                participant_update_params.ParticipantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Participant,
        )

    async def delete(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantDeleteResponse:
        """
        Removes a participant by GrowSurf participant ID or email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._delete(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantDeleteResponse,
        )

    async def add(
        self,
        id: str,
        *,
        email: str,
        fingerprint: str | Omit = omit,
        first_name: str | Omit = omit,
        ip_address: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        referral_status: Literal["CREDIT_PENDING", "CREDIT_AWARDED"] | Omit = omit,
        referred_by: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Participant:
        """Adds a new participant to the program.

        If the email already exists, the existing
        participant is returned.

        Args:
          metadata: Shallow custom metadata object.

          referred_by: Referrer participant ID or email address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/participant", id=id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "fingerprint": fingerprint,
                    "first_name": first_name,
                    "ip_address": ip_address,
                    "last_name": last_name,
                    "metadata": metadata,
                    "referral_status": referral_status,
                    "referred_by": referred_by,
                },
                participant_add_params.ParticipantAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Participant,
        )

    async def list_commissions(
        self,
        participant_id_or_email: str,
        *,
        id: str,
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
        Retrieves a paged list of commissions earned by a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/commissions",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_commissions_params.ParticipantListCommissionsParams,
                ),
            ),
            cast_to=ParticipantCommissionList,
        )

    async def list_payouts(
        self,
        participant_id_or_email: str,
        *,
        id: str,
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
        Retrieves a paged list of payouts that belong to a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/payouts",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_payouts_params.ParticipantListPayoutsParams,
                ),
            ),
            cast_to=ParticipantPayoutList,
        )

    async def list_referrals(
        self,
        participant_id_or_email: str,
        *,
        id: str,
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
        Retrieves referrals and email invites made by a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/referrals",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_referrals_params.ParticipantListReferralsParams,
                ),
            ),
            cast_to=ReferralList,
        )

    async def list_rewards(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        limit: int | Omit = omit,
        next_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantListRewardsResponse:
        """
        Retrieves a paged list of rewards earned by a participant.

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
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._get(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/rewards",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
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
                    participant_list_rewards_params.ParticipantListRewardsParams,
                ),
            ),
            cast_to=ParticipantListRewardsResponse,
        )

    async def record_transaction(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        currency: str,
        gross_amount: int,
        amount_cash_net: int | Omit = omit,
        amount_paid: int | Omit = omit,
        charge_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        invoice_id: str | Omit = omit,
        invoice_subtotal_excluding_tax: int | Omit = omit,
        invoice_total: int | Omit = omit,
        invoice_total_excluding_tax: int | Omit = omit,
        net_amount: int | Omit = omit,
        order_id: str | Omit = omit,
        paid_at: int | Omit = omit,
        payment_id: str | Omit = omit,
        payment_intent_id: str | Omit = omit,
        subscription_id: str | Omit = omit,
        tax_amount: int | Omit = omit,
        total_tax_amount: int | Omit = omit,
        total_tax_amounts: Iterable[Dict[str, object]] | Omit = omit,
        total_taxes: Iterable[Dict[str, object]] | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantRecordTransactionResponse:
        """
        Records a sale made by a referred customer and generates affiliate commissions
        for their referrer when applicable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return cast(
            ParticipantRecordTransactionResponse,
            await self._post(
                path_template(
                    "/campaign/{id}/participant/{participant_id_or_email}/transaction",
                    id=id,
                    participant_id_or_email=participant_id_or_email,
                ),
                body=await async_maybe_transform(
                    {
                        "currency": currency,
                        "gross_amount": gross_amount,
                        "amount_cash_net": amount_cash_net,
                        "amount_paid": amount_paid,
                        "charge_id": charge_id,
                        "customer_id": customer_id,
                        "description": description,
                        "external_id": external_id,
                        "invoice_id": invoice_id,
                        "invoice_subtotal_excluding_tax": invoice_subtotal_excluding_tax,
                        "invoice_total": invoice_total,
                        "invoice_total_excluding_tax": invoice_total_excluding_tax,
                        "net_amount": net_amount,
                        "order_id": order_id,
                        "paid_at": paid_at,
                        "payment_id": payment_id,
                        "payment_intent_id": payment_intent_id,
                        "subscription_id": subscription_id,
                        "tax_amount": tax_amount,
                        "total_tax_amount": total_tax_amount,
                        "total_tax_amounts": total_tax_amounts,
                        "total_taxes": total_taxes,
                        "transaction_id": transaction_id,
                    },
                    participant_record_transaction_params.ParticipantRecordTransactionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParticipantRecordTransactionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def send_invites(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        email_addresses: SequenceNotStr[str],
        message_text: str,
        subject_text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantSendInvitesResponse:
        """
        Sends email invites on behalf of a participant to a list of email addresses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._post(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/invites",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=await async_maybe_transform(
                {
                    "email_addresses": email_addresses,
                    "message_text": message_text,
                    "subject_text": subject_text,
                },
                participant_send_invites_params.ParticipantSendInvitesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantSendInvitesResponse,
        )

    async def trigger_referral(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantTriggerReferralResponse:
        """
        Triggers referral credit for an existing referred participant by GrowSurf
        participant ID or email address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id_or_email:
            raise ValueError(
                f"Expected a non-empty value for `participant_id_or_email` but received {participant_id_or_email!r}"
            )
        return await self._post(
            path_template(
                "/campaign/{id}/participant/{participant_id_or_email}/ref",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantTriggerReferralResponse,
        )


class ParticipantResourceWithRawResponse:
    def __init__(self, participant: ParticipantResource) -> None:
        self._participant = participant

        self.retrieve = to_raw_response_wrapper(
            participant.retrieve,
        )
        self.update = to_raw_response_wrapper(
            participant.update,
        )
        self.delete = to_raw_response_wrapper(
            participant.delete,
        )
        self.add = to_raw_response_wrapper(
            participant.add,
        )
        self.list_commissions = to_raw_response_wrapper(
            participant.list_commissions,
        )
        self.list_payouts = to_raw_response_wrapper(
            participant.list_payouts,
        )
        self.list_referrals = to_raw_response_wrapper(
            participant.list_referrals,
        )
        self.list_rewards = to_raw_response_wrapper(
            participant.list_rewards,
        )
        self.record_transaction = to_raw_response_wrapper(
            participant.record_transaction,
        )
        self.send_invites = to_raw_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = to_raw_response_wrapper(
            participant.trigger_referral,
        )


class AsyncParticipantResourceWithRawResponse:
    def __init__(self, participant: AsyncParticipantResource) -> None:
        self._participant = participant

        self.retrieve = async_to_raw_response_wrapper(
            participant.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            participant.update,
        )
        self.delete = async_to_raw_response_wrapper(
            participant.delete,
        )
        self.add = async_to_raw_response_wrapper(
            participant.add,
        )
        self.list_commissions = async_to_raw_response_wrapper(
            participant.list_commissions,
        )
        self.list_payouts = async_to_raw_response_wrapper(
            participant.list_payouts,
        )
        self.list_referrals = async_to_raw_response_wrapper(
            participant.list_referrals,
        )
        self.list_rewards = async_to_raw_response_wrapper(
            participant.list_rewards,
        )
        self.record_transaction = async_to_raw_response_wrapper(
            participant.record_transaction,
        )
        self.send_invites = async_to_raw_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = async_to_raw_response_wrapper(
            participant.trigger_referral,
        )


class ParticipantResourceWithStreamingResponse:
    def __init__(self, participant: ParticipantResource) -> None:
        self._participant = participant

        self.retrieve = to_streamed_response_wrapper(
            participant.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            participant.update,
        )
        self.delete = to_streamed_response_wrapper(
            participant.delete,
        )
        self.add = to_streamed_response_wrapper(
            participant.add,
        )
        self.list_commissions = to_streamed_response_wrapper(
            participant.list_commissions,
        )
        self.list_payouts = to_streamed_response_wrapper(
            participant.list_payouts,
        )
        self.list_referrals = to_streamed_response_wrapper(
            participant.list_referrals,
        )
        self.list_rewards = to_streamed_response_wrapper(
            participant.list_rewards,
        )
        self.record_transaction = to_streamed_response_wrapper(
            participant.record_transaction,
        )
        self.send_invites = to_streamed_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = to_streamed_response_wrapper(
            participant.trigger_referral,
        )


class AsyncParticipantResourceWithStreamingResponse:
    def __init__(self, participant: AsyncParticipantResource) -> None:
        self._participant = participant

        self.retrieve = async_to_streamed_response_wrapper(
            participant.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            participant.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            participant.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            participant.add,
        )
        self.list_commissions = async_to_streamed_response_wrapper(
            participant.list_commissions,
        )
        self.list_payouts = async_to_streamed_response_wrapper(
            participant.list_payouts,
        )
        self.list_referrals = async_to_streamed_response_wrapper(
            participant.list_referrals,
        )
        self.list_rewards = async_to_streamed_response_wrapper(
            participant.list_rewards,
        )
        self.record_transaction = async_to_streamed_response_wrapper(
            participant.record_transaction,
        )
        self.send_invites = async_to_streamed_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = async_to_streamed_response_wrapper(
            participant.trigger_referral,
        )
