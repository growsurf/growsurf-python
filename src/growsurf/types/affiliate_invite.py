# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AffiliateInvite"]


class AffiliateInvite(BaseModel):
    id: Optional[str] = None
    """Invite ID."""

    accepted_at: Optional[int] = FieldInfo(alias="acceptedAt", default=None)
    """When the invite was accepted, in Unix milliseconds. `null` until accepted."""

    created_at: Optional[int] = FieldInfo(alias="createdAt", default=None)
    """When the invite was created, in Unix milliseconds."""

    email: Optional[str] = None
    """Invitee email address."""

    expires_at: Optional[int] = FieldInfo(alias="expiresAt", default=None)
    """When the emailed accept link stops working, in Unix milliseconds."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """Invitee first name, when provided."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """Invitee last name, when provided."""

    last_sent_at: Optional[int] = FieldInfo(alias="lastSentAt", default=None)
    """When the invite email was last sent, in Unix milliseconds."""

    revoked_at: Optional[int] = FieldInfo(alias="revokedAt", default=None)
    """When the invite was revoked, in Unix milliseconds. `null` unless revoked."""

    status: Optional[Literal["PENDING", "ACCEPTED", "EXPIRED", "REVOKED"]] = None
    """The invite's lifecycle state.

    Accepting a pending invite enrolls the invitee as an approved affiliate.
    """
