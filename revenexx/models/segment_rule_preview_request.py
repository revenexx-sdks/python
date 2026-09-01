from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .segment_rule_condition import SegmentRuleCondition
from ..enums.segment_rule_preview_request_rule_match import SegmentRulePreviewRequestRuleMatch
from ..enums.segment_rule_preview_request_target import SegmentRulePreviewRequestTarget

class SegmentRulePreviewRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    conditions : List[SegmentRuleCondition]
        The conditions, combined by `rule_match`. At least one, at most 25.
    rule_match : Optional[SegmentRulePreviewRequestRuleMatch]
        How the conditions combine. Default &#039;all&#039;.
    target : Optional[SegmentRulePreviewRequestTarget]
        Only &#039;organizations&#039; is supported; any other value is rejected. A segment groups COMPANIES — the people are reached through them.
    """
    conditions: List[SegmentRuleCondition] = Field(..., alias='conditions')
    rule_match: Optional[SegmentRulePreviewRequestRuleMatch] = Field(default=None, alias='rule_match')
    target: Optional[SegmentRulePreviewRequestTarget] = Field(default=None, alias='target')
