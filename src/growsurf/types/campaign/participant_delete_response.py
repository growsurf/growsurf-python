# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .pending_analytics_erasure import PendingAnalyticsErasure

__all__ = ["ParticipantDeleteResponse"]


class ParticipantDeleteResponse(BaseModel):
    analytics_erasure: Optional[PendingAnalyticsErasure] = FieldInfo(alias="analyticsErasure", default=None)
    """Analytics erasure is pending. Reports can retain removed participants until erasure completes. Do not repeat successful deletions."""

    success: bool
