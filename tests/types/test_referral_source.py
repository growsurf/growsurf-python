from typing import get_args

from growsurf.types.campaign.referral_source import ReferralSource


def test_referral_source_includes_every_runtime_value() -> None:
    assert set(get_args(ReferralSource)) == {
        "DIRECT",
        "PARTICIPANT",
        "DELETED_PARTICIPANT",
        "IMPORT",
        "MANUAL",
    }
