# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignEmails"]

# A program's email configuration (the dashboard Program Editor's Emails tab):
# each editable email template plus the shared `settings` block. The set of
# templates depends on the program type; it is intentionally modeled as a loose
# object. See the API reference for the full field list:
# https://docs.growsurf.com/developer-tools/rest-api
CampaignEmails: TypeAlias = Dict[str, object]
