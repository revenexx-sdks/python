from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.pricing_type import PricingType;
from ..models.error import Error;
from ..enums.shipping_method_matrix_basis import ShippingMethodMatrixBasis;
from ..enums.shipping_method_pricing_type import ShippingMethodPricingType;
from ..models.shipping_rate_tier_replace_item import ShippingRateTierReplaceItem;
from ..models.shipping_tax_class_usage import ShippingTaxClassUsage;

class ShippingMethods(Service):

    def __init__(self, client) -> None:
        super(ShippingMethods, self).__init__(client)

    def shipping_methods_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        code: Optional[str] = None,
        enabled: Optional[bool] = None,
        pricing_type: Optional[PricingType] = None,
        carrier_id: Optional[str] = None,
        carrier: Optional[str] = None,
        tax_class: Optional[str] = None
    ) -> Error:
        """
        Filterable by exact column value — `?code=`, `?enabled=`, `?pricing_type=`, `?carrier_id=`, `?carrier=` and `?tax_class=` are applied as equalities and echoed back in `filter`. `?carrier_id=` and `?carrier=` are the two halves of one question: the first finds the methods holding a reference, the second the ones still resolving through the legacy code text. A query key that names no column of this entity is SILENTLY IGNORED — `?status=` on this route is the trap, since carriers have a status and methods do not: the page comes back unfiltered, 200, with an empty `filter`.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200). A value outside the range is clamped rather than refused, and `page.limit` echoes what was applied.
        offset : Optional[float]
            Row offset for pagination (default 0). The next page is `page.offset + page.returned`.
        order : Optional[str]
            Sort as 'column.asc' | 'column.desc' — a bare 'column' sorts ascending. The column must be one this entity has; anything else is a 400 from the data plane.
        code : Optional[str]
            Exact-match filter on `code`. Unique per tenant, so this resolves a code a checkout already holds without paging the whole list.
        enabled : Optional[bool]
            Exact-match filter on `enabled`. Only enabled methods are ever quoted, so this is the storefront-facing subset.
        pricing_type : Optional[PricingType]
            Exact-match filter on `pricing_type`. Pricing model — `matrix` is the set whose tiers a rate-matrix editor has to load.
        carrier_id : Optional[str]
            Exact-match filter on `carrier_id`. The methods that ship with one carrier — what a merchant needs before pausing it. Matches `carrier_id` only, never the legacy `carrier` text.
        carrier : Optional[str]
            Exact-match filter on `carrier`. The other half of that question: the methods still resolving their carrier through the legacy free-text CODE rather than a reference. Together with `?carrier_id=` this is how a merchant finds what a carrier is still holding before retiring it.
        tax_class : Optional[str]
            Exact-match filter on `tax_class`. The methods naming one tax class — the same question GET /shipping/tax-classes/{code}/usage counts, when the caller wants the rows rather than the count. Only a method's OWN class; a method falling back to the tenant setting does not match.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if pricing_type is not None:
            api_params['pricing_type'] = self._normalize_value(pricing_type)
        if carrier_id is not None:
            api_params['carrier_id'] = self._normalize_value(carrier_id)
        if carrier is not None:
            api_params['carrier'] = self._normalize_value(carrier)
        if tax_class is not None:
            api_params['tax_class'] = self._normalize_value(tax_class)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_methods_create(
        self,
        code: str,
        name: str,
        carrier: Optional[str] = None,
        carrier_id: Optional[str] = None,
        countries: Optional[List[str]] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        eta_days_max: Optional[float] = None,
        eta_days_min: Optional[float] = None,
        free_above: Optional[float] = None,
        labels: Optional[Dict[str, Any]] = None,
        matrix_attribute: Optional[str] = None,
        matrix_basis: Optional[ShippingMethodMatrixBasis] = None,
        metadata: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        price: Optional[float] = None,
        pricing_type: Optional[ShippingMethodPricingType] = None,
        quote_above: Optional[float] = None,
        tax_class: Optional[str] = None
    ) -> Error:
        """
        A shipping method is the line a buyer picks in the checkout: a pricing model ('fixed', 'free' or 'matrix'), the countries it may be offered into, a free-above threshold, and the carrier it ships with. The method owns the PRICE; the delivery promise — tracking template, cut-off, handling and transit days — is inherited from the carrier wherever the method states none of its own. A create cannot omit `code` and `name`; every other column is optional or defaulted by the database. Two rows of this tenant may not share `code` — that is the 409. The new method is quoted by nobody until two further things are true: `enabled` defaults to FALSE, and a 'matrix' method has no tiers yet — until POST or PUT …/tiers gives it some it appears in `excluded` with 'matrix has no rate tiers configured' rather than in the rates. `carrier_id` and the legacy `carrier` code are both accepted and neither is verified against the carrier table here: an unmatched code is a plain carrier name on the rate, not an error.

        Parameters
        ----------
        code : str
            Stable method code, unique per tenant (e.g. standard, express). What a checkout and an order line store, so it is the value every integration joins on.
        name : str
            Display name shown in the checkout.
        carrier : Optional[str]
            Carrier CODE, kept from before shipping_carriers existed. Looked up in the carrier table when carrier_id is not set, so an existing value keeps working and gains a tracking template; a code nobody maintains is still reported as a plain name.
        carrier_id : Optional[str]
            The carrier this method ships with. Wins over `carrier` and supplies the tracking template, pickup cut-off, handling time and transit days.
        countries : Optional[List[str]]
            The countries this method may be offered into. ISO 3166-1 alpha-2 codes; null or an empty array means no restriction. Compared upper-cased, so a lower-case entry still matches. Declared as an array rather than the bare object a jsonb column derives to — this one is always a list. ANDed with the carrier's own reach.
        currency : Optional[str]
            ISO 4217 code (default EUR). Exactly three characters — the column says so. Echoed into a rate, never converted: this app prices in the currency the method carries.
        description : Optional[str]
            The sentence under the name in the checkout — the delivery promise in words. Null when the name says enough.
        enabled : Optional[bool]
            Only enabled methods are ever quoted (default false); a disabled one is reported in `excluded` rather than hidden.
        eta_days_max : Optional[float]
            Transit time upper bound in calendar days. Falls back to the carrier's when null.
        eta_days_min : Optional[float]
            Transit time lower bound in calendar days, for the checkout. Falls back to the carrier's when null.
        free_above : Optional[float]
            Free shipping at or above this order value — wins over every pricing model, including a matrix. Compared net or gross as the market's free_above_compares setting declares. Null falls back to the tenant's shop-wide free_shipping_threshold.
        labels : Optional[Dict[str, Any]]
            Localized display names. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        matrix_attribute : Optional[str]
            Attribute name for matrix_basis 'attribute' — the key the rate request's `attributes` map is read at. Free text: the set of attributes is the catalogue's, not this app's.
        matrix_basis : Optional[ShippingMethodMatrixBasis]
            The measure a matrix method prices its tiers over: total basket weight (in the market's weight unit), total item count, order value, or 'attribute' — any number the rate request carries under matrix_attribute. Null falls back to the tenant's matrix_basis_default. Ignored unless pricing_type is 'matrix'.
        metadata : Optional[Dict[str, Any]]
            Free-form jsonb the platform never reads or validates — whatever the merchant or their integration needs to keep beside the row (a customer number with the carrier, an ERP key, a label-printer id). The shape varies BY INTEGRATION, not by anything this app knows, so no key is declared and none is reserved; the example is one plausible instance rather than a schema. A flat map of scalars is the convention, and nothing enforces it.
        position : Optional[float]
            Sort order in the checkout (default 0) — a rate answer is returned in this order.
        price : Optional[float]
            The fixed price (default 0), in `currency` — ignored for 'free' and 'matrix'.
        pricing_type : Optional[ShippingMethodPricingType]
            Pricing model (default 'fixed'): 'fixed' is one price for every basket, 'free' is no price at all, 'matrix' is a tiered price read off this method's rate tiers. Only 'matrix' looks at matrix_basis, quote_above and the tier table.
        quote_above : Optional[float]
            Above this MATRIX MEASURE the method carries no automatic price: it is still offered, flagged `quote_required` with a reason, and the storefront shows 'shipping on request'. For bulky or overweight freight priced by hand. Null = every measure is priced automatically.
        tax_class : Optional[str]
            This method's own tax class, as a CODE into the buyer market's tax classes (markets.tax_classes) — never a rate. First step of the tax chain: unset falls back to the tenant's shipping_tax_class setting, then the market default. Not a foreign key and it could not be (ADR-0055); GET /shipping/tax-classes/{code}/usage is the integrity question markets asks in its place.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')


        api_params['carrier'] = self._normalize_value(carrier)
        api_params['carrier_id'] = self._normalize_value(carrier_id)
        api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['eta_days_max'] = self._normalize_value(eta_days_max)
        api_params['eta_days_min'] = self._normalize_value(eta_days_min)
        api_params['free_above'] = self._normalize_value(free_above)
        api_params['labels'] = self._normalize_value(labels)
        api_params['matrix_attribute'] = self._normalize_value(matrix_attribute)
        api_params['matrix_basis'] = self._normalize_value(matrix_basis)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)
        if pricing_type is not None:
            api_params['pricing_type'] = self._normalize_value(pricing_type)
        api_params['quote_above'] = self._normalize_value(quote_above)
        api_params['tax_class'] = self._normalize_value(tax_class)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_methods_defaults(
        self
    ) -> Dict[str, Any]:
        """
        Runs the carrier seed first, then creates any missing method: the three lines a shop is expected to offer — standard, express and pickup. The app runs this itself on `app.installed`, so a fresh install already has them; calling it by hand afterwards is how a tenant that deleted one gets it back, and calling it twice costs nothing, because it reconciles rather than seeds. The seeded methods deliberately name no carrier: which carrier carries the standard method is a contract, not a default, and a method that says 'dhl' resolves to the seeded DHL row anyway.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def shipping_methods_delete(
        self,
        id: str
    ) -> Error:
        """
        Deleting one takes every `shipping_rate_tiers` row that points at it with it — the foreign keys decide that, not this route. So the whole rate matrix goes with the method, which is also why this never answers a conflict and why there is no way to recover the table afterwards — for a method a checkout may still be holding in a session, `enabled: false` is the safer edit.

        Parameters
        ----------
        id : str
            The row id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_methods_get(
        self,
        id: str
    ) -> Error:
        """
        A shipping method is the line a buyer picks in the checkout: a pricing model ('fixed', 'free' or 'matrix'), the countries it may be offered into, a free-above threshold, and the carrier it ships with. The method owns the PRICE; the delivery promise — tracking template, cut-off, handling and transit days — is inherited from the carrier wherever the method states none of its own. This is the CONFIGURATION of one, by row id — not what a buyer would be charged. A matrix method's prices are not in here at all: they are its rate tiers, GET /shipping/methods/{method_id}/tiers, and the price for a given basket is POST /shipping/rates, which is the only place free-above thresholds, country restrictions, the carrier's reach and tax are applied. A checkout that reads `price` off this row prices a matrix method at 0.

        Parameters
        ----------
        id : str
            The row id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_methods_update(
        self,
        id: str,
        carrier: Optional[str] = None,
        carrier_id: Optional[str] = None,
        code: Optional[str] = None,
        countries: Optional[List[str]] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        eta_days_max: Optional[float] = None,
        eta_days_min: Optional[float] = None,
        free_above: Optional[float] = None,
        labels: Optional[Dict[str, Any]] = None,
        matrix_attribute: Optional[str] = None,
        matrix_basis: Optional[ShippingMethodMatrixBasis] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        price: Optional[float] = None,
        pricing_type: Optional[ShippingMethodPricingType] = None,
        quote_above: Optional[float] = None,
        tax_class: Optional[str] = None
    ) -> Error:
        """
        A shipping method is the line a buyer picks in the checkout: a pricing model ('fixed', 'free' or 'matrix'), the countries it may be offered into, a free-above threshold, and the carrier it ships with. The method owns the PRICE; the delivery promise — tracking template, cut-off, handling and transit days — is inherited from the carrier wherever the method states none of its own. A partial update — send only what changes, whether that is taking the method in or out of the checkout, its pricing, the countries it is restricted to or the delivery estimate it states of its own; a payload carrying no column at all is refused rather than answering a row it did not touch. Flipping `enabled` is what puts the method in front of a buyer or takes it away, and a disabled method is reported in the rate answer's `excluded` rather than hidden. Changing `pricing_type` away from 'matrix' does NOT delete the tier table — it stops being read, and changing back reinstates the old prices, so a method switched to 'fixed' and back quotes what it quoted before. Two rows of this tenant may not share `code` — that is the 409.

        Parameters
        ----------
        id : str
            The row id.
        carrier : Optional[str]
            Carrier CODE, kept from before shipping_carriers existed. Looked up in the carrier table when carrier_id is not set, so an existing value keeps working and gains a tracking template; a code nobody maintains is still reported as a plain name.
        carrier_id : Optional[str]
            The carrier this method ships with. Wins over `carrier` and supplies the tracking template, pickup cut-off, handling time and transit days.
        code : Optional[str]
            Stable method code, unique per tenant (e.g. standard, express). What a checkout and an order line store, so it is the value every integration joins on.
        countries : Optional[List[str]]
            The countries this method may be offered into. ISO 3166-1 alpha-2 codes; null or an empty array means no restriction. Compared upper-cased, so a lower-case entry still matches. Declared as an array rather than the bare object a jsonb column derives to — this one is always a list. ANDed with the carrier's own reach.
        currency : Optional[str]
            ISO 4217 code (default EUR). Exactly three characters — the column says so. Echoed into a rate, never converted: this app prices in the currency the method carries.
        description : Optional[str]
            The sentence under the name in the checkout — the delivery promise in words. Null when the name says enough.
        enabled : Optional[bool]
            Only enabled methods are ever quoted (default false); a disabled one is reported in `excluded` rather than hidden.
        eta_days_max : Optional[float]
            Transit time upper bound in calendar days. Falls back to the carrier's when null.
        eta_days_min : Optional[float]
            Transit time lower bound in calendar days, for the checkout. Falls back to the carrier's when null.
        free_above : Optional[float]
            Free shipping at or above this order value — wins over every pricing model, including a matrix. Compared net or gross as the market's free_above_compares setting declares. Null falls back to the tenant's shop-wide free_shipping_threshold.
        labels : Optional[Dict[str, Any]]
            Localized display names. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        matrix_attribute : Optional[str]
            Attribute name for matrix_basis 'attribute' — the key the rate request's `attributes` map is read at. Free text: the set of attributes is the catalogue's, not this app's.
        matrix_basis : Optional[ShippingMethodMatrixBasis]
            The measure a matrix method prices its tiers over: total basket weight (in the market's weight unit), total item count, order value, or 'attribute' — any number the rate request carries under matrix_attribute. Null falls back to the tenant's matrix_basis_default. Ignored unless pricing_type is 'matrix'.
        metadata : Optional[Dict[str, Any]]
            Free-form jsonb the platform never reads or validates — whatever the merchant or their integration needs to keep beside the row (a customer number with the carrier, an ERP key, a label-printer id). The shape varies BY INTEGRATION, not by anything this app knows, so no key is declared and none is reserved; the example is one plausible instance rather than a schema. A flat map of scalars is the convention, and nothing enforces it.
        name : Optional[str]
            Display name shown in the checkout.
        position : Optional[float]
            Sort order in the checkout (default 0) — a rate answer is returned in this order.
        price : Optional[float]
            The fixed price (default 0), in `currency` — ignored for 'free' and 'matrix'.
        pricing_type : Optional[ShippingMethodPricingType]
            Pricing model (default 'fixed'): 'fixed' is one price for every basket, 'free' is no price at all, 'matrix' is a tiered price read off this method's rate tiers. Only 'matrix' looks at matrix_basis, quote_above and the tier table.
        quote_above : Optional[float]
            Above this MATRIX MEASURE the method carries no automatic price: it is still offered, flagged `quote_required` with a reason, and the storefront shows 'shipping on request'. For bulky or overweight freight priced by hand. Null = every measure is priced automatically.
        tax_class : Optional[str]
            This method's own tax class, as a CODE into the buyer market's tax classes (markets.tax_classes) — never a rate. First step of the tax chain: unset falls back to the tenant's shipping_tax_class setting, then the market default. Not a foreign key and it could not be (ADR-0055); GET /shipping/tax-classes/{code}/usage is the integrity question markets asks in its place.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['carrier'] = self._normalize_value(carrier)
        api_params['carrier_id'] = self._normalize_value(carrier_id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['eta_days_max'] = self._normalize_value(eta_days_max)
        api_params['eta_days_min'] = self._normalize_value(eta_days_min)
        api_params['free_above'] = self._normalize_value(free_above)
        api_params['labels'] = self._normalize_value(labels)
        api_params['matrix_attribute'] = self._normalize_value(matrix_attribute)
        api_params['matrix_basis'] = self._normalize_value(matrix_basis)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)
        if pricing_type is not None:
            api_params['pricing_type'] = self._normalize_value(pricing_type)
        api_params['quote_above'] = self._normalize_value(quote_above)
        api_params['tax_class'] = self._normalize_value(tax_class)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_list(
        self,
        method_id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        from_value: Optional[float] = None
    ) -> Error:
        """
        The rate matrix of one method — every `from_value` threshold with the price charged at or above it — lowest threshold first. Filterable by `?from_value=` — the unique index is (tenant_id, method_id, from_value), so that addresses one row of the matrix by the threshold it prices rather than by an id a bulk replace has already discarded. The applied filters are echoed in `filter`, which always carries the `method_id` taken from the path.

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        limit : Optional[float]
            Page size (default 50, max 200). A value outside the range is clamped rather than refused, and `page.limit` echoes what was applied.
        offset : Optional[float]
            Row offset for pagination (default 0). The next page is `page.offset + page.returned`.
        order : Optional[str]
            Sort as 'column.asc' | 'column.desc' — a bare 'column' sorts ascending. The column must be one this entity has; anything else is a 400 from the data plane.
        from_value : Optional[float]
            Exact-match filter on `from_value`. The tier at exactly this threshold. (tenant_id, method_id, from_value) is unique, so this addresses one row of the matrix by what it MEANS rather than by an id a bulk replace has already thrown away.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if from_value is not None:
            api_params['from_value'] = self._normalize_value(from_value)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_create(
        self,
        method_id: str,
        from_value: Optional[float] = None,
        position: Optional[float] = None,
        price: Optional[float] = None
    ) -> Error:
        """
        A rate tier is one row of a matrix method's price table: a `from_value` threshold and the price charged at or above it. The bound is INCLUSIVE and the winning tier is the one with the highest `from_value` at or below the measured value, so a measure of exactly 10 is priced by the tier at 10. What the number measures is the method's `matrix_basis` — kilograms in the market's own weight unit, items, money in the method's currency, or a named attribute — and the last tier has no upper bound. This adds ONE row to the table of the method in the path, leaving the rest alone — the edit for a merchant who has added a heavier bracket. To lay a whole table down at once use PUT …/tiers (set semantics) or POST …/tiers/ladder (evenly stepped), and note that both of those DISCARD the ids of the rows they replace. Two rows of this tenant may not share the combination of `method_id` + `from_value` — that is the 409. `method_id` is taken from the path on every write, so a body naming a different method is ignored rather than obeyed.

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        from_value : Optional[float]
            Lower bound of this tier, in the method's matrix measure — kilograms (or whatever the market's `weight_unit` names, converted through its factor) for a weight matrix, items for quantity, money in the method's currency for order_value, and the raw attribute value for 'attribute'. INCLUSIVE: the tier applies from this value upward, and the tier that wins is the one with the highest from_value at or below the measured value, so a measure of exactly 10 is priced by the tier at 10 rather than the one below it. The last tier has no upper bound. Unique per method — a second tier at the same threshold is a 409, because which of the two won would be whatever the database returned first. Defaults to 0.
        position : Optional[float]
            Display order in the matrix editor (default 0; a bulk replace derives it from the array index). Pricing reads from_value, never this.
        price : Optional[float]
            What this tier costs, in the method's currency. Charged in full for the whole consignment — a matrix is a lookup table, not a rate per unit. Defaults to 0.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))

        if from_value is not None:
            api_params['from_value'] = self._normalize_value(from_value)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_replace(
        self,
        method_id: str,
        tiers: List[ShippingRateTierReplaceItem]
    ) -> Error:
        """
        The write behind a table editor: a merchant edits the whole matrix on screen and saves it in one call, rather than diffing it into a row added here and a row deleted there. Set semantics, and it replaces EVERY tier the method had: the tiers this method has afterwards are exactly the ones handed in, positions derived from the array order. An empty `tiers` array clears the table — and a matrix method with no tiers quotes nothing, with a reason.

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        tiers : List[ShippingRateTierReplaceItem]
            The complete new tier set (set semantics) — positions are derived from the array order. An empty array clears the matrix, and a matrix method with no tiers quotes nothing.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        if tiers is None:
            raise RevenexxException('Missing required parameter: "tiers"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))

        api_params['tiers'] = self._normalize_value(tiers)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_ladder(
        self,
        method_id: str,
        base_price: float,
        step: float,
        to_value: float,
        from_value: Optional[float] = None,
        replace: Optional[bool] = None,
        step_price: Optional[float] = None
    ) -> Error:
        """
        The tier table a merchant describes in words — "0 to 30 kg, every 5 kg, €4.90 plus €2 a step" — without typing every row. Replaces the method's tiers by default (set replace=false to append).

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        base_price : float
            Price of the first tier.
        step : float
            Distance between two tiers. Must be > 0.
        to_value : float
            Last tier threshold. The final tier keeps applying above it — a matrix has no upper bound. Must be >= from_value.
        from_value : Optional[float]
            First tier threshold (default 0), in the method's matrix measure.
        replace : Optional[bool]
            Replace the whole table (default true) or append to it.
        step_price : Optional[float]
            Added to each subsequent tier (default 0). A negative value is allowed as long as no tier ends up below 0.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers/ladder'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        if base_price is None:
            raise RevenexxException('Missing required parameter: "base_price"')

        if step is None:
            raise RevenexxException('Missing required parameter: "step"')

        if to_value is None:
            raise RevenexxException('Missing required parameter: "to_value"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))

        api_params['base_price'] = self._normalize_value(base_price)
        api_params['from_value'] = self._normalize_value(from_value)
        api_params['replace'] = self._normalize_value(replace)
        api_params['step'] = self._normalize_value(step)
        api_params['step_price'] = self._normalize_value(step_price)
        api_params['to_value'] = self._normalize_value(to_value)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_delete(
        self,
        method_id: str,
        id: str
    ) -> Error:
        """
        A rate tier is one row of a matrix method's price table: a `from_value` threshold and the price charged at or above it. The bound is INCLUSIVE and the winning tier is the one with the highest `from_value` at or below the measured value, so a measure of exactly 10 is priced by the tier at 10. What the number measures is the method's `matrix_basis` — kilograms in the market's own weight unit, items, money in the method's currency, or a named attribute — and the last tier has no upper bound. Removing a tier in the MIDDLE of a table is harmless — the measures it used to cover fall to the highest remaining threshold below them. Removing the LOWEST one is not: a measure under the new lowest threshold matches no tier at all, and the method is then left out of POST /shipping/rates with 'no tier covers measure …' instead of being quoted at 0, so an entire band of baskets silently stops being offered this method. Deleting the last tier takes the method out of the checkout altogether. Rebuilding the table wholesale is PUT …/tiers or POST …/tiers/ladder; deleting the method deletes its tiers on its own.

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        id : str
            The row id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers/{id}'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_get(
        self,
        method_id: str,
        id: str
    ) -> Error:
        """
        A rate tier is one row of a matrix method's price table: a `from_value` threshold and the price charged at or above it. The bound is INCLUSIVE and the winning tier is the one with the highest `from_value` at or below the measured value, so a measure of exactly 10 is priced by the tier at 10. What the number measures is the method's `matrix_basis` — kilograms in the market's own weight unit, items, money in the method's currency, or a named attribute — and the last tier has no upper bound. This reads one row of that table by id, under the method that owns it; a tier id belonging to another method is a 404 rather than somebody else's price. A tier id is not durable: PUT …/tiers and POST …/tiers/ladder replace the table by deleting and recreating it, so an id read before either of them names nothing afterwards. Where a caller wants a stable handle, address the row by what it MEANS — GET …/tiers?from_value=… — since (method_id, from_value) is unique.

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        id : str
            The row id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers/{id}'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tiers_update(
        self,
        method_id: str,
        id: str,
        from_value: Optional[float] = None,
        position: Optional[float] = None,
        price: Optional[float] = None
    ) -> Error:
        """
        A tier id is not stable across a bulk edit: `PUT …/tiers` and `POST …/tiers/ladder` replace the table by deleting and recreating it, so an id read before either of them is gone afterwards.

        Parameters
        ----------
        method_id : str
            The shipping method these tiers belong to. A method this tenant does not have is a 404, never an empty page.
        id : str
            The row id.
        from_value : Optional[float]
            Lower bound of this tier, in the method's matrix measure — kilograms (or whatever the market's `weight_unit` names, converted through its factor) for a weight matrix, items for quantity, money in the method's currency for order_value, and the raw attribute value for 'attribute'. INCLUSIVE: the tier applies from this value upward, and the tier that wins is the one with the highest from_value at or below the measured value, so a measure of exactly 10 is priced by the tier at 10 rather than the one below it. The last tier has no upper bound. Unique per method — a second tier at the same threshold is a 409, because which of the two won would be whatever the database returned first. Defaults to 0.
        position : Optional[float]
            Display order in the matrix editor (default 0; a bulk replace derives it from the array index). Pricing reads from_value, never this.
        price : Optional[float]
            What this tier costs, in the method's currency. Charged in full for the whole consignment — a matrix is a lookup table, not a rate per unit. Defaults to 0.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers/{id}'
        api_params = {}
        if method_id is None:
            raise RevenexxException('Missing required parameter: "method_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{method_id}', str(self._normalize_value(method_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if from_value is not None:
            api_params['from_value'] = self._normalize_value(from_value)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_rates(
        self,
        at: Optional[str] = None,
        attributes: Optional[Dict[str, Any]] = None,
        country: Optional[str] = None,
        currency: Optional[str] = None,
        market_id: Optional[str] = None,
        order_value: Optional[float] = None,
        order_value_gross: Optional[float] = None,
        order_value_net: Optional[float] = None,
        quantity: Optional[float] = None,
        weight: Optional[float] = None,
        weight_unit: Optional[str] = None
    ) -> Error:
        """
        The question a checkout asks, and the only route that answers a PRICE. Hand in the buyer context — the destination country, the order value, and whatever the matrix methods measure: a weight, a quantity or a named product attribute — and this comes back with the methods that may be offered and what each of them costs, free-above thresholds, country restrictions, the carrier's delivery promise and tax already applied. A method that does not apply is never an error: it moves to `excluded` with a reason. So is a tax rate that cannot be resolved — `tax.resolved: false` means the rates are UNKNOWN, not untaxed.

        Parameters
        ----------
        at : Optional[str]
            The instant to evaluate the delivery estimate at (ISO 8601). Omitted: now. Lets a storefront compute the cut-off in its own timezone.
        attributes : Optional[Dict[str, Any]]
            Measure values for attribute matrices, keyed by attribute NAME — the key a matrix method names in its matrix_attribute, and the value the number its tiers are matched against. Summed over the basket by the caller, not by this app. Only the key a method asks for is read; anything else in the map is carried along and ignored, and a value that is not a finite number excludes that method with a reason rather than failing the quote.
        country : Optional[str]
            Destination ISO 3166-1 alpha-2 code — compared upper-cased against method and carrier country restrictions. Omitted or null: every method that restricts by country is excluded, with a reason.
        currency : Optional[str]
            ISO 4217 code, echoed into the rates (default 'EUR'). Echoed, not converted: this app prices in the currency the method carries.
        market_id : Optional[str]
            Buyer market for tax resolution. Omitted: the market matching `country`, else the tenant's sole market — never an arbitrary one.
        order_value : Optional[float]
            Order value (default 0) — drives order_value matrices, and free-above thresholds when no sided value is sent. Read on the basis the tenant's free_above_compares setting declares.
        order_value_gross : Optional[float]
            Order value including tax. Compared against free-above thresholds when free_above_compares is 'gross'.
        order_value_net : Optional[float]
            Order value excluding tax. Compared against free-above thresholds when free_above_compares is 'net'.
        quantity : Optional[float]
            Total quantity — measure for quantity matrices.
        weight : Optional[float]
            Total weight — measure for weight matrices. Read in weight_unit and converted to the unit the tiers are keyed in.
        weight_unit : Optional[str]
            The unit `weight` is expressed in, as a CODE into the tenant's own weight units (GET /shipping/weight-units). Omitted, it is the unit this market quotes in. A unit the tenant does not keep is a 400 — a mis-read weight prices the wrong bracket silently, and guessing is worse than refusing.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/rates'
        api_params = {}

        api_params['at'] = self._normalize_value(at)
        api_params['attributes'] = self._normalize_value(attributes)
        api_params['country'] = self._normalize_value(country)
        api_params['currency'] = self._normalize_value(currency)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['order_value'] = self._normalize_value(order_value)
        api_params['order_value_gross'] = self._normalize_value(order_value_gross)
        api_params['order_value_net'] = self._normalize_value(order_value_net)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['weight'] = self._normalize_value(weight)
        api_params['weight_unit'] = self._normalize_value(weight_unit)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tax_classes_usage(
        self,
        code: str
    ) -> ShippingTaxClassUsage:
        """
        markets.tax_classes is the source of record for the rate and this app points at it by CODE from two places: a method's own tax_class and the tenant's shipping_tax_class fallback. Neither is a foreign key and neither could be — a cross-app FK is what ADR-0055 forbids — so integrity is a question one app asks the other, and this is the answering half. It is asked before a destructive edit: markets calls it when an operator tries to delete a tax class, and a count above zero is what stops the delete rather than leaving these methods pointing at a code nobody serves. Matched as a CODE, not a row: a tax class is unique per market, so 'reduced' may exist in several and a method naming it does not say which one it meant. Reports at most 500 methods and names the first 20. Every code answers, used or not — a code nobody points at is `in_use: false`, never a 404.

        Parameters
        ----------
        code : str
            The tax-class CODE, as markets spells it — not a row id. Matched against every shipping method's `tax_class` and against this market's `shipping_tax_class` setting.
        
        Returns
        -------
        ShippingTaxClassUsage
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/tax-classes/{code}/usage'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', str(self._normalize_value(code)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ShippingTaxClassUsage)

