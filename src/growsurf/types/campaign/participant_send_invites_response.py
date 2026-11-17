# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantSendInvitesResponse"]


class ParticipantSendInvitesResponse(BaseModel):
    invites_sent: int = FieldInfo(alias="invitesSent")

    message_type: str = FieldInfo(alias="messageType")

    success: bool

    message: Optional[str] = None
    """Human-readable detail for the result. Empty when there is nothing to add."""
