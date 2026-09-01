from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.categories_rule_match import CategoriesRuleMatch

class CategoriesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The category&#039;s stable identifier — what an import and a storefront join on, and what survives a rename of the label. Unique per tenant.
    labels : Optional[Dict[str, Any]]
        The category name a person sees, per language tag. The catalog reads by name, not by code — a locale left blank falls back to the next filled one.
    parent_id : Optional[str]
        The category this one hangs under. Null is a root of the tree. Deleting a parent lifts its children to the root rather than deleting them, so a mis-click never takes a subtree with it.
    path : Optional[str]
        A materialized position in the tree, kept for importers that carry one (`tools/power_tools/cordless_drills`). Nothing in this app writes or reads it — `parent_id` is the structure this app navigates.
    position : Optional[float]
        Order among the siblings under the same parent, ascending.
    rule_match : Optional[CategoriesRuleMatch]
        How the conditions combine: &#039;all&#039; ANDs them (the default), &#039;any&#039; ORs them. It is a column of its own rather than a key of `rules` because the compiler reads the two separately.
    rules : Optional[Dict[str, Any]]
        The selector that makes this a RULE-DRIVEN category. Null means hand-picked. Matching products are MATERIALIZED as `product_categories` rows with source `rule`, next to the hand-picked ones a recompute never touches; `POST /products/categories/{category_id}/rules/preview` dry-runs this exact document before it is stored. Conditions address the `common` bucket of a product&#039;s values — a value held per locale or per channel has no single answer for a rule to test.
    rules_computed_at : Optional[str]
        When the rule last ran TO COMPLETION and its memberships were synced. Null means no pass has ever finished — a recompute is chunked, so a half-finished pass leaves this untouched.
    values : Optional[Dict[str, Any]]
        Whatever this catalog keeps on a category beyond the model — the keys belong to the tenant, not to this app, and nothing here reads them.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    path: Optional[str] = Field(default=None, alias='path')
    position: Optional[float] = Field(default=None, alias='position')
    rule_match: Optional[CategoriesRuleMatch] = Field(default=None, alias='rule_match')
    rules: Optional[Dict[str, Any]] = Field(default=None, alias='rules')
    rules_computed_at: Optional[str] = Field(default=None, alias='rules_computed_at')
    values: Optional[Dict[str, Any]] = Field(default=None, alias='values')
