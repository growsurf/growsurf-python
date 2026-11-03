# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .webhook_event import WebhookEvent

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    payload_url: Required[Annotated[str, PropertyInfo(alias="payloadUrl")]]
    """The URL that receives webhook deliveries."""

    events: List[WebhookEvent]
    """The events this webhook is subscribed to.

    When omitted, the webhook is subscribed to every event its program type offers,
    like a webhook added in the dashboard: referral programs offer
    `PARTICIPANT_REACHED_A_GOAL`, `NEW_PARTICIPANT_ADDED`,
    `PARTICIPANT_FRAUD_STATUS_UPDATED`, and `CAMPAIGN_ENDED`; affiliate programs offer
    `NEW_COMMISSION_ADDED`, `COMMISSION_ADJUSTED`, `NEW_PAYOUT_ISSUED`,
    `NEW_PARTICIPANT_ADDED`, `PARTICIPANT_FRAUD_STATUS_UPDATED`, and `CAMPAIGN_ENDED`.
    Send `[]` to subscribe to no events. An event the program type does not offer
    returns `400`.
    """

    is_enabled: Annotated[bool, PropertyInfo(alias="isEnabled")]

    secret: str
    """Write-only.

    Used to sign deliveries (the `GrowSurf-Signature` HMAC header). Never returned.
    """
