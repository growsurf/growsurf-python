# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign.reward_group import RewardGroup
from ...types.campaign.reward_group_rule_param import RewardGroupRuleParam
from ...types.campaign.reward_group_list_response import RewardGroupListResponse
from ...types.campaign.delete_reward_group_response import DeleteRewardGroupResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


def _body(**values: object) -> Dict[str, object]:
    return {key: value for key, value in values.items() if value is not omit}


class GroupsResource(SyncAPIResource):
    """Group operations. Groups give some participants a different reward list."""

    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroupListResponse:
        """
        Lists the program's groups in display order. Groups give some participants a
        different reward list. Each participant is in one group, and `groupId: null` is
        Default, which holds the program's standard rewards and is
        not in this list. A group's rewards replace Default's whole reward list for its
        members' new referrals. Leaderboard rewards stay program-wide.
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/groups", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroupListResponse,
        )

    def create(
        self,
        id: str,
        *,
        name: str,
        rules: Iterable[RewardGroupRuleParam] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroup:
        """
        Creates an empty group. Add Campaign Rewards with its `groupId` before adding
        participants or rules. Omit `rules` or send an empty array; nonempty rules return `400`.
        Group names must be unique, ignoring case. Duplicate names return `409`; "Default" returns `400`.

        Args:
          name: The group name (internal only, never shown to participants). 1 to 100
              characters.

          rules: Omit or send an empty array. Add rules after configuring a reward.
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/campaign/{id}/groups", id=id),
            body=_body(name=name, rules=rules),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroup,
        )

    def retrieve(
        self,
        group_id: str,
        *,
        id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroup:
        """
        Retrieves one of the program's groups.
        """
        if not id or not group_id:
            raise ValueError("Expected non-empty `id` and `group_id` values")
        return self._get(
            path_template("/campaign/{id}/groups/{group_id}", id=id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroup,
        )

    def update(
        self,
        group_id: str,
        *,
        id: str,
        name: str | Omit = omit,
        order: int | Omit = omit,
        rules: Iterable[RewardGroupRuleParam] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroup:
        """
        Renames, reorders, or changes the rules of a group. Sending `rules` replaces the
        whole list. An added `PARTICIPANT` rule moves that participant in now; a removed
        one moves them back to Default if they are still in this group. Email and domain
        rule changes move no one. To change the group's rewards, update its Campaign
        Rewards. Group names must be unique in the program, ignoring case. A name that
        another group uses returns `409`, and "Default" returns `400`.

        Args:
          name: The group name (internal only, never shown to participants). 1 to 100
              characters.

          order: The group's position in the program's group list.

          rules: Replaces the group's whole rule list. Up to 500.
        """
        if not id or not group_id:
            raise ValueError("Expected non-empty `id` and `group_id` values")
        return self._patch(
            path_template("/campaign/{id}/groups/{group_id}", id=id, group_id=group_id),
            body=_body(name=name, order=order, rules=rules),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroup,
        )

    def delete(
        self,
        group_id: str,
        *,
        id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteRewardGroupResponse:
        """
        Deletes a group. Its members move to Default, and its Campaign Rewards are
        removed from the program, so they no longer appear in
        `GET /campaign/{id}/reward-configs`. Rewards already earned keep their amounts
        and can still be sent.
        """
        if not id or not group_id:
            raise ValueError("Expected non-empty `id` and `group_id` values")
        return self._delete(
            path_template("/campaign/{id}/groups/{group_id}", id=id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteRewardGroupResponse,
        )


class AsyncGroupsResource(AsyncAPIResource):
    """Group operations. Groups give some participants a different reward list."""

    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroupListResponse:
        """
        Lists the program's groups in display order. Groups give some participants a
        different reward list. Each participant is in one group, and `groupId: null` is
        Default, which holds the program's standard rewards and is
        not in this list. A group's rewards replace Default's whole reward list for its
        members' new referrals. Leaderboard rewards stay program-wide.
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/groups", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroupListResponse,
        )

    async def create(
        self,
        id: str,
        *,
        name: str,
        rules: Iterable[RewardGroupRuleParam] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroup:
        """
        Creates an empty group. Add Campaign Rewards with its `groupId` before adding
        participants or rules. Omit `rules` or send an empty array; nonempty rules return `400`.
        Group names must be unique, ignoring case. Duplicate names return `409`; "Default" returns `400`.

        Args:
          name: The group name (internal only, never shown to participants). 1 to 100
              characters.

          rules: Omit or send an empty array. Add rules after configuring a reward.
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/campaign/{id}/groups", id=id),
            body=_body(name=name, rules=rules),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroup,
        )

    async def retrieve(
        self,
        group_id: str,
        *,
        id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroup:
        """
        Retrieves one of the program's groups.
        """
        if not id or not group_id:
            raise ValueError("Expected non-empty `id` and `group_id` values")
        return await self._get(
            path_template("/campaign/{id}/groups/{group_id}", id=id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroup,
        )

    async def update(
        self,
        group_id: str,
        *,
        id: str,
        name: str | Omit = omit,
        order: int | Omit = omit,
        rules: Iterable[RewardGroupRuleParam] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RewardGroup:
        """
        Renames, reorders, or changes the rules of a group. Sending `rules` replaces the
        whole list. An added `PARTICIPANT` rule moves that participant in now; a removed
        one moves them back to Default if they are still in this group. Email and domain
        rule changes move no one. To change the group's rewards, update its Campaign
        Rewards. Group names must be unique in the program, ignoring case. A name that
        another group uses returns `409`, and "Default" returns `400`.

        Args:
          name: The group name (internal only, never shown to participants). 1 to 100
              characters.

          order: The group's position in the program's group list.

          rules: Replaces the group's whole rule list. Up to 500.
        """
        if not id or not group_id:
            raise ValueError("Expected non-empty `id` and `group_id` values")
        return await self._patch(
            path_template("/campaign/{id}/groups/{group_id}", id=id, group_id=group_id),
            body=_body(name=name, order=order, rules=rules),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardGroup,
        )

    async def delete(
        self,
        group_id: str,
        *,
        id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteRewardGroupResponse:
        """
        Deletes a group. Its members move to Default, and its Campaign Rewards are
        removed from the program, so they no longer appear in
        `GET /campaign/{id}/reward-configs`. Rewards already earned keep their amounts
        and can still be sent.
        """
        if not id or not group_id:
            raise ValueError("Expected non-empty `id` and `group_id` values")
        return await self._delete(
            path_template("/campaign/{id}/groups/{group_id}", id=id, group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteRewardGroupResponse,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self.list = to_raw_response_wrapper(groups.list)
        self.create = to_raw_response_wrapper(groups.create)
        self.retrieve = to_raw_response_wrapper(groups.retrieve)
        self.update = to_raw_response_wrapper(groups.update)
        self.delete = to_raw_response_wrapper(groups.delete)


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self.list = async_to_raw_response_wrapper(groups.list)
        self.create = async_to_raw_response_wrapper(groups.create)
        self.retrieve = async_to_raw_response_wrapper(groups.retrieve)
        self.update = async_to_raw_response_wrapper(groups.update)
        self.delete = async_to_raw_response_wrapper(groups.delete)


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self.list = to_streamed_response_wrapper(groups.list)
        self.create = to_streamed_response_wrapper(groups.create)
        self.retrieve = to_streamed_response_wrapper(groups.retrieve)
        self.update = to_streamed_response_wrapper(groups.update)
        self.delete = to_streamed_response_wrapper(groups.delete)


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self.list = async_to_streamed_response_wrapper(groups.list)
        self.create = async_to_streamed_response_wrapper(groups.create)
        self.retrieve = async_to_streamed_response_wrapper(groups.retrieve)
        self.update = async_to_streamed_response_wrapper(groups.update)
        self.delete = async_to_streamed_response_wrapper(groups.delete)
