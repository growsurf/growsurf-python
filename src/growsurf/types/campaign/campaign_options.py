# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignOptions"]

# A program's options (the dashboard Program Editor's Options tab): reward/fraud
# approval, anti-fraud lists + toggles, referral windows, reCAPTCHA, payout +
# tax settings (affiliate only), and notification-email settings. It is
# intentionally modeled as a loose object. See the API reference for the full
# field list: https://docs.growsurf.com/developer-tools/rest-api
CampaignOptions: TypeAlias = Dict[str, object]
