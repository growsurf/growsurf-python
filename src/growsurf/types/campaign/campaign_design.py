# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

__all__ = ["CampaignDesign"]

# A program's design configuration (the dashboard Program Editor's Design tab).
# This is a large, deeply-nested object whose available fields depend on the
# program type; it is intentionally modeled as a loose object. See the API
# reference for the full field list:
# https://docs.growsurf.com/developer-tools/rest-api
CampaignDesign: TypeAlias = Dict[str, object]
