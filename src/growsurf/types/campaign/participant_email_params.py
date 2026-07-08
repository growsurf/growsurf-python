# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantEmailParams"]


class ParticipantEmailParams(TypedDict, total=False):
    id: Required[str]

    email_type: Annotated[str, PropertyInfo(alias="emailType")]
    """The program email template to trigger (template mode).

    The valid values depend on the program type; the template's `isEnabled` setting only
    controls automatic sends. Referral programs: `welcomeNonReferred`, `referralLinkViewedFirstTime`,
    `referralLinkUsed`, `referredSignup`, `welcomeReferred`, `goalAchieved`,
    `campaignEndedWinners`, `campaignEndedNonWinners`, `progressUpdateMonthly`. Affiliate
    programs: `welcomeNonReferred`, `referralLinkViewedFirstTime`, `referredSignup`,
    `commissionGenerated`, `commissionAdjusted`, `payoutPending`, `payoutSentSuccess`,
    `progressUpdateMonthly`. System/transactional types (login link, PayPal confirmation,
    tax) and the invite email cannot be sent.
    """

    body: str
    """HTML body for a free-form email. You can personalize it with dynamic text, inserting `{{...}}` tokens like `{{firstName}}` or `{{shareUrl}}`. See [Guide to using dynamic text in GrowSurf emails](https://support.growsurf.com/article/213-guide-to-using-dynamic-text-in-growsurf-emails)."""

    preheader: str
    """Optional preheader text for a free-form email."""

    subject: str
    """Subject line for a free-form email. Supports dynamic text (`{{...}}` tokens), the same as the body."""
