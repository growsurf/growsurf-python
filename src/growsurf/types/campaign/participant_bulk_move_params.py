# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ParticipantBulkMoveParams"]


class ParticipantBulkMoveParams(TypedDict, total=False):
    participants: Required[SequenceNotStr[str]]
    """GrowSurf participant IDs and/or email addresses to move.

    Mixed entries are allowed. 1 to 200 entries.
    """

    group_id: Required[Annotated[Optional[str], PropertyInfo(alias="groupId")]]
    """The group to move them to (`grp_…`), or `None` for Default."""
