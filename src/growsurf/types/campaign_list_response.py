# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .campaign.campaign import Campaign

__all__ = ["CampaignListResponse"]


class CampaignListResponse(BaseModel):
    campaigns: List[Campaign]
