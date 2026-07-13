# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Required, TypedDict

__all__ = ["TeamUpdateParams"]


class TeamUpdateParams(TypedDict, total=False):
    name: Required[str]
    """The team's display name."""
