from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class StockLevelUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    location_id : Optional[str]
        The location this balance is held at — a `locations` row of this tenant (GET /inventories/locations). There is ONE stock row per (location, item): the same SKU in three warehouses is three rows, and what a storefront shows is their sum (POST /inventories/availability). Deleting the location deletes its stock rows with it. It has to exist already (GET /inventories/locations); an id no location carries is answered 400 by the foreign key, not 404.
    metadata : Optional[Dict[str, Any]]
        Free-form data the tenant keeps on this stock row, and ONE key this app reads: `backorder`. A literal boolean `true` there opts this item into backorders while `backorder_policy` is &#039;allow_per_sku&#039; — anything else, including the string &quot;true&quot;, does not, and the reservation is refused with 422. That is how a merchant backorders the supplier-stocked half of a catalogue without promising the rest.
    product_id : Optional[str]
        The product this row tracks, as the products app knows it. A row tracks a `product_id` or a `sku` — the database insists on at least one (CHECK `product_id is not null or sku is not null`) — and matching is exact: a row keyed by SKU is not found by product id.
    reorder_point : Optional[float]
        The available quantity at or below which this row belongs on the replenishment worklist (GET /inventories/reorder-alerts). Null falls back to the `reorder_point_default` setting, so replenishment works without a threshold per SKU; 0 never alerts, which is how one row opts out.
    sku : Optional[str]
        The article number this row tracks when there is no product id, which is the normal case for an ERP-stocked catalogue. Exact match, and the identity every stock call may use instead of a uuid.
    """
    location_id: Optional[str] = Field(default=None, alias='location_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    reorder_point: Optional[float] = Field(default=None, alias='reorder_point')
    sku: Optional[str] = Field(default=None, alias='sku')
