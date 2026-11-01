# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomDomainSetParams"]


class CustomDomainSetParams(TypedDict, total=False):
    domain: Required[str]
    """
    The hostname to serve the program's landing pages from, with or without
    `https://`. Up to 255 characters.
    """
