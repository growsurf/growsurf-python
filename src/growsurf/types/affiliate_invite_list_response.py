# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .affiliate_invite import AffiliateInvite

__all__ = ["AffiliateInviteListResponse"]


class AffiliateInviteListResponse(BaseModel):
    invites: List[AffiliateInvite]
    """One page of the program's invites, newest first."""

    total: int
    """Total number of invites matching the filter."""

    limit: Optional[int] = None
    """The page size used."""

    offset: Optional[int] = None
    """The offset this page started at."""
