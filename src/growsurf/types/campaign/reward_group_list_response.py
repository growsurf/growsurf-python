# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .reward_group import RewardGroup

__all__ = ["RewardGroupListResponse"]


class RewardGroupListResponse(BaseModel):
    groups: List[RewardGroup]
    """The program's groups in display order. Default is not listed."""
