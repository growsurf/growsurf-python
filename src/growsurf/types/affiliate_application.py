# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .affiliate_application_answer import AffiliateApplicationAnswer

__all__ = ["AffiliateApplication"]


class AffiliateApplication(BaseModel):
    id: str
    """Public application ID."""

    answers: List[AffiliateApplicationAnswer]
    """Configurable application responses captured from the saved form.

    Use `fieldId` as the stable question identifier.
    """

    created_at: int = FieldInfo(alias="createdAt")
    """When the application was submitted, as a Unix timestamp in milliseconds."""

    decided_at: Optional[int] = FieldInfo(alias="decidedAt")
    """When the decision was made, in Unix milliseconds, or `null` while pending."""

    email: Optional[str]
    """Required applicant email address.

    `null` after applicant data is removed under the Program's retention policy.
    """

    first_name: Optional[str] = FieldInfo(alias="firstName")
    """Required applicant first name, or `null` after retention removal."""

    last_name: Optional[str] = FieldInfo(alias="lastName")
    """Required applicant last name, or `null` after retention removal."""

    participant_id: Optional[str] = FieldInfo(alias="participantId")
    """Public participant ID created or upgraded by approval, or `null` before approval."""

    reapply_allowed_at: Optional[int] = FieldInfo(alias="reapplyAllowedAt")
    """When a denied applicant may apply again, in Unix milliseconds.

    `null` when not applicable.
    """

    rejection_reason: Optional[str] = FieldInfo(alias="rejectionReason")
    """Reason recorded when the application was denied, or `null` before denial."""

    reviewed_at: Optional[int] = FieldInfo(alias="reviewedAt")
    """When the application was reviewed, in Unix milliseconds, or `null` while pending."""

    risk_level: Optional[Literal["LOW", "MEDIUM", "HIGH"]] = FieldInfo(alias="riskLevel")
    """GrowSurf risk assessment.

    Applications that are not `LOW` risk are held for manual review.
    """

    status: Literal["PENDING", "APPROVED", "DENIED"]
    """Where the application is in review. Only `PENDING` applications can be decided."""

    terms_accepted_at: Optional[int] = FieldInfo(alias="termsAcceptedAt")
    """When the applicant accepted the Program Terms, or `null` when not required."""
