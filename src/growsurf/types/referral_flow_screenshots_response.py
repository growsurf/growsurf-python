# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReferralFlowScreenshotsResponse", "ReferralFlowScreenshot"]


class ReferralFlowScreenshot(BaseModel):
    view: Literal["referrer", "referredFriend"]
    """The referral-flow view captured in this screenshot."""

    url: str
    """Image URL for the generated screenshot."""

    width: int
    """Screenshot viewport width in CSS pixels."""

    height: int
    """Screenshot viewport height in CSS pixels."""


class ReferralFlowScreenshotsResponse(BaseModel):
    referrer: ReferralFlowScreenshot
    """Screenshot of the referral flow as a signed-in referrer sees it."""

    referred_friend: ReferralFlowScreenshot = FieldInfo(alias="referredFriend")
    """Screenshot of the referral flow as the referred friend sees it."""

    generated_at: int = FieldInfo(alias="generatedAt")
    """When the screenshots were generated, as a Unix timestamp in milliseconds."""
