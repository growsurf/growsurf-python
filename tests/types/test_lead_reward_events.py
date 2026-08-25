from typing_extensions import Literal

from growsurf.types.campaign.reward import Reward
from growsurf.types.campaign.campaign import Reward as CampaignReward
from growsurf.types.commission_structure import CommissionStructure
from growsurf.types.campaign.participant_reward import ParticipantReward
from growsurf.types.participant_commission_list import Commission


def test_reward_and_commission_events_parse_from_public_wire_values() -> None:
    reward = Reward(
        id="crew_signup",
        isUnlimited=True,
        metadata={},
        type="SINGLE_SIDED",
        event="LEAD",
    )
    embedded_reward = CampaignReward(
        id="crew_signup",
        isUnlimited=True,
        metadata={},
        type="SINGLE_SIDED",
        event="LEAD",
    )
    commission = Commission(
        id="comm_signup",
        amount=500,
        createdAt=1,
        currencyISO="USD",
        event="LEAD",
        referredId="part_friend",
        referrerId="part_advocate",
        saleAmount=None,
        status="PENDING",
    )

    assert reward.event == "LEAD"
    assert embedded_reward.event == "LEAD"
    assert commission.event == "LEAD"
    assert commission.sale_amount is None


def test_cancelled_participant_reward_parses_from_public_wire_value() -> None:
    reward = ParticipantReward(
        id="participant_reward_cancelled",
        rewardId="reward_cancelled",
        status="CANCELLED",
    )

    assert reward.status == "CANCELLED"


def test_commission_structure_exposes_supported_event_contract() -> None:
    click = CommissionStructure(event="CLICK")
    lead = CommissionStructure(event="LEAD")
    sale = CommissionStructure(event="SALE")
    assert click.event is not None

    event: Literal["CLICK", "LEAD", "SALE"] = click.event
    assert event == "CLICK"
    assert lead.event == "LEAD"
    assert sale.event == "SALE"
