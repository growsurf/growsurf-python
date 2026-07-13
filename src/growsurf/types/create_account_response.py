# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateAccountResponse"]


class CreateAccountResponse(BaseModel):
    email: str
    """Email address for the new account."""

    api_key: str = FieldInfo(alias="apiKey")
    """An API key for the new account.

    Use it as the `Bearer` token on subsequent requests. It is shown once, locked
    (`403` `EMAIL_NOT_VERIFIED_ERROR`) until the account's email is verified, and
    rotated when the account owner first signs in to the GrowSurf dashboard.
    """

    verification_status: Literal["NOT_REQUESTED", "REQUESTED", "VERIFIED"] = FieldInfo(alias="verificationStatus")
    """GrowSurf team verification state.

    `VERIFIED` is required before a program can send participant emails.
    """
