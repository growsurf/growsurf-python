# Campaign

Types:

```python
from growsurf.types import (
    Campaign,
    CommissionStructure,
    ParticipantCommissionList,
    ParticipantList,
    ParticipantPayoutList,
    ReferralList,
    CampaignListResponse,
    CampaignRetrieveAnalyticsResponse,
)
```

Methods:

- <code title="get /campaign/{id}">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">retrieve</a>(id) -> <a href="./src/growsurf/types/campaign/campaign.py">Campaign</a></code>
- <code title="get /campaigns">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list</a>() -> <a href="./src/growsurf/types/campaign_list_response.py">CampaignListResponse</a></code>
- <code title="get /campaign/{id}/commissions">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list_commissions</a>(id, \*\*<a href="src/growsurf/types/campaign_list_commissions_params.py">params</a>) -> <a href="./src/growsurf/types/participant_commission_list.py">ParticipantCommissionList</a></code>
- <code title="get /campaign/{id}/leaderboard">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list_leaderboard</a>(id, \*\*<a href="src/growsurf/types/campaign_list_leaderboard_params.py">params</a>) -> <a href="./src/growsurf/types/participant_list.py">ParticipantList</a></code>
- <code title="get /campaign/{id}/participants">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list_participants</a>(id, \*\*<a href="src/growsurf/types/campaign_list_participants_params.py">params</a>) -> <a href="./src/growsurf/types/participant_list.py">ParticipantList</a></code>
- <code title="get /campaign/{id}/payouts">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list_payouts</a>(id, \*\*<a href="src/growsurf/types/campaign_list_payouts_params.py">params</a>) -> <a href="./src/growsurf/types/participant_payout_list.py">ParticipantPayoutList</a></code>
- <code title="get /campaign/{id}/referrals">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list_referrals</a>(id, \*\*<a href="src/growsurf/types/campaign_list_referrals_params.py">params</a>) -> <a href="./src/growsurf/types/referral_list.py">ReferralList</a></code>
- <code title="get /campaign/{id}/analytics">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">retrieve_analytics</a>(id, \*\*<a href="src/growsurf/types/campaign_retrieve_analytics_params.py">params</a>) -> <a href="./src/growsurf/types/campaign_retrieve_analytics_response.py">CampaignRetrieveAnalyticsResponse</a></code>

## Participant

Types:

```python
from growsurf.types.campaign import (
    FraudRiskLevel,
    Participant,
    ParticipantReward,
    ReferralSource,
    ReferralStatus,
    ParticipantDeleteResponse,
    ParticipantCreateMobileTokenResponse,
    ParticipantListRewardsResponse,
    ParticipantRecordTransactionResponse,
    ParticipantSendInvitesResponse,
    ParticipantTriggerReferralResponse,
)
```

Methods:

- <code title="get /campaign/{id}/participant/{participantIdOrEmail}">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">retrieve</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant.py">Participant</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">update</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_update_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant.py">Participant</a></code>
- <code title="delete /campaign/{id}/participant/{participantIdOrEmail}">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">delete</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant_delete_response.py">ParticipantDeleteResponse</a></code>
- <code title="post /campaign/{id}/participant">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">add</a>(id, \*\*<a href="src/growsurf/types/campaign/participant_add_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant.py">Participant</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/mobile-token">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">create_mobile_token</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant_create_mobile_token_response.py">ParticipantCreateMobileTokenResponse</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/commissions">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_commissions</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_commissions_params.py">params</a>) -> <a href="./src/growsurf/types/participant_commission_list.py">ParticipantCommissionList</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/payouts">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_payouts</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_payouts_params.py">params</a>) -> <a href="./src/growsurf/types/participant_payout_list.py">ParticipantPayoutList</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/referrals">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_referrals</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_referrals_params.py">params</a>) -> <a href="./src/growsurf/types/referral_list.py">ReferralList</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/rewards">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_rewards</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_rewards_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_list_rewards_response.py">ParticipantListRewardsResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/transaction">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">record_transaction</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_record_transaction_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_record_transaction_response.py">ParticipantRecordTransactionResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/invites">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">send_invites</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_send_invites_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_send_invites_response.py">ParticipantSendInvitesResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/ref">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">trigger_referral</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant_trigger_referral_response.py">ParticipantTriggerReferralResponse</a></code>

## Reward

Types:

```python
from growsurf.types.campaign import (
    RewardDeleteResponse,
    RewardApproveResponse,
    RewardFulfillResponse,
)
```

Methods:

- <code title="delete /campaign/{id}/reward/{rewardId}">client.campaign.reward.<a href="./src/growsurf/resources/campaign/reward.py">delete</a>(reward_id, \*, id) -> <a href="./src/growsurf/types/campaign/reward_delete_response.py">RewardDeleteResponse</a></code>
- <code title="post /campaign/{id}/reward/{rewardId}/approve">client.campaign.reward.<a href="./src/growsurf/resources/campaign/reward.py">approve</a>(reward_id, \*, id, \*\*<a href="src/growsurf/types/campaign/reward_approve_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/reward_approve_response.py">RewardApproveResponse</a></code>
- <code title="post /campaign/{id}/reward/{rewardId}/fulfill">client.campaign.reward.<a href="./src/growsurf/resources/campaign/reward.py">fulfill</a>(reward_id, \*, id) -> <a href="./src/growsurf/types/campaign/reward_fulfill_response.py">RewardFulfillResponse</a></code>

## Commission

Types:

```python
from growsurf.types.campaign import CommissionDeleteResponse, CommissionApproveResponse
```

Methods:

- <code title="delete /campaign/{id}/commission/{commissionId}">client.campaign.commission.<a href="./src/growsurf/resources/campaign/commission.py">delete</a>(commission_id, \*, id) -> <a href="./src/growsurf/types/campaign/commission_delete_response.py">CommissionDeleteResponse</a></code>
- <code title="post /campaign/{id}/commission/{commissionId}/approve">client.campaign.commission.<a href="./src/growsurf/resources/campaign/commission.py">approve</a>(commission_id, \*, id) -> <a href="./src/growsurf/types/campaign/commission_approve_response.py">CommissionApproveResponse</a></code>
