# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ParticipantRequestPayoutDestinationConfirmationParams"]


class ParticipantRequestPayoutDestinationConfirmationParams(TypedDict, total=False):
    id: Required[str]

    provider: Required[Literal["PAYPAL", "VENMO", "WISECOM"]]
    """The payout provider the participant should confirm a destination for. `VENMO` uses a confirmed email and is available only when connected PayPal Payouts and payout-email confirmation are enabled in a USD program. Venmo recipients must be in the United States."""
