# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .campaign.participant import Participant

__all__ = ["CampaignCreateMobileParticipantTokenResponse"]


class CampaignCreateMobileParticipantTokenResponse(BaseModel):
    expires_in: int = FieldInfo(alias="expiresIn")
    """Token lifetime in seconds."""

    is_new: bool = FieldInfo(alias="isNew")
    """Whether this request created a new participant.

    Returns false when the participant already existed.
    """

    participant: Participant

    participant_token: str = FieldInfo(alias="participantToken")
    """Participant-scoped bearer token for GrowSurf mobile SDK participant endpoints."""
