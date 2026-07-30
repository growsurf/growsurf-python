from growsurf.types.campaign import Participant
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
