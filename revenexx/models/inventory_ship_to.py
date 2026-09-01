from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryShipTo(AppwriteModel):
    """
    Where the order is going. Read ONLY when the tenant&#039;s `allocation_strategy` is &#039;nearest&#039; — under &#039;priority&#039; or &#039;single_location&#039; it is accepted and ignored, so sending it is never wrong, it is just not always heard.

    Attributes
    ----------
    country : Optional[str]
        ISO country code of the delivery address. Locations whose `address.country` matches are tried before the rest, which is what stops a German order pulling from an overseas warehouse that merely sorts first.
    location_code : Optional[str]
        Prefer this location above everything else — a click-and-collect store the customer picked. It is a preference, not a demand: if it cannot cover the item the allocator moves on to the next location.
    """
    country: Optional[str] = Field(default=None, alias='country')
    location_code: Optional[str] = Field(default=None, alias='location_code')
