from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.segment_rule_operator import SegmentRuleOperator

class SegmentRuleCondition(AppwriteModel):
    """
    

    Attributes
    ----------
    field : str
        What the organization IS: an organizations column (name, status, vat_id, branche, external_team_id) or &#039;setting:&lt;key&gt;&#039; for a top-level key of organizations.settings. Or what it DID, read from the organization_metrics projection: order_count, order_count_30d/90d/365d, revenue_total, revenue_30d/90d/365d, avg_order_value, avg_order_value_365d, first_order_at, last_order_at, currency — plus the virtual days_since_last_order (gt/gte/lt/lte only), which compares last_order_at against a cut-off computed at evaluation time and never matches an organization that never ordered (use last_order_at is_empty for those).
    operator : SegmentRuleOperator
        How `value` is compared to `field`. `contains`/`starts_with`/`ends_with` are text matches; `in` takes an array; `is_empty`/`is_not_empty` take no value at all.
    value : Optional[str]
        Omitted for is_empty/is_not_empty; an array for &#039;in&#039;; a string, number or boolean otherwise. A number or boolean makes a &#039;setting:&#039; condition compare as JSONB, so it only matches values stored as a JSON number/boolean.
    """
    field: str = Field(..., alias='field')
    operator: SegmentRuleOperator = Field(..., alias='operator')
    value: Optional[str] = Field(default=None, alias='value')
