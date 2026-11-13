# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RewardGroupRuleParam"]


class RewardGroupRuleParam(TypedDict, total=False):
    type: Required[Literal["PARTICIPANT", "EMAIL", "DOMAIN"]]
    """The kind of rule: an existing participant ID, an exact email, or a company domain."""

    value: Required[str]
    """The participant ID, email address, or domain. 1 to 254 characters."""
