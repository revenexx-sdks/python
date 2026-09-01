from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class LocationAvailability(AppwriteModel):
    """
    What one location holds of this item. Only enabled locations appear, and only those with a stock row for the item — a location that has never held it is absent rather than zero.

    Attributes
    ----------
    available : Optional[float]
        on_hand − reserved at this location — what this one place can still promise.
    location : Optional[str]
        The location CODE (`locations.code`) — the same value `location_code` takes in a request. Falls back to the raw location id in the rare case where the location row disappeared between the two reads.
    on_hand : Optional[float]
        Physically at this location, promised units included.
    reserved : Optional[float]
        Held for orders at this location.
    """
    available: Optional[float] = Field(default=None, alias='available')
    location: Optional[str] = Field(default=None, alias='location')
    on_hand: Optional[float] = Field(default=None, alias='on_hand')
    reserved: Optional[float] = Field(default=None, alias='reserved')
