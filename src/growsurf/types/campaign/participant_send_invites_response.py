# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantSendInvitesResponse"]


class ParticipantSendInvitesResponse(BaseModel):
    invites_sent: int = FieldInfo(alias="invitesSent")

    message_type: str = FieldInfo(alias="messageType")

    success: bool
