from growsurf.types import EmailAnalytics
from growsurf.types.campaign import ParticipantAnalyticsParams


def test_email_analytics_model_and_participant_include() -> None:
    analytics = EmailAnalytics(
        sent=2,
        delivered=1,
        opened=1,
        clicked=0,
        bounced=1,
        spamComplaints=0,
        deliveryRate=0.5,
        openRate=1,
        clickRate=0,
        bounceRate=0.5,
        byType=[],
        coverageStartDate=None,
        isPartial=False,
    )
    params: ParticipantAnalyticsParams = {"id": "campaign", "include": "email,futureEnrichment"}

    assert analytics.sent == 2
    assert params["include"] == "email,futureEnrichment"
