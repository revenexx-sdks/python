from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.shipping_carriers_list_status import ShippingCarriersListStatus;
from ..models.error import Error;
from ..enums.shipping_carrier_status import ShippingCarrierStatus;

class ShippingCarriers(Service):

    def __init__(self, client) -> None:
        super(ShippingCarriers, self).__init__(client)

    def shipping_carriers_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        code: Optional[str] = None,
        status: Optional[ShippingCarriersListStatus] = None,
        service_level: Optional[str] = None
    ) -> Error:
        """
        Filterable by exact column value — `?code=`, `?status=` and `?service_level=` are applied as equalities and echoed back in `filter`. A query key that names no column of this entity is SILENTLY IGNORED: the page comes back unfiltered, 200, with an empty `filter`, so compare the echo against what you sent rather than trusting the status.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200). A value outside the range is clamped rather than refused, and `page.limit` echoes what was applied.
        offset : Optional[float]
            Row offset for pagination (default 0). The next page is `page.offset + page.returned`.
        order : Optional[str]
            Sort as 'column.asc' | 'column.desc' — a bare 'column' sorts ascending. The column must be one this entity has; anything else is a 400 from the data plane.
        code : Optional[str]
            Exact-match filter on `code`. Unique per tenant, so this resolves a code an order shipment already stores without paging the whole list.
        status : Optional[ShippingCarriersListStatus]
            Exact-match filter on `status`. Quoting state — the cheap way to list only the carriers that may currently be quoted.
        service_level : Optional[str]
            Exact-match filter on `service_level`. A code into the tenant's own service levels (GET /shipping/service-levels).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/carriers'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if service_level is not None:
            api_params['service_level'] = self._normalize_value(service_level)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_carriers_create(
        self,
        code: str,
        name: str,
        countries: Optional[List[str]] = None,
        cutoff_time: Optional[str] = None,
        eta_days_max: Optional[float] = None,
        eta_days_min: Optional[float] = None,
        handling_days: Optional[float] = None,
        labels: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        service_level: Optional[str] = None,
        status: Optional[ShippingCarrierStatus] = None,
        tracking_url_template: Optional[str] = None
    ) -> Error:
        """
        A carrier row is one company shipping one class of service: it owns the tracking-URL template, the service level, the transit days, the pickup cut-off and the handling days, and every method that ships with it inherits all of those unless it states its own. A carrier selling both a parcel and an express product is two rows. Reach for it for a carrier this app does not describe — a regional courier, a forwarder, an own fleet; for the DACH networks read GET /shipping/carriers/catalog and let POST /shipping/carriers/defaults write them. A create cannot omit `code` and `name`; every other column is optional or defaulted by the database. Two rows of this tenant may not share `code` — that is the 409. `service_level` has to name one of the tenant's own levels and `cutoff_time` has to be HH:MM in 24-hour UTC — both are refused rather than stored, because a cut-off the estimator cannot read would be dropped in silence and the shop would keep promising a ship date nobody computed. Creating a carrier quotes nothing on its own: a method has to reference it (`carrier_id`, or a `carrier` text equal to this code) before any of it is inherited.

        Parameters
        ----------
        code : str
            Stable carrier code, unique per tenant (e.g. dhl, dpd, gls). A method whose `carrier` text equals this code resolves to this carrier — that is the migration path off the free-text field. Deliberately no slug pattern: the column asks only for a non-empty string, and a contract stricter than the implementation would refuse codes merchants already keep.
        name : str
            Display name, as an operator typed it.
        countries : Optional[List[str]]
            The countries this carrier serves. ISO 3166-1 alpha-2 codes; null or an empty array means no restriction. Compared upper-cased, so a lower-case entry still matches. Declared as an array rather than the bare object a jsonb column derives to — this one is always a list. ANDed with the method's own restriction: a method may not be offered into a country its carrier does not reach.
        cutoff_time : Optional[str]
            This carrier's own daily pickup cut-off, HH:MM in 24-hour form, UTC. Overrides the tenant's cutoff_time for methods on this carrier — one shop-wide time cannot be both DHL's 16:00 and a forwarder's 12:00. Null or the empty string means this carrier declares none; any other shape is a 400, because a cut-off the estimator cannot read is a delivery promise silently computed without one.
        eta_days_max : Optional[float]
            Transit time upper bound, in calendar days from the ship date.
        eta_days_min : Optional[float]
            Transit time lower bound, in calendar days from the ship date — inherited by any method on this carrier that states no ETA of its own.
        handling_days : Optional[float]
            Days needed to make a consignment ready for THIS carrier, added to the ship date before the transit days. Overrides the tenant's handling_days.
        labels : Optional[Dict[str, Any]]
            Localized display names. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        metadata : Optional[Dict[str, Any]]
            Free-form jsonb the platform never reads or validates — whatever the merchant or their integration needs to keep beside the row (a customer number with the carrier, an ERP key, a label-printer id). The shape varies BY INTEGRATION, not by anything this app knows, so no key is declared and none is reserved; the example is one plausible instance rather than a schema. A flat map of scalars is the convention, and nothing enforces it.
        position : Optional[float]
            Sort order among the carriers; ties fall back to whatever the database returns.
        service_level : Optional[str]
            The class of service this row represents (default 'standard'), as a CODE into the tenant's own service levels (GET /shipping/service-levels). One row is one class: a carrier selling both a parcel and an express product is two rows. Deliberately not an enum here — the set is the merchant's, so a fixed list in this contract would make the gateway reject a level they created. A code the tenant does not keep is a 400 naming the codes they do.
        status : Optional[ShippingCarrierStatus]
            Whether this carrier may be quoted (default 'active'). Anything else excludes every method that ships with it from POST /shipping/rates, with a reason. Tracking links are NOT gated on it — a retired carrier's old shipments stay resolvable.
        tracking_url_template : Optional[str]
            Tracking page URL with {tracking_code} where the number goes; {postal_code} and {country} are also substituted, URL-encoded. Null for a carrier with no public tracking page.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/carriers'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')


        api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        api_params['cutoff_time'] = self._normalize_value(cutoff_time)
        api_params['eta_days_max'] = self._normalize_value(eta_days_max)
        api_params['eta_days_min'] = self._normalize_value(eta_days_min)
        api_params['handling_days'] = self._normalize_value(handling_days)
        api_params['labels'] = self._normalize_value(labels)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if service_level is not None:
            api_params['service_level'] = self._normalize_value(service_level)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['tracking_url_template'] = self._normalize_value(tracking_url_template)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_carriers_catalog(
        self
    ) -> Dict[str, Any]:
        """
        The DACH set — the three German parcel networks, the express carriers, the AT/CH incumbents and the pallet forwarders — each with the tracking template, service level, transit time and pickup cut-off it would be created with. `seeded` marks the four a fresh install already has. Adding a carrier is a data change, never a code change, and a merchant may of course create one that is not in here at all.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/carriers/catalog'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def shipping_carriers_defaults(
        self
    ) -> Dict[str, Any]:
        """
        The four networks a DACH shop is expected to have — DHL, DPD, GLS and UPS — created by code, and only the ones that are missing. The app runs this itself on `app.installed`, so a fresh install already has them; calling it by hand afterwards is how a tenant that predates a catalog entry catches up, and calling it twice costs nothing, because it reconciles rather than seeds. An existing row belongs to the merchant: only columns that are genuinely EMPTY are filled in (a tracking template added to the catalog after their install), never a value they set. Nothing is deleted.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/carriers/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def shipping_carriers_delete(
        self,
        id: str
    ) -> Error:
        """
        Deleting one clears `shipping_methods.carrier_id` rather than deleting those rows — the foreign keys decide that, not this route. So a method that referenced this carrier keeps working and resolves through its `carrier` code instead, which is also why this never answers a conflict — and it is the reason to prefer `status: 'retired'` where the carrier is merely finished. What the method silently LOSES is everything it was inheriting: the tracking template, the pickup cut-off, the handling days and the transit days. Unless its `carrier` text still matches another carrier, its ship date is recomputed on the market's own cut-off and handling settings, and a method that stated no `eta_days_min`/`max` of its own stops carrying a `delivery` estimate altogether. Nothing errors; the promise in the checkout just changes.

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

        api_path = '/v1/shipping/carriers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_carriers_get(
        self,
        id: str
    ) -> Error:
        """
        A carrier row is one company shipping one class of service: it owns the tracking-URL template, the service level, the transit days, the pickup cut-off and the handling days, and every method that ships with it inherits all of those unless it states its own. A carrier selling both a parcel and an express product is two rows. Read it when you need to know what a method's delivery promise really is: `cutoff_time`, `handling_days` and `eta_days_min`/`max` are inherited from here, so a shop that seems to promise the wrong ship date is usually explained by this row rather than by the method. It does NOT say which methods ship with it — that is GET /shipping/methods?carrier_id=… for the ones holding a reference and ?carrier=… for the ones still resolving through the legacy code text.

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

        api_path = '/v1/shipping/carriers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_carriers_update(
        self,
        id: str,
        code: Optional[str] = None,
        countries: Optional[List[str]] = None,
        cutoff_time: Optional[str] = None,
        eta_days_max: Optional[float] = None,
        eta_days_min: Optional[float] = None,
        handling_days: Optional[float] = None,
        labels: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        service_level: Optional[str] = None,
        status: Optional[ShippingCarrierStatus] = None,
        tracking_url_template: Optional[str] = None
    ) -> Error:
        """
        A carrier row is one company shipping one class of service: it owns the tracking-URL template, the service level, the transit days, the pickup cut-off and the handling days, and every method that ships with it inherits all of those unless it states its own. A carrier selling both a parcel and an express product is two rows. A partial update — send only what changes, which is where a carrier is paused, given a different tracking template, or moved to another pickup cut-off or transit time. This is the one switch that acts on several methods at once, in both directions. Moving `status` off 'active' takes every method that ships with this carrier out of POST /shipping/rates with a reason, which beats disabling each of them and forgetting one; tracking links are deliberately not gated on it, so a retired carrier's old shipments stay resolvable. Editing `cutoff_time`, `handling_days` or `eta_days_min`/`max` MOVES THE PROMISED SHIP DATE of every method that states none of its own: the estimator adds the handling days, then one further day when the cut-off has already passed at the instant being evaluated — compared at or after, in UTC, and as calendar days that do not skip a weekend. Two rows of this tenant may not share `code` — that is the 409.

        Parameters
        ----------
        id : str
            The row id.
        code : Optional[str]
            Stable carrier code, unique per tenant (e.g. dhl, dpd, gls). A method whose `carrier` text equals this code resolves to this carrier — that is the migration path off the free-text field. Deliberately no slug pattern: the column asks only for a non-empty string, and a contract stricter than the implementation would refuse codes merchants already keep.
        countries : Optional[List[str]]
            The countries this carrier serves. ISO 3166-1 alpha-2 codes; null or an empty array means no restriction. Compared upper-cased, so a lower-case entry still matches. Declared as an array rather than the bare object a jsonb column derives to — this one is always a list. ANDed with the method's own restriction: a method may not be offered into a country its carrier does not reach.
        cutoff_time : Optional[str]
            This carrier's own daily pickup cut-off, HH:MM in 24-hour form, UTC. Overrides the tenant's cutoff_time for methods on this carrier — one shop-wide time cannot be both DHL's 16:00 and a forwarder's 12:00. Null or the empty string means this carrier declares none; any other shape is a 400, because a cut-off the estimator cannot read is a delivery promise silently computed without one.
        eta_days_max : Optional[float]
            Transit time upper bound, in calendar days from the ship date.
        eta_days_min : Optional[float]
            Transit time lower bound, in calendar days from the ship date — inherited by any method on this carrier that states no ETA of its own.
        handling_days : Optional[float]
            Days needed to make a consignment ready for THIS carrier, added to the ship date before the transit days. Overrides the tenant's handling_days.
        labels : Optional[Dict[str, Any]]
            Localized display names. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        metadata : Optional[Dict[str, Any]]
            Free-form jsonb the platform never reads or validates — whatever the merchant or their integration needs to keep beside the row (a customer number with the carrier, an ERP key, a label-printer id). The shape varies BY INTEGRATION, not by anything this app knows, so no key is declared and none is reserved; the example is one plausible instance rather than a schema. A flat map of scalars is the convention, and nothing enforces it.
        name : Optional[str]
            Display name, as an operator typed it.
        position : Optional[float]
            Sort order among the carriers; ties fall back to whatever the database returns.
        service_level : Optional[str]
            The class of service this row represents (default 'standard'), as a CODE into the tenant's own service levels (GET /shipping/service-levels). One row is one class: a carrier selling both a parcel and an express product is two rows. Deliberately not an enum here — the set is the merchant's, so a fixed list in this contract would make the gateway reject a level they created. A code the tenant does not keep is a 400 naming the codes they do.
        status : Optional[ShippingCarrierStatus]
            Whether this carrier may be quoted (default 'active'). Anything else excludes every method that ships with it from POST /shipping/rates, with a reason. Tracking links are NOT gated on it — a retired carrier's old shipments stay resolvable.
        tracking_url_template : Optional[str]
            Tracking page URL with {tracking_code} where the number goes; {postal_code} and {country} are also substituted, URL-encoded. Null for a carrier with no public tracking page.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/carriers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        api_params['cutoff_time'] = self._normalize_value(cutoff_time)
        api_params['eta_days_max'] = self._normalize_value(eta_days_max)
        api_params['eta_days_min'] = self._normalize_value(eta_days_min)
        api_params['handling_days'] = self._normalize_value(handling_days)
        api_params['labels'] = self._normalize_value(labels)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if service_level is not None:
            api_params['service_level'] = self._normalize_value(service_level)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['tracking_url_template'] = self._normalize_value(tracking_url_template)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_tracking(
        self,
        carrier: str,
        country: Optional[str] = None,
        postal_code: Optional[str] = None,
        tracking_code: Optional[str] = None
    ) -> Error:
        """
        Hand in a carrier code and the tracking number printed on the label, and this answers the URL a buyer follows. The carrier owns the URL format, so nobody else has to. `order_shipments` stores a tracking_url per shipment today, which is one carrier's URL shape copied into every row — the day it changes, every historic link is wrong. Ask here instead. Tracking is NOT gated on carrier status: a retired carrier's old shipments stay resolvable.

        Parameters
        ----------
        carrier : str
            Carrier code (what an order shipment already stores) or the carrier row id — a value matching the uuid form is read as the id, anything else as a code, case-insensitively. Must name a carrier THIS tenant keeps; one that does not is a 404.
        country : Optional[str]
            Destination ISO 3166-1 alpha-2 code — only needed by a template that names {country}. Upper-cased before substitution.
        postal_code : Optional[str]
            Destination postcode — only needed by a template that names {postal_code}.
        tracking_code : Optional[str]
            The carrier's tracking number. Required by every template that names {tracking_code}, which is all of them in the shipped catalog. URL-encoded before substitution, so a code with a space or a slash cannot reshape the link.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/tracking'
        api_params = {}
        if carrier is None:
            raise RevenexxException('Missing required parameter: "carrier"')


        api_params['carrier'] = self._normalize_value(carrier)
        api_params['country'] = self._normalize_value(country)
        api_params['postal_code'] = self._normalize_value(postal_code)
        api_params['tracking_code'] = self._normalize_value(tracking_code)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

