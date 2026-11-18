# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RewardGroupSource"]

RewardGroupSource: TypeAlias = Literal["MANUAL", "LINK", "EMAIL", "DOMAIN"]
"""How a participant got into their group.

`MANUAL` — a move (a `PARTICIPANT` rule, Update participant, bulk move, or the
dashboard), including a move to Default. `LINK` — the group's signup link.
`EMAIL` — an `EMAIL` rule. `DOMAIN` — a `DOMAIN` rule.
"""
