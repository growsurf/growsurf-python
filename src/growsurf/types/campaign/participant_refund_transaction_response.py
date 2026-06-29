# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantRefundTransactionResponse"]


class ParticipantRefundTransactionResponse(BaseModel):
    adjusted: int

    amendment_type: Literal["REFUND", "CHARGEBACK"] = FieldInfo(alias="amendmentType")

    deleted: int

    matched: int

    matching_commission_ids: List[str] = FieldInfo(alias="matchingCommissionIds")

    message: str

    reversed: int

    success: bool

    not_found: Optional[bool] = FieldInfo(alias="notFound", default=None)
