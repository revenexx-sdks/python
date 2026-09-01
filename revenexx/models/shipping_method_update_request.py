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
        Carrier CODE, kept from before shipping_carriers existed. Looked up in the carrier table when carrier_id is not set, so an existing value keeps working and gains a tracking template; a code nobody maintains is still reported as a plain name.
    carrier_id : Optional[str]
        The carrier this method ships with. Wins over `carrier` and supplies the tracking template, pickup cut-off, handling time and transit days.
    code : Optional[str]
        Stable method code, unique per tenant (e.g. standard, express). What a checkout and an order line store, so it is the value every integration joins on.
    countries : Optional[List[Any]]
        The countries this method may be offered into. ISO 3166-1 alpha-2 codes; null or an empty array means no restriction. Compared upper-cased, so a lower-case entry still matches. Declared as an array rather than the bare object a jsonb column derives to — this one is always a list. ANDed with the carrier&#039;s own reach.
    currency : Optional[str]
        ISO 4217 code (default EUR). Exactly three characters — the column says so. Echoed into a rate, never converted: this app prices in the currency the method carries.
    description : Optional[str]
        The sentence under the name in the checkout — the delivery promise in words. Null when the name says enough.
    enabled : Optional[bool]
        Only enabled methods are ever quoted (default false); a disabled one is reported in `excluded` rather than hidden.
    eta_days_max : Optional[float]
        Transit time upper bound in calendar days. Falls back to the carrier&#039;s when null.
    eta_days_min : Optional[float]
        Transit time lower bound in calendar days, for the checkout. Falls back to the carrier&#039;s when null.
    free_above : Optional[float]
        Free shipping at or above this order value — wins over every pricing model, including a matrix. Compared net or gross as the market&#039;s free_above_compares setting declares. Null falls back to the tenant&#039;s shop-wide free_shipping_threshold.
    labels : Optional[Dict[str, Any]]
        Localized display names. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    matrix_attribute : Optional[str]
        Attribute name for matrix_basis &#039;attribute&#039; — the key the rate request&#039;s `attributes` map is read at. Free text: the set of attributes is the catalogue&#039;s, not this app&#039;s.
    matrix_basis : Optional[ShippingMethodMatrixBasis]
        The measure a matrix method prices its tiers over: total basket weight (in the market&#039;s weight unit), total item count, order value, or &#039;attribute&#039; — any number the rate request carries under matrix_attribute. Null falls back to the tenant&#039;s matrix_basis_default. Ignored unless pricing_type is &#039;matrix&#039;.
    metadata : Optional[Dict[str, Any]]
        Free-form jsonb the platform never reads or validates — whatever the merchant or their integration needs to keep beside the row (a customer number with the carrier, an ERP key, a label-printer id). The shape varies BY INTEGRATION, not by anything this app knows, so no key is declared and none is reserved; the example is one plausible instance rather than a schema. A flat map of scalars is the convention, and nothing enforces it.
    name : Optional[str]
        Display name shown in the checkout.
    position : Optional[float]
        Sort order in the checkout (default 0) — a rate answer is returned in this order.
    price : Optional[float]
        The fixed price (default 0), in `currency` — ignored for &#039;free&#039; and &#039;matrix&#039;.
    pricing_type : Optional[ShippingMethodPricingType]
        Pricing model (default &#039;fixed&#039;): &#039;fixed&#039; is one price for every basket, &#039;free&#039; is no price at all, &#039;matrix&#039; is a tiered price read off this method&#039;s rate tiers. Only &#039;matrix&#039; looks at matrix_basis, quote_above and the tier table.
    quote_above : Optional[float]
        Above this MATRIX MEASURE the method carries no automatic price: it is still offered, flagged `quote_required` with a reason, and the storefront shows &#039;shipping on request&#039;. For bulky or overweight freight priced by hand. Null = every measure is priced automatically.
    tax_class : Optional[str]
        This method&#039;s own tax class, as a CODE into the buyer market&#039;s tax classes (markets.tax_classes) — never a rate. First step of the tax chain: unset falls back to the tenant&#039;s shipping_tax_class setting, then the market default. Not a foreign key and it could not be (ADR-0055); GET /shipping/tax-classes/{code}/usage is the integrity question markets asks in its place.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    carrier_id: Optional[str] = Field(default=None, alias='carrier_id')
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
    quote_above: Optional[float] = Field(default=None, alias='quote_above')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
