from __future__ import annotations

from importlib import import_module

import httpx
import pytest
from respx import MockRouter

from growsurf import Growsurf
from growsurf.types import CreateAccountResponse
from growsurf._compat import get_model_fields

from ..conftest import base_url


@pytest.mark.respx(base_url=base_url)
def test_final_team_request_paths(client: Growsurf, respx_mock: MockRouter) -> None:
    team_response = {
        "name": "Pied Piper",
        "verificationStatus": "VERIFIED",
        "verificationRequestedAt": 1719792000000,
    }
    retrieve = respx_mock.get("/team").mock(return_value=httpx.Response(200, json=team_response))
    update = respx_mock.patch("/team").mock(return_value=httpx.Response(200, json=team_response))
    request_verification = respx_mock.post("/team/verification-request").mock(
        return_value=httpx.Response(200, json=team_response)
    )
    resend_email = respx_mock.post("/team/owner/verification-email").mock(
        return_value=httpx.Response(200, json={"success": True, "status": "SENT"})
    )
    rotate = respx_mock.post("/api-key/rotate").mock(
        return_value=httpx.Response(200, json={"apiKey": "sk_api_replacement"})
    )

    assert client.team.retrieve().name == "Pied Piper"
    client.team.update(name="Pied Piper Labs")
    client.team.request_verification()
    client.team.resend_owner_verification_email()
    assert client.team.rotate_api_key().api_key == "sk_api_replacement"

    assert retrieve.called
    assert update.calls.last.request.content == b'{"name":"Pied Piper Labs"}'
    assert request_verification.called
    assert resend_email.called
    assert rotate.called


def test_safe_team_and_onboarding_models() -> None:
    team_type = import_module("growsurf.types.team").Team

    assert set(get_model_fields(team_type)) == {
        "name",
        "verification_status",
        "verification_requested_at",
    }
    assert set(get_model_fields(CreateAccountResponse)) == {
        "email",
        "api_key",
        "verification_status",
    }
