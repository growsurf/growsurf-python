# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .affiliate_application import AffiliateApplication

__all__ = ["AffiliateApplicationListResponse"]


class AffiliateApplicationListResponse(BaseModel):
    applications: List[AffiliateApplication]
    """One page of the program's applications, newest first."""

    total: int
    """Total number of applications matching the filter."""

    limit: Optional[int] = None
    """The page size used."""

    offset: Optional[int] = None
    """The offset this page started at."""
