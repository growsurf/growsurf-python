# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, cast
from typing_extensions import Literal

import httpx

__all__ = [
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
]


class GrowsurfError(Exception):
    pass


class APIError(GrowsurfError):
    message: str
    request: httpx.Request

    body: object | None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:  # noqa: ARG002
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body


class APIResponseValidationError(APIError):
    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, body: object | None, *, message: str | None = None) -> None:
        super().__init__(message or "Data returned by API invalid for expected schema.", response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    # Documented error-body fields. Each is `None` when the body omits it or sends another
    # type; `body` keeps the complete response body, including fields added later.
    error_name: str | None
    """Error name returned for the failed request."""

    error_code: str | None
    """Stable machine-readable error code."""

    error_message: str | None
    """Human-readable error message."""

    errors: List[Dict[str, object]] | None
    """Optional validation details for specific request fields."""

    support_url: str | None
    """Support URL related to the error, when available."""

    policy_name: str | None
    """Rate-limit policy name for `429` errors, when available."""

    level: str | None
    """Error severity level, when available."""

    timestamp: str | None
    """When the error response was created."""

    fraud_risk_level: str | None
    """Fraud risk level assigned to the blocked signup."""

    fraud_reason_code: str | None
    """Machine-readable reason code for the fraud decision."""

    matched_participant_ids: List[str] | None
    """Existing participant IDs related to the fraud match."""

    email: str | None
    """Email address from the blocked signup attempt."""

    referrer_id: str | None
    """Referrer participant ID supplied with the blocked signup, or `null`."""

    ip_address: str | None
    """IP address supplied with the blocked signup, or `null`."""

    fingerprint: str | None
    """Browser fingerprint supplied with the blocked signup, or `null`."""

    blocked_at: str | None
    """When the signup was blocked."""

    def __init__(self, message: str, *, response: httpx.Response, body: object | None) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code

        fields = cast(Dict[str, object], body) if isinstance(body, dict) else {}
        self.error_name = _str_or_none(fields.get("name"))
        self.error_code = _str_or_none(fields.get("code"))
        self.error_message = _str_or_none(fields.get("message"))
        self.errors = _record_list_or_none(fields.get("errors"))
        self.support_url = _str_or_none(fields.get("supportUrl"))
        self.policy_name = _str_or_none(fields.get("policyName"))
        self.level = _str_or_none(fields.get("level"))
        self.timestamp = _str_or_none(fields.get("timestamp"))
        self.fraud_risk_level = _str_or_none(fields.get("fraudRiskLevel"))
        self.fraud_reason_code = _str_or_none(fields.get("fraudReasonCode"))
        self.matched_participant_ids = _str_list_or_none(fields.get("matchedParticipantIds"))
        self.email = _str_or_none(fields.get("email"))
        self.referrer_id = _str_or_none(fields.get("referrerId"))
        self.ip_address = _str_or_none(fields.get("ipAddress"))
        self.fingerprint = _str_or_none(fields.get("fingerprint"))
        self.blocked_at = _str_or_none(fields.get("blockedAt"))


class APIConnectionError(APIError):
    def __init__(self, *, message: str = "Connection error.", request: httpx.Request) -> None:
        super().__init__(message, request, body=None)


class APITimeoutError(APIConnectionError):
    def __init__(self, request: httpx.Request) -> None:
        super().__init__(message="Request timed out.", request=request)


class BadRequestError(APIStatusError):
    status_code: Literal[400] = 400  # pyright: ignore[reportIncompatibleVariableOverride]


class AuthenticationError(APIStatusError):
    status_code: Literal[401] = 401  # pyright: ignore[reportIncompatibleVariableOverride]


class PermissionDeniedError(APIStatusError):
    status_code: Literal[403] = 403  # pyright: ignore[reportIncompatibleVariableOverride]


class NotFoundError(APIStatusError):
    status_code: Literal[404] = 404  # pyright: ignore[reportIncompatibleVariableOverride]


class ConflictError(APIStatusError):
    status_code: Literal[409] = 409  # pyright: ignore[reportIncompatibleVariableOverride]


class UnprocessableEntityError(APIStatusError):
    status_code: Literal[422] = 422  # pyright: ignore[reportIncompatibleVariableOverride]


class RateLimitError(APIStatusError):
    status_code: Literal[429] = 429  # pyright: ignore[reportIncompatibleVariableOverride]


class InternalServerError(APIStatusError):
    pass


def _str_or_none(value: object) -> str | None:
    return value if isinstance(value, str) else None


def _str_list_or_none(value: object) -> List[str] | None:
    if not isinstance(value, list):
        return None
    items = cast(List[object], value)
    if not all(isinstance(item, str) for item in items):
        return None
    return cast(List[str], items)


def _record_list_or_none(value: object) -> List[Dict[str, object]] | None:
    if not isinstance(value, list):
        return None
    items = cast(List[object], value)
    if not all(isinstance(item, dict) for item in items):
        return None
    return cast(List[Dict[str, object]], items)
