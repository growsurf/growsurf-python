# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union

from pydantic import Field as FieldInfo, StrictInt, StrictStr, StrictBool, StrictFloat

from ..._models import BaseModel

__all__ = ["ProgramResourceUploadTicket"]


class ProgramResourceUploadTicket(BaseModel):
    ticket: str
    expires_in: int = FieldInfo(alias="expiresIn")
    upload_url: str = FieldInfo(alias="uploadUrl")
    upload_parameters: Dict[str, Union[StrictStr, StrictInt, StrictFloat, StrictBool]] = FieldInfo(
        alias="uploadParameters"
    )
    """Opaque signed scalar fields that must be sent unchanged with the file upload."""
