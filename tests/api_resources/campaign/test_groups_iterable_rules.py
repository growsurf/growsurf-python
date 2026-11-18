# Regression: `rules` accepts any Iterable, so iterators and generators must be
# sent as JSON arrays instead of failing before the request.
from __future__ import annotations

import os
import json

import httpx
import pytest
from respx import MockRouter

from growsurf import Growsurf, AsyncGrowsurf

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

RULES = [{"type": "EMAIL", "value": "a@hooli.com"}, {"type": "DOMAIN", "value": "hooli.com"}]
GROUP = {
    "id": "g1",
    "createdAt": 0,
    "name": "VIP",
    "order": 0,
    "rules": RULES,
    "signupCode": "VIP",
    "updatedAt": 0,
}


def _rule_inputs():
    yield "iterator", lambda: iter(RULES)
    yield "generator", lambda: (rule for rule in RULES)
    yield "tuple", lambda: tuple(RULES)


@pytest.mark.parametrize("make_rules", [m for _, m in _rule_inputs()], ids=[n for n, _ in _rule_inputs()])
@pytest.mark.respx(base_url=base_url)
def test_update_sends_iterable_rules_as_list(client: Growsurf, respx_mock: MockRouter, make_rules) -> None:
    route = respx_mock.patch("/campaign/c1/groups/g1").mock(return_value=httpx.Response(200, json=GROUP))
    client.campaign.groups.update(group_id="g1", id="c1", rules=make_rules())
    assert json.loads(route.calls.last.request.content)["rules"] == RULES


@pytest.mark.parametrize("make_rules", [m for _, m in _rule_inputs()], ids=[n for n, _ in _rule_inputs()])
@pytest.mark.respx(base_url=base_url)
async def test_async_update_sends_iterable_rules_as_list(
    async_client: AsyncGrowsurf, respx_mock: MockRouter, make_rules
) -> None:
    route = respx_mock.patch("/campaign/c1/groups/g1").mock(return_value=httpx.Response(200, json=GROUP))
    await async_client.campaign.groups.update(group_id="g1", id="c1", rules=make_rules())
    assert json.loads(route.calls.last.request.content)["rules"] == RULES
