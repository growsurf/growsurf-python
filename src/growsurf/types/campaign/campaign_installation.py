# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignInstallation"]

# A program's installation configuration (the dashboard Program Editor's
# Installation tab, plus Mobile SDK settings): referral trigger, signup
# tracking, share URL + whitelist, custom-form signup, and mobile SDK settings.
# It is intentionally modeled as a loose object. To see the full object with
# every field and its current value, `GET` the resource, then `PATCH` back only
# the fields you want to change.
CampaignInstallation: TypeAlias = Dict[str, object]
