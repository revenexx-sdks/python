from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamilyVariantsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    axes : Optional[Dict[str, Any]]
        The attribute codes a product model splits its variants on. Two shapes are in the wild and both are read: a bare list of codes, or one entry per level, outermost first — `[{&quot;level&quot;: 1, &quot;axes&quot;: [&quot;colour&quot;]}, {&quot;level&quot;: 2, &quot;axes&quot;: [&quot;size&quot;]}]`. An attribute named here is READ-ONLY on the model and set on each variant, which is what `AttributeField.readonly_reason` reports.
    code : str
        The variant structure&#039;s stable identifier — how this family splits, not which product it splits. Unique per tenant.
    family_id : str
        The family this variant structure belongs to. A family may carry several, and a product names the one it follows through `family_variant_id`.
    labels : Optional[Dict[str, Any]]
        What the variant structure is called, per language tag.
    """
    axes: Optional[Dict[str, Any]] = Field(default=None, alias='axes')
    code: str = Field(..., alias='code')
    family_id: str = Field(..., alias='family_id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
