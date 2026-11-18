# Regression: `rules` accepts any Iterable, so iterators and generators must be
# sent as JSON arrays instead of failing before the request.
from __future__ import annotations

import os
import json
from typing import Any, Dict, List, Callable, Iterable

import httpx
import pytest
from respx import MockRouter

from growsurf import Growsurf, AsyncGrowsurf
from growsurf.types.campaign.reward_group_rule_param import RewardGroupRuleParam

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

RULES: List[RewardGroupRuleParam] = [
    {"type": "EMAIL", "value": "a@hooli.com"},
    {"type": "DOMAIN", "value": "hooli.com"},
]
GROUP: Dict[str, Any] = {
    "id": "g1",
    "createdAt": 0,
    "name": "VIP",
    "order": 0,
    "rules": RULES,
    "signupCode": "VIP",
    "updatedAt": 0,
}

MakeRules = Callable[[], Iterable[RewardGroupRuleParam]]
RULE_INPUTS: List[MakeRules] = [
    lambda: iter(RULES),
    lambda: (rule for rule in RULES),
    lambda: tuple(RULES),
]
IDS = ["iterator", "generator", "tuple"]


@pytest.mark.parametrize("make_rules", RULE_INPUTS, ids=IDS)
@pytest.mark.respx(base_url=base_url)
def test_update_sends_iterable_rules_as_list(client: Growsurf, respx_mock: MockRouter, make_rules: MakeRules) -> None:
    route = respx_mock.patch("/campaign/c1/groups/g1").mock(return_value=httpx.Response(200, json=GROUP))
    client.campaign.groups.update(group_id="g1", id="c1", rules=make_rules())
    assert json.loads(route.calls.last.request.content)["rules"] == RULES


@pytest.mark.parametrize("make_rules", RULE_INPUTS, ids=IDS)
@pytest.mark.respx(base_url=base_url)
async def test_async_update_sends_iterable_rules_as_list(
    async_client: AsyncGrowsurf, respx_mock: MockRouter, make_rules: MakeRules
) -> None:
    route = respx_mock.patch("/campaign/c1/groups/g1").mock(return_value=httpx.Response(200, json=GROUP))
    await async_client.campaign.groups.update(group_id="g1", id="c1", rules=make_rules())
    assert json.loads(route.calls.last.request.content)["rules"] == RULES
