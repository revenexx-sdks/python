from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRatesRequest(AppwriteModel):
    """
    The buyer context the checkout resolves rates for — matrix methods need their measure (weight, quantity, order value or attribute) to apply.

    Attributes
    ----------
    attributes : Optional[Dict[str, Any]]
        Measure values for attribute matrices, keyed by attribute name.
    country : Optional[str]
        Destination ISO 3166-1 alpha-2 code — checked against method country restrictions.
    currency : Optional[str]
        Echoed into the rates (default &#039;EUR&#039;).
    market_id : Optional[str]
        Buyer market for tax resolution (else inferred from country, else first market).
    order_value : Optional[float]
        Order value (default 0) — drives free-above thresholds and order_value matrices.
    quantity : Optional[float]
        Total quantity — measure for quantity matrices.
    weight : Optional[float]
        Total weight — measure for weight matrices.
    """
    attributes: Optional[Dict[str, Any]] = Field(default=None, alias='attributes')
    country: Optional[str] = Field(default=None, alias='country')
    currency: Optional[str] = Field(default=None, alias='currency')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    order_value: Optional[float] = Field(default=None, alias='order_value')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    weight: Optional[float] = Field(default=None, alias='weight')
