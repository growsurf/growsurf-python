# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DeleteCampaignCustomDomainResponse"]


class DeleteCampaignCustomDomainResponse(BaseModel):
    domain: str
    """The custom domain that was removed."""

    success: bool
    """Whether the custom domain was removed."""
