# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .campaign.participant import Participant

__all__ = ["ParticipantList"]


class ParticipantList(BaseModel):
    limit: int

    next_id: Optional[str] = FieldInfo(alias="nextId", default=None)

    participants: List[Participant]
