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

    goal: Literal[
        "CUSTOMERS",
        "USERS",
        "SUBSCRIBERS",
        "WAITLIST",
        "B2B_SAAS_SELF_SERVICE",
        "B2B_SAAS_ENTERPRISE",
        "B2C_SUBSCRIPTIONS",
        "FINANCIAL_SERVICES",
        "ONLINE_EDUCATION",
        "INSURANCE",
        "ONLINE_INSURANCE",
        "TELEHEALTH",
        "HEALTHCARE_PROVIDERS",
    ]
    """What the program is for, which seeds the share buttons and the starter rewards that
    suit that audience.

    Programs whose participants refer other businesses (`CUSTOMERS`, `USERS`,
    `B2B_SAAS_SELF_SERVICE`, `B2B_SAAS_ENTERPRISE`, `HEALTHCARE_PROVIDERS`) start with
    the LinkedIn share button visible; consumer, financial, education, insurance,
    telehealth, newsletter, and waitlist programs (`B2C_SUBSCRIPTIONS`,
    `FINANCIAL_SERVICES`, `ONLINE_EDUCATION`, `INSURANCE`, `ONLINE_INSURANCE`,
    `TELEHEALTH`, `SUBSCRIBERS`, `WAITLIST`) start with it hidden, and on a referral
    program each goal also sets the rest of its share buttons to suit that audience.
    When you create a referral program without `rewards`, the goal also decides the
    starter rewards: most goals get one double-sided reward, `HEALTHCARE_PROVIDERS` gets
    a single-sided reward, `SUBSCRIBERS` gets a four-step milestone ladder, and
    `WAITLIST` gets a leaderboard. Every one arrives switched off with a placeholder
    name, so the program awards nothing until you set the amount and turn one on.
    `TELEHEALTH` is for consumer telehealth and wellness subscriptions;
    `HEALTHCARE_PROVIDERS` is for provider networks and clinician-facing products.
    `INSURANCE` replaces `ONLINE_INSURANCE`, which is still accepted. Omit it and every
    share button keeps its standard default. Set only when the program is created; it is
    not accepted on update.
    """

    name: str
    """The program name. Defaults to a generated friendly label plus the creation date."""

    rewards: Iterable[RewardCreateParams]
    """Optional inline rewards to create with the program."""
