from growsurf.types.campaign_retrieve_analytics_response import StatusCountsRewardStatus
from growsurf.types.campaign.participant_analytics_response import Analytics as ParticipantAnalytics


def test_campaign_and_participant_analytics_share_reward_status_buckets() -> None:
    assert set(StatusCountsRewardStatus.__annotations__) == {"unapproved", "unfulfilled", "completed"}
    assert "reward_status" in ParticipantAnalytics.__annotations__
    assert "pending_rewards" not in ParticipantAnalytics.__annotations__
    assert "rewards_earned" not in ParticipantAnalytics.__annotations__

    reward_status = StatusCountsRewardStatus(unapproved=1, unfulfilled=2, completed=3)
    analytics = ParticipantAnalytics(rewardStatus=reward_status)

    assert analytics.reward_status == reward_status
