# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantActivityLogsResponse", "ActivityLog"]


class ActivityLog(BaseModel):
    created_at: int = FieldInfo(alias="createdAt")
    """When the activity occurred, as a Unix timestamp in milliseconds."""

    text: str

    type: str
    """The activity family (e.g. `REFERRAL`, `SHARE`, `REWARD`, `EMAIL`, `COMMON`)."""


class ParticipantActivityLogsResponse(BaseModel):
    activity_logs: List[ActivityLog] = FieldInfo(alias="activityLogs")

    limit: int

    offset: Optional[int] = None
    """The offset for the next page, or null when there are no more logs."""
