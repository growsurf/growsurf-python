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
    participant_email_params,
    participant_update_params,
    participant_analytics_params,
    participant_bulk_delete_params,
    participant_list_payouts_params,
    participant_list_rewards_params,
    participant_send_invites_params,
    participant_list_referrals_params,
    participant_list_commissions_params,
    participant_trigger_referral_params,
    participant_list_activity_logs_params,
    participant_record_transaction_params,
    participant_refund_transaction_params,
)
from ...types.referral_list import ReferralList
from ...types.campaign.participant import Participant
from ...types.participant_payout_list import ParticipantPayoutList
from ...types.campaign.referral_status import ReferralStatus
from ...types.participant_commission_list import ParticipantCommissionList
from ...types.campaign.email_participant_response import EmailParticipantResponse
from ...types.campaign.participant_delete_response import ParticipantDeleteResponse
from ...types.campaign.participant_analytics_response import ParticipantAnalyticsResponse
from ...types.campaign.participant_bulk_delete_response import ParticipantBulkDeleteResponse
from ...types.campaign.participant_list_rewards_response import ParticipantListRewardsResponse
from ...types.campaign.participant_send_invites_response import ParticipantSendInvitesResponse
from ...types.campaign.participant_activity_logs_response import ParticipantActivityLogsResponse
from ...types.campaign.participant_trigger_referral_response import ParticipantTriggerReferralResponse
from ...types.campaign.participant_record_transaction_response import ParticipantRecordTransactionResponse
from ...types.campaign.participant_refund_transaction_response import ParticipantRefundTransactionResponse

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
        notes: str | Omit = omit,
        paypal_email: str | Omit = omit,
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

          notes: Freeform internal notes about the participant (internal only, never exposed to
              participants).

          paypal_email: The participant's PayPal email address, used for affiliate payouts.

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
                    "notes": notes,
                    "paypal_email": paypal_email,
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

    def bulk_delete(
        self,
        id: str,
        *,
        participants: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantBulkDeleteResponse:
        """Deletes a list of participants from a program in one request.

        Each entry in
        `participants` is a GrowSurf participant ID or an email address (mixed lists
        are allowed). Up to `200` entries per request — chunk larger lists across
        multiple calls. The response reports a per-row `status` for every submitted
        entry, so a `200` can include rows that were `NOT_FOUND` or failed. Deletion
        is permanent and removes the participants' referrals, rewards, commissions,
        and payout records.

        Args:
          participants: GrowSurf participant IDs and/or email addresses to delete. Mixed entries are
              allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/participants/bulk-delete", id=id),
            body=maybe_transform(
                {"participants": participants}, participant_bulk_delete_params.ParticipantBulkDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantBulkDeleteResponse,
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
        mobile_instance_id: str | Omit = omit,
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

          mobile_instance_id: Optional app-install scoped identifier for native mobile anti-fraud. Recommended
              for mobile participant creation and mobile participant token flows. The official
              mobile SDKs generate this as a lowercase UUID.

          referral_status: The referral credit status. Only meaningful when `referred_by` resolves to a
              referrer. When omitted it is derived from the program's referral trigger
              (`CREDIT_AWARDED`, `CREDIT_PENDING`, or `CREDIT_EXPIRED`); left unset when no referrer
              resolves.

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
                    "mobile_instance_id": mobile_instance_id,
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

        At least one transaction identifier is required: one of ``external_id``,
        ``transaction_id``, ``order_id``, ``payment_id``, ``invoice_id``,
        ``payment_intent_id``, or ``charge_id``. ``customer_id`` and ``subscription_id``
        do not count, since they identify the customer or subscription rather than the
        specific transaction. Without an identifier, resending the same sale creates a
        duplicate commission and double-pays the referrer; the server rejects such
        requests with HTTP 400.

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

    def refund_transaction(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        amendment_type: Literal["REFUND", "CHARGEBACK"] | Omit = omit,
        amount: int | Omit = omit,
        amount_refunded: int | Omit = omit,
        charge_id: str | Omit = omit,
        currency: str | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        invoice_id: str | Omit = omit,
        order_id: str | Omit = omit,
        payment_id: str | Omit = omit,
        payment_intent_id: str | Omit = omit,
        refund_amount: int | Omit = omit,
        refund_id: str | Omit = omit,
        refund_status: str | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantRefundTransactionResponse:
        """
        Records an amendment (refund, partial refund, refund cancellation, or
        chargeback) against a previously recorded transaction and reverses or adjusts
        the referrer's commission. The inverse of Record Affiliate Transaction.
        Commissions already paid out are not clawed back; the amendment is recorded for
        tax reporting only.

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
                "/campaign/{id}/participant/{participant_id_or_email}/transaction/refund",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=maybe_transform(
                {
                    "amendment_type": amendment_type,
                    "amount": amount,
                    "amount_refunded": amount_refunded,
                    "charge_id": charge_id,
                    "currency": currency,
                    "description": description,
                    "external_id": external_id,
                    "invoice_id": invoice_id,
                    "order_id": order_id,
                    "payment_id": payment_id,
                    "payment_intent_id": payment_intent_id,
                    "refund_amount": refund_amount,
                    "refund_id": refund_id,
                    "refund_status": refund_status,
                    "transaction_id": transaction_id,
                },
                participant_refund_transaction_params.ParticipantRefundTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRefundTransactionResponse,
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

        Sending invites via the API requires a verified custom email domain on the
        program; the request fails until one is verified.

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
        delay_in_days: int | Omit = omit,
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
          delay_in_days: Number of whole days to hold referral credit before it is awarded. Useful for
              honoring a refund window before crediting a referrer. Omit this field to award
              credit immediately. The credit is awarded automatically once the delay elapses,
              and can be cancelled before then with the Cancel delayed referral trigger
              request.

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
            body=maybe_transform(
                {"delay_in_days": delay_in_days}, participant_trigger_referral_params.ParticipantTriggerReferralParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantTriggerReferralResponse,
        )

    def cancel_delayed_referral(
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
        Cancels a pending delayed referral trigger for a participant by GrowSurf
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
        return self._delete(
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

    def email(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        email_type: str | Omit = omit,
        body: str | Omit = omit,
        preheader: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailParticipantResponse:
        """
        Sends an email to a participant. Provide EITHER ``email_type`` to trigger one of
        the program's configured email templates, OR ``subject`` + ``body`` for a
        free-form email. Free-form emails are sent with the same compliance handling
        (company name, postal address, and an unsubscribe link are added automatically,
        and unsubscribed participants are suppressed). Sending requires the team to be
        verified by GrowSurf. Requires a verified custom email domain on the
        program (set up in Campaign Editor > 3. Emails > Email Settings). Returns `400`
        until one is verified. The email is accepted for delivery.

        Args:
          email_type: The program email template to trigger (template mode). The valid values depend on
              the program type; the template's `isEnabled` setting only controls automatic sends.
              Referral programs: `welcomeNonReferred`, `referralLinkViewedFirstTime`, `referralLinkUsed`,
              `referredSignup`, `welcomeReferred`, `goalAchieved`, `campaignEndedWinners`,
              `campaignEndedNonWinners`, `progressUpdateMonthly`. Affiliate programs:
              `welcomeNonReferred`, `referralLinkViewedFirstTime`, `referredSignup`,
              `commissionGenerated`, `commissionAdjusted`, `payoutPending`, `payoutSentSuccess`,
              `progressUpdateMonthly`. System/transactional types (login link, PayPal confirmation,
              tax) and the invite email cannot be sent.

          body: HTML body for a free-form email. You can personalize it with dynamic text, inserting `{{...}}` tokens like `{{firstName}}` or `{{shareUrl}}`. See [Guide to using dynamic text in GrowSurf emails](https://support.growsurf.com/article/213-guide-to-using-dynamic-text-in-growsurf-emails).

          preheader: Optional preheader text for a free-form email.

          subject: Subject line for a free-form email. Supports dynamic text (`{{...}}` tokens), the same as the body.

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
                "/campaign/{id}/participant/{participant_id_or_email}/email",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=maybe_transform(
                {
                    "email_type": email_type,
                    "body": body,
                    "preheader": preheader,
                    "subject": subject,
                },
                participant_email_params.ParticipantEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailParticipantResponse,
        )

    def list_activity_logs(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantActivityLogsResponse:
        """
        Returns a participant's activity logs, most recent first (offset/limit
        paginated).

        Args:
          limit: Number of logs to return (1–100, default 20).

          offset: Number of logs to skip.

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
                "/campaign/{id}/participant/{participant_id_or_email}/activity-logs",
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
                        "offset": offset,
                    },
                    participant_list_activity_logs_params.ParticipantListActivityLogsParams,
                ),
            ),
            cast_to=ParticipantActivityLogsResponse,
        )

    def retrieve_analytics(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        days: int | Omit = omit,
        end_date: int | Omit = omit,
        include: Literal["series"] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        start_date: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantAnalyticsResponse:
        """
        Retrieves analytics for a single participant — all-time engagement counters,
        leaderboard ranks, and per-channel share counts (plus affiliate money metrics for
        affiliate programs). Useful for segmenting and re-engaging participants. Pass
        ``include=series`` to also get this participant's own activity over time.

        Args:
          days: Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825.

          end_date: End date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          include: Set to `series` to also return this participant's own activity per period.

          interval: Bucket size for the `series` (only used with `include=series`). Defaults to
              `day`.

          start_date: Start date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

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
                "/campaign/{id}/participant/{participant_id_or_email}/analytics",
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
                        "days": days,
                        "end_date": end_date,
                        "include": include,
                        "interval": interval,
                        "start_date": start_date,
                    },
                    participant_analytics_params.ParticipantAnalyticsParams,
                ),
            ),
            cast_to=ParticipantAnalyticsResponse,
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
        notes: str | Omit = omit,
        paypal_email: str | Omit = omit,
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

          notes: Freeform internal notes about the participant (internal only, never exposed to
              participants).

          paypal_email: The participant's PayPal email address, used for affiliate payouts.

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
                    "notes": notes,
                    "paypal_email": paypal_email,
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

    async def bulk_delete(
        self,
        id: str,
        *,
        participants: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantBulkDeleteResponse:
        """Deletes a list of participants from a program in one request.

        Each entry in
        `participants` is a GrowSurf participant ID or an email address (mixed lists
        are allowed). Up to `200` entries per request — chunk larger lists across
        multiple calls. The response reports a per-row `status` for every submitted
        entry, so a `200` can include rows that were `NOT_FOUND` or failed. Deletion
        is permanent and removes the participants' referrals, rewards, commissions,
        and payout records.

        Args:
          participants: GrowSurf participant IDs and/or email addresses to delete. Mixed entries are
              allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/participants/bulk-delete", id=id),
            body=await async_maybe_transform(
                {"participants": participants}, participant_bulk_delete_params.ParticipantBulkDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantBulkDeleteResponse,
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
        mobile_instance_id: str | Omit = omit,
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

          mobile_instance_id: Optional app-install scoped identifier for native mobile anti-fraud. Recommended
              for mobile participant creation and mobile participant token flows. The official
              mobile SDKs generate this as a lowercase UUID.

          referral_status: The referral credit status. Only meaningful when `referred_by` resolves to a
              referrer. When omitted it is derived from the program's referral trigger
              (`CREDIT_AWARDED`, `CREDIT_PENDING`, or `CREDIT_EXPIRED`); left unset when no referrer
              resolves.

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
                    "mobile_instance_id": mobile_instance_id,
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

        At least one transaction identifier is required: one of ``external_id``,
        ``transaction_id``, ``order_id``, ``payment_id``, ``invoice_id``,
        ``payment_intent_id``, or ``charge_id``. ``customer_id`` and ``subscription_id``
        do not count, since they identify the customer or subscription rather than the
        specific transaction. Without an identifier, resending the same sale creates a
        duplicate commission and double-pays the referrer; the server rejects such
        requests with HTTP 400.

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

    async def refund_transaction(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        amendment_type: Literal["REFUND", "CHARGEBACK"] | Omit = omit,
        amount: int | Omit = omit,
        amount_refunded: int | Omit = omit,
        charge_id: str | Omit = omit,
        currency: str | Omit = omit,
        description: str | Omit = omit,
        external_id: str | Omit = omit,
        invoice_id: str | Omit = omit,
        order_id: str | Omit = omit,
        payment_id: str | Omit = omit,
        payment_intent_id: str | Omit = omit,
        refund_amount: int | Omit = omit,
        refund_id: str | Omit = omit,
        refund_status: str | Omit = omit,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantRefundTransactionResponse:
        """
        Records an amendment (refund, partial refund, refund cancellation, or
        chargeback) against a previously recorded transaction and reverses or adjusts
        the referrer's commission. The inverse of Record Affiliate Transaction.
        Commissions already paid out are not clawed back; the amendment is recorded for
        tax reporting only.

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
                "/campaign/{id}/participant/{participant_id_or_email}/transaction/refund",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=await async_maybe_transform(
                {
                    "amendment_type": amendment_type,
                    "amount": amount,
                    "amount_refunded": amount_refunded,
                    "charge_id": charge_id,
                    "currency": currency,
                    "description": description,
                    "external_id": external_id,
                    "invoice_id": invoice_id,
                    "order_id": order_id,
                    "payment_id": payment_id,
                    "payment_intent_id": payment_intent_id,
                    "refund_amount": refund_amount,
                    "refund_id": refund_id,
                    "refund_status": refund_status,
                    "transaction_id": transaction_id,
                },
                participant_refund_transaction_params.ParticipantRefundTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRefundTransactionResponse,
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

        Sending invites via the API requires a verified custom email domain on the
        program; the request fails until one is verified.

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
        delay_in_days: int | Omit = omit,
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
          delay_in_days: Number of whole days to hold referral credit before it is awarded. Useful for
              honoring a refund window before crediting a referrer. Omit this field to award
              credit immediately. The credit is awarded automatically once the delay elapses,
              and can be cancelled before then with the Cancel delayed referral trigger
              request.

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
            body=await async_maybe_transform(
                {"delay_in_days": delay_in_days}, participant_trigger_referral_params.ParticipantTriggerReferralParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantTriggerReferralResponse,
        )

    async def cancel_delayed_referral(
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
        Cancels a pending delayed referral trigger for a participant by GrowSurf
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
        return await self._delete(
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

    async def email(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        email_type: str | Omit = omit,
        body: str | Omit = omit,
        preheader: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailParticipantResponse:
        """
        Sends an email to a participant. Provide EITHER ``email_type`` to trigger one of
        the program's configured email templates, OR ``subject`` + ``body`` for a
        free-form email. Free-form emails are sent with the same compliance handling
        (company name, postal address, and an unsubscribe link are added automatically,
        and unsubscribed participants are suppressed). Sending requires the team to be
        verified by GrowSurf. Requires a verified custom email domain on the
        program (set up in Campaign Editor > 3. Emails > Email Settings). Returns `400`
        until one is verified. The email is accepted for delivery.

        Args:
          email_type: The program email template to trigger (template mode). The valid values depend on
              the program type; the template's `isEnabled` setting only controls automatic sends.
              Referral programs: `welcomeNonReferred`, `referralLinkViewedFirstTime`, `referralLinkUsed`,
              `referredSignup`, `welcomeReferred`, `goalAchieved`, `campaignEndedWinners`,
              `campaignEndedNonWinners`, `progressUpdateMonthly`. Affiliate programs:
              `welcomeNonReferred`, `referralLinkViewedFirstTime`, `referredSignup`,
              `commissionGenerated`, `commissionAdjusted`, `payoutPending`, `payoutSentSuccess`,
              `progressUpdateMonthly`. System/transactional types (login link, PayPal confirmation,
              tax) and the invite email cannot be sent.

          body: HTML body for a free-form email. You can personalize it with dynamic text, inserting `{{...}}` tokens like `{{firstName}}` or `{{shareUrl}}`. See [Guide to using dynamic text in GrowSurf emails](https://support.growsurf.com/article/213-guide-to-using-dynamic-text-in-growsurf-emails).

          preheader: Optional preheader text for a free-form email.

          subject: Subject line for a free-form email. Supports dynamic text (`{{...}}` tokens), the same as the body.

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
                "/campaign/{id}/participant/{participant_id_or_email}/email",
                id=id,
                participant_id_or_email=participant_id_or_email,
            ),
            body=await async_maybe_transform(
                {
                    "email_type": email_type,
                    "body": body,
                    "preheader": preheader,
                    "subject": subject,
                },
                participant_email_params.ParticipantEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailParticipantResponse,
        )

    async def list_activity_logs(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantActivityLogsResponse:
        """
        Returns a participant's activity logs, most recent first (offset/limit
        paginated).

        Args:
          limit: Number of logs to return (1–100, default 20).

          offset: Number of logs to skip.

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
                "/campaign/{id}/participant/{participant_id_or_email}/activity-logs",
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
                        "offset": offset,
                    },
                    participant_list_activity_logs_params.ParticipantListActivityLogsParams,
                ),
            ),
            cast_to=ParticipantActivityLogsResponse,
        )

    async def retrieve_analytics(
        self,
        participant_id_or_email: str,
        *,
        id: str,
        days: int | Omit = omit,
        end_date: int | Omit = omit,
        include: Literal["series"] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        start_date: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantAnalyticsResponse:
        """
        Retrieves analytics for a single participant — all-time engagement counters,
        leaderboard ranks, and per-channel share counts (plus affiliate money metrics for
        affiliate programs). Useful for segmenting and re-engaging participants. Pass
        ``include=series`` to also get this participant's own activity over time.

        Args:
          days: Last number of days to retrieve analytics for. Defaults to 365. Maximum 1825.

          end_date: End date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

          include: Set to `series` to also return this participant's own activity per period.

          interval: Bucket size for the `series` (only used with `include=series`). Defaults to
              `day`.

          start_date: Start date of the analytics timeframe as a Unix timestamp in milliseconds.
              Required if `days` is not set.

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
                "/campaign/{id}/participant/{participant_id_or_email}/analytics",
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
                        "days": days,
                        "end_date": end_date,
                        "include": include,
                        "interval": interval,
                        "start_date": start_date,
                    },
                    participant_analytics_params.ParticipantAnalyticsParams,
                ),
            ),
            cast_to=ParticipantAnalyticsResponse,
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
        self.bulk_delete = to_raw_response_wrapper(
            participant.bulk_delete,
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
        self.refund_transaction = to_raw_response_wrapper(
            participant.refund_transaction,
        )
        self.send_invites = to_raw_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = to_raw_response_wrapper(
            participant.trigger_referral,
        )
        self.cancel_delayed_referral = to_raw_response_wrapper(
            participant.cancel_delayed_referral,
        )
        self.email = to_raw_response_wrapper(
            participant.email,
        )
        self.list_activity_logs = to_raw_response_wrapper(
            participant.list_activity_logs,
        )
        self.retrieve_analytics = to_raw_response_wrapper(
            participant.retrieve_analytics,
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
        self.bulk_delete = async_to_raw_response_wrapper(
            participant.bulk_delete,
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
        self.refund_transaction = async_to_raw_response_wrapper(
            participant.refund_transaction,
        )
        self.send_invites = async_to_raw_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = async_to_raw_response_wrapper(
            participant.trigger_referral,
        )
        self.cancel_delayed_referral = async_to_raw_response_wrapper(
            participant.cancel_delayed_referral,
        )
        self.email = async_to_raw_response_wrapper(
            participant.email,
        )
        self.list_activity_logs = async_to_raw_response_wrapper(
            participant.list_activity_logs,
        )
        self.retrieve_analytics = async_to_raw_response_wrapper(
            participant.retrieve_analytics,
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
        self.bulk_delete = to_streamed_response_wrapper(
            participant.bulk_delete,
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
        self.refund_transaction = to_streamed_response_wrapper(
            participant.refund_transaction,
        )
        self.send_invites = to_streamed_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = to_streamed_response_wrapper(
            participant.trigger_referral,
        )
        self.cancel_delayed_referral = to_streamed_response_wrapper(
            participant.cancel_delayed_referral,
        )
        self.email = to_streamed_response_wrapper(
            participant.email,
        )
        self.list_activity_logs = to_streamed_response_wrapper(
            participant.list_activity_logs,
        )
        self.retrieve_analytics = to_streamed_response_wrapper(
            participant.retrieve_analytics,
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
        self.bulk_delete = async_to_streamed_response_wrapper(
            participant.bulk_delete,
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
        self.refund_transaction = async_to_streamed_response_wrapper(
            participant.refund_transaction,
        )
        self.send_invites = async_to_streamed_response_wrapper(
            participant.send_invites,
        )
        self.trigger_referral = async_to_streamed_response_wrapper(
            participant.trigger_referral,
        )
        self.cancel_delayed_referral = async_to_streamed_response_wrapper(
            participant.cancel_delayed_referral,
        )
        self.email = async_to_streamed_response_wrapper(
            participant.email,
        )
        self.list_activity_logs = async_to_streamed_response_wrapper(
            participant.list_activity_logs,
        )
        self.retrieve_analytics = async_to_streamed_response_wrapper(
            participant.retrieve_analytics,
        )
