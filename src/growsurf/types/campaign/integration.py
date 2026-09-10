# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Integration"]


class Integration(BaseModel):
    id: str
    """
    Stable integration key, the same value the GrowSurf dashboard uses for this
    integration.
    """

    auto_disabled: bool = FieldInfo(alias="autoDisabled")
    """
    Whether GrowSurf switched the integration off after repeated delivery failures.
    Its credentials are still stored, but it delivers nothing until it is reconnected
    in the GrowSurf dashboard.
    """

    connect_url: str = FieldInfo(alias="connectUrl")
    """
    Dashboard link that opens this integration's connect panel in the GrowSurf Program
    Editor. Give it to the person running the program: connecting an account is a step
    they complete in the dashboard, and the API cannot do it for them.
    """

    connected: bool
    """Whether the program has stored credentials for this integration."""

    enabled: bool
    """Whether the integration is switched on and currently working."""

    name: str
    """Display name, matching what the GrowSurf dashboard calls this integration."""
