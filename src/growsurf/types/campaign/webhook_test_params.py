# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .webhook_event import WebhookEvent

__all__ = ["WebhookTestParams"]


class WebhookTestParams(TypedDict, total=False):
    id: Required[str]

    event: WebhookEvent
    """The event to simulate.

    When omitted, the webhook's first enabled event is used (`400` if it has none).
    """
