# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RotateApiKeyResponse"]


class RotateApiKeyResponse(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")
    """The new API key. Store it now; the key used for rotation stops working immediately."""
