# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CommissionStructure"]


class CommissionStructure(BaseModel):
    amount: Optional[int] = None

    amount_iso: Optional[str] = FieldInfo(alias="amountISO", default=None)

    approval_required: Optional[bool] = FieldInfo(alias="approvalRequired", default=None)

    duration: Optional[str] = None

    duration_in_months: Optional[int] = FieldInfo(alias="durationInMonths", default=None)

    event: Optional[str] = None

    has_intro: Optional[bool] = FieldInfo(alias="hasIntro", default=None)

    has_max_amount: Optional[bool] = FieldInfo(alias="hasMaxAmount", default=None)

    hold_duration: Optional[int] = FieldInfo(alias="holdDuration", default=None)

    intro_amount: Optional[int] = FieldInfo(alias="introAmount", default=None)

    intro_amount_iso: Optional[str] = FieldInfo(alias="introAmountISO", default=None)

    intro_duration: Optional[str] = FieldInfo(alias="introDuration", default=None)

    intro_duration_in_months: Optional[int] = FieldInfo(alias="introDurationInMonths", default=None)

    intro_percent: Optional[float] = FieldInfo(alias="introPercent", default=None)

    intro_type: Optional[str] = FieldInfo(alias="introType", default=None)

    max_amount: Optional[int] = FieldInfo(alias="maxAmount", default=None)

    max_amount_iso: Optional[str] = FieldInfo(alias="maxAmountISO", default=None)

    min_paid_referrals: Optional[int] = FieldInfo(alias="minPaidReferrals", default=None)

    percent: Optional[float] = None

    type: Optional[Literal["PERCENT", "FIXED"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
