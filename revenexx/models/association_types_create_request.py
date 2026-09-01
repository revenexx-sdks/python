from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssociationTypesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The kind of relation between two products. Unique per tenant.
    is_quantified : Optional[bool]
        Declares that a relation of this kind carries a quantity — a bundle, a bill of materials. `product_associations.quantity` is where that number goes, and it is meaningless without this flag.
    is_two_way : Optional[bool]
        Declares the relation symmetric — an accessory of A is an accessory of B. It is a declaration a client reads: this app stores one row per direction and does not create the mirror for you.
    labels : Optional[Dict[str, Any]]
        What the relation is called in a product form, per language tag.
    """
    code: str = Field(..., alias='code')
    is_quantified: Optional[bool] = Field(default=None, alias='is_quantified')
    is_two_way: Optional[bool] = Field(default=None, alias='is_two_way')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
