# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignListParticipantsParams"]


class CampaignListParticipantsParams(TypedDict, total=False):
    limit: int
    """Number of results to return. Maximum 100."""

    metadata: Dict[str, str]
    """
    Return only participants whose metadata matches every given key and value
    exactly. Send each pair as `metadata[key]=value`. Up to 3 keys per request.
    Values compare as strings, which is how metadata is stored.
    """

    next_id: Annotated[str, PropertyInfo(alias="nextId")]
    """ID to start the next paged result set with."""
