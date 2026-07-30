# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo, StrictInt, StrictStr, StrictBool, StrictFloat

from .._models import BaseModel

__all__ = ["AffiliateApplicationAnswer"]


class AffiliateApplicationAnswer(BaseModel):
    field_id: str = FieldInfo(alias="fieldId")
    """Stable key of the saved application-form field this answer belongs to."""

    label: str
    """Customer-configured field label captured when the applicant submitted."""

    type: Literal["text", "textarea", "url", "country", "number", "dropdown", "radio", "checkbox"]
    """Saved field type that determined how the scalar answer was validated."""

    value: Union[StrictStr, StrictInt, StrictFloat, StrictBool]
    """Applicant answer represented as one validated string, number, or boolean."""
