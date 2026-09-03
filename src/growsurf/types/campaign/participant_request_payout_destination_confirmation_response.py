# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantRequestPayoutDestinationConfirmationResponse"]


class ParticipantRequestPayoutDestinationConfirmationResponse(BaseModel):
    expires_at: Optional[int] = FieldInfo(alias="expiresAt")
    """When the confirmation link expires, as a Unix timestamp in milliseconds."""

    provider: str
    """The provider the participant was asked to confirm."""

    provider_display_name: str = FieldInfo(alias="providerDisplayName")
    """The customer-facing provider name (e.g. "PayPal", "Wise")."""

    status: Literal["CONFIRMATION_REQUESTED"]
    """Confirms the message was requested."""
