# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DeleteRewardResponse"]


class DeleteRewardResponse(BaseModel):
    id: str
    """The deleted reward ID."""

    success: bool
