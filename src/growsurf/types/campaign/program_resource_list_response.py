# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .program_resource import ProgramResource

__all__ = ["ProgramResourceListResponse"]


class ProgramResourceListResponse(BaseModel):
    resources: List[ProgramResource]
