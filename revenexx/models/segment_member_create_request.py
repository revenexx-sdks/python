from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.segment_member_source import SegmentMemberSource

class SegmentMemberCreateRequest(AppwriteModel):
    """
    Add one organization to a segment. Use source=&#039;manual&#039; (the default) for hand-picked members; rule members are materialized by the recompute route.

    Attributes
    ----------
    organization_id : str
        The member company. Segments group companies, never people — a person is reached through their organization.
    segment_id : str
        The segment.
    source : Optional[SegmentMemberSource]
        How this membership came about: &#039;manual&#039; is hand-picked, &#039;rule&#039; was materialized by a recompute. The distinction is load-bearing — a recompute only ever inserts and deletes &#039;rule&#039; rows, so a hand-picked member survives every rule change. Default &#039;manual&#039;.
    """
    organization_id: str = Field(..., alias='organization_id')
    segment_id: str = Field(..., alias='segment_id')
    source: Optional[SegmentMemberSource] = Field(default=None, alias='source')
