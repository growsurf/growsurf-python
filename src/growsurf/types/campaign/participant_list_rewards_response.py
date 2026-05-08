# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .participant_reward import ParticipantReward

__all__ = ["ParticipantListRewardsResponse"]


class ParticipantListRewardsResponse(BaseModel):
    limit: int

    next_id: Optional[str] = FieldInfo(alias="nextId", default=None)

    rewards: List[ParticipantReward]
