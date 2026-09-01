from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_carrier_source import ShippingCarrierSource
from .shipping_delivery_estimate import ShippingDeliveryEstimate
from ..enums.shipping_rate_pricing_type import ShippingRatePricingType
from ..enums.shipping_tax_source import ShippingTaxSource

class ShippingRate(AppwriteModel):
    """
    One offerable shipping method with its computed price for this buyer context.

    Attributes
    ----------
    carrier : Optional[str]
        The carrier CODE — unchanged for every caller that already reads it. The method&#039;s carrier_id, else its `carrier` text, else the tenant&#039;s default_carrier.
    carrier_name : Optional[str]
        The carrier row&#039;s display name, or null when the code names no maintained carrier.
    carrier_service_level : Optional[str]
        The class of service this rate is, from the carrier row — a code into the tenant&#039;s service levels.
    carrier_source : Optional[ShippingCarrierSource]
        Which step of the chain answered: &#039;method&#039; (carrier_id), &#039;method_code&#039; (the method&#039;s text matched a carrier), &#039;method_text&#039; (it matched none), &#039;tenant_default&#039; / &#039;tenant_default_text&#039; (the setting, matched or not).
    code : Optional[str]
        Stable method code, unique per tenant (e.g. standard, express). What a checkout and an order line store, so it is the value every integration joins on.
    currency : Optional[str]
        ISO 4217 code (default EUR). Exactly three characters — the column says so. Echoed into a rate, never converted: this app prices in the currency the method carries.
    delivery : Optional[ShippingDeliveryEstimate]
        The delivery window a checkout can print. Calendar days, cut-off evaluated in UTC (send `at` to control the instant).
    description : Optional[str]
        The sentence under the name in the checkout — the delivery promise in words. Null when the name says enough.
    eta_days_max : Optional[float]
        Transit time upper bound in calendar days, as applied: the method&#039;s own, else the carrier&#039;s.
    eta_days_min : Optional[float]
        Transit time lower bound in calendar days, as applied: the method&#039;s own, else the carrier&#039;s.
    free_reason : Optional[str]
        Only when a free-above threshold applied. Names the compared value AND its basis (net or gross), and says whether the threshold was the method&#039;s own or shop-wide — the free-shipping promise is a common dispute and this is the sentence that settles it.
    labels : Optional[Dict[str, Any]]
        Localized display names. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    name : Optional[str]
        Display name shown in the checkout.
    position : Optional[float]
        Sort order in the checkout (default 0) — a rate answer is returned in this order.
    price : Optional[float]
        The shipping fee for this basket, in `currency`, rounded to two decimals — 0 when a free-above threshold or a &#039;free&#039; method applied. NULL when `quote_required` is true: the price is unknown, not zero, and a checkout must not add 0.00 for it.
    pricing_type : Optional[ShippingRatePricingType]
        Pricing model (default &#039;fixed&#039;): &#039;fixed&#039; is one price for every basket, &#039;free&#039; is no price at all, &#039;matrix&#039; is a tiered price read off this method&#039;s rate tiers. Only &#039;matrix&#039; looks at matrix_basis, quote_above and the tier table.
    quote_reason : Optional[str]
        Only when quote_required — the measure and the threshold it exceeded, so an operator pricing it by hand can see what triggered the referral.
    quote_required : Optional[bool]
        True when the matrix measure is above the method&#039;s quote_above threshold: the method is still offered, carries no price, and the storefront shows &#039;shipping on request&#039;. The order is placed without a computed shipping fee.
    tax_class : Optional[str]
        The tax class this rate was taxed under, as a code in markets.tax_classes — the method&#039;s own, the tenant&#039;s shipping_tax_class, or the market&#039;s default, whichever answered. Null means unresolved, not untaxed.
    tax_rate : Optional[float]
        The rate in percent from markets.tax_classes for this market and tax_class — 19 means 19 %. Null means UNKNOWN, never 0: read `tax.resolved` before treating a missing rate as tax-free.
    tax_source : Optional[ShippingTaxSource]
        Which step of the chain supplied the rate: the method&#039;s own class, the tenant&#039;s shipping_tax_class, the market default, or the tenant&#039;s default_shipping_tax_rate. Null means unknown, NOT untaxed.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    carrier_name: Optional[str] = Field(default=None, alias='carrier_name')
    carrier_service_level: Optional[str] = Field(default=None, alias='carrier_service_level')
    carrier_source: Optional[ShippingCarrierSource] = Field(default=None, alias='carrier_source')
    code: Optional[str] = Field(default=None, alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    delivery: Optional[ShippingDeliveryEstimate] = Field(default=None, alias='delivery')
    description: Optional[str] = Field(default=None, alias='description')
    eta_days_max: Optional[float] = Field(default=None, alias='eta_days_max')
    eta_days_min: Optional[float] = Field(default=None, alias='eta_days_min')
    free_reason: Optional[str] = Field(default=None, alias='free_reason')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
    pricing_type: Optional[ShippingRatePricingType] = Field(default=None, alias='pricing_type')
    quote_reason: Optional[str] = Field(default=None, alias='quote_reason')
    quote_required: Optional[bool] = Field(default=None, alias='quote_required')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    tax_source: Optional[ShippingTaxSource] = Field(default=None, alias='tax_source')
