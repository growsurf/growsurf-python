# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeleteRewardGroupResponse"]


class DeleteRewardGroupResponse(BaseModel):
    id: str
    """The deleted group ID."""

    moved_to_default: int = FieldInfo(alias="movedToDefault")
    """The number of members moved to Default."""

    success: bool
    """Whether the group was deleted."""
