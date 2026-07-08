# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    company: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
