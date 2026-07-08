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
    """The events this webhook is subscribed to. When omitted, it is subscribed to no events."""

    is_enabled: Annotated[bool, PropertyInfo(alias="isEnabled")]

    secret: str
    """Write-only.

    Used to sign deliveries (the `GrowSurf-Signature` HMAC header). Never returned.
    """
