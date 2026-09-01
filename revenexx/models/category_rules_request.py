from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .category_rule_condition import CategoryRuleCondition
from ..enums.category_rule_match import CategoryRuleMatch

class CategoryRulesRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    conditions : List[CategoryRuleCondition]
        Between 1 and 25 conditions — a rule is a selector, not a query language. An empty list is a 400, not &quot;everything&quot;.
    rule_match : Optional[CategoryRuleMatch]
        &#039;all&#039; ANDs every condition (default), &#039;any&#039; ORs them.
    """
    conditions: List[CategoryRuleCondition] = Field(..., alias='conditions')
    rule_match: Optional[CategoryRuleMatch] = Field(default=None, alias='rule_match')
