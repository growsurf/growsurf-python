from growsurf._compat import parse_obj, get_model_fields
from growsurf.types.campaign.participant_get_payout_destination_response import (
    ParticipantGetPayoutDestinationResponse,
)
from growsurf.types.campaign.participant_request_payout_destination_confirmation_response import (
    ParticipantRequestPayoutDestinationConfirmationResponse,
)


def test_unknown_future_payout_provider_decodes() -> None:
    response = parse_obj(
        ParticipantGetPayoutDestinationResponse,
        {
            "activeProvider": "TESTBANK",
            "enabledProviders": ["TESTBANK"],
            "destinations": [
                {
                    "provider": "TESTBANK",
                    "providerDisplayName": "Test Bank",
                    "status": "ACTIVE",
                    "claimEmail": "richard@piedpiper.com",
                    "legalEntityType": "INDIVIDUAL",
                    "confirmedAt": 1752000000000,
                    "needsRepairReason": None,
                }
            ],
        },
    )

    assert response.active_provider == "TESTBANK"
    assert response.enabled_providers == ["TESTBANK"]
    assert response.destinations and response.destinations[0].provider == "TESTBANK"

    confirmation = parse_obj(
        ParticipantRequestPayoutDestinationConfirmationResponse,
        {
            "provider": "TESTBANK",
            "providerDisplayName": "Test Bank",
            "status": "CONFIRMATION_REQUESTED",
            "expiresAt": 1752604800000,
        },
    )
    assert confirmation.provider == "TESTBANK"


def test_payout_destination_response_omits_redundant_participant_id() -> None:
    assert "participant_id" not in get_model_fields(ParticipantGetPayoutDestinationResponse)
