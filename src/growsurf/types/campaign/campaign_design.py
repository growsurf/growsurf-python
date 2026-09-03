# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Literal
from typing_extensions import TypeAlias, TypedDict

__all__ = ["CampaignDesign", "CampaignDesignResources", "CampaignDesignResourcesIcon"]


class CampaignDesignResourcesIcon(TypedDict, total=False):
    """Icon configuration for the participant Resources destination."""

    type: Literal["DEFAULT", "IMAGE", "NONE"]
    """Use the default icon, a configured image, or no icon."""

    imageUrl: str
    """LIST-mode icon image URL when `type` is `IMAGE`. Maximum 500 characters."""


class CampaignDesignResources(TypedDict, total=False):
    """Participant presentation settings for Resources; resource items use Program Resources operations."""

    isPublicDisplayed: bool
    """Enables the destination. It stays hidden until at least one valid resource is published."""

    title: str
    """Participant-visible section title. Maximum 100 characters."""

    viewResourcesLinkText: str
    """LIST-mode row text. Maximum 100 characters."""

    backLinkText: str
    """LIST-mode detail Back text. Maximum 100 characters."""

    copyButtonText: str
    """TEXT resource copy action. Maximum 100 characters."""

    copiedText: str
    """TEXT resource copy confirmation. Maximum 100 characters."""

    emptyState: str
    """Shown in place of the list when no resources are published. Maximum 500 characters."""

    icon: CampaignDesignResourcesIcon
    """Icon configuration for the destination."""

# A program's design configuration. It includes the dashboard Program Editor's
# Design tab and the payout-destination confirmation page copy configured from
# payout integration cards. The exact fields available depend on the program type
# (for example, `referralSummary` is referral-only, while `affiliateSummary`,
# `commissions`, and `payouts` are affiliate-only). `participantSettings` is
# available to both program types; its manual payout and Wise fields are
# affiliate-only. `referredExperience` includes the Claim Offer Popup for both
# program types, with its colors under `theme.referredExperienceOfferPopup`.
# `GET` returns the fields configured for the program;
# `payoutDestinationConfirmation` is omitted when no confirmation fields are
# stored. Stored `null` fields are returned as `null`; omitted and `null` fields
# use localized defaults. `PATCH` back only the sections or fields you want to
# change (arrays such as `signup.fields` replace wholesale).
# `participantAvatarStyle` accepts `CHARACTERS`, `INITIALS`, `ANIMALS`, or
# `GRADIENT`; new programs use `CHARACTERS`, while missing or unknown stored
# values return `INITIALS`. `resources` uses `CampaignDesignResources` and controls
# participant presentation; resource items use the Program Resources operations. The
# top-level Design object remains intentionally loose so other current and future sections
# pass through unchanged.
CampaignDesign: TypeAlias = Dict[str, object]
