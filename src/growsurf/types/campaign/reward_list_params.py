# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RewardListParams"]


class RewardListParams(TypedDict, total=False):
    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """Return only this group's rewards (`grp_…`).

    To get Default's rewards, omit `group_id` and keep the rewards whose `group_id` is `None`. An
    ID that is not a group in this program returns `404`.
    """
