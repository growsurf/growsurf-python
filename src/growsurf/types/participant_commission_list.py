# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ParticipantCommissionList", "Commission"]


class Commission(BaseModel):
    id: str

    amount: int

    created_at: int = FieldInfo(alias="createdAt")

    currency_iso: str = FieldInfo(alias="currencyISO")

    referred_id: str = FieldInfo(alias="referredId")

    referrer_id: str = FieldInfo(alias="referrerId")

    sale_amount: int = FieldInfo(alias="saleAmount")

    status: Literal["PENDING", "APPROVED", "PAID", "REVERSED", "DELETED"]

    amount_in_campaign_currency: Optional[int] = FieldInfo(alias="amountInCampaignCurrency", default=None)

    approved_at: Optional[int] = FieldInfo(alias="approvedAt", default=None)

    campaign_currency_iso: Optional[str] = FieldInfo(alias="campaignCurrencyISO", default=None)

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)

    exchange_rate_at: Optional[int] = FieldInfo(alias="exchangeRateAt", default=None)

    fx_error: Optional[str] = FieldInfo(alias="fxError", default=None)

    hold_duration: Optional[int] = FieldInfo(alias="holdDuration", default=None)

    paid_at: Optional[int] = FieldInfo(alias="paidAt", default=None)

    payout_queued_at: Optional[int] = FieldInfo(alias="payoutQueuedAt", default=None)

    provider: Optional[str] = None

    reversed_at: Optional[int] = FieldInfo(alias="reversedAt", default=None)

    sale_amount_amount_in_campaign_currency: Optional[int] = FieldInfo(
        alias="saleAmountAmountInCampaignCurrency", default=None
    )


class ParticipantCommissionList(BaseModel):
    commissions: List[Commission]

    limit: int

    next_id: Optional[str] = FieldInfo(alias="nextId", default=None)
