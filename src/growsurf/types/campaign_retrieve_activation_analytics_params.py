# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignRetrieveActivationAnalyticsParams"]


class CampaignRetrieveActivationAnalyticsParams(TypedDict, total=False):
    cohort_from: Annotated[int, PropertyInfo(alias="cohortFrom")]
    """Inclusive cohort enrollment start as a Unix timestamp in milliseconds."""

    cohort_to: Annotated[int, PropertyInfo(alias="cohortTo")]
    """Exclusive cohort enrollment end as a Unix timestamp in milliseconds."""

    cohort_interval: Annotated[Literal["day", "week", "month"], PropertyInfo(alias="cohortInterval")]
    """Cohort bucket size. Defaults to `day`."""

    observation_window_days: Annotated[Literal[7, 30], PropertyInfo(alias="observationWindowDays")]
    """Days after enrollment allowed for each participant to reach a stage. Defaults to `30`."""

    timezone: str
    """IANA timezone used for cohort bounds. Defaults to `UTC`."""
