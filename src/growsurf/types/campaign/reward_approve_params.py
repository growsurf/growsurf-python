# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RewardApproveParams"]


class RewardApproveParams(TypedDict, total=False):
    id: Required[str]

    fulfill: bool
    """Set true to mark the reward as fulfilled after approval."""
