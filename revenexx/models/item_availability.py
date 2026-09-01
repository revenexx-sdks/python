from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .location_availability import LocationAvailability

class ItemAvailability(AppwriteModel):
    """
    

    Attributes
    ----------
    available : Optional[float]
        on_hand − reserved across the locations in scope: available-to-promise, and the number a storefront shows. It can be NEGATIVE once backorders have been reserved beyond stock — nothing floors it, because &quot;sold more than we hold&quot; is a real state a merchant needs to see.
    locations : Optional[List[LocationAvailability]]
        The per-location breakdown behind the summed figures — which place could actually ship it.
    on_hand : Optional[float]
        Physically in stock, summed across the locations in scope (every enabled location, or the one `location_code` named). Promised units are included, so this is NOT what may be sold.
    orderable : Optional[bool]
        True when the item is tracked and `available &gt;= requested` at this moment. A SNAPSHOT, not a hold: nothing is set aside until POST /inventories/reserve, and two checkouts can both read true for the last unit.
    product_id : Optional[str]
        The product id as it was asked for, echoed. Null when the item was named by SKU.
    requested : Optional[float]
        The quantity the check was made against — the item&#039;s own `quantity`, or 1 when none was sent. `orderable` answers &quot;can I have this many?&quot;, so it is only as strict as this number.
    reserved : Optional[float]
        Already promised to orders, summed across the same locations — the part of `on_hand` that is spoken for.
    sku : Optional[str]
        The SKU as it was asked for, echoed. Null when the item was named by product id.
    tracked : Optional[bool]
        False when this app has never seen the item: no stock row anywhere in scope. It is not an error and not a zero — the storefront decides whether an untracked item sells freely (a service, a made-to-order piece) or not at all. `on_hand`, `reserved` and `available` are 0 in that case, and `orderable` is false.
    """
    available: Optional[float] = Field(default=None, alias='available')
    locations: Optional[List[LocationAvailability]] = Field(default=None, alias='locations')
    on_hand: Optional[float] = Field(default=None, alias='on_hand')
    orderable: Optional[bool] = Field(default=None, alias='orderable')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    requested: Optional[float] = Field(default=None, alias='requested')
    reserved: Optional[float] = Field(default=None, alias='reserved')
    sku: Optional[str] = Field(default=None, alias='sku')
    tracked: Optional[bool] = Field(default=None, alias='tracked')
