# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailAnalytics", "EmailAnalyticsByType", "EmailAnalyticsCounts"]


class EmailAnalyticsCounts(BaseModel):
    sent: int
    delivered: int
    opened: int
    clicked: int
    bounced: int
    spam_complaints: int = FieldInfo(alias="spamComplaints")


class EmailAnalyticsByType(EmailAnalyticsCounts):
    email_type: str = FieldInfo(alias="emailType")
    delivery_rate: float = FieldInfo(alias="deliveryRate")
    open_rate: float = FieldInfo(alias="openRate")
    click_rate: float = FieldInfo(alias="clickRate")
    bounce_rate: float = FieldInfo(alias="bounceRate")


class EmailAnalytics(EmailAnalyticsCounts):
    delivery_rate: float = FieldInfo(alias="deliveryRate")
    open_rate: float = FieldInfo(alias="openRate")
    click_rate: float = FieldInfo(alias="clickRate")
    bounce_rate: float = FieldInfo(alias="bounceRate")
    by_type: List[EmailAnalyticsByType] = FieldInfo(alias="byType")
    coverage_start_date: Optional[int] = FieldInfo(alias="coverageStartDate")
    is_partial: bool = FieldInfo(alias="isPartial")
