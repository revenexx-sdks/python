from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_price_snapshot_mode import CartPriceSnapshotMode

class CartConversionPricing(AppwriteModel):
    """
    How price_snapshot_mode settled the two prices every line carries.

    Attributes
    ----------
    lines : Optional[float]
        Lines in the cart when it converted.
    lines_changed : Optional[float]
        Lines the mode had to rewrite because snapshot and unit_price disagreed — repriced in &#039;snapshot&#039; mode, re-snapshotted in &#039;live&#039; mode. A line whose snapshot carries no readable price is never touched in either mode.
    mode : Optional[CartPriceSnapshotMode]
        The tenant&#039;s price_snapshot_mode, as it ran. &#039;snapshot&#039; books the order on the price the buyer was shown; &#039;live&#039; books it on the line&#039;s current unit_price and rewrites the snapshot to agree, so the frozen line never claims a price nobody was charged.
    subtotal_after : Optional[float]
        The cart&#039;s frozen subtotal, and what the order is booked on.
    subtotal_before : Optional[float]
        The cart&#039;s subtotal as it stood before the mode was applied. Compare it with subtotal_after and &#039;why is the order €4 off the cart&#039; is answered by the response instead of by an argument.
    """
    lines: Optional[float] = Field(default=None, alias='lines')
    lines_changed: Optional[float] = Field(default=None, alias='lines_changed')
    mode: Optional[CartPriceSnapshotMode] = Field(default=None, alias='mode')
    subtotal_after: Optional[float] = Field(default=None, alias='subtotal_after')
    subtotal_before: Optional[float] = Field(default=None, alias='subtotal_before')
