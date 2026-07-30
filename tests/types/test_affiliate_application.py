from growsurf.types.affiliate_application import AffiliateApplication
from growsurf.types.affiliate_application_answer import AffiliateApplicationAnswer


def test_affiliate_application_uses_answer_only_scalar_contract() -> None:
    application = AffiliateApplication(
        id="app_123",
        answers=[
            AffiliateApplicationAnswer(
                fieldId="primaryChannelUrl",
                label="Website or social media channel",
                type="url",
                value="https://aviato.com",
            ),
            AffiliateApplicationAnswer(
                fieldId="acceptRules",
                label="Accept rules",
                type="checkbox",
                value=True,
            ),
        ],
        createdAt=1752710400000,
        decidedAt=None,
        email=None,
        firstName=None,
        lastName=None,
        participantId=None,
        reapplyAllowedAt=None,
        rejectionReason=None,
        reviewedAt=None,
        riskLevel=None,
        status="PENDING",
        termsAcceptedAt=None,
    )

    payload = application.model_dump(by_alias=True)
    assert payload["answers"][0]["fieldId"] == "primaryChannelUrl"
    assert "websiteUrl" not in payload
    assert "promotionChannels" not in payload


def test_affiliate_application_answer_preserves_scalar_json_types() -> None:
    values = ["text", 42, 4.25, True, False]

    parsed = [
        AffiliateApplicationAnswer(
            fieldId=f"field_{index}",
            label="Question",
            type="checkbox" if isinstance(value, bool) else "number",
            value=value,
        ).value
        for index, value in enumerate(values)
    ]

    assert parsed == values
    assert [type(value) for value in parsed] == [str, int, float, bool, bool]
