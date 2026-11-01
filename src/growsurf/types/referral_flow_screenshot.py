# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReferralFlowScreenshot"]


class ReferralFlowScreenshot(BaseModel):
    view: Optional[Literal["referrer", "referredFriend"]] = None
    """Which side of the referral flow the image shows."""

    label: Optional[str] = None
    """Short human-readable name for the view, such as `Referrer window`."""

    url: Optional[str] = None
    """Private URL of the image. It stops working at `expiresAt`."""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """ISO 8601 time after which `url` no longer resolves."""

    width: Optional[int] = None
    """Image width in pixels."""

    height: Optional[int] = None
    """Image height in pixels."""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """MIME type of the image."""
