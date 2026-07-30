# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantGetPayoutDestinationResponse", "Destination"]


class Destination(BaseModel):
    claim_email: Optional[str] = FieldInfo(alias="claimEmail", default=None)
    """The confirmed payout email for this provider."""

    confirmed_at: Optional[int] = FieldInfo(alias="confirmedAt", default=None)
    """When the destination was confirmed, as a Unix timestamp in milliseconds."""

    legal_entity_type: Optional[Literal["INDIVIDUAL", "BUSINESS"]] = FieldInfo(alias="legalEntityType", default=None)
    """The legal recipient type the participant confirmed, if any."""

    needs_repair_reason: Optional[str] = FieldInfo(alias="needsRepairReason", default=None)
    """When status is `NEEDS_REPAIR`, why (e.g. a bounced delivery)."""

    provider: Optional[str] = None
    """The payout provider this entry describes."""

    provider_display_name: Optional[str] = FieldInfo(alias="providerDisplayName", default=None)
    """The customer-facing provider name (e.g. "PayPal", "Wise")."""

    status: Optional[str] = None
    """The destination's current status: `NONE` (not set up), `PENDING_CONFIRMATION`,
    `CONFIRMED`, `ACTIVE`, `NEEDS_REPAIR`, or `EXPIRED`.

    Historical superseded or revoked destinations are projected as `NONE`.
    """


class ParticipantGetPayoutDestinationResponse(BaseModel):
    active_provider: Optional[str] = FieldInfo(alias="activeProvider", default=None)
    """The provider that currently gets paid, or null until the participant confirms one."""

    destinations: Optional[List[Destination]] = None
    """One entry per enabled payout provider describing the participant's destination for
    it.
    """

    enabled_providers: Optional[List[str]] = FieldInfo(alias="enabledProviders", default=None)
    """The payout providers enabled for this program."""
