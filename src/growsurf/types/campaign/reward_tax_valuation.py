# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Literal, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RewardTaxValuation"]


class RewardTaxValuation(BaseModel):
    """Tax valuation settings for a campaign reward.

    Only relevant when the program collects tax documentation.
    """

    fair_market_value_usd: Optional[float] = FieldInfo(alias="fairMarketValueUSD", default=None)
    """Manual fair-market value in USD (major units).

    Used as the fallback when the reward value cannot be resolved automatically.
    `None` = no manual value.
    """

    tax_character: Optional[
        Literal[
            "NONEMPLOYEE_SERVICES",
            "PRIZE_OR_AWARD",
            "PURCHASE_REBATE",
            "OTHER_INCOME",
            "REVIEW_REQUIRED",
        ]
    ] = FieldInfo(alias="taxCharacter", default=None)
    """The reason the recipient earns this reward.

    `None` inherits the program's confirmed tax treatment for configurable non-commission
    rewards. Commission rewards always use `NONEMPLOYEE_SERVICES`.
    """
