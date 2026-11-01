# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CampaignCustomDomain", "CampaignCustomDomainDNSRecord"]


class CampaignCustomDomainDNSRecord(BaseModel):
    name: str
    """The hostname the record is for."""

    type: Literal["CNAME"]
    """The record type. Always `CNAME`."""

    value: str
    """The record's target."""


class CampaignCustomDomain(BaseModel):
    """The custom domain that serves a program's landing pages."""

    created_at: Optional[int] = FieldInfo(alias="createdAt", default=None)
    """When the domain was set, in epoch milliseconds. `null` when no domain is set."""

    dns_record: Optional[CampaignCustomDomainDNSRecord] = FieldInfo(alias="dnsRecord", default=None)
    """The DNS record to add at your DNS provider. `null` when no domain is set."""

    domain: Optional[str] = None
    """The custom domain, or `null` when none is set."""

    is_verified: bool = FieldInfo(alias="isVerified")
    """
    Whether the domain's `CNAME` record pointed to `dnsRecord.value` at the last
    check. Landing pages load on the domain only when this is `true`.
    """

    updated_at: Optional[int] = FieldInfo(alias="updatedAt", default=None)
    """
    When the domain record last changed, in epoch milliseconds. `null` when no
    domain is set.
    """

    verified_at: Optional[int] = FieldInfo(alias="verifiedAt", default=None)
    """When the DNS check passed, in epoch milliseconds. `null` while unverified."""
