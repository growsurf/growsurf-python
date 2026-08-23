from growsurf.types.campaign_retrieve_analytics_response import (
    Series as CampaignSeries,
    Analytics as CampaignAnalytics,
    StatusCountsRewardStatus,
)
from growsurf.types.campaign.participant_analytics_response import (
    Series as ParticipantSeries,
    Analytics as ParticipantAnalytics,
)


def test_campaign_and_participant_analytics_share_reward_status_buckets() -> None:
    assert set(StatusCountsRewardStatus.__annotations__) == {"unapproved", "unfulfilled", "completed"}
    assert "reward_status" in ParticipantAnalytics.__annotations__
    assert "pending_rewards" not in ParticipantAnalytics.__annotations__
    assert "rewards_earned" not in ParticipantAnalytics.__annotations__

    reward_status = StatusCountsRewardStatus(unapproved=1, unfulfilled=2, completed=3)
    analytics = ParticipantAnalytics(rewardStatus=reward_status)

    assert analytics.reward_status == reward_status


def test_campaign_analytics_exposes_unique_commission_referrals() -> None:
    analytics = CampaignAnalytics(uniqueCommissionReferrals=4)
    campaign_series = CampaignSeries(uniqueCommissionReferrals=3)
    participant_series = ParticipantSeries(uniqueCommissionReferrals=2)

    assert analytics.unique_commission_referrals == 4
    assert campaign_series.unique_commission_referrals == 3
    assert participant_series.unique_commission_referrals == 2
    assert analytics.to_dict() == {"uniqueCommissionReferrals": 4}
    assert campaign_series.to_dict() == {"uniqueCommissionReferrals": 3}
    assert participant_series.to_dict() == {"uniqueCommissionReferrals": 2}
