from __future__ import annotations

import pytest
from pydantic import ValidationError

from growsurf.types import ParticipantList, ParticipantPayoutList, ParticipantCommissionList
from growsurf._compat import parse_obj
from growsurf._models import BaseModel
from growsurf.types.campaign import Campaign, Participant
from growsurf.types.campaign.participant_reward import ParticipantReward
from growsurf.types.participant_commission_list import Commission
from growsurf.types.campaign.participant_list_rewards_response import ParticipantListRewardsResponse
from growsurf.types.campaign_create_mobile_participant_token_params import (
    CampaignCreateMobileParticipantTokenParams,
)


def test_affiliate_participant_can_omit_share_url() -> None:
    participant = Participant(
        id="participant-id",
        email="affiliate@example.com",
        monthlyRank=0,
        monthlyReferralCount=0,
        rank=0,
        referralCount=0,
        rewards=[],
    )

    assert participant.share_url is None


def test_mobile_participant_token_accepts_is_affiliate() -> None:
    assert "is_affiliate" in CampaignCreateMobileParticipantTokenParams.__annotations__


@pytest.mark.parametrize("status", ["PENDING", "CANCELLED"])
def test_campaign_accepts_every_runtime_status(status: str) -> None:
    campaign = parse_obj(
        Campaign,
        {
            "id": "program-id",
            "impressionCount": 0,
            "inviteCount": 0,
            "name": "Pied Piper Referral Program",
            "participantCount": 0,
            "referralCount": 0,
            "rewards": [],
            "status": status,
            "type": "REFERRAL",
            "winnerCount": 0,
        },
    )

    assert campaign.status == status


def test_commission_requires_nullable_amount_fields() -> None:
    payload = {
        "id": "commission-id",
        "amount": None,
        "createdAt": 1767225600000,
        "currencyISO": "USD",
        "event": "SALE",
        "referredId": "referred-id",
        "referrerId": "referrer-id",
        "saleAmount": None,
        "status": "APPROVED",
    }

    commission = parse_obj(Commission, payload)
    assert commission.amount is None
    assert commission.sale_amount is None

    for field in ("amount", "saleAmount"):
        incomplete = {key: value for key, value in payload.items() if key != field}
        with pytest.raises(ValidationError):
            parse_obj(Commission, incomplete)


def test_participant_reward_exposes_delivered_amount_and_currency() -> None:
    reward = parse_obj(
        ParticipantReward,
        {
            "id": "participant-reward-id",
            "rewardId": "campaign-reward-id",
            "status": "FULFILLED",
            "amount": 2.5,
            "currencyISO": "USD",
        },
    )

    assert reward.amount == 2.5
    assert reward.currency_iso == "USD"

    reward_without_amount = ParticipantReward(
        id="participant-reward-without-amount",
        rewardId="campaign-reward-id",
        status="PENDING",
    )
    assert reward_without_amount.amount is None
    assert reward_without_amount.currency_iso is None


@pytest.mark.parametrize(
    ("model", "payload"),
    [
        (ParticipantList, {"participants": [], "limit": 10}),
        (ParticipantListRewardsResponse, {"rewards": [], "limit": 10}),
        (ParticipantCommissionList, {"commissions": [], "limit": 10}),
        (ParticipantPayoutList, {"payouts": [], "limit": 10}),
    ],
)
def test_cursor_page_requires_nullable_next_id(model: type[BaseModel], payload: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        parse_obj(model, payload)
