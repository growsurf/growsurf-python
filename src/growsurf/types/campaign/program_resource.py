# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProgramResource", "ProgramResourceFile"]


class ProgramResourceFile(BaseModel):
    file_name: str = FieldInfo(alias="fileName")
    mime_type: str = FieldInfo(alias="mimeType")
    bytes: int
    format: str
    moderation_status: Literal["PENDING", "APPROVED", "REJECTED"] = FieldInfo(alias="moderationStatus")


class ProgramResource(BaseModel):
    id: str
    type: Literal["FILE", "LINK", "TEXT"]
    title: str
    description: Optional[str] = FieldInfo(default=...)
    category: Optional[str] = FieldInfo(default=...)
    url: Optional[str] = FieldInfo(default=...)
    text: Optional[str] = FieldInfo(default=...)
    file: Optional[ProgramResourceFile] = FieldInfo(default=...)
    is_published: bool = FieldInfo(alias="isPublished")
    position: int
    created_at: int = FieldInfo(alias="createdAt")
    """Unix time in milliseconds when the resource was created."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """Unix time in milliseconds when the resource was last updated."""
