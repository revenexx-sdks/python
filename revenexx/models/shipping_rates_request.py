from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRatesRequest(AppwriteModel):
    """
    The buyer context the checkout resolves rates for — matrix methods need their measure (weight, quantity, order value or attribute) to apply.

    Attributes
    ----------
    at : Optional[str]
        The instant to evaluate the delivery estimate at (ISO 8601). Omitted: now. Lets a storefront compute the cut-off in its own timezone.
    attributes : Optional[Dict[str, Any]]
        Measure values for attribute matrices, keyed by attribute NAME — the key a matrix method names in its matrix_attribute, and the value the number its tiers are matched against. Summed over the basket by the caller, not by this app. Only the key a method asks for is read; anything else in the map is carried along and ignored, and a value that is not a finite number excludes that method with a reason rather than failing the quote.
    country : Optional[str]
        Destination ISO 3166-1 alpha-2 code — compared upper-cased against method and carrier country restrictions. Omitted or null: every method that restricts by country is excluded, with a reason.
    currency : Optional[str]
        ISO 4217 code, echoed into the rates (default &#039;EUR&#039;). Echoed, not converted: this app prices in the currency the method carries.
    market_id : Optional[str]
        Buyer market for tax resolution. Omitted: the market matching `country`, else the tenant&#039;s sole market — never an arbitrary one.
    order_value : Optional[float]
        Order value (default 0) — drives order_value matrices, and free-above thresholds when no sided value is sent. Read on the basis the tenant&#039;s free_above_compares setting declares.
    order_value_gross : Optional[float]
        Order value including tax. Compared against free-above thresholds when free_above_compares is &#039;gross&#039;.
    order_value_net : Optional[float]
        Order value excluding tax. Compared against free-above thresholds when free_above_compares is &#039;net&#039;.
    quantity : Optional[float]
        Total quantity — measure for quantity matrices.
    weight : Optional[float]
        Total weight — measure for weight matrices. Read in weight_unit and converted to the unit the tiers are keyed in.
    weight_unit : Optional[str]
        The unit `weight` is expressed in, as a CODE into the tenant&#039;s own weight units (GET /shipping/weight-units). Omitted, it is the unit this market quotes in. A unit the tenant does not keep is a 400 — a mis-read weight prices the wrong bracket silently, and guessing is worse than refusing.
    """
    at: Optional[str] = Field(default=None, alias='at')
    attributes: Optional[Dict[str, Any]] = Field(default=None, alias='attributes')
    country: Optional[str] = Field(default=None, alias='country')
    currency: Optional[str] = Field(default=None, alias='currency')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    order_value: Optional[float] = Field(default=None, alias='order_value')
    order_value_gross: Optional[float] = Field(default=None, alias='order_value_gross')
    order_value_net: Optional[float] = Field(default=None, alias='order_value_net')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    weight: Optional[float] = Field(default=None, alias='weight')
    weight_unit: Optional[str] = Field(default=None, alias='weight_unit')
