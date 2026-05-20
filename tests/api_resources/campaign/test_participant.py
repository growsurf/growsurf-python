# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types import ReferralList, ParticipantPayoutList, ParticipantCommissionList
from growsurf.types.campaign import (
    Participant,
    ParticipantDeleteResponse,
    ParticipantListRewardsResponse,
    ParticipantSendInvitesResponse,
    ParticipantTriggerReferralResponse,
    ParticipantRecordTransactionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParticipant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Growsurf) -> None:
        participant = client.campaign.participant.retrieve(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.retrieve(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.retrieve(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(Participant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.retrieve(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.retrieve(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Growsurf) -> None:
        participant = client.campaign.participant.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email="dev@stainless.com",
            first_name="Gavin",
            last_name="Belson",
            metadata={"company": "bar"},
            referral_status="CREDIT_PENDING",
            referred_by="referredBy",
            unsubscribed=False,
            vanity_keys=["_1k--w2KifJ1"],
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(Participant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.update(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.update(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Growsurf) -> None:
        participant = client.campaign.participant.delete(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantDeleteResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.delete(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantDeleteResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.delete(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantDeleteResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.delete(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.delete(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Growsurf) -> None:
        participant = client.campaign.participant.add(
            id="id",
            email="dev@stainless.com",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.add(
            id="id",
            email="dev@stainless.com",
            fingerprint="fingerprint",
            first_name="firstName",
            ip_address="ipAddress",
            last_name="lastName",
            metadata={"foo": "bar"},
            mobile_instance_id="mobileInstanceId",
            referral_status="CREDIT_PENDING",
            referred_by="referredBy",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.add(
            id="id",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.add(
            id="id",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(Participant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.add(
                id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_commissions(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantCommissionList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_commissions_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            limit=1,
            next_id="nextId",
            status="PENDING",
        )
        assert_matches_type(ParticipantCommissionList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_commissions(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantCommissionList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_commissions(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantCommissionList, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_commissions(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.list_commissions(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.list_commissions(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payouts(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantPayoutList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payouts_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            limit=1,
            next_id="nextId",
            status="UPCOMING",
        )
        assert_matches_type(ParticipantPayoutList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_payouts(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantPayoutList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_payouts(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantPayoutList, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_payouts(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.list_payouts(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.list_payouts(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_referrals(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ReferralList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_referrals_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            desc=True,
            email="email",
            first_name="firstName",
            last_name="lastName",
            limit=1,
            next_id="nextId",
            offset=0,
            referral_status="CREDIT_PENDING",
            sort_by="updatedAt",
        )
        assert_matches_type(ReferralList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_referrals(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ReferralList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_referrals(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ReferralList, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_referrals(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.list_referrals(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.list_referrals(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rewards(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rewards_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            limit=1,
            next_id="nextId",
        )
        assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_rewards(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_rewards(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_rewards(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.list_rewards(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.list_rewards(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_record_transaction(self, client: Growsurf) -> None:
        participant = client.campaign.participant.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
        )
        assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_record_transaction_with_all_params(self, client: Growsurf) -> None:
        participant = client.campaign.participant.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
            amount_cash_net=7900,
            amount_paid=0,
            charge_id="chargeId",
            customer_id="customerId",
            description="Renewal for Pro subscription",
            external_id="externalId",
            invoice_id="invoice_54",
            invoice_subtotal_excluding_tax=0,
            invoice_total=0,
            invoice_total_excluding_tax=0,
            net_amount=0,
            order_id="orderId",
            paid_at=1733702400000,
            payment_id="paymentId",
            payment_intent_id="paymentIntentId",
            subscription_id="subscriptionId",
            tax_amount=0,
            total_tax_amount=0,
            total_tax_amounts=[{"foo": "bar"}],
            total_taxes=[{"foo": "bar"}],
            transaction_id="transactionId",
        )
        assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_record_transaction(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_record_transaction(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_record_transaction(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.record_transaction(
                participant_id_or_email="participantIdOrEmail",
                id="",
                currency="USD",
                gross_amount=9900,
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.record_transaction(
                participant_id_or_email="",
                id="id",
                currency="USD",
                gross_amount=9900,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_invites(self, client: Growsurf) -> None:
        participant = client.campaign.participant.send_invites(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email_addresses=["erlich@aviato.com"],
            message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
            subject_text="Join me on Pied Piper",
        )
        assert_matches_type(ParticipantSendInvitesResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_invites(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.send_invites(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email_addresses=["erlich@aviato.com"],
            message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
            subject_text="Join me on Pied Piper",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantSendInvitesResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_invites(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.send_invites(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email_addresses=["erlich@aviato.com"],
            message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
            subject_text="Join me on Pied Piper",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantSendInvitesResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_invites(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.send_invites(
                participant_id_or_email="participantIdOrEmail",
                id="",
                email_addresses=["erlich@aviato.com"],
                message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
                subject_text="Join me on Pied Piper",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.send_invites(
                participant_id_or_email="",
                id="id",
                email_addresses=["erlich@aviato.com"],
                message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
                subject_text="Join me on Pied Piper",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_referral(self, client: Growsurf) -> None:
        participant = client.campaign.participant.trigger_referral(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantTriggerReferralResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_referral(self, client: Growsurf) -> None:
        response = client.campaign.participant.with_raw_response.trigger_referral(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantTriggerReferralResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger_referral(self, client: Growsurf) -> None:
        with client.campaign.participant.with_streaming_response.trigger_referral(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantTriggerReferralResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_trigger_referral(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.participant.with_raw_response.trigger_referral(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            client.campaign.participant.with_raw_response.trigger_referral(
                participant_id_or_email="",
                id="id",
            )


class TestAsyncParticipant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.retrieve(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.retrieve(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.retrieve(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(Participant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.retrieve(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.retrieve(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email="dev@stainless.com",
            first_name="Gavin",
            last_name="Belson",
            metadata={"company": "bar"},
            referral_status="CREDIT_PENDING",
            referred_by="referredBy",
            unsubscribed=False,
            vanity_keys=["_1k--w2KifJ1"],
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.update(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(Participant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.update(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.update(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.delete(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantDeleteResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.delete(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantDeleteResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.delete(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantDeleteResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.delete(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.delete(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.add(
            id="id",
            email="dev@stainless.com",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.add(
            id="id",
            email="dev@stainless.com",
            fingerprint="fingerprint",
            first_name="firstName",
            ip_address="ipAddress",
            last_name="lastName",
            metadata={"foo": "bar"},
            mobile_instance_id="mobileInstanceId",
            referral_status="CREDIT_PENDING",
            referred_by="referredBy",
        )
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.add(
            id="id",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(Participant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.add(
            id="id",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(Participant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.add(
                id="",
                email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantCommissionList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_commissions_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            limit=1,
            next_id="nextId",
            status="PENDING",
        )
        assert_matches_type(ParticipantCommissionList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantCommissionList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.list_commissions(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantCommissionList, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_commissions(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.list_commissions(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.list_commissions(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantPayoutList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payouts_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            limit=1,
            next_id="nextId",
            status="UPCOMING",
        )
        assert_matches_type(ParticipantPayoutList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantPayoutList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.list_payouts(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantPayoutList, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_payouts(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.list_payouts(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.list_payouts(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ReferralList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_referrals_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            desc=True,
            email="email",
            first_name="firstName",
            last_name="lastName",
            limit=1,
            next_id="nextId",
            offset=0,
            referral_status="CREDIT_PENDING",
            sort_by="updatedAt",
        )
        assert_matches_type(ReferralList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ReferralList, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.list_referrals(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ReferralList, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_referrals(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.list_referrals(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.list_referrals(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rewards(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rewards_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            limit=1,
            next_id="nextId",
        )
        assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_rewards(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_rewards(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.list_rewards(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantListRewardsResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_rewards(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.list_rewards(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.list_rewards(
                participant_id_or_email="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_record_transaction(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
        )
        assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_record_transaction_with_all_params(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
            amount_cash_net=7900,
            amount_paid=0,
            charge_id="chargeId",
            customer_id="customerId",
            description="Renewal for Pro subscription",
            external_id="externalId",
            invoice_id="invoice_54",
            invoice_subtotal_excluding_tax=0,
            invoice_total=0,
            invoice_total_excluding_tax=0,
            net_amount=0,
            order_id="orderId",
            paid_at=1733702400000,
            payment_id="paymentId",
            payment_intent_id="paymentIntentId",
            subscription_id="subscriptionId",
            tax_amount=0,
            total_tax_amount=0,
            total_tax_amounts=[{"foo": "bar"}],
            total_taxes=[{"foo": "bar"}],
            transaction_id="transactionId",
        )
        assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_record_transaction(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_record_transaction(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.record_transaction(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            currency="USD",
            gross_amount=9900,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantRecordTransactionResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_record_transaction(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.record_transaction(
                participant_id_or_email="participantIdOrEmail",
                id="",
                currency="USD",
                gross_amount=9900,
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.record_transaction(
                participant_id_or_email="",
                id="id",
                currency="USD",
                gross_amount=9900,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_invites(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.send_invites(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email_addresses=["erlich@aviato.com"],
            message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
            subject_text="Join me on Pied Piper",
        )
        assert_matches_type(ParticipantSendInvitesResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_invites(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.send_invites(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email_addresses=["erlich@aviato.com"],
            message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
            subject_text="Join me on Pied Piper",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantSendInvitesResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_invites(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.send_invites(
            participant_id_or_email="participantIdOrEmail",
            id="id",
            email_addresses=["erlich@aviato.com"],
            message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
            subject_text="Join me on Pied Piper",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantSendInvitesResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_invites(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.send_invites(
                participant_id_or_email="participantIdOrEmail",
                id="",
                email_addresses=["erlich@aviato.com"],
                message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
                subject_text="Join me on Pied Piper",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.send_invites(
                participant_id_or_email="",
                id="id",
                email_addresses=["erlich@aviato.com"],
                message_text="{{referrerFirstName}} invited you with {{referrerShareUrl}}.",
                subject_text="Join me on Pied Piper",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_referral(self, async_client: AsyncGrowsurf) -> None:
        participant = await async_client.campaign.participant.trigger_referral(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )
        assert_matches_type(ParticipantTriggerReferralResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_referral(self, async_client: AsyncGrowsurf) -> None:
        response = await async_client.campaign.participant.with_raw_response.trigger_referral(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantTriggerReferralResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_referral(self, async_client: AsyncGrowsurf) -> None:
        async with async_client.campaign.participant.with_streaming_response.trigger_referral(
            participant_id_or_email="participantIdOrEmail",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantTriggerReferralResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_trigger_referral(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.participant.with_raw_response.trigger_referral(
                participant_id_or_email="participantIdOrEmail",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `participant_id_or_email` but received ''"
        ):
            await async_client.campaign.participant.with_raw_response.trigger_referral(
                participant_id_or_email="",
                id="id",
            )
