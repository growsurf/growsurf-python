# Account

Types:

```python
from growsurf.types import (
    CreateAccountResponse,
)
```

Methods:

- <code title="post /accounts">client.account.<a href="./src/growsurf/resources/account.py">create</a>(\*\*<a href="src/growsurf/types/account_create_params.py">params</a>) -> <a href="./src/growsurf/types/create_account_response.py">CreateAccountResponse</a></code>

# Team

Types:

```python
from growsurf.types import (
    Team,
    RotateApiKeyResponse,
    VerificationEmailResponse,
)
```

Methods:

- <code title="get /team">client.team.<a href="./src/growsurf/resources/team.py">retrieve</a>() -> <a href="./src/growsurf/types/team.py">Team</a></code>
- <code title="patch /team">client.team.<a href="./src/growsurf/resources/team.py">update</a>(\*\*<a href="src/growsurf/types/team_update_params.py">params</a>) -> <a href="./src/growsurf/types/team.py">Team</a></code>
- <code title="post /api-key/rotate">client.team.<a href="./src/growsurf/resources/team.py">rotate_api_key</a>() -> <a href="./src/growsurf/types/rotate_api_key_response.py">RotateApiKeyResponse</a></code>
- <code title="post /team/verification-request">client.team.<a href="./src/growsurf/resources/team.py">request_verification</a>() -> <a href="./src/growsurf/types/team.py">Team</a></code>
- <code title="post /team/owner/verification-email">client.team.<a href="./src/growsurf/resources/team.py">resend_owner_verification_email</a>() -> <a href="./src/growsurf/types/verification_email_response.py">VerificationEmailResponse</a></code>

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
    CampaignCreateMobileParticipantTokenResponse,
    CampaignRetrieveAnalyticsResponse,
)
```

Methods:

- <code title="post /campaigns">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">create</a>(\*\*<a href="src/growsurf/types/campaign_create_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/campaign.py">Campaign</a></code>
- <code title="get /campaign/{id}">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">retrieve</a>(id) -> <a href="./src/growsurf/types/campaign/campaign.py">Campaign</a></code>
- <code title="patch /campaign/{id}">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">update</a>(id, \*\*<a href="src/growsurf/types/campaign_update_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/campaign.py">Campaign</a></code>
- <code title="get /campaigns">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">list</a>() -> <a href="./src/growsurf/types/campaign_list_response.py">CampaignListResponse</a></code>
- <code title="post /campaign/{id}/clone">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">clone</a>(id) -> <a href="./src/growsurf/types/campaign/campaign.py">Campaign</a></code>
- <code title="post /campaign/{id}/mobile-participant-token">client.campaign.<a href="./src/growsurf/resources/campaign/campaign.py">create_mobile_participant_token</a>(id, \*\*<a href="src/growsurf/types/campaign_create_mobile_participant_token_params.py">params</a>) -> <a href="./src/growsurf/types/campaign_create_mobile_participant_token_response.py">CampaignCreateMobileParticipantTokenResponse</a></code>
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
    Create,
    FraudRiskLevel,
    Participant,
    ParticipantReward,
    ReferralSource,
    ReferralStatus,
    EmailParticipantResponse,
    ParticipantDeleteResponse,
    ParticipantAnalyticsResponse,
    ParticipantBulkDeleteResponse,
    ParticipantListRewardsResponse,
    ParticipantActivityLogsResponse,
    ParticipantRecordTransactionResponse,
    ParticipantRefundTransactionResponse,
    ParticipantSendInvitesResponse,
    ParticipantTriggerReferralResponse,
)
```

Methods:

