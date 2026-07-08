# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .webhook_event import WebhookEvent

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str
    """The webhook id (`primary` for the program's primary webhook)."""

    auto_disabled_due_to_failures: bool = FieldInfo(alias="autoDisabledDueToFailures")
    """Read-only.

    Whether GrowSurf auto-disabled this webhook after repeated delivery failures.
    """

    events: List[WebhookEvent]

    failure_count: int = FieldInfo(alias="failureCount")
    """Read-only. Consecutive delivery failures."""

    is_enabled: bool = FieldInfo(alias="isEnabled")

    last_failure_at: Optional[int] = FieldInfo(alias="lastFailureAt", default=None)
    """Read-only.

    When the last delivery failure occurred, as a Unix timestamp in milliseconds.
    """

    payload_url: Optional[str] = FieldInfo(alias="payloadUrl", default=None)
    """The URL that receives webhook deliveries."""
