from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRateTierReplaceItem(AppwriteModel):
    """
    A matrix tier of the new set (from_value → price) — null falls back to 0, position derives from the array order.

    Attributes
    ----------
    from_value : Optional[float]
        Lower bound of this tier, in the method&#039;s matrix measure — kilograms (or whatever the market&#039;s `weight_unit` names, converted through its factor) for a weight matrix, items for quantity, money in the method&#039;s currency for order_value, and the raw attribute value for &#039;attribute&#039;. INCLUSIVE: the tier applies from this value upward, and the tier that wins is the one with the highest from_value at or below the measured value, so a measure of exactly 10 is priced by the tier at 10 rather than the one below it. The last tier has no upper bound. Unique per method — a second tier at the same threshold is a 409, because which of the two won would be whatever the database returned first. Null falls back to 0.
    position : Optional[float]
        Ignored — derived from the array index.
    price : Optional[float]
        What this tier costs, in the method&#039;s currency. Charged in full for the whole consignment — a matrix is a lookup table, not a rate per unit. Null falls back to 0.
    """
    from_value: Optional[float] = Field(default=None, alias='from_value')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
