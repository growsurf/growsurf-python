# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Team"]


class Team(BaseModel):
    name: str
    """The team's display name."""

    verification_status: Literal["NOT_REQUESTED", "REQUESTED", "VERIFIED"] = FieldInfo(alias="verificationStatus")
    """GrowSurf team verification state.

    `VERIFIED` is required before a program can send participant emails.
    """

    verification_requested_at: Optional[int] = FieldInfo(alias="verificationRequestedAt")
    """When team verification was last requested, as a Unix timestamp in milliseconds."""
