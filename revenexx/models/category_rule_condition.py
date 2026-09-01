from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.category_rule_operator import CategoryRuleOperator

class CategoryRuleCondition(AppwriteModel):
    """
    

    Attributes
    ----------
    field : str
        A product column (sku, kind, enabled, family_id, parent_id) or &#039;attribute:&lt;code&gt;&#039; for the common bucket of attribute_values. An attribute code is [A-Za-z0-9_]+. Locale-/channel-scoped attributes are not supported.
    operator : CategoryRuleOperator
        How to compare. &#039;eq&#039;/&#039;neq&#039; are equality, &#039;gt&#039;/&#039;gte&#039;/&#039;lt&#039;/&#039;lte&#039; order (numerically for a number, as text for a string), &#039;in&#039; membership, &#039;contains&#039;/&#039;starts_with&#039;/&#039;ends_with&#039; substring, &#039;is_empty&#039;/&#039;is_not_empty&#039; presence — those last two take no `value`.
    value : Optional[str]
        Comparison value. An array for &#039;in&#039; — non-empty, at most 200 entries, all of the same type; omitted for &#039;is_empty&#039;/&#039;is_not_empty&#039;; a non-empty string for &#039;contains&#039;/&#039;starts_with&#039;/&#039;ends_with&#039;; a string or number for gt/gte/lt/lte. Numbers compare numerically (jsonb), strings as text.
    """
    field: str = Field(..., alias='field')
    operator: CategoryRuleOperator = Field(..., alias='operator')
    value: Optional[str] = Field(default=None, alias='value')
