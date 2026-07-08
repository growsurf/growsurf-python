# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEvent"]

WebhookEvent: TypeAlias = Literal[
    "PARTICIPANT_REACHED_A_GOAL",
    "NEW_PARTICIPANT_ADDED",
    "CAMPAIGN_ENDED",
    "PARTICIPANT_FRAUD_STATUS_UPDATED",
    "NEW_COMMISSION_ADDED",
    "COMMISSION_ADJUSTED",
    "NEW_PAYOUT_ISSUED",
]
