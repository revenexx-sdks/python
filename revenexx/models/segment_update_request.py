from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.segment_rule_match import SegmentRuleMatch
from .segment_rules import SegmentRules

class SegmentUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Stable identifier, unique per tenant — what other apps and integrations name the segment by. Free text, but lowercase with underscores is the convention every seeded vocabulary follows.
    labels : Optional[Dict[str, Any]]
        Localized display names keyed by language tag. Null means nobody translated it and a client falls back to showing the code.
    position : Optional[float]
        Sort order in the cockpit, ascending. Ties fall back to insertion order. Default 0.
    rule_match : Optional[SegmentRuleMatch]
        How the conditions combine: &#039;all&#039; (default) is AND, &#039;any&#039; is OR. Null means the same as &#039;all&#039;.
    rules : Optional[SegmentRules]
        The selector that decides membership, stored verbatim. Null means the segment is manual-only. The same rule language product categories use, evaluated over organization columns, `setting:&lt;key&gt;` entries and the organization_metrics projection — so &#039;no order in 365 days&#039; is expressible without joining the orders app. Null makes the segment manual-only. Changing it does not move a single membership — run the recompute.
    """
    code: Optional[str] = Field(default=None, alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    rule_match: Optional[SegmentRuleMatch] = Field(default=None, alias='rule_match')
    rules: Optional[SegmentRules] = Field(default=None, alias='rules')
