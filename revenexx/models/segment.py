from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.segment_rule_match import SegmentRuleMatch

class Segment(AppwriteModel):
    """
    A named group of ORGANIZATIONS — by hand, by rule, or both at once.

    Attributes
    ----------
    code : Optional[str]
        Stable identifier, unique per tenant — what other apps and integrations name the segment by. Free text, but lowercase with underscores is the convention every seeded vocabulary follows.
    created_at : Optional[str]
        When the segment was created.
    id : Optional[str]
        Primary key of the segment.
    labels : Optional[Dict[str, Any]]
        Localized display names keyed by language tag. Null means nobody translated it and a client falls back to showing the code.
    position : Optional[float]
        Sort order in the cockpit, ascending. Ties fall back to insertion order.
    rule_match : Optional[SegmentRuleMatch]
        How the conditions combine: &#039;all&#039; (default) is AND, &#039;any&#039; is OR. Null means the same as &#039;all&#039;.
    rules : Optional[Dict[str, Any]]
        The selector that decides membership, stored verbatim. Null means the segment is manual-only. The same rule language product categories use, evaluated over organization columns, `setting:&lt;key&gt;` entries and the organization_metrics projection — so &#039;no order in 365 days&#039; is expressible without joining the orders app.
    rules_computed_at : Optional[str]
        When the rule last finished a COMPLETE recompute. Null after a rule change, and while a chunked recompute is still running — so it doubles as &quot;are the rule memberships trustworthy right now?&quot;.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    updated_at : Optional[str]
        When any column of this row last changed.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    rule_match: Optional[SegmentRuleMatch] = Field(default=None, alias='rule_match')
    rules: Optional[Dict[str, Any]] = Field(default=None, alias='rules')
    rules_computed_at: Optional[str] = Field(default=None, alias='rules_computed_at')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
