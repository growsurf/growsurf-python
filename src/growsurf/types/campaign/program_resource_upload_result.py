# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, NotRequired

__all__ = ["ProgramResourceUploadResult"]


class ProgramResourceUploadResult(TypedDict):
    """The signed upload fields GrowSurf requires.

    Runtime dictionaries may also contain provider-added fields; the SDK passes them through.
    """

    public_id: str
    version: int
    signature: str
    resource_type: Literal["image", "raw"]
    type: Literal["authenticated"]
    bytes: int
    secure_url: str
    asset_id: NotRequired[str]
    format: NotRequired[str]
