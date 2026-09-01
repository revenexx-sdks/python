from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .segment_rule_condition import SegmentRuleCondition
from ..enums.segment_rules_target import SegmentRulesTarget

class SegmentRules(AppwriteModel):
    """
    The selector that decides membership, stored verbatim. Null means the segment is manual-only. The same rule language product categories use, evaluated over organization columns, `setting:&lt;key&gt;` entries and the organization_metrics projection — so &#039;no order in 365 days&#039; is expressible without joining the orders app. Null makes the segment manual-only. Changing it does not move a single membership — run the recompute.

    Attributes
    ----------
    conditions : List[SegmentRuleCondition]
        The conditions, combined by `rule_match`. At least one, at most 25.
    target : Optional[SegmentRulesTarget]
        Only &#039;organizations&#039; is supported; any other value is rejected. A segment groups COMPANIES — the people are reached through them.
    """
    conditions: List[SegmentRuleCondition] = Field(..., alias='conditions')
    target: Optional[SegmentRulesTarget] = Field(default=None, alias='target')
