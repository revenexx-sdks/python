from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;
from ..models.organization_metrics_freshness import OrganizationMetricsFreshness;
from ..enums.customers_organizations_list_status import CustomersOrganizationsListStatus;
from ..enums.organization_status import OrganizationStatus;

class CustomersOrganizations(Service):

    def __init__(self, client) -> None:
        super(CustomersOrganizations, self).__init__(client)

    def customers_addresses_list(
        self,
        id: Optional[str] = None,
        organization_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        type: Optional[str] = None,
        company: Optional[str] = None,
        name: Optional[str] = None,
        street: Optional[str] = None,
        street2: Optional[str] = None,
        zip: Optional[str] = None,
        city: Optional[str] = None,
        region: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        is_default: Optional[bool] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        A postal address used for billing or for shipping, owned by exactly one of the two parties: an organization (the company address everyone in it may use) or a contact (a private one only that person uses). Both owner columns are nullable and exactly one is set — sending both, or neither, is refused. Every address this tenant holds, filterable by owner (`organization_id`, `contact_id`), by `type` and by any other column. It is how the addresses tab of a company or a person is filled; the page is `limit`/`offset`/`order`.

        Parameters
        ----------
        id : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the address.
        organization_id : Optional[str]
            Filter to one owning company.
        contact_id : Optional[str]
            Filter to one owning contact — a personal address book.
        type : Optional[str]
            Filter by address type (GET /customers/address-types) — 'billing' or 'shipping' unless the merchant added their own.
        company : Optional[str]
            Filter to rows whose `company` is exactly this value. Company line on the label. Often the owning organization's name, but not always — a delivery to a construction site carries the site.
        name : Optional[str]
            Filter to rows whose `name` is exactly this value. Recipient line on the label — the person or department the parcel is addressed to.
        street : Optional[str]
            Filter to rows whose `street` is exactly this value. Street and house number, on one line, as the local post expects it.
        street2 : Optional[str]
            Filter to rows whose `street2` is exactly this value. The second address line: building, floor, gate, c/o. Null when there is none.
        zip : Optional[str]
            Filter to rows whose `zip` is exactly this value. Postal code, as text — leading zeros are real in most countries.
        city : Optional[str]
            Filter to rows whose `city` is exactly this value. City or town.
        region : Optional[str]
            Filter to rows whose `region` is exactly this value. State, province or Bundesland. Required by some destinations (US, CA), unused by most European ones.
        country : Optional[str]
            Filter by ISO 3166-1 alpha-2 country code.
        phone : Optional[str]
            Filter to rows whose `phone` is exactly this value. Phone number for the carrier to reach at this address — often a different one from the contact's own.
        is_default : Optional[bool]
            Filter to the default addresses. With `type` and an owner, this is the one address a checkout should preselect.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the address was created.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When any column of this row last changed.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/addresses'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if contact_id is not None:
            api_params['contact_id'] = self._normalize_value(contact_id)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if company is not None:
            api_params['company'] = self._normalize_value(company)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if street is not None:
            api_params['street'] = self._normalize_value(street)
        if street2 is not None:
            api_params['street2'] = self._normalize_value(street2)
        if zip is not None:
            api_params['zip'] = self._normalize_value(zip)
        if city is not None:
            api_params['city'] = self._normalize_value(city)
        if region is not None:
            api_params['region'] = self._normalize_value(region)
        if country is not None:
            api_params['country'] = self._normalize_value(country)
        if phone is not None:
            api_params['phone'] = self._normalize_value(phone)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_addresses_create(
        self,
        city: str,
        country: str,
        street: str,
        zip: str,
        company: Optional[str] = None,
        contact_id: Optional[str] = None,
        is_default: Optional[bool] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        region: Optional[str] = None,
        street2: Optional[str] = None,
        type: Optional[str] = None
    ) -> Error:
        """
        A postal address used for billing or for shipping, owned by exactly one of the two parties: an organization (the company address everyone in it may use) or a contact (a private one only that person uses). Both owner columns are nullable and exactly one is set — sending both, or neither, is refused. `type` names one of this tenant's own address types — billing and shipping are seeded, and a merchant may add a works entrance or a central accounts office without a release of this app. `is_default` picks the one a checkout should preselect for that owner and that type. A create cannot omit `street`, `zip`, `city` and `country`; everything else is optional or defaulted by the database.

        Parameters
        ----------
        city : str
            City or town.
        country : str
            ISO 3166-1 alpha-2 country code, exactly two letters. Uppercase by convention; it is what shipping and tax both key off.
        street : str
            Street and house number, on one line, as the local post expects it.
        zip : str
            Postal code, as text — leading zeros are real in most countries.
        company : Optional[str]
            Company line on the label. Often the owning organization's name, but not always — a delivery to a construction site carries the site.
        contact_id : Optional[str]
            Owning person — a personal address only that contact uses. Exactly one of organization_id / contact_id is set.
        is_default : Optional[bool]
            The default address of its owner AND type: one default billing and one default shipping address per owner. Setting it moves the flag off the previous holder. Default false.
        name : Optional[str]
            Recipient line on the label — the person or department the parcel is addressed to.
        organization_id : Optional[str]
            Owning company — a company address, shared by everyone in it. Exactly one of organization_id / contact_id is set.
        phone : Optional[str]
            Phone number for the carrier to reach at this address — often a different one from the contact's own.
        region : Optional[str]
            State, province or Bundesland. Required by some destinations (US, CA), unused by most European ones.
        street2 : Optional[str]
            The second address line: building, floor, gate, c/o. Null when there is none.
        type : Optional[str]
            What the address is FOR — one of the tenant's own address types (GET /customers/address-types), seeded with billing and shipping. A merchant may add their own (a works entrance, a central accounts office) without a release of this app. A create without it gets the type flagged as default; a type the tenant does not keep is a 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/addresses'
        api_params = {}
        if city is None:
            raise RevenexxException('Missing required parameter: "city"')

        if country is None:
            raise RevenexxException('Missing required parameter: "country"')

        if street is None:
            raise RevenexxException('Missing required parameter: "street"')

        if zip is None:
            raise RevenexxException('Missing required parameter: "zip"')


        api_params['city'] = self._normalize_value(city)
        api_params['company'] = self._normalize_value(company)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['country'] = self._normalize_value(country)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        api_params['region'] = self._normalize_value(region)
        api_params['street'] = self._normalize_value(street)
        api_params['street2'] = self._normalize_value(street2)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        api_params['zip'] = self._normalize_value(zip)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_addresses_delete(
        self,
        id: str
    ) -> Error:
        """
        A postal address used for billing or for shipping, owned by exactly one of the two parties: an organization (the company address everyone in it may use) or a contact (a private one only that person uses). Both owner columns are nullable and exactly one is set — sending both, or neither, is refused. Removes the address. Orders already placed keep the address they were placed with; nothing in this app reaches back. Nothing else in this app points at it, so nothing else goes with it.

        Parameters
        ----------
        id : str
            The address to delete.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/addresses/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_addresses_get(
        self,
        id: str
    ) -> Error:
        """
        A postal address used for billing or for shipping, owned by exactly one of the two parties: an organization (the company address everyone in it may use) or a contact (a private one only that person uses). Both owner columns are nullable and exactly one is set — sending both, or neither, is refused. One address by id, whichever of the two owners it hangs off.

        Parameters
        ----------
        id : str
            The address to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/addresses/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_addresses_update(
        self,
        id: str,
        city: Optional[str] = None,
        company: Optional[str] = None,
        contact_id: Optional[str] = None,
        country: Optional[str] = None,
        is_default: Optional[bool] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        region: Optional[str] = None,
        street: Optional[str] = None,
        street2: Optional[str] = None,
        type: Optional[str] = None,
        zip: Optional[str] = None
    ) -> Error:
        """
        A postal address used for billing or for shipping, owned by exactly one of the two parties: an organization (the company address everyone in it may use) or a contact (a private one only that person uses). Both owner columns are nullable and exactly one is set — sending both, or neither, is refused. A partial update — send only what changes. An empty body is refused rather than answered as a no-op, so a client that built the wrong patch finds out.

        Parameters
        ----------
        id : str
            The address to update.
        city : Optional[str]
            City or town.
        company : Optional[str]
            Company line on the label. Often the owning organization's name, but not always — a delivery to a construction site carries the site.
        contact_id : Optional[str]
            Owning person — a personal address only that contact uses. Exactly one of organization_id / contact_id is set.
        country : Optional[str]
            ISO 3166-1 alpha-2 country code, exactly two letters. Uppercase by convention; it is what shipping and tax both key off.
        is_default : Optional[bool]
            The default address of its owner AND type: one default billing and one default shipping address per owner. Setting it moves the flag off the previous holder. Default false.
        name : Optional[str]
            Recipient line on the label — the person or department the parcel is addressed to.
        organization_id : Optional[str]
            Owning company — a company address, shared by everyone in it. Exactly one of organization_id / contact_id is set.
        phone : Optional[str]
            Phone number for the carrier to reach at this address — often a different one from the contact's own.
        region : Optional[str]
            State, province or Bundesland. Required by some destinations (US, CA), unused by most European ones.
        street : Optional[str]
            Street and house number, on one line, as the local post expects it.
        street2 : Optional[str]
            The second address line: building, floor, gate, c/o. Null when there is none.
        type : Optional[str]
            What the address is FOR — one of the tenant's own address types (GET /customers/address-types), seeded with billing and shipping. A merchant may add their own (a works entrance, a central accounts office) without a release of this app. A create without it gets the type flagged as default; a type the tenant does not keep is a 400.
        zip : Optional[str]
            Postal code, as text — leading zeros are real in most countries.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/addresses/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if city is not None:
            api_params['city'] = self._normalize_value(city)
        api_params['company'] = self._normalize_value(company)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if country is not None:
            api_params['country'] = self._normalize_value(country)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        api_params['region'] = self._normalize_value(region)
        if street is not None:
            api_params['street'] = self._normalize_value(street)
        api_params['street2'] = self._normalize_value(street2)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if zip is not None:
            api_params['zip'] = self._normalize_value(zip)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organization_metrics_list(
        self,
        id: Optional[str] = None,
        organization_id: Optional[str] = None,
        order_count: Optional[float] = None,
        order_count_30d: Optional[float] = None,
        order_count_90d: Optional[float] = None,
        order_count_365d: Optional[float] = None,
        revenue_total: Optional[float] = None,
        revenue_30d: Optional[float] = None,
        revenue_90d: Optional[float] = None,
        revenue_365d: Optional[float] = None,
        avg_order_value: Optional[float] = None,
        avg_order_value_365d: Optional[float] = None,
        first_order_at: Optional[str] = None,
        last_order_at: Optional[str] = None,
        currency: Optional[str] = None,
        currency_mixed: Optional[bool] = None,
        orders_as_of: Optional[str] = None,
        computed_at: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        What an organization has BOUGHT, materialized into this app from the orders app: lifetime revenue, revenue over the last 30/90/365 days, order count, average order value, and the first and last order dates. Revenue lives in orders and may not be joined (ADR-0055: no cross-app foreign key, grant or view), so it is pulled on a schedule and stored here — one row per organization, all-zero for a company that never ordered, so that a "never bought anything" rule has something to match. The customer-value list: sort by `revenue_365d` for the best customers, filter `last_order_at` for the dormant ones. Every row carries `computed_at`, and a row is only as current as the last refresh — `GET /customers/organization_metrics/freshness` says how stale the set is before a number is shown to anybody.

        Parameters
        ----------
        id : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the projection row.
        organization_id : Optional[str]
            Read the metrics of one company.
        order_count : Optional[float]
            Filter to rows whose `order_count` is exactly this value. Orders ever counted for this company.
        order_count_30d : Optional[float]
            Filter to rows whose `order_count_30d` is exactly this value. Orders in the 30 days before `orders_as_of`. A rolling window, not a calendar month.
        order_count_90d : Optional[float]
            Filter to rows whose `order_count_90d` is exactly this value. Orders in the 90 days before `orders_as_of`.
        order_count_365d : Optional[float]
            Filter to rows whose `order_count_365d` is exactly this value. Orders in the 365 days before `orders_as_of`.
        revenue_total : Optional[float]
            Filter to rows whose `revenue_total` is exactly this value. Revenue ever counted, in `currency`. Which orders count is the orders app's decision, not this app's.
        revenue_30d : Optional[float]
            Filter to rows whose `revenue_30d` is exactly this value. Revenue in the 30 days before `orders_as_of`.
        revenue_90d : Optional[float]
            Filter to rows whose `revenue_90d` is exactly this value. Revenue in the 90 days before `orders_as_of`.
        revenue_365d : Optional[float]
            Filter to rows whose `revenue_365d` is exactly this value. Revenue in the 365 days before `orders_as_of`. The usual "how big is this customer" number, and the one a key-account rule should read.
        avg_order_value : Optional[float]
            Filter to rows whose `avg_order_value` is exactly this value. revenue_total / order_count, computed here from the sums rather than averaged upstream. Zero when there are no orders.
        avg_order_value_365d : Optional[float]
            Filter to rows whose `avg_order_value_365d` is exactly this value. revenue_365d / order_count_365d. Zero when there were none in the window.
        first_order_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When this company first ordered. Null if it never has — that is what makes it usable as "is this a customer at all?".
        last_order_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When this company last ordered. Null if it never has, which is why the virtual `days_since_last_order` rule field never matches those companies: use `last_order_at is_empty` for them.
        currency : Optional[str]
            Filter to rows whose `currency` is exactly this value. The single ISO 4217 currency all counted orders were in. NULL when there were none, and also when there were several — read `currency_mixed` to tell those two apart.
        currency_mixed : Optional[bool]
            Filter to rows whose `currency_mixed` is exactly this value. True when this company ordered in more than one currency. The sums are still stored (dropping money is worse), but they are not comparable against a threshold, and a rule reading revenue should say so.
        orders_as_of : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. The instant the rolling windows were measured from. Pinned across a chunked refresh, so a multi-call pass cannot let the windows slide underneath it.
        computed_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When this row was last written. The projection is materialized, so this is how stale the numbers are.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the projection row first appeared.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the row last changed. Unchanged numbers are not rewritten, so this can lag `computed_at`.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organization_metrics'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if order_count is not None:
            api_params['order_count'] = self._normalize_value(order_count)
        if order_count_30d is not None:
            api_params['order_count_30d'] = self._normalize_value(order_count_30d)
        if order_count_90d is not None:
            api_params['order_count_90d'] = self._normalize_value(order_count_90d)
        if order_count_365d is not None:
            api_params['order_count_365d'] = self._normalize_value(order_count_365d)
        if revenue_total is not None:
            api_params['revenue_total'] = self._normalize_value(revenue_total)
        if revenue_30d is not None:
            api_params['revenue_30d'] = self._normalize_value(revenue_30d)
        if revenue_90d is not None:
            api_params['revenue_90d'] = self._normalize_value(revenue_90d)
        if revenue_365d is not None:
            api_params['revenue_365d'] = self._normalize_value(revenue_365d)
        if avg_order_value is not None:
            api_params['avg_order_value'] = self._normalize_value(avg_order_value)
        if avg_order_value_365d is not None:
            api_params['avg_order_value_365d'] = self._normalize_value(avg_order_value_365d)
        if first_order_at is not None:
            api_params['first_order_at'] = self._normalize_value(first_order_at)
        if last_order_at is not None:
            api_params['last_order_at'] = self._normalize_value(last_order_at)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if currency_mixed is not None:
            api_params['currency_mixed'] = self._normalize_value(currency_mixed)
        if orders_as_of is not None:
            api_params['orders_as_of'] = self._normalize_value(orders_as_of)
        if computed_at is not None:
            api_params['computed_at'] = self._normalize_value(computed_at)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_organization_metrics_freshness(
        self
    ) -> OrganizationMetricsFreshness:
        """
        The projection is materialized, so it is only as true as its last refresh. This is that fact as one answer: the OLDEST computed_at in the table (the floor, not an average), the anchor those numbers were measured from, and how many organizations are not covered at all yet.

        Returns
        -------
        OrganizationMetricsFreshness
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organization_metrics/freshness'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=OrganizationMetricsFreshness)


    def customers_organization_metrics_refresh(
        self,
        as_of: Optional[str] = None,
        cursor: Optional[str] = None,
        organization_ids: Optional[List[str]] = None
    ) -> Error:
        """
        Revenue lives in the orders app and cannot be joined (ADR-0055: no cross-app FK, grant or view), so it is PULLED: this route walks organizations in id order, asks orders.reports.customer-rollup about a batch of them at a time and materializes the answer into organization_metrics — one row per organization, all-zero for those that never ordered, so that 'never bought' rules match something. Rows are only rewritten when a value actually changed, so a routine refresh costs almost no writes. Bounded by a wall-clock budget below the gateway's upstream timeout: while 'done' is false, POST again with the returned 'cursor' AND 'as_of' (pinning as_of is what stops the rolling windows sliding during a multi-call refresh). 'organization_ids' refreshes exactly those organizations in a single call — the targeted path after a customer ordered.

        Parameters
        ----------
        as_of : Optional[str]
            Anchor for the rolling windows — pass back the value the previous call returned.
        cursor : Optional[str]
            Continue an unfinished refresh: the value the previous call returned, verbatim. It is the id of the last organization processed, so only a value this API handed out ever resolves.
        organization_ids : Optional[List[str]]
            Refresh exactly these organizations in one call instead of walking all of them.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organization_metrics/refresh'
        api_params = {}

        api_params['as_of'] = self._normalize_value(as_of)
        api_params['cursor'] = self._normalize_value(cursor)
        api_params['organization_ids'] = self._normalize_value(organization_ids)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organization_metrics_get(
        self,
        id: str
    ) -> Error:
        """
        What an organization has BOUGHT, materialized into this app from the orders app: lifetime revenue, revenue over the last 30/90/365 days, order count, average order value, and the first and last order dates. Revenue lives in orders and may not be joined (ADR-0055: no cross-app foreign key, grant or view), so it is pulled on a schedule and stored here — one row per organization, all-zero for a company that never ordered, so that a "never bought anything" rule has something to match. One company's numbers by the metrics row id. All zeroes mean the company has never ordered, not that the projection is missing — a missing row means the refresh has not reached that company yet.

        Parameters
        ----------
        id : str
            The organization metrics row to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organization_metrics/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organizations_list(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        vat_id: Optional[str] = None,
        branche: Optional[str] = None,
        customer_number: Optional[str] = None,
        status: Optional[CustomersOrganizationsListStatus] = None,
        lifecycle_stage: Optional[str] = None,
        payment_terms: Optional[str] = None,
        credit_limit: Optional[float] = None,
        price_list: Optional[str] = None,
        delivery_block: Optional[bool] = None,
        external_team_id: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        An organization is a buying COMPANY — the unit a contract, a credit limit, a price list and a payment term belong to, and the unit an order is placed on behalf of. It is not a household and not a person: the people are `contacts`, and a company with no contacts yet is a perfectly normal row. Every organization is mirrored into platform auth as a team, so a name written here is the name storefront authentication shows. The company list a sales or service desk works from, and the read a segment rule is written against. Every column of the table is a filter and the page is `limit`/`offset`/`order` — including the two that are constantly confused: `status` is ACCESS (active or blocked) and `lifecycle_stage` is the sales PIPELINE, so filtering the wrong one answers with the wrong companies rather than with an error.

        Parameters
        ----------
        id : Optional[str]
            Filter to exactly one company. `GET /customers/organizations/{id}` is the direct form; this exists because the list honours it too.
        name : Optional[str]
            Filter by the EXACT company name — this is an equality, not a search. There is no substring or fuzzy match on this API.
        vat_id : Optional[str]
            Look a company up by its VAT id — the check an integration runs before founding a duplicate.
        branche : Optional[str]
            Filter by exact industry. Free text a merchant typed, matched exactly and case-sensitively — 'Maschinenbau' does not find 'maschinenbau', and there is no substring search to fall back on.
        customer_number : Optional[str]
            Look a company up by its ERP number — the lookup an ERP integration and a service desk both start from. Exact match; the real numbers come from the merchant, so the example here resolves nowhere.
        status : Optional[CustomersOrganizationsListStatus]
            Filter by status — access, not pipeline.
        lifecycle_stage : Optional[str]
            Filter by pipeline stage. One of the tenant's own stages (GET /customers/lifecycle-stages); a fresh install starts with lead, prospect, customer, churned.
        payment_terms : Optional[str]
            Filter to rows whose `payment_terms` is exactly this value. When this company has to pay — one of the tenant's own terms (GET /customers/payment-terms, seeded with prepayment, direct_debit, net_7/14/30/60/90). Null means nothing was agreed and the order flow falls back to the market's `default_payment_terms`. This is a commercial term, not a payment method: HOW they pay is the payments app's business.
        credit_limit : Optional[float]
            Filter to rows whose `credit_limit` is exactly this value. Ceiling on open receivables in the market's currency, and one of the inputs that decide whether an order is accepted at all. Null means NO limit — not a limit of zero.
        price_list : Optional[str]
            Filter to rows whose `price_list` is exactly this value. Code of the price list this company buys on — plain text pointing into the prices app. ADR-0055 forbids the cross-app foreign key, so nothing here checks it: a code that names no list simply prices nothing. `standard` is the list the prices app seeds on install.
        delivery_block : Optional[bool]
            Filter to companies whose shipments are stopped.
        external_team_id : Optional[str]
            Find the organization behind a platform team id. The reverse of the mirror, and the way an auth-side id becomes a customer record.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When this company record was created in this app. Not when the customer relationship began — an ERP import creates decade-old customers today.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When any column of this row last changed.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organizations'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if vat_id is not None:
            api_params['vat_id'] = self._normalize_value(vat_id)
        if branche is not None:
            api_params['branche'] = self._normalize_value(branche)
        if customer_number is not None:
            api_params['customer_number'] = self._normalize_value(customer_number)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if lifecycle_stage is not None:
            api_params['lifecycle_stage'] = self._normalize_value(lifecycle_stage)
        if payment_terms is not None:
            api_params['payment_terms'] = self._normalize_value(payment_terms)
        if credit_limit is not None:
            api_params['credit_limit'] = self._normalize_value(credit_limit)
        if price_list is not None:
            api_params['price_list'] = self._normalize_value(price_list)
        if delivery_block is not None:
            api_params['delivery_block'] = self._normalize_value(delivery_block)
        if external_team_id is not None:
            api_params['external_team_id'] = self._normalize_value(external_team_id)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_organizations_create(
        self,
        name: str,
        branche: Optional[str] = None,
        credit_limit: Optional[float] = None,
        customer_number: Optional[str] = None,
        delivery_block: Optional[bool] = None,
        lifecycle_stage: Optional[str] = None,
        payment_terms: Optional[str] = None,
        price_list: Optional[str] = None,
        settings: Optional[Dict[str, Any]] = None,
        status: Optional[OrganizationStatus] = None,
        vat_id: Optional[str] = None
    ) -> Error:
        """
        An organization is a buying COMPANY — the unit a contract, a credit limit, a price list and a payment term belong to, and the unit an order is placed on behalf of. It is not a household and not a person: the people are `contacts`, and a company with no contacts yet is a perfectly normal row. Every organization is mirrored into platform auth as a team, so a name written here is the name storefront authentication shows. Registers a company as a customer. It is mirrored into platform auth as a team in the same call, so a failure of the identity service fails the create rather than leaving half a company behind. `payment_terms` and `lifecycle_stage` name values from this tenant's own sets, and a newly founded company inherits the tenant's `default_payment_terms` / `default_credit_limit` where the merchant set them. `name` is the only field a create cannot omit; everything else is optional or defaulted by the database. Two rows of this tenant may not share `customer_number` (while customer_number IS NOT NULL) or `external_team_id` (while external_team_id IS NOT NULL).

        Parameters
        ----------
        name : str
            Legal or trading name of the COMPANY — never a person. Mirrored to the platform team, so a rename here is a rename in storefront auth too.
        branche : Optional[str]
            Industry / line of business, in the merchant's own words. Free text: no NACE code, no WZ number, no list to pick from — whatever somebody typed on the company. Segment rules read it, and both `?branche=` and an `eq` condition match it EXACTLY and case-sensitively, so 'Maschinenbau' and 'maschinenbau' are two different industries. Indexed, so it stays cheap to filter on.
        credit_limit : Optional[float]
            Ceiling on open receivables in the market's currency, and one of the inputs that decide whether an order is accepted at all. Null means NO limit — not a limit of zero. A create without it inherits the tenant's `default_credit_limit`.
        customer_number : Optional[str]
            The number this company carries in the merchant's own ERP — the key an ERP integration joins on, and what a service desk asks for on the phone. Free text with NO enforced format (a letter prefix and a running number is the common shape, but plain digits are just as valid), unique per tenant while it is set, and one of the fields duplicate detection can be pointed at. The real values come out of the merchant's ERP; nothing published here can name one that exists. A second company with the same number is a 409.
        delivery_block : Optional[bool]
            True stops SHIPMENTS to this company while leaving login and ordering alone — the "they may order, we are just not sending anything until this is settled" state. Separate from `status` on purpose: blocking the login to stop a delivery locks out the people who could settle it. Default false.
        lifecycle_stage : Optional[str]
            Where the company stands in the SALES PIPELINE, and a deliberately separate axis from `status`: a prospect that may log in and a customer that may not are both ordinary states, and one column cannot say that. One of the tenant's own stages (GET /customers/lifecycle-stages) — a fresh install starts with lead, prospect, customer, churned, and the merchant may add their own. Nothing moves it automatically; a stage changes when a person or an integration says so. A create without it gets the stage flagged as default; a value the tenant does not keep is a 400.
        payment_terms : Optional[str]
            When this company has to pay — one of the tenant's own terms (GET /customers/payment-terms, seeded with prepayment, direct_debit, net_7/14/30/60/90). Null means nothing was agreed and the order flow falls back to the market's `default_payment_terms`. This is a commercial term, not a payment method: HOW they pay is the payments app's business. A create without it inherits the market's `default_payment_terms`; a value the tenant does not keep is a 400.
        price_list : Optional[str]
            Code of the price list this company buys on — plain text pointing into the prices app. ADR-0055 forbids the cross-app foreign key, so nothing here checks it: a code that names no list simply prices nothing. `standard` is the list the prices app seeds on install.
        settings : Optional[Dict[str, Any]]
            Free-form per-organization settings, keyed by whatever the merchant's own integrations agree on — this app never branches on a key in here. Segment rules can address a TOP-LEVEL key as `setting:<key>`, which is the whole reason the blob survives: a flag an ERP writes here selects a segment without a schema change. Commercial terms are typed columns now (payment_terms, credit_limit); writing them back in here leaves the checkout reading the column and finding nothing. Replaced wholesale on an update — send the whole object, not a patch of it.
        status : Optional[OrganizationStatus]
            ACCESS, not pipeline: 'blocked' stops this company's people from logging in and is where a rejected registration parks the company it founded. 'active' is the default. For how far along a company is, read `lifecycle_stage` — reading this one for that is how a won deal gets locked out. Default 'active'.
        vat_id : Optional[str]
            VAT identification number (USt-IdNr. in Germany) — the closest thing a B2B buyer has to a legal identity. Validated against the EU VIES service when the tenant's `organization_vat_id_required` setting is on, and stored verbatim otherwise, including for buyers outside the EU.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organizations'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')


        api_params['branche'] = self._normalize_value(branche)
        api_params['credit_limit'] = self._normalize_value(credit_limit)
        api_params['customer_number'] = self._normalize_value(customer_number)
        if delivery_block is not None:
            api_params['delivery_block'] = self._normalize_value(delivery_block)
        if lifecycle_stage is not None:
            api_params['lifecycle_stage'] = self._normalize_value(lifecycle_stage)
        api_params['name'] = self._normalize_value(name)
        api_params['payment_terms'] = self._normalize_value(payment_terms)
        api_params['price_list'] = self._normalize_value(price_list)
        api_params['settings'] = self._normalize_value(settings)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['vat_id'] = self._normalize_value(vat_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organizations_delete(
        self,
        id: str
    ) -> Error:
        """
        An organization is a buying COMPANY — the unit a contract, a credit limit, a price list and a payment term belong to, and the unit an order is placed on behalf of. It is not a household and not a person: the people are `contacts`, and a company with no contacts yet is a perfectly normal row. Every organization is mirrored into platform auth as a team, so a name written here is the name storefront authentication shows. Removes the company and its mirrored team. Its people are NOT deleted: they become standalone buyers who can still sign in and still order, which is the behaviour a merchant winding down a subsidiary wants. Deleting one takes every `contact_events`, `addresses`, `organization_metrics` and `segment_members` row that points at it with it and clears `contacts.organization_id` rather than deleting those rows — the foreign keys decide, not this route.

        Parameters
        ----------
        id : str
            The organization to delete.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organizations_get(
        self,
        id: str
    ) -> Error:
        """
        An organization is a buying COMPANY — the unit a contract, a credit limit, a price list and a payment term belong to, and the unit an order is placed on behalf of. It is not a household and not a person: the people are `contacts`, and a company with no contacts yet is a perfectly normal row. Every organization is mirrored into platform auth as a team, so a name written here is the name storefront authentication shows. One company by id, with its commercial terms as stored. What it has BOUGHT is not in here — that is the `organization_metrics` row for the same id, refreshed on its own schedule.

        Parameters
        ----------
        id : str
            The organization to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organizations_update(
        self,
        id: str,
        branche: Optional[str] = None,
        credit_limit: Optional[float] = None,
        customer_number: Optional[str] = None,
        delivery_block: Optional[bool] = None,
        lifecycle_stage: Optional[str] = None,
        name: Optional[str] = None,
        payment_terms: Optional[str] = None,
        price_list: Optional[str] = None,
        settings: Optional[Dict[str, Any]] = None,
        status: Optional[OrganizationStatus] = None,
        vat_id: Optional[str] = None
    ) -> Error:
        """
        An organization is a buying COMPANY — the unit a contract, a credit limit, a price list and a payment term belong to, and the unit an order is placed on behalf of. It is not a household and not a person: the people are `contacts`, and a company with no contacts yet is a perfectly normal row. Every organization is mirrored into platform auth as a team, so a name written here is the name storefront authentication shows. A partial update — send only what changes. `external_team_id` is mirror-managed and ignored if sent. Blocking a company here is what stops it trading; moving it through the pipeline is `lifecycle_stage`, and the two are independent. Two rows of this tenant may not share `customer_number` (while customer_number IS NOT NULL) or `external_team_id` (while external_team_id IS NOT NULL).

        Parameters
        ----------
        id : str
            The organization to update.
        branche : Optional[str]
            Industry / line of business, in the merchant's own words. Free text: no NACE code, no WZ number, no list to pick from — whatever somebody typed on the company. Segment rules read it, and both `?branche=` and an `eq` condition match it EXACTLY and case-sensitively, so 'Maschinenbau' and 'maschinenbau' are two different industries. Indexed, so it stays cheap to filter on.
        credit_limit : Optional[float]
            Ceiling on open receivables in the market's currency, and one of the inputs that decide whether an order is accepted at all. Null means NO limit — not a limit of zero. A create without it inherits the tenant's `default_credit_limit`.
        customer_number : Optional[str]
            The number this company carries in the merchant's own ERP — the key an ERP integration joins on, and what a service desk asks for on the phone. Free text with NO enforced format (a letter prefix and a running number is the common shape, but plain digits are just as valid), unique per tenant while it is set, and one of the fields duplicate detection can be pointed at. The real values come out of the merchant's ERP; nothing published here can name one that exists. A second company with the same number is a 409.
        delivery_block : Optional[bool]
            True stops SHIPMENTS to this company while leaving login and ordering alone — the "they may order, we are just not sending anything until this is settled" state. Separate from `status` on purpose: blocking the login to stop a delivery locks out the people who could settle it. Default false.
        lifecycle_stage : Optional[str]
            Where the company stands in the SALES PIPELINE, and a deliberately separate axis from `status`: a prospect that may log in and a customer that may not are both ordinary states, and one column cannot say that. One of the tenant's own stages (GET /customers/lifecycle-stages) — a fresh install starts with lead, prospect, customer, churned, and the merchant may add their own. Nothing moves it automatically; a stage changes when a person or an integration says so. A create without it gets the stage flagged as default; a value the tenant does not keep is a 400.
        name : Optional[str]
            Legal or trading name of the COMPANY — never a person. Mirrored to the platform team, so a rename here is a rename in storefront auth too.
        payment_terms : Optional[str]
            When this company has to pay — one of the tenant's own terms (GET /customers/payment-terms, seeded with prepayment, direct_debit, net_7/14/30/60/90). Null means nothing was agreed and the order flow falls back to the market's `default_payment_terms`. This is a commercial term, not a payment method: HOW they pay is the payments app's business. A create without it inherits the market's `default_payment_terms`; a value the tenant does not keep is a 400.
        price_list : Optional[str]
            Code of the price list this company buys on — plain text pointing into the prices app. ADR-0055 forbids the cross-app foreign key, so nothing here checks it: a code that names no list simply prices nothing. `standard` is the list the prices app seeds on install.
        settings : Optional[Dict[str, Any]]
            Free-form per-organization settings, keyed by whatever the merchant's own integrations agree on — this app never branches on a key in here. Segment rules can address a TOP-LEVEL key as `setting:<key>`, which is the whole reason the blob survives: a flag an ERP writes here selects a segment without a schema change. Commercial terms are typed columns now (payment_terms, credit_limit); writing them back in here leaves the checkout reading the column and finding nothing. Replaced wholesale on an update — send the whole object, not a patch of it.
        status : Optional[OrganizationStatus]
            ACCESS, not pipeline: 'blocked' stops this company's people from logging in and is where a rejected registration parks the company it founded. 'active' is the default. For how far along a company is, read `lifecycle_stage` — reading this one for that is how a won deal gets locked out. Default 'active'.
        vat_id : Optional[str]
            VAT identification number (USt-IdNr. in Germany) — the closest thing a B2B buyer has to a legal identity. Validated against the EU VIES service when the tenant's `organization_vat_id_required` setting is on, and stored verbatim otherwise, including for buyers outside the EU.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['branche'] = self._normalize_value(branche)
        api_params['credit_limit'] = self._normalize_value(credit_limit)
        api_params['customer_number'] = self._normalize_value(customer_number)
        if delivery_block is not None:
            api_params['delivery_block'] = self._normalize_value(delivery_block)
        if lifecycle_stage is not None:
            api_params['lifecycle_stage'] = self._normalize_value(lifecycle_stage)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['payment_terms'] = self._normalize_value(payment_terms)
        api_params['price_list'] = self._normalize_value(price_list)
        api_params['settings'] = self._normalize_value(settings)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['vat_id'] = self._normalize_value(vat_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

