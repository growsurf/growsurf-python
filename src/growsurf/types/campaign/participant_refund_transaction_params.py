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

    refund_id: Annotated[str, PropertyInfo(alias="refundId")]

    refund_status: Annotated[str, PropertyInfo(alias="refundStatus")]

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
