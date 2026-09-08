# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantRefundTransactionParams"]


class ParticipantRefundTransactionParams(TypedDict, total=False):
    id: Required[str]

    amendment_type: Annotated[Literal["REFUND", "CHARGEBACK"], PropertyInfo(alias="amendmentType")]

    amount: int

    amount_refunded: Annotated[int, PropertyInfo(alias="amountRefunded")]

    charge_id: Annotated[str, PropertyInfo(alias="chargeId")]

    currency: str

    description: str

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    invoice_id: Annotated[str, PropertyInfo(alias="invoiceId")]

    order_id: Annotated[str, PropertyInfo(alias="orderId")]

    payment_id: Annotated[str, PropertyInfo(alias="paymentId")]

    payment_intent_id: Annotated[str, PropertyInfo(alias="paymentIntentId")]

    refund_amount: Annotated[int, PropertyInfo(alias="refundAmount")]
    """Positive amount for this individual refund, no greater than the sale amount, in minor units. Record it with `refundId` on each original refund to support cancellation and out-of-order amendments. A cancellation may omit an already recorded amount. Missing or conflicting refund history returns `409` without applying the cancellation. Newly observed higher cumulative refunds and incomplete coverage are retained for reconciliation."""

    refund_history_complete: Annotated[bool, PropertyInfo(alias="refundHistoryComplete")]
    """Confirm only after every original refund ID and amount is recorded, including canceled refunds. Resolves previously incomplete history. Replaying an old confirmation cannot resolve a later gap; confirm a newly reconciled refund or complete provider list."""

    refund_id: Annotated[str, PropertyInfo(alias="refundId")]
    """Stable per-refund identifier.

    Required when canceling a refund or changing the refunded total after a cancellation.
    Reuse the original refund's identifier for its cancellation.
    """

    refund_status: Annotated[str, PropertyInfo(alias="refundStatus")]

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
