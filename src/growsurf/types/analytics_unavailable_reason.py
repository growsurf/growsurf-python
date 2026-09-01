# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AnalyticsUnavailableReason"]

AnalyticsUnavailableReason: TypeAlias = Literal[
    "COVERAGE_UNAVAILABLE",
    "PRE_COVERAGE",
    "PARTIAL_COVERAGE",
    "INSUFFICIENT_COVERAGE",
    "EMPTY_DENOMINATOR",
    "QUERY_LIMIT_EXCEEDED",
    "PARTICIPANT_NOT_ELIGIBLE",
]
