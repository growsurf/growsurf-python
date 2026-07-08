# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    company_logo_image_url: Annotated[str, PropertyInfo(alias="companyLogoImageUrl")]

    company_name: Annotated[str, PropertyInfo(alias="companyName")]

    name: str

    status: Literal["IN_PROGRESS", "COMPLETE"]
    """The requested program status.

    `IN_PROGRESS` publishes or resumes the program; `COMPLETE` ends it. Any other
    value returns a `400`.
    """
