from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PendingAnalyticsErasure"]


class PendingAnalyticsErasure(BaseModel):
    status: Literal["pending"]
    """Analytics erasure has been accepted but is not confirmed complete."""

    operation_id: str = FieldInfo(alias="operationId")
    """Opaque reference for support inquiries about this analytics erasure."""
