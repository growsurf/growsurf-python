# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantCreateMobileTokenResponse"]


class ParticipantCreateMobileTokenResponse(BaseModel):
    expires_in: int = FieldInfo(alias="expiresIn")
    """Token lifetime in seconds."""

    participant_token: str = FieldInfo(alias="participantToken")
    """Participant-scoped bearer token for GrowSurf mobile SDK participant endpoints."""
