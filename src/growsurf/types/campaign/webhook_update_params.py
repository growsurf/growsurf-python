# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .webhook_event import WebhookEvent

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    id: Required[str]

    events: List[WebhookEvent]

    is_enabled: Annotated[bool, PropertyInfo(alias="isEnabled")]

    payload_url: Annotated[str, PropertyInfo(alias="payloadUrl")]

    secret: str
    """Write-only."""
