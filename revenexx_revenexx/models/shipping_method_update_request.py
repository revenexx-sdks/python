from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_method_matrix_basis import ShippingMethodMatrixBasis
from ..enums.shipping_method_pricing_type import ShippingMethodPricingType

class ShippingMethodUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    carrier : Optional[str]
        Carrier anchor for the upcoming carrier connect (dynamic rates, tracking links).
    code : Optional[str]
        Stable method code, unique per tenant (e.g. standard, express).
    countries : Optional[List[Any]]
        Allowed ISO 3166-1 alpha-2 codes; null or empty = worldwide.
    currency : Optional[str]
        ISO 4217 code (default EUR).
    description : Optional[str]
        Typed model field.
    enabled : Optional[bool]
        Only enabled methods appear in rate responses (default false).
    eta_days_max : Optional[float]
        Delivery-time estimate for the checkout (days, upper bound).
    eta_days_min : Optional[float]
        Delivery-time estimate for the checkout (days, lower bound).
    free_above : Optional[float]
        Free shipping at or above this order value — wins over every pricing model.
    labels : Optional[Dict[str, Any]]
        Localized display names keyed by locale (e.g. {de, en}).
    matrix_attribute : Optional[str]
        Attribute name for matrix_basis &#039;attribute&#039;.
    matrix_basis : Optional[ShippingMethodMatrixBasis]
        The measure a matrix method prices over; &#039;attribute&#039; reads matrix_attribute from the rate request.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : Optional[str]
        Display name.
    position : Optional[float]
        Sort order in the checkout (default 0).
    price : Optional[float]
        The fixed price (default 0) — ignored for &#039;free&#039; and &#039;matrix&#039;.
    pricing_type : Optional[ShippingMethodPricingType]
        Pricing model (default &#039;fixed&#039;): one price, no price, or tiered over a measure.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    code: Optional[str] = Field(default=None, alias='code')
    countries: Optional[List[Any]] = Field(default=None, alias='countries')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    eta_days_max: Optional[float] = Field(default=None, alias='eta_days_max')
    eta_days_min: Optional[float] = Field(default=None, alias='eta_days_min')
    free_above: Optional[float] = Field(default=None, alias='free_above')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    matrix_attribute: Optional[str] = Field(default=None, alias='matrix_attribute')
    matrix_basis: Optional[ShippingMethodMatrixBasis] = Field(default=None, alias='matrix_basis')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
    pricing_type: Optional[ShippingMethodPricingType] = Field(default=None, alias='pricing_type')
