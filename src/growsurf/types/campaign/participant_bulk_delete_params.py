# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ParticipantBulkDeleteParams"]


class ParticipantBulkDeleteParams(TypedDict, total=False):
    participants: Required[SequenceNotStr[str]]
    """GrowSurf participant IDs and/or email addresses to delete.

    Mixed entries are allowed.
    """
