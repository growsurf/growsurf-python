# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign import reward_create_params, reward_update_params
from ...types.campaign.reward import Reward
from ...types.commission_structure import CommissionStructure
from ...types.campaign.reward_tax_valuation import RewardTaxValuation
from ...types.campaign.delete_reward_response import DeleteRewardResponse
from ...types.campaign.campaign_reward_list_response import CampaignRewardListResponse

__all__ = ["RewardsResource", "AsyncRewardsResource"]


class RewardsResource(SyncAPIResource):
    """Campaign reward (`CampaignReward`) configuration operations."""

    @cached_property
    def with_raw_response(self) -> RewardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return RewardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RewardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return RewardsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        type: Literal["SINGLE_SIDED", "DOUBLE_SIDED", "MILESTONE", "LEADERBOARD", "AFFILIATE"],
        commission_structure: CommissionStructure | Omit = omit,
        conversions_required: int | Omit = omit,
        coupon_code: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        is_unlimited: bool | Omit = omit,
        is_visible: bool | Omit = omit,
        limit: int | Omit = omit,
        limit_duration: Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        next_milestone_prefix: Optional[str] | Omit = omit,
        next_milestone_suffix: Optional[str] | Omit = omit,
        number_of_winners: int | Omit = omit,
        order: int | Omit = omit,
        referral_coupon_code: Optional[str] | Omit = omit,
        referral_description: Optional[str] | Omit = omit,
        referred_reward_upfront: bool | Omit = omit,
        referred_value: RewardTaxValuation | Omit = omit,
        title: str | Omit = omit,
        value: RewardTaxValuation | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Reward:
        """
        Creates a new campaign reward (`CampaignReward`) with a server-generated ID. The
        reward type must be compatible with the program type (affiliate programs support
        only `AFFILIATE` rewards; referral programs support all other types). Enabling an
        active reward of a type automatically enables that reward type on the program.

        Args:
          type: The reward type. Immutable after creation.

          commission_structure: The affiliate commission structure (AFFILIATE rewards only).

          conversions_required: The number of referrals required to earn the reward.

          description: The reward description shown to the referrer.

          image_url: An image URL for the reward.

          is_active: Whether the reward is active (awardable).

          is_unlimited: Whether the reward can be earned an unlimited number of times.

          is_visible: Whether the reward is visible.

          limit: The number of times a participant can earn the reward (overridden by
              `isUnlimited`).

          limit_duration: The window over which `limit` applies.

          metadata: Custom key/value metadata (single-level; values are stored as strings).

          number_of_winners: The maximum number of winners (LEADERBOARD rewards).

          order: The display order of the reward.

          referral_description: The reward description shown to the referred friend (double-sided rewards).

          referred_reward_upfront: For double-sided rewards, deliver the referred friend's reward upfront as a
              discount.

          referred_value: Tax valuation for the referred friend's side of a double-sided reward.
              Defaults to not tax-reportable (a purchase rebate).

          title: The reward title (internal label).

          value: Tax valuation for the reward (the referrer's side of a double-sided reward).
              Used by tax documentation / 1099 reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/reward-configs", id=id),
            body=maybe_transform(
                {
                    "type": type,
                    "commission_structure": commission_structure,
                    "conversions_required": conversions_required,
                    "coupon_code": coupon_code,
                    "description": description,
                    "image_url": image_url,
                    "is_active": is_active,
                    "is_unlimited": is_unlimited,
                    "is_visible": is_visible,
                    "limit": limit,
                    "limit_duration": limit_duration,
                    "metadata": metadata,
                    "next_milestone_prefix": next_milestone_prefix,
                    "next_milestone_suffix": next_milestone_suffix,
                    "number_of_winners": number_of_winners,
                    "order": order,
                    "referral_coupon_code": referral_coupon_code,
                    "referral_description": referral_description,
                    "referred_reward_upfront": referred_reward_upfront,
                    "referred_value": referred_value,
                    "title": title,
                    "value": value,
                },
                reward_create_params.RewardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reward,
        )

    def update(
        self,
        campaign_reward_id: str,
        *,
        id: str,
        commission_structure: CommissionStructure | Omit = omit,
        conversions_required: int | Omit = omit,
        coupon_code: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        is_unlimited: bool | Omit = omit,
        is_visible: bool | Omit = omit,
        limit: int | Omit = omit,
        limit_duration: Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        next_milestone_prefix: Optional[str] | Omit = omit,
        next_milestone_suffix: Optional[str] | Omit = omit,
        number_of_winners: int | Omit = omit,
        order: int | Omit = omit,
        referral_coupon_code: Optional[str] | Omit = omit,
        referral_description: Optional[str] | Omit = omit,
        referred_reward_upfront: bool | Omit = omit,
        referred_value: RewardTaxValuation | Omit = omit,
        title: str | Omit = omit,
        value: RewardTaxValuation | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Reward:
        """
        Updates an existing campaign reward (`CampaignReward`). The reward `type` is
        immutable and cannot be changed.

        Args:
          commission_structure: The affiliate commission structure (AFFILIATE rewards only).

          conversions_required: The number of referrals required to earn the reward.

          description: The reward description shown to the referrer.

          image_url: An image URL for the reward.

          is_active: Whether the reward is active (awardable).

          is_unlimited: Whether the reward can be earned an unlimited number of times.

          is_visible: Whether the reward is visible.

          limit: The number of times a participant can earn the reward (overridden by
              `isUnlimited`).

          limit_duration: The window over which `limit` applies.

          metadata: Custom key/value metadata (single-level; values are stored as strings).

          number_of_winners: The maximum number of winners (LEADERBOARD rewards).

          order: The display order of the reward.

          referral_description: The reward description shown to the referred friend (double-sided rewards).

          referred_reward_upfront: For double-sided rewards, deliver the referred friend's reward upfront as a
              discount.

          referred_value: Tax valuation for the referred friend's side of a double-sided reward.
              Defaults to not tax-reportable (a purchase rebate).

          title: The reward title (internal label).

          value: Tax valuation for the reward (the referrer's side of a double-sided reward).
              Used by tax documentation / 1099 reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not campaign_reward_id:
            raise ValueError(f"Expected a non-empty value for `campaign_reward_id` but received {campaign_reward_id!r}")
        return self._patch(
            path_template("/campaign/{id}/reward-configs/{campaign_reward_id}", id=id, campaign_reward_id=campaign_reward_id),
            body=maybe_transform(
                {
                    "commission_structure": commission_structure,
                    "conversions_required": conversions_required,
                    "coupon_code": coupon_code,
                    "description": description,
                    "image_url": image_url,
                    "is_active": is_active,
                    "is_unlimited": is_unlimited,
                    "is_visible": is_visible,
                    "limit": limit,
                    "limit_duration": limit_duration,
                    "metadata": metadata,
                    "next_milestone_prefix": next_milestone_prefix,
                    "next_milestone_suffix": next_milestone_suffix,
                    "number_of_winners": number_of_winners,
                    "order": order,
                    "referral_coupon_code": referral_coupon_code,
                    "referral_description": referral_description,
                    "referred_reward_upfront": referred_reward_upfront,
                    "referred_value": referred_value,
                    "title": title,
                    "value": value,
                },
                reward_update_params.RewardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reward,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRewardListResponse:
        """
        Retrieves the list of a program's configured rewards (`CampaignReward`s). Returns
        the active, visible, and enabled rewards — the same set embedded in the `rewards`
        array of the campaign response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/reward-configs", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignRewardListResponse,
        )

    def delete(
        self,
        campaign_reward_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteRewardResponse:
        """
        Deletes a campaign reward (`CampaignReward`). The reward is deactivated, removed
        from the program's reward set, and any connected upfront-discount coupons are
        cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not campaign_reward_id:
            raise ValueError(f"Expected a non-empty value for `campaign_reward_id` but received {campaign_reward_id!r}")
        return self._delete(
            path_template("/campaign/{id}/reward-configs/{campaign_reward_id}", id=id, campaign_reward_id=campaign_reward_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteRewardResponse,
        )


class AsyncRewardsResource(AsyncAPIResource):
    """Campaign reward (`CampaignReward`) configuration operations."""

    @cached_property
    def with_raw_response(self) -> AsyncRewardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/growsurf/growsurf-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRewardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRewardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/growsurf/growsurf-python#with_streaming_response
        """
        return AsyncRewardsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        type: Literal["SINGLE_SIDED", "DOUBLE_SIDED", "MILESTONE", "LEADERBOARD", "AFFILIATE"],
        commission_structure: CommissionStructure | Omit = omit,
        conversions_required: int | Omit = omit,
        coupon_code: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        is_unlimited: bool | Omit = omit,
        is_visible: bool | Omit = omit,
        limit: int | Omit = omit,
        limit_duration: Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        next_milestone_prefix: Optional[str] | Omit = omit,
        next_milestone_suffix: Optional[str] | Omit = omit,
        number_of_winners: int | Omit = omit,
        order: int | Omit = omit,
        referral_coupon_code: Optional[str] | Omit = omit,
        referral_description: Optional[str] | Omit = omit,
        referred_reward_upfront: bool | Omit = omit,
        referred_value: RewardTaxValuation | Omit = omit,
        title: str | Omit = omit,
        value: RewardTaxValuation | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Reward:
        """
        Creates a new campaign reward (`CampaignReward`) with a server-generated ID. The
        reward type must be compatible with the program type (affiliate programs support
        only `AFFILIATE` rewards; referral programs support all other types). Enabling an
        active reward of a type automatically enables that reward type on the program.

        Args:
          type: The reward type. Immutable after creation.

          commission_structure: The affiliate commission structure (AFFILIATE rewards only).

          conversions_required: The number of referrals required to earn the reward.

          description: The reward description shown to the referrer.

          image_url: An image URL for the reward.

          is_active: Whether the reward is active (awardable).

          is_unlimited: Whether the reward can be earned an unlimited number of times.

          is_visible: Whether the reward is visible.

          limit: The number of times a participant can earn the reward (overridden by
              `isUnlimited`).

          limit_duration: The window over which `limit` applies.

          metadata: Custom key/value metadata (single-level; values are stored as strings).

          number_of_winners: The maximum number of winners (LEADERBOARD rewards).

          order: The display order of the reward.

          referral_description: The reward description shown to the referred friend (double-sided rewards).

          referred_reward_upfront: For double-sided rewards, deliver the referred friend's reward upfront as a
              discount.

          referred_value: Tax valuation for the referred friend's side of a double-sided reward.
              Defaults to not tax-reportable (a purchase rebate).

          title: The reward title (internal label).

          value: Tax valuation for the reward (the referrer's side of a double-sided reward).
              Used by tax documentation / 1099 reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/reward-configs", id=id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "commission_structure": commission_structure,
                    "conversions_required": conversions_required,
                    "coupon_code": coupon_code,
                    "description": description,
                    "image_url": image_url,
                    "is_active": is_active,
                    "is_unlimited": is_unlimited,
                    "is_visible": is_visible,
                    "limit": limit,
                    "limit_duration": limit_duration,
                    "metadata": metadata,
                    "next_milestone_prefix": next_milestone_prefix,
                    "next_milestone_suffix": next_milestone_suffix,
                    "number_of_winners": number_of_winners,
                    "order": order,
                    "referral_coupon_code": referral_coupon_code,
                    "referral_description": referral_description,
                    "referred_reward_upfront": referred_reward_upfront,
                    "referred_value": referred_value,
                    "title": title,
                    "value": value,
                },
                reward_create_params.RewardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reward,
        )

    async def update(
        self,
        campaign_reward_id: str,
        *,
        id: str,
        commission_structure: CommissionStructure | Omit = omit,
        conversions_required: int | Omit = omit,
        coupon_code: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        is_active: bool | Omit = omit,
        is_unlimited: bool | Omit = omit,
        is_visible: bool | Omit = omit,
        limit: int | Omit = omit,
        limit_duration: Literal["IN_TOTAL", "PER_MONTH", "PER_YEAR"] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        next_milestone_prefix: Optional[str] | Omit = omit,
        next_milestone_suffix: Optional[str] | Omit = omit,
        number_of_winners: int | Omit = omit,
        order: int | Omit = omit,
        referral_coupon_code: Optional[str] | Omit = omit,
        referral_description: Optional[str] | Omit = omit,
        referred_reward_upfront: bool | Omit = omit,
        referred_value: RewardTaxValuation | Omit = omit,
        title: str | Omit = omit,
        value: RewardTaxValuation | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Reward:
        """
        Updates an existing campaign reward (`CampaignReward`). The reward `type` is
        immutable and cannot be changed.

        Args:
          commission_structure: The affiliate commission structure (AFFILIATE rewards only).

          conversions_required: The number of referrals required to earn the reward.

          description: The reward description shown to the referrer.

          image_url: An image URL for the reward.

          is_active: Whether the reward is active (awardable).

          is_unlimited: Whether the reward can be earned an unlimited number of times.

          is_visible: Whether the reward is visible.

          limit: The number of times a participant can earn the reward (overridden by
              `isUnlimited`).

          limit_duration: The window over which `limit` applies.

          metadata: Custom key/value metadata (single-level; values are stored as strings).

          number_of_winners: The maximum number of winners (LEADERBOARD rewards).

          order: The display order of the reward.

          referral_description: The reward description shown to the referred friend (double-sided rewards).

          referred_reward_upfront: For double-sided rewards, deliver the referred friend's reward upfront as a
              discount.

          referred_value: Tax valuation for the referred friend's side of a double-sided reward.
              Defaults to not tax-reportable (a purchase rebate).

          title: The reward title (internal label).

          value: Tax valuation for the reward (the referrer's side of a double-sided reward).
              Used by tax documentation / 1099 reporting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not campaign_reward_id:
            raise ValueError(f"Expected a non-empty value for `campaign_reward_id` but received {campaign_reward_id!r}")
        return await self._patch(
            path_template("/campaign/{id}/reward-configs/{campaign_reward_id}", id=id, campaign_reward_id=campaign_reward_id),
            body=await async_maybe_transform(
                {
                    "commission_structure": commission_structure,
                    "conversions_required": conversions_required,
                    "coupon_code": coupon_code,
                    "description": description,
                    "image_url": image_url,
                    "is_active": is_active,
                    "is_unlimited": is_unlimited,
                    "is_visible": is_visible,
                    "limit": limit,
                    "limit_duration": limit_duration,
                    "metadata": metadata,
                    "next_milestone_prefix": next_milestone_prefix,
                    "next_milestone_suffix": next_milestone_suffix,
                    "number_of_winners": number_of_winners,
                    "order": order,
                    "referral_coupon_code": referral_coupon_code,
                    "referral_description": referral_description,
                    "referred_reward_upfront": referred_reward_upfront,
                    "referred_value": referred_value,
                    "title": title,
                    "value": value,
                },
                reward_update_params.RewardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Reward,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CampaignRewardListResponse:
        """
        Retrieves the list of a program's configured rewards (`CampaignReward`s). Returns
        the active, visible, and enabled rewards — the same set embedded in the `rewards`
        array of the campaign response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/reward-configs", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignRewardListResponse,
        )

    async def delete(
        self,
        campaign_reward_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteRewardResponse:
        """
        Deletes a campaign reward (`CampaignReward`). The reward is deactivated, removed
        from the program's reward set, and any connected upfront-discount coupons are
        cleaned up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not campaign_reward_id:
            raise ValueError(f"Expected a non-empty value for `campaign_reward_id` but received {campaign_reward_id!r}")
        return await self._delete(
            path_template("/campaign/{id}/reward-configs/{campaign_reward_id}", id=id, campaign_reward_id=campaign_reward_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteRewardResponse,
        )


class RewardsResourceWithRawResponse:
    def __init__(self, rewards: RewardsResource) -> None:
        self._rewards = rewards

        self.create = to_raw_response_wrapper(
            rewards.create,
        )
        self.update = to_raw_response_wrapper(
            rewards.update,
        )
        self.list = to_raw_response_wrapper(
            rewards.list,
        )
        self.delete = to_raw_response_wrapper(
            rewards.delete,
        )


class AsyncRewardsResourceWithRawResponse:
    def __init__(self, rewards: AsyncRewardsResource) -> None:
        self._rewards = rewards

        self.create = async_to_raw_response_wrapper(
            rewards.create,
        )
        self.update = async_to_raw_response_wrapper(
            rewards.update,
        )
        self.list = async_to_raw_response_wrapper(
            rewards.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rewards.delete,
        )


class RewardsResourceWithStreamingResponse:
    def __init__(self, rewards: RewardsResource) -> None:
        self._rewards = rewards

        self.create = to_streamed_response_wrapper(
            rewards.create,
        )
        self.update = to_streamed_response_wrapper(
            rewards.update,
        )
        self.list = to_streamed_response_wrapper(
            rewards.list,
        )
        self.delete = to_streamed_response_wrapper(
            rewards.delete,
        )


class AsyncRewardsResourceWithStreamingResponse:
    def __init__(self, rewards: AsyncRewardsResource) -> None:
        self._rewards = rewards

        self.create = async_to_streamed_response_wrapper(
            rewards.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rewards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rewards.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rewards.delete,
        )
