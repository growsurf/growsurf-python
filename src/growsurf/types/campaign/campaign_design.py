# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignDesign"]

# A program's design configuration. It includes the dashboard Program Editor's
# Design tab and the payout-destination confirmation page copy configured from
# payout integration cards. The exact fields available depend on the program type
# (for example, `referralSummary` is referral-only, while `affiliateSummary`,
# `commissions`, and `payouts` are affiliate-only). `participantSettings` is
# available to both program types; its manual payout and Wise fields are
# affiliate-only. `GET` returns the fields configured for the program;
# `payoutDestinationConfirmation` is omitted when no confirmation fields are
# stored. Stored `null` fields are returned as `null`; omitted and `null` fields
# use localized defaults. `PATCH` back only the sections or fields you want to
# change (arrays such as `signup.fields` replace wholesale). It is intentionally
# modeled as a loose object.
CampaignDesign: TypeAlias = Dict[str, object]
