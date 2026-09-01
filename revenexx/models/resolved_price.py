from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_on_request_reason import PriceOnRequestReason
from ..enums.price_tax_basis import PriceTaxBasis
from ..enums.price_tax_basis_source import PriceTaxBasisSource
from .price_tier import PriceTier

class ResolvedPrice(AppwriteModel):
    """
    What one item costs this buyer, and which list said so.

    Attributes
    ----------
    currency : Optional[str]
        ISO 4217 currency of every amount on this item. Always the winning list’s currency, which always equals the call’s top-level `currency` — resolution only considers lists that match it, so a list and its answer can never disagree. null on an on-request item.
    error : Optional[str]
        Present ONLY on an item that named neither `product_id` nor `sku`, and always with this exact text. The call still answers 200 and the item comes back on_request, because one malformed line must not cost a whole cart its prices.
    line_total : Optional[float]
        `unit_price × quantity`, on the SAME basis as `unit_price` (so net if the list is net) and rounded to `basis.price_precision`. Not a tax-adjusted total — a cart computes its own from the net/gross pair.
    on_request : Optional[bool]
        true = no price for this buyer context — show &quot;price on request&quot;, never 0.
    on_request_reason : Optional[PriceOnRequestReason]
        Why there is no price: nothing prices it, a list marks it on-request, the tenant hides prices from anonymous buyers, or the item named neither product_id nor sku.
    price_list : Optional[Dict[str, Any]]
        The list that priced this item — null when nothing did. On an `on_request_entry` answer it is the list that said &quot;ask us&quot;.
    product_id : Optional[str]
        Echo of the requested `product_id` — null when the item was identified by SKU.
    quantity : Optional[float]
        The quantity this answer was computed for: what you sent, or 1 where you sent nothing or a non-positive value. It selects the tier and multiplies into `line_total`.
    sku : Optional[str]
        Echo of the requested `sku` — null when the item was identified by product id.
    tax_basis : Optional[PriceTaxBasis]
        Whether the stored amount is net or gross. THE fact a price cannot be without.
    tax_basis_source : Optional[PriceTaxBasisSource]
        Who decided it: the list&#039;s own tax_basis, a legacy tax_included=true on the list, or the tenant&#039;s tax_inclusive_default setting.
    tax_class : Optional[str]
        The tax class code that produced `tax_rate`: the product’s own class where the products app knows one, otherwise the buyer market’s default class. The codes are the tenant’s, defined in `markets.tax_classes` — conventionally `standard` and `reduced`. null when tax could not be resolved.
    tax_included : Optional[bool]
        Whether unit_price already contains tax. Never null on a priced item — it is `tax_basis` as a boolean, kept for existing callers.
    tax_rate : Optional[float]
        Tax rate as a PERCENTAGE (19 means 19 %, not 0.19), read from `markets.tax_classes` for this market and `tax_class`. null means UNKNOWN — a checkout must be able to tell that apart from a genuine 0 %.
    tiers : Optional[List[PriceTier]]
        The FULL quantity ladder the winning list holds for this item, ascending by `quantity_min` — what a PDP renders as a tier table. Empty on an on-request item.
    unit_price : Optional[float]
        Price for ONE unit, in `currency` and on the basis `tax_basis` names — a decimal amount in major units (19.90 EUR), never minor units/cents. It is the stored rung exactly as a merchant typed it, unrounded. Do not display it without reading `tax_basis`; prefer `unit_price_net`/`unit_price_gross`, which are unambiguous.
    unit_price_gross : Optional[float]
        Unit price INCLUDING tax, in `currency`, rounded to `basis.price_precision` under `basis.rounding_mode`. Derived from `unit_price` and `tax_rate` in whichever direction `tax_basis` requires. Present only when `tax.resolved` is true.
    unit_price_net : Optional[float]
        Unit price EXCLUDING tax, in `currency`, rounded to `basis.price_precision` under `basis.rounding_mode`. Present only when `tax.resolved` is true — null means the rate is unknown, not that there is no tax.
    """
    currency: Optional[str] = Field(default=None, alias='currency')
    error: Optional[str] = Field(default=None, alias='error')
    line_total: Optional[float] = Field(default=None, alias='line_total')
    on_request: Optional[bool] = Field(default=None, alias='on_request')
    on_request_reason: Optional[PriceOnRequestReason] = Field(default=None, alias='on_request_reason')
    price_list: Optional[Dict[str, Any]] = Field(default=None, alias='price_list')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_basis: Optional[PriceTaxBasis] = Field(default=None, alias='tax_basis')
    tax_basis_source: Optional[PriceTaxBasisSource] = Field(default=None, alias='tax_basis_source')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
    tax_included: Optional[bool] = Field(default=None, alias='tax_included')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    tiers: Optional[List[PriceTier]] = Field(default=None, alias='tiers')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    unit_price_gross: Optional[float] = Field(default=None, alias='unit_price_gross')
    unit_price_net: Optional[float] = Field(default=None, alias='unit_price_net')
