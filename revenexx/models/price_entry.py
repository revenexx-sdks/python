from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_entry_type import PriceEntryType

class PriceEntry(AppwriteModel):
    """
    One rung of one item’s quantity ladder inside one price list. The ladder IS the set of entries sharing an identity (product_id or sku); the amount is in the LIST’s currency and on the LIST’s tax basis.

    Attributes
    ----------
    created_at : Optional[str]
        When the entry was created.
    id : Optional[str]
        The entry itself — one rung of one item’s quantity ladder.
    metadata : Optional[Dict[str, Any]]
        Free-form bag, unvalidated and never read by this app: whatever JSON object you write round-trips exactly. Its keys are the integration’s own, e.g. {&quot;source_system&quot;: &quot;erp&quot;, &quot;imported_batch&quot;: &quot;2026-02-14&quot;}.
    price_list_id : Optional[str]
        The price list this entry belongs to, and therefore the currency and tax basis its amount is on. Set from the path on write.
    price_type : Optional[PriceEntryType]
        `standard` is a number. `on_request` is the explicit no-price marker: it STOPS resolution for this item on this list and answers price-on-request, even where a cheaper list exists — the list is authoritative for this buyer and it says &quot;ask us&quot;.
    product_id : Optional[str]
        The product this rung prices. An entry needs `product_id` or `sku` (a row CHECK enforces it); an entry that carries both prices whichever of the two the resolve item names.
    quantity_min : Optional[float]
        Lowest quantity this price applies from (Staffelpreis). The ladder for one item is the set of entries sharing its identity: the rung with the HIGHEST quantity_min at or below the requested quantity wins, and below the first rung the first rung’s price applies — a minimum order quantity belongs to the catalog, not to the ladder.
    sku : Optional[str]
        The article number this rung prices, for a price book keyed by SKU rather than by product id — matched exactly, never normalised or case-folded.
    unit : Optional[str]
        The unit of measure the price is per — ‘pcs’, ‘m’, ‘kg’, a packaging size. Free text: this app neither validates nor converts it, and the `quantity` of a resolve call is counted in it.
    unit_price : Optional[float]
        Price for ONE unit of `unit`, expressed in the list’s `currency` and on the list’s `tax_basis` — a decimal amount in major units (19.90 EUR), never minor units/cents. Stored at 4 decimals so a per-1000-piece price survives, and echoed back exactly as it was written; only DERIVED amounts (net, gross, line totals) are rounded to the tenant’s `price_precision`.
    updated_at : Optional[str]
        When the entry last changed. A bulk adjust only writes the rows whose price actually moved, so this is a real &quot;the price changed here&quot; marker.
    valid_from : Optional[str]
        Start of this entry’s own validity; null = open-ended. This is how a promo price is expressed — a second rung for the same item and quantity, live only for its window.
    valid_until : Optional[str]
        End of this entry’s own validity; null = open-ended. Outside the window the rung is skipped and the ladder resolves as if it were not there.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    price_list_id: Optional[str] = Field(default=None, alias='price_list_id')
    price_type: Optional[PriceEntryType] = Field(default=None, alias='price_type')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity_min: Optional[float] = Field(default=None, alias='quantity_min')
    sku: Optional[str] = Field(default=None, alias='sku')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
