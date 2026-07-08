# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    email: Required[str]
    """The email address for the new account.

    Personal emails and disposable email addresses are not accepted.
    """

    company: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
