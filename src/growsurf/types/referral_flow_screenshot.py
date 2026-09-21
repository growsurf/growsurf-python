# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReferralFlowScreenshot"]


class ReferralFlowScreenshot(BaseModel):
    view: Literal["referrer", "referredFriend"]
    """Which side of the referral flow the image shows."""

    label: str
    """Short human-readable name for the view, such as `Referrer window`."""

    url: str
    """Private URL of the image. It stops working at `expiresAt`."""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """ISO 8601 time after which `url` no longer resolves."""

    width: int
    """Image width in pixels."""

    height: int
    """Image height in pixels."""

    content_type: str = FieldInfo(alias="contentType")
    """MIME type of the image."""
