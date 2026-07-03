# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignInstallation"]

# A program's installation configuration (the dashboard Program Editor's
# Installation tab, plus Mobile SDK settings): referral trigger, signup
# tracking, share URL + whitelist, custom-form signup, and mobile SDK settings.
# It is intentionally modeled as a loose object. See the API reference for the
# full field list: https://docs.growsurf.com/developer-tools/rest-api
CampaignInstallation: TypeAlias = Dict[str, object]
