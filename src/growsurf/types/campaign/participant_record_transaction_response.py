# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipantRecordTransactionResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    duplicate: Literal[False]

    first_sale: bool = FieldInfo(alias="firstSale")

    message: str

    success: Literal[True]


class UnionMember1(BaseModel):
    commissions_created: int = FieldInfo(alias="commissionsCreated")

    duplicate: Literal[True]

    duplicate_fields: List[str] = FieldInfo(alias="duplicateFields")

    matching_commission_ids: List[str] = FieldInfo(alias="matchingCommissionIds")

    message: str

    success: Literal[False]


ParticipantRecordTransactionResponse: TypeAlias = Union[UnionMember0, UnionMember1]
