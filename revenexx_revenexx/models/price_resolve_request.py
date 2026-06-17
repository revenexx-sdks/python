from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_resolve_item import PriceResolveItem

class PriceResolveRequest(AppwriteModel):
    """
    Buyer context + items. Unpriceable items come back as on_request — a missing price is a first-class state, never 0.

    Attributes
    ----------
    at : Optional[str]
        Point in time for validity windows (ISO 8601 timestamp, default now).
    channel_id : Optional[str]
        Buyer context: channel.
    contact_id : Optional[str]
        Buyer context: contact — most specific scope.
    currency : Optional[str]
        ISO 4217 code (default EUR) — only lists in this currency resolve.
    items : List[PriceResolveItem]
        Items to price (at most 200 per call).
    market_id : Optional[str]
        Buyer context: market.
    organization_id : Optional[str]
        Buyer context: organization.
    """
    at: Optional[str] = Field(default=None, alias='at')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    items: List[PriceResolveItem] = Field(..., alias='items')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
