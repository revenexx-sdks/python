from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductAssociationsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    association_type_id : str
        Which kind of relation this is — the `association_types` row.
    position : Optional[float]
        Order in which the targets are shown, ascending.
    product_id : str
        The product the relation starts at — the one whose detail page shows it.
    quantity : Optional[float]
        How many of the target belong to the source — the 4 in &quot;this bundle contains 4 casters&quot;. Only meaningful when the association type carries `is_quantified`; null on an ordinary cross-sell.
    target_product_id : str
        The product the relation points at — the accessory, the spare part, the cross-sell.
    """
    association_type_id: str = Field(..., alias='association_type_id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: str = Field(..., alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    target_product_id: str = Field(..., alias='target_product_id')
