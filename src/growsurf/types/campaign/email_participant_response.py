# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmailParticipantResponse"]


class EmailParticipantResponse(BaseModel):
    status: Literal["queued"]
    """The email was accepted for delivery."""

    success: bool
