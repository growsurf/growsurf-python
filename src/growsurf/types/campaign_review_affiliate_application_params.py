# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CampaignReviewAffiliateApplicationParams"]


class CampaignReviewAffiliateApplicationParams(TypedDict, total=False):
    """Either decide a pending application with `status`, or move a denied application's
    reapplication window with `reapply_allowed_at`.

    Provide exactly one of those fields.
    """

    id: Required[str]

    allow_immediate_reapply: Annotated[bool, PropertyInfo(alias="allowImmediateReapply")]
    """When denying, let the applicant reapply right away instead of waiting out the
    program's reapplication cooldown.

    Only valid when `status` is `DENIED`.
    """

    reapply_allowed_at: Annotated[int, PropertyInfo(alias="reapplyAllowedAt")]
    """For an already-denied application, move the reapplication window to this earlier
    time, in Unix milliseconds.

    Send without `status`.
    """

    rejection_reason: Annotated[str, PropertyInfo(alias="rejectionReason")]
    """Short reason recorded with a denial.

    Only valid when `status` is `DENIED`. Maximum 255 characters.
    """

    review_note: Annotated[str, PropertyInfo(alias="reviewNote")]
    """Private note recorded with a denial.

    Only valid when `status` is `DENIED`; never shown to the applicant. Maximum 500
    characters.
    """

    status: Literal["APPROVED", "DENIED"]
    """The decision.

    `APPROVED` enrolls the applicant as an affiliate; `DENIED` closes the
    application.
    """
