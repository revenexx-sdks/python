from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRateTiersLadderRequest(AppwriteModel):
    """
    An evenly-stepped tier table. Tiers are generated at from_value, from_value+step, … up to to_value; each costs step_price more than the one before.

    Attributes
    ----------
    base_price : float
        Price of the first tier.
    from_value : Optional[float]
        First tier threshold (default 0), in the method&#039;s matrix measure.
    replace : Optional[bool]
        Replace the whole table (default true) or append to it.
    step : float
        Distance between two tiers. Must be &gt; 0.
    step_price : Optional[float]
        Added to each subsequent tier (default 0). A negative value is allowed as long as no tier ends up below 0.
    to_value : float
        Last tier threshold. The final tier keeps applying above it — a matrix has no upper bound. Must be &gt;= from_value.
    """
    base_price: float = Field(..., alias='base_price')
    from_value: Optional[float] = Field(default=None, alias='from_value')
    replace: Optional[bool] = Field(default=None, alias='replace')
    step: float = Field(..., alias='step')
    step_price: Optional[float] = Field(default=None, alias='step_price')
    to_value: float = Field(..., alias='to_value')
