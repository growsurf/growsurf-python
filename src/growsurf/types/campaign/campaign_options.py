# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignOptions"]

# A program's options (the dashboard Program Editor's Options tab): reward/fraud
# approval, anti-fraud lists + toggles, the `LAST_CLICK` or `FIRST_CLICK`
# attribution model, referral windows, reCAPTCHA, affiliate enrollment +
# application review, payout + tax settings (affiliate only), and notification-
# email settings. It is intentionally modeled as a loose object. To see the full
# object with every field and its current value, `GET` the resource, then `PATCH`
# back only the fields you want to change.
CampaignOptions: TypeAlias = Dict[str, object]
