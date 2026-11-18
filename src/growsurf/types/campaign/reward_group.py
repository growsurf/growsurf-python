# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RewardGroup", "RewardGroupRule"]


class RewardGroupRule(BaseModel):
    type: Literal["PARTICIPANT", "EMAIL", "DOMAIN"]
    """The kind of rule.

    `PARTICIPANT` — an existing participant ID; the participant moves in now.
    `EMAIL` — an exact email address. `DOMAIN` — a company domain such as
    `hooli.com`, which also matches its subdomains. Email and domain rules place new
    signups and affiliate approvals.
    """

    value: str
    """The participant ID, email address, or domain."""


class RewardGroup(BaseModel):
    """A group of participants who earn their own rewards.

    Its rewards are the Campaign Rewards whose `group_id` is this group's `id`.
    """

    id: str
    """The group ID. Participants, Campaign Rewards, and participant rewards name it as `groupId`."""

    created_at: int = FieldInfo(alias="createdAt")
    """When the group was created, in Unix milliseconds."""

    name: str
    """The group name (internal only, never shown to participants)."""

    order: int
    """The group's position in the program's group list."""

    rules: List[RewardGroupRule]
    """The rules that place participants in this group."""

    signup_code: str = FieldInfo(alias="signupCode")
    """The code for this group's signup link.

    A participant who signs up through the link joins this group.
    """

    updated_at: int = FieldInfo(alias="updatedAt")
    """When the group was last changed, in Unix milliseconds."""
