# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantRecordTransactionParams"]


class ParticipantRecordTransactionParams(TypedDict, total=False):
    id: Required[str]

    currency: Required[str]

    gross_amount: Required[Annotated[int, PropertyInfo(alias="grossAmount")]]

    amount_cash_net: Annotated[int, PropertyInfo(alias="amountCashNet")]

    amount_paid: Annotated[int, PropertyInfo(alias="amountPaid")]

    charge_id: Annotated[str, PropertyInfo(alias="chargeId")]

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]

    description: str

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    invoice_id: Annotated[str, PropertyInfo(alias="invoiceId")]

    invoice_subtotal_excluding_tax: Annotated[int, PropertyInfo(alias="invoiceSubtotalExcludingTax")]

    invoice_total: Annotated[int, PropertyInfo(alias="invoiceTotal")]

    invoice_total_excluding_tax: Annotated[int, PropertyInfo(alias="invoiceTotalExcludingTax")]

    net_amount: Annotated[int, PropertyInfo(alias="netAmount")]

    order_id: Annotated[str, PropertyInfo(alias="orderId")]

    paid_at: Annotated[int, PropertyInfo(alias="paidAt")]

    payment_id: Annotated[str, PropertyInfo(alias="paymentId")]

    payment_intent_id: Annotated[str, PropertyInfo(alias="paymentIntentId")]

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]

    tax_amount: Annotated[int, PropertyInfo(alias="taxAmount")]

    total_tax_amount: Annotated[int, PropertyInfo(alias="totalTaxAmount")]

    total_tax_amounts: Annotated[Iterable[Dict[str, object]], PropertyInfo(alias="totalTaxAmounts")]

    total_taxes: Annotated[Iterable[Dict[str, object]], PropertyInfo(alias="totalTaxes")]

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
