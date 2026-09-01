from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartConversionReservation(AppwriteModel):
    """
    What this app ASKED inventories for, and what it answered. This app holds no stock: inventories picks the location, applies the backorder policy and owns the hold&#039;s expiry.

    Attributes
    ----------
    backordered : Optional[float]
        Lines inventories accepted without stock behind them, under the tenant&#039;s backorder policy — its policy, not this app&#039;s.
    expires_at : Optional[str]
        inventories&#039; hold deadline — its TTL, not this app&#039;s.
    ok : Optional[bool]
        A hold exists. False with `requested: true` means inventories was asked and refused — `reason` says why, and only convert_reserves_stock = require turns that into a 409.
    order_ref : Optional[str]
        The reference the reservation was booked under: the `order_ref` of the request, or the cart id when the call carried none. This is the string to hand inventories when releasing the hold.
    reason : Optional[str]
        Why no hold exists — stated, never implied. Present whenever `ok` is false, and also on the never case.
    requested : Optional[bool]
        False when convert_reserves_stock is &#039;never&#039; — no call was made at all, which is reported rather than dressed up as a silent success.
    reservations : Optional[float]
        Lines inventories confirmed a hold for.
    status : Optional[float]
        The HTTP status inventories answered with, present only when it refused. 404 is its own case: the tenant has no inventories app at all, which is a different problem from not enough stock.
    """
    backordered: Optional[float] = Field(default=None, alias='backordered')
    expires_at: Optional[str] = Field(default=None, alias='expires_at')
    ok: Optional[bool] = Field(default=None, alias='ok')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    reason: Optional[str] = Field(default=None, alias='reason')
    requested: Optional[bool] = Field(default=None, alias='requested')
    reservations: Optional[float] = Field(default=None, alias='reservations')
    status: Optional[float] = Field(default=None, alias='status')
