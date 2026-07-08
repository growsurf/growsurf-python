# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookTestResponse", "Response"]


class Response(BaseModel):
    msg: Optional[str] = None

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)


class WebhookTestResponse(BaseModel):
    success: bool

    payload: Optional[Dict[str, object]] = None
    """The mock event payload that was sent."""

    response: Optional[Response] = None
