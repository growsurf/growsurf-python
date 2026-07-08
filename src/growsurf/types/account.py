# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Account"]


class Account(BaseModel):
    id: str
    """The account's unique identifier."""

    email: str

    verification_status: Literal["NOT_REQUESTED", "REQUESTED", "VERIFIED"] = FieldInfo(alias="verificationStatus")
    """GrowSurf-team verification state.

    `VERIFIED` is required before a program can send participant emails.
    """

    company: Optional[str] = None

    created_at: Optional[int] = FieldInfo(alias="createdAt", default=None)
    """When the account was created, as a Unix timestamp in milliseconds."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    verification_requested_at: Optional[int] = FieldInfo(alias="verificationRequestedAt", default=None)
    """When team verification was last requested, as a Unix timestamp in milliseconds."""
