# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

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

    is_tax_reportable: Optional[bool] = FieldInfo(alias="isTaxReportable", default=None)
    """Whether the reward's value counts toward 1099 thresholds/totals.

    `None` = use the smart default for the reward's source.
    """
