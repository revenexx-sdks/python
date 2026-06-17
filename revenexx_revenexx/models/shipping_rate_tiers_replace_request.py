from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .shipping_rate_tier_replace_item import ShippingRateTierReplaceItem

class ShippingRateTiersReplaceRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    tiers : List[ShippingRateTierReplaceItem]
        The complete new tier set (set semantics) — positions are derived from the array order.
    """
    tiers: List[ShippingRateTierReplaceItem] = Field(..., alias='tiers')
