from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.segment_rule_preview_response_rule_match import SegmentRulePreviewResponseRuleMatch
from ..enums.segment_rule_preview_response_target import SegmentRulePreviewResponseTarget

class SegmentRulePreviewResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    cap : Optional[float]
        The cap that applied (5000), or null when the rule was answered by a single count query and no cap was needed.
    capped : Optional[bool]
        True when the combined evaluation hit the id cap, which makes `count` a lower bound.
    count : Optional[float]
        How many organizations the rule selects. Exact when &#039;capped&#039; is false; a LOWER BOUND when it is true.
    rule_match : Optional[SegmentRulePreviewResponseRuleMatch]
        How the conditions were combined for this preview.
    sample : Optional[List[Any]]
        A handful of the organizations the rule selects — enough for an operator to recognise whether the rule means what they thought. Never the full set.
    segment_id : Optional[str]
        The segment named in the path. It is not read — the rule comes from the body — but it has to exist.
    target : Optional[SegmentRulePreviewResponseTarget]
        What the rule selects. Only &#039;organizations&#039; exists.
    """
    cap: Optional[float] = Field(default=None, alias='cap')
    capped: Optional[bool] = Field(default=None, alias='capped')
    count: Optional[float] = Field(default=None, alias='count')
    rule_match: Optional[SegmentRulePreviewResponseRuleMatch] = Field(default=None, alias='rule_match')
    sample: Optional[List[Any]] = Field(default=None, alias='sample')
    segment_id: Optional[str] = Field(default=None, alias='segment_id')
    target: Optional[SegmentRulePreviewResponseTarget] = Field(default=None, alias='target')
