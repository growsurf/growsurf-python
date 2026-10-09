# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["Language"]

# A language a program can run in. Participants see the portal and receive program
# emails in their language.
Language: TypeAlias = Literal["en", "es", "fr", "de", "it", "pt-BR", "nl", "pl", "sv", "tr", "ja", "ko", "zh-CN", "id"]
