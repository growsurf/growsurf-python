# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .referral_flow_screenshot import ReferralFlowScreenshot

__all__ = ["ReferralFlowScreenshotsResponse"]


class ReferralFlowScreenshotsResponse(BaseModel):
    generated_at: datetime = FieldInfo(alias="generatedAt")
    """ISO 8601 time the images were rendered."""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """ISO 8601 time after which every `url` in `screenshots` stops working."""

    screenshots: List[ReferralFlowScreenshot]
    """One entry per view, in referrer then referred-friend order."""
