# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .campaign.reward_create_params import RewardCreateParams

__all__ = ["CampaignCreateParams"]


class CampaignCreateParams(TypedDict, total=False):
    type: Required[Literal["REFERRAL", "AFFILIATE"]]
    """The program type. Immutable after creation."""

    company_logo_image_url: Annotated[str, PropertyInfo(alias="companyLogoImageUrl")]

    company_name: Annotated[str, PropertyInfo(alias="companyName")]

    currency_iso: Annotated[str, PropertyInfo(alias="currencyISO")]
    """ISO 4217 currency code.

    Defaults to USD. Chosen when the program is created and immutable afterward — it
    cannot be changed on update.
    """

    name: str
    """The program name. Defaults to "Untitled Program"."""

    rewards: Iterable[RewardCreateParams]
    """Optional inline rewards to create with the program."""
