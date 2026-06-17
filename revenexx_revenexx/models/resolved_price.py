from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ResolvedPrice(AppwriteModel):
    """
    

    Attributes
    ----------
    currency : Optional[str]
        Typed model field.
    line_total : Optional[float]
        Typed model field.
    on_request : Optional[bool]
        true = no price for this buyer context — show &quot;price on request&quot;, never 0.
    price_list : Optional[Dict[str, Any]]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    tax_class : Optional[str]
        Resolved tax class code (from the product, or the market default).
    tax_included : Optional[bool]
        Typed model field.
    tax_rate : Optional[float]
        Tax rate % from markets.tax_classes for this market + tax_class.
    tiers : Optional[List[Any]]
        Typed model field.
    unit_price : Optional[float]
        Stored price as-is (net or gross per tax_included). Prefer unit_price_net/unit_price_gross.
    unit_price_gross : Optional[float]
        Gross unit price (incl. tax).
    unit_price_net : Optional[float]
        Net unit price (excl. tax).
    """
    currency: Optional[str] = Field(default=None, alias='currency')
    line_total: Optional[float] = Field(default=None, alias='line_total')
    on_request: Optional[bool] = Field(default=None, alias='on_request')
    price_list: Optional[Dict[str, Any]] = Field(default=None, alias='price_list')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
    tax_included: Optional[bool] = Field(default=None, alias='tax_included')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    tiers: Optional[List[Any]] = Field(default=None, alias='tiers')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    unit_price_gross: Optional[float] = Field(default=None, alias='unit_price_gross')
    unit_price_net: Optional[float] = Field(default=None, alias='unit_price_net')
