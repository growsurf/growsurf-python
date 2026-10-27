# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantEmailParams"]


class ParticipantEmailParams(TypedDict, total=False):
    id: Required[str]

    email_type: Annotated[str, PropertyInfo(alias="emailType")]
    """The program email template to trigger (template mode).

    Send the camelCase email-type key. The available types depend on the program type;
    the template's `isEnabled` setting controls automatic sends only. This endpoint can
    trigger any sendable template. System and transactional types (login link, payout
    destination confirmation, tax notifications), the invite email, and the follow-up
    reminder cannot be sent. Referral programs: `welcomeNonReferred`,
    `referralLinkViewedFirstTime`, `referralLinkUsed`, `referredSignup`,
    `welcomeReferred`, `offerClaimed`, `goalAchieved`, `campaignEndedWinners`,
    `campaignEndedNonWinners`, `progressUpdateMonthly`. Affiliate programs:
    `welcomeNonReferred`, `referralLinkViewedFirstTime`, `referredSignup`,
    `offerClaimed`, `commissionGenerated`, `commissionAdjusted`, `payoutPending`,
    `payoutSentSuccess`, `progressUpdateMonthly`.
    `welcomeNonReferred` can only be sent to advocates or approved, enrolled affiliates in a program
    that has not ended.
    """

    body: str
    """HTML body for a free-form email. You can personalize it with dynamic text, inserting `{{...}}` tokens like `{{firstName}}` or `{{shareUrl}}`. See [Guide to using dynamic text in GrowSurf emails](https://support.growsurf.com/article/213-guide-to-using-dynamic-text-in-growsurf-emails)."""

    preheader: str
    """Optional preheader text for a free-form email."""

    subject: str
    """Subject line for a free-form email. Supports dynamic text (`{{...}}` tokens), the same as the body."""
