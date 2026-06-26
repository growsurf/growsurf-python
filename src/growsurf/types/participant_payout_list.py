# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ParticipantPayoutList", "Payout"]


class Payout(BaseModel):
    id: str

    amount: int

    commission_ids: List[str] = FieldInfo(alias="commissionIds")

    created_at: int = FieldInfo(alias="createdAt")

    currency_iso: str = FieldInfo(alias="currencyISO")

    participant_id: str = FieldInfo(alias="participantId")

    status: Literal["UPCOMING", "QUEUED", "ISSUED", "FAILED"]

    amount_in_campaign_currency: Optional[int] = FieldInfo(alias="amountInCampaignCurrency", default=None)

    campaign_currency_iso: Optional[str] = FieldInfo(alias="campaignCurrencyISO", default=None)

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)

    exchange_rate_at: Optional[int] = FieldInfo(alias="exchangeRateAt", default=None)

    failed_at: Optional[int] = FieldInfo(alias="failedAt", default=None)

    fx_error: Optional[str] = FieldInfo(alias="fxError", default=None)

    issued_at: Optional[int] = FieldInfo(alias="issuedAt", default=None)

    provider: Optional[str] = None

    queued_at: Optional[int] = FieldInfo(alias="queuedAt", default=None)


class ParticipantPayoutList(BaseModel):
    limit: int

    next_id: Optional[str] = FieldInfo(alias="nextId", default=None)

    payouts: List[Payout]
