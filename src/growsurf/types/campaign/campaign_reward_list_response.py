# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .reward import Reward
from ..._models import BaseModel

__all__ = ["CampaignRewardListResponse"]


class CampaignRewardListResponse(BaseModel):
    rewards: List[Reward]
    """The program's active, visible, and enabled rewards."""