- <code title="get /campaign/{id}/participant/{participantIdOrEmail}">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">retrieve</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant.py">Participant</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">update</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_update_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant.py">Participant</a></code>
- <code title="delete /campaign/{id}/participant/{participantIdOrEmail}">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">delete</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant_delete_response.py">ParticipantDeleteResponse</a></code>
- <code title="post /campaign/{id}/participants/bulk-delete">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">bulk_delete</a>(id, \*\*<a href="src/growsurf/types/campaign/participant_bulk_delete_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_bulk_delete_response.py">ParticipantBulkDeleteResponse</a></code>
- <code title="post /campaign/{id}/participant">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">add</a>(id, \*\*<a href="src/growsurf/types/campaign/participant_add_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant.py">Participant</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/commissions">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_commissions</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_commissions_params.py">params</a>) -> <a href="./src/growsurf/types/participant_commission_list.py">ParticipantCommissionList</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/payouts">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_payouts</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_payouts_params.py">params</a>) -> <a href="./src/growsurf/types/participant_payout_list.py">ParticipantPayoutList</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/referrals">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_referrals</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_referrals_params.py">params</a>) -> <a href="./src/growsurf/types/referral_list.py">ReferralList</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/rewards">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_rewards</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_rewards_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_list_rewards_response.py">ParticipantListRewardsResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/transaction">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">record_transaction</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_record_transaction_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_record_transaction_response.py">ParticipantRecordTransactionResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/transaction/refund">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">refund_transaction</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_refund_transaction_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_refund_transaction_response.py">ParticipantRefundTransactionResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/invites">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">send_invites</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_send_invites_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_send_invites_response.py">ParticipantSendInvitesResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/ref">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">trigger_referral</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_trigger_referral_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_trigger_referral_response.py">ParticipantTriggerReferralResponse</a></code>
- <code title="delete /campaign/{id}/participant/{participantIdOrEmail}/ref">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">cancel_delayed_referral</a>(participant_id_or_email, \*, id) -> <a href="./src/growsurf/types/campaign/participant_trigger_referral_response.py">ParticipantTriggerReferralResponse</a></code>
- <code title="post /campaign/{id}/participant/{participantIdOrEmail}/email">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">email</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_email_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/email_participant_response.py">EmailParticipantResponse</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/activity-logs">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">list_activity_logs</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_list_activity_logs_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_activity_logs_response.py">ParticipantActivityLogsResponse</a></code>
- <code title="get /campaign/{id}/participant/{participantIdOrEmail}/analytics">client.campaign.participant.<a href="./src/growsurf/resources/campaign/participant.py">retrieve_analytics</a>(participant_id_or_email, \*, id, \*\*<a href="src/growsurf/types/campaign/participant_analytics_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/participant_analytics_response.py">ParticipantAnalyticsResponse</a></code>

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

## Rewards

Types:

```python
from growsurf.types.campaign import (
    Reward,
    RewardTaxValuation,
    CampaignRewardListResponse,
    DeleteRewardResponse,
)
```

Methods:

- <code title="post /campaign/{id}/reward-configs">client.campaign.rewards.<a href="./src/growsurf/resources/campaign/rewards.py">create</a>(id, \*\*<a href="src/growsurf/types/campaign/reward_create_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/reward.py">Reward</a></code>
- <code title="patch /campaign/{id}/reward-configs/{campaignRewardId}">client.campaign.rewards.<a href="./src/growsurf/resources/campaign/rewards.py">update</a>(campaign_reward_id, \*, id, \*\*<a href="src/growsurf/types/campaign/reward_update_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/reward.py">Reward</a></code>
- <code title="get /campaign/{id}/reward-configs">client.campaign.rewards.<a href="./src/growsurf/resources/campaign/rewards.py">list</a>(id) -> <a href="./src/growsurf/types/campaign/campaign_reward_list_response.py">CampaignRewardListResponse</a></code>
- <code title="delete /campaign/{id}/reward-configs/{campaignRewardId}">client.campaign.rewards.<a href="./src/growsurf/resources/campaign/rewards.py">delete</a>(campaign_reward_id, \*, id) -> <a href="./src/growsurf/types/campaign/delete_reward_response.py">DeleteRewardResponse</a></code>

## Webhooks

Types:

```python
from growsurf.types.campaign import (
    Webhook,
    WebhookEvent,
    DeleteWebhookResponse,
    WebhookListResponse,
    WebhookTestResponse,
)
```

Methods:

- <code title="post /campaign/{id}/webhooks">client.campaign.webhooks.<a href="./src/growsurf/resources/campaign/webhooks.py">create</a>(id, \*\*<a href="src/growsurf/types/campaign/webhook_create_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/webhook.py">Webhook</a></code>
- <code title="patch /campaign/{id}/webhooks/{webhookId}">client.campaign.webhooks.<a href="./src/growsurf/resources/campaign/webhooks.py">update</a>(webhook_id, \*, id, \*\*<a href="src/growsurf/types/campaign/webhook_update_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/webhook.py">Webhook</a></code>
- <code title="get /campaign/{id}/webhooks">client.campaign.webhooks.<a href="./src/growsurf/resources/campaign/webhooks.py">list</a>(id) -> <a href="./src/growsurf/types/campaign/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /campaign/{id}/webhooks/{webhookId}">client.campaign.webhooks.<a href="./src/growsurf/resources/campaign/webhooks.py">delete</a>(webhook_id, \*, id) -> <a href="./src/growsurf/types/campaign/delete_webhook_response.py">DeleteWebhookResponse</a></code>
- <code title="post /campaign/{id}/webhooks/{webhookId}/test">client.campaign.webhooks.<a href="./src/growsurf/resources/campaign/webhooks.py">test</a>(webhook_id, \*, id, \*\*<a href="src/growsurf/types/campaign/webhook_test_params.py">params</a>) -> <a href="./src/growsurf/types/campaign/webhook_test_response.py">WebhookTestResponse</a></code>

## Design

Types:

```python
from growsurf.types.campaign import CampaignDesign
```

Methods:

- <code title="get /campaign/{id}/design">client.campaign.design.<a href="./src/growsurf/resources/campaign/design.py">retrieve</a>(id) -> <a href="./src/growsurf/types/campaign/campaign_design.py">CampaignDesign</a></code>
- <code title="patch /campaign/{id}/design">client.campaign.design.<a href="./src/growsurf/resources/campaign/design.py">update</a>(id, \*, body) -> <a href="./src/growsurf/types/campaign/campaign_design.py">CampaignDesign</a></code>

## Emails

Types:

```python
from growsurf.types.campaign import CampaignEmails
```

Methods:

- <code title="get /campaign/{id}/emails">client.campaign.emails.<a href="./src/growsurf/resources/campaign/emails.py">retrieve</a>(id) -> <a href="./src/growsurf/types/campaign/campaign_emails.py">CampaignEmails</a></code>
- <code title="patch /campaign/{id}/emails">client.campaign.emails.<a href="./src/growsurf/resources/campaign/emails.py">update</a>(id, \*, body) -> <a href="./src/growsurf/types/campaign/campaign_emails.py">CampaignEmails</a></code>

## Options

Types:

```python
from growsurf.types.campaign import CampaignOptions
```

Methods:

- <code title="get /campaign/{id}/options">client.campaign.options.<a href="./src/growsurf/resources/campaign/options.py">retrieve</a>(id) -> <a href="./src/growsurf/types/campaign/campaign_options.py">CampaignOptions</a></code>
- <code title="patch /campaign/{id}/options">client.campaign.options.<a href="./src/growsurf/resources/campaign/options.py">update</a>(id, \*, body) -> <a href="./src/growsurf/types/campaign/campaign_options.py">CampaignOptions</a></code>

## Installation

Types:

```python
from growsurf.types.campaign import CampaignInstallation
```

Methods:

- <code title="get /campaign/{id}/installation">client.campaign.installation.<a href="./src/growsurf/resources/campaign/installation.py">retrieve</a>(id) -> <a href="./src/growsurf/types/campaign/campaign_installation.py">CampaignInstallation</a></code>
- <code title="patch /campaign/{id}/installation">client.campaign.installation.<a href="./src/growsurf/resources/campaign/installation.py">update</a>(id, \*, body) -> <a href="./src/growsurf/types/campaign/campaign_installation.py">CampaignInstallation</a></code>
