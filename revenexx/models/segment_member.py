from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.segment_member_source import SegmentMemberSource

class SegmentMember(AppwriteModel):
    """
    One organization inside one segment, and the record of how it got there (hand-picked or matched by the rule).

    Attributes
    ----------
    created_at : Optional[str]
        When the organization joined the segment.
    id : Optional[str]
        Primary key of the membership row.
    organization_id : Optional[str]
        The member company. Segments group companies, never people — a person is reached through their organization.
    segment_id : Optional[str]
        The segment.
    source : Optional[SegmentMemberSource]
        How this membership came about: &#039;manual&#039; is hand-picked, &#039;rule&#039; was materialized by a recompute. The distinction is load-bearing — a recompute only ever inserts and deletes &#039;rule&#039; rows, so a hand-picked member survives every rule change.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    segment_id: Optional[str] = Field(default=None, alias='segment_id')
    source: Optional[SegmentMemberSource] = Field(default=None, alias='source')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
