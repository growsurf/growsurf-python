from __future__ import annotations

import json

import httpx
import pytest
from respx import MockRouter

from growsurf import Growsurf, AsyncGrowsurf
from tests.utils import assert_matches_type
from growsurf.types.campaign import CampaignCustomDomain, DeleteCampaignCustomDomainResponse

from ...conftest import base_url

UNVERIFIED = {
    "domain": "https://refer.piedpiper.com",
    "isVerified": False,
    "verifiedAt": None,
    "dnsRecord": {"type": "CNAME", "name": "refer.piedpiper.com", "value": "grow.surf"},
    "createdAt": 1761955200000,
    "updatedAt": 1761955200000,
}
VERIFIED = {**UNVERIFIED, "isVerified": True, "verifiedAt": 1761955260000}
EMPTY = {
    "domain": None,
    "isVerified": False,
    "verifiedAt": None,
    "dnsRecord": None,
    "createdAt": None,
    "updatedAt": None,
}
DELETED = {"domain": "https://refer.piedpiper.com", "success": True}


class TestCustomDomain:
    @pytest.mark.respx(base_url=base_url)
    def test_retrieve_without_domain(self, client: Growsurf, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/campaign/abc123/custom-domain").mock(return_value=httpx.Response(200, json=EMPTY))

        custom_domain = client.campaign.custom_domain.retrieve("abc123")

        assert route.called
        assert_matches_type(CampaignCustomDomain, custom_domain, path=["response"])
        assert custom_domain.domain is None
        assert custom_domain.dns_record is None

    @pytest.mark.respx(base_url=base_url)
    def test_set_uses_put(self, client: Growsurf, respx_mock: MockRouter) -> None:
        route = respx_mock.put("/campaign/abc123/custom-domain").mock(return_value=httpx.Response(200, json=UNVERIFIED))

        custom_domain = client.campaign.custom_domain.set("abc123", domain="refer.piedpiper.com")

        assert json.loads(route.calls.last.request.content) == {"domain": "refer.piedpiper.com"}
        assert custom_domain.is_verified is False
        assert custom_domain.dns_record is not None
        assert custom_domain.dns_record.type == "CNAME"
        assert custom_domain.dns_record.value == "grow.surf"

    @pytest.mark.respx(base_url=base_url)
    def test_verify(self, client: Growsurf, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/campaign/abc123/custom-domain/verify").mock(
            return_value=httpx.Response(200, json=VERIFIED)
        )

        custom_domain = client.campaign.custom_domain.verify("abc123")

        assert route.called
        assert custom_domain.is_verified is True
        assert custom_domain.verified_at == 1761955260000

    @pytest.mark.respx(base_url=base_url)
    def test_delete(self, client: Growsurf, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/campaign/abc123/custom-domain").mock(return_value=httpx.Response(200, json=DELETED))

        deleted = client.campaign.custom_domain.delete("abc123")

        assert route.called
        assert_matches_type(DeleteCampaignCustomDomainResponse, deleted, path=["response"])
        assert deleted.success is True

    @pytest.mark.respx(base_url=base_url)
    def test_raw_and_streaming_responses(self, client: Growsurf, respx_mock: MockRouter) -> None:
        respx_mock.put("/campaign/abc123/custom-domain").mock(return_value=httpx.Response(200, json=UNVERIFIED))

        response = client.campaign.with_raw_response.custom_domain.set("abc123", domain="refer.piedpiper.com")
        assert response.is_closed is True
        assert response.parse().domain == "https://refer.piedpiper.com"

        with client.campaign.with_streaming_response.custom_domain.set(
            "abc123", domain="refer.piedpiper.com"
        ) as streamed:
            assert not streamed.is_closed
            assert streamed.parse().domain == "https://refer.piedpiper.com"
        assert streamed.is_closed

    @pytest.mark.parametrize("method", ["retrieve", "verify", "delete"])
    def test_path_params(self, client: Growsurf, method: str) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            getattr(client.campaign.custom_domain, method)("")

    def test_path_params_set(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.campaign.custom_domain.set("", domain="refer.piedpiper.com")


class TestAsyncCustomDomain:
    @pytest.mark.respx(base_url=base_url)
    async def test_all_methods(self, async_client: AsyncGrowsurf, respx_mock: MockRouter) -> None:
        path = "/campaign/abc123/custom-domain"
        respx_mock.get(path).mock(return_value=httpx.Response(200, json=EMPTY))
        put = respx_mock.put(path).mock(return_value=httpx.Response(200, json=UNVERIFIED))
        respx_mock.post(f"{path}/verify").mock(return_value=httpx.Response(200, json=VERIFIED))
        respx_mock.delete(path).mock(return_value=httpx.Response(200, json=DELETED))

        assert (await async_client.campaign.custom_domain.retrieve("abc123")).domain is None
        assert (
            await async_client.campaign.custom_domain.set("abc123", domain="refer.piedpiper.com")
        ).is_verified is False
        assert json.loads(put.calls.last.request.content) == {"domain": "refer.piedpiper.com"}
        assert (await async_client.campaign.custom_domain.verify("abc123")).is_verified is True
        assert (await async_client.campaign.custom_domain.delete("abc123")).success is True

    async def test_path_params(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.custom_domain.retrieve("")
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.campaign.custom_domain.set("", domain="refer.piedpiper.com")
