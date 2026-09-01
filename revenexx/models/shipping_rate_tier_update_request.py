from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRateTierUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    from_value : Optional[float]
        Lower bound of this tier, in the method&#039;s matrix measure — kilograms (or whatever the market&#039;s `weight_unit` names, converted through its factor) for a weight matrix, items for quantity, money in the method&#039;s currency for order_value, and the raw attribute value for &#039;attribute&#039;. INCLUSIVE: the tier applies from this value upward, and the tier that wins is the one with the highest from_value at or below the measured value, so a measure of exactly 10 is priced by the tier at 10 rather than the one below it. The last tier has no upper bound. Unique per method — a second tier at the same threshold is a 409, because which of the two won would be whatever the database returned first. Defaults to 0.
    position : Optional[float]
        Display order in the matrix editor (default 0; a bulk replace derives it from the array index). Pricing reads from_value, never this.
    price : Optional[float]
        What this tier costs, in the method&#039;s currency. Charged in full for the whole consignment — a matrix is a lookup table, not a rate per unit. Defaults to 0.
    """
    from_value: Optional[float] = Field(default=None, alias='from_value')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
