# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RotateApiKeyResponse"]


class RotateApiKeyResponse(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")
    """The new API key. The previous key is revoked immediately."""
