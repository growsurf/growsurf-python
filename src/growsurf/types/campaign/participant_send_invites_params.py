# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ParticipantSendInvitesParams"]


class ParticipantSendInvitesParams(TypedDict, total=False):
    id: Required[str]

    email_addresses: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="emailAddresses")]]

    message_text: Required[Annotated[str, PropertyInfo(alias="messageText")]]

    subject_text: Required[Annotated[str, PropertyInfo(alias="subjectText")]]
