from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.price_list_status import PriceListStatus;
from ..enums.price_list_tax_basis import PriceListTaxBasis;
from ..models.error import Error;
from ..models.price_list_defaults_response import PriceListDefaultsResponse;
from ..enums.price_entry_type import PriceEntryType;
from ..models.price_entry_replace_item import PriceEntryReplaceItem;
from ..enums.price_ending_rule import PriceEndingRule;
from ..enums.price_entries_bulk_mode import PriceEntriesBulkMode;
from ..models.price_resolve_item import PriceResolveItem;
from ..models.price_vocabulary_index import PriceVocabularyIndex;
from ..enums.prices_vocabularies_get_name import PricesVocabulariesGetName;

class Prices(Service):

    def __init__(self, client) -> None:
        super(Prices, self).__init__(client)

    def prices_lists_list(
        self,
        id: Optional[str] = None,
        code: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        currency: Optional[str] = None,
        status: Optional[PriceListStatus] = None,
        priority: Optional[float] = None,
        is_default: Optional[bool] = None,
        tax_basis: Optional[PriceListTaxBasis] = None,
        tax_included: Optional[bool] = None,
        requires_auth: Optional[bool] = None,
        contact_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        One page of the tenant's price list HEADERS — code, currency, tax basis, status, priority, validity window, buyer scope and the default flag. Never the prices themselves: those are a separate page per list (`GET /prices/lists/{list_id}/entries`).
        
        Every filter is an EXACT match on a column, ANDed together; a query key that is not a column is dropped in silence, which is why the answer echoes `filter`. The scope, currency and status filters are the useful ones, because between them they narrow the set to the candidates a resolve call in a given currency for a given buyer can draw on at all.
        
        Market is deliberately not among them: a list is scoped to a market by an assignment, not a column, and the `X-Revenexx-Market` header is what narrows the set — this admin listing shows the tenant's lists whatever their market.

        Parameters
        ----------
        id : Optional[str]
            Filter to one list by id. The same row `GET /prices/lists/{id}` returns, in page form.
        code : Optional[str]
            Filter by the exact list code — the unique per-tenant handle every integration joins on.
        name : Optional[str]
            Filter by the exact operator-facing name. Exact match, not a search: prefer `code`.
        description : Optional[str]
            Filter by the exact description text. Exact match, not a search.
        currency : Optional[str]
            Filter to one ISO 4217 currency. Resolution only ever considers lists in the currency of the call, so this is how to see the set a given quote can draw on.
        status : Optional[PriceListStatus]
            Filter by status. Only `active` lists take part in resolution, so `?status=active` is the candidate set.
        priority : Optional[float]
            Filter to one exact priority value — the tie-break within a specificity group.
        is_default : Optional[bool]
            Filter to the default list — the one `prices.lists.make-default` moves the flag onto. `?is_default=true` should answer exactly one row; two is the state that leaves a tie unsettled.
        tax_basis : Optional[PriceListTaxBasis]
            Filter by declared basis. `?tax_basis=` cannot select the lists that state NONE (a filter is an equality, never a null test) — those are the lists that inherit the tenant’s `tax_inclusive_default`, and the resolve answer names them with `tax_basis_source: "tenant"`.
        tax_included : Optional[bool]
            Filter by the legacy gross mirror. `?tax_included=true` finds the lists whose basis was stated the old way.
        requires_auth : Optional[bool]
            Filter to the lists that resolve only for an authenticated buyer — what an anonymous storefront will never see.
        contact_id : Optional[str]
            Filter to the lists scoped to one contact — the most specific buyer scope there is.
        organization_id : Optional[str]
            Filter to the lists scoped to one organization.
        channel_id : Optional[str]
            Filter to the lists scoped to one sales channel.
        valid_from : Optional[str]
            Exact equality on the start of the list’s validity window — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        valid_until : Optional[str]
            Exact equality on the end of the list’s validity window — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        created_at : Optional[str]
            Exact equality on the creation instant — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        updated_at : Optional[str]
            Exact equality on the last change — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if tax_basis is not None:
            api_params['tax_basis'] = self._normalize_value(tax_basis)
        if tax_included is not None:
            api_params['tax_included'] = self._normalize_value(tax_included)
        if requires_auth is not None:
            api_params['requires_auth'] = self._normalize_value(requires_auth)
        if contact_id is not None:
            api_params['contact_id'] = self._normalize_value(contact_id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        if valid_from is not None:
            api_params['valid_from'] = self._normalize_value(valid_from)
        if valid_until is not None:
            api_params['valid_until'] = self._normalize_value(valid_until)
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

        return self._parse_response(response, model=Error)


    def prices_lists_create(
        self,
        code: str,
        name: str,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        organization_id: Optional[str] = None,
        priority: Optional[float] = None,
        requires_auth: Optional[bool] = None,
        status: Optional[PriceListStatus] = None,
        tax_basis: Optional[PriceListTaxBasis] = None,
        tax_included: Optional[bool] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> Error:
        """
        Opens an empty book, and states in one row the four things that decide whether it will ever price anything: its currency, its priority within a specificity group, its validity window, and its buyer scope (contact, organization or channel — leave all three empty for a list open to everyone).
        
        `code` and `name` are the only fields required — they are the two columns with no default — and `code` is unique per tenant, so a code already in use is a 409 rather than an overwrite of prices somebody is selling on.
        
        Everything else has a default, and two of them are worth choosing rather than accepting. `currency` defaults to EUR and is the currency of every amount in the list, since entries carry none; a resolve call only considers lists in the currency it is asked about, and nothing is ever converted. `tax_basis` defaults to NOTHING, which means the amounts inherit the tenant's `tax_inclusive_default` — state net or gross here and the answer stops depending on a tenant setting somebody may change later.
        
        `is_default: true` here does NOT demote the list that currently holds the flag: you end up with two defaults, and which of them prices an item is left to the tenant's tie-break. Create the list, then move the flag with `POST /prices/lists/{list_id}/make-default`.
        
        A new list prices nothing at all until it has entries, so it is inert until you add them — which makes it safe to create one ahead of the prices that will fill it.

        Parameters
        ----------
        code : str
            Unique list code per tenant — the handle every import and integration addresses this list by. A code already in use answers 409.
        name : str
            Operator-facing name, shown wherever a human picks a list.
        channel_id : Optional[str]
            Scope: only this sales channel. Beats the open lists, loses to contact and organization.
        contact_id : Optional[str]
            Scope: only this contact. The most specific scope there is — it beats organization, channel and every open list, whatever their priority.
        currency : Optional[str]
            ISO 4217 code (default EUR) — the currency of EVERY amount in this list, since entries carry none of their own. Resolution only considers lists matching the currency of the call; nothing is ever converted.
        description : Optional[str]
            Free text for whoever maintains the list — why it exists and who it is for. Never shown to a buyer.
        is_default : Optional[bool]
            The fallback list. Within its group it sorts LAST, so it wins only where nothing more specific priced the item. Use prices.lists.make-default to move the flag rather than setting it here — two defaults leave a tie to row order.
        labels : Optional[Dict[str, Any]]
            Localised names, keyed by language tag — {"de": "Händlerpreise", "en": "Dealer prices"}. Omit to show `name` everywhere.
        metadata : Optional[Dict[str, Any]]
            Free-form bag: whatever JSON object you write round-trips exactly, and this app never reads it. Its keys are yours — ERP provenance is the usual content.
        organization_id : Optional[str]
            Scope: only buyers of this organization. Beats channel-scoped and open lists.
        priority : Optional[float]
            Tie-break WITHIN a specificity group (higher wins, default 0). It never beats scope: an organization list at 0 still wins over an open list at 100.
        requires_auth : Optional[bool]
            Gate: when true the list resolves only for an authenticated buyer (contact or organization context); anonymous resolve calls get on_request. Default false (open to everyone).
        status : Optional[PriceListStatus]
            Default 'active' — only active lists resolve. 'inactive' retires a list without deleting its prices.
        tax_basis : Optional[PriceListTaxBasis]
            Whether the amounts in this list are net (tax excluded) or gross (tax included) — the one fact a price cannot be without. Omit (null) to inherit the tenant's tax_inclusive_default setting; the resolve answer names which of the two decided under tax_basis_source.
        tax_included : Optional[bool]
            LEGACY mirror of tax_basis. false is the column default and is NOT read as a statement of intent; true is read as gross, and only where tax_basis is null. Prefer tax_basis.
        valid_from : Optional[str]
            Start of the validity window of the WHOLE list (ISO 8601); null = open-ended. Outside it the list is not a candidate at all.
        valid_until : Optional[str]
            End of the validity window of the whole list; null = open-ended. Lets a season expire on its own instead of being deactivated by hand.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')


        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['code'] = self._normalize_value(code)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if requires_auth is not None:
            api_params['requires_auth'] = self._normalize_value(requires_auth)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['tax_basis'] = self._normalize_value(tax_basis)
        if tax_included is not None:
            api_params['tax_included'] = self._normalize_value(tax_included)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_lists_defaults(
        self
    ) -> PriceListDefaultsResponse:
        """
        Gives a tenant the one open list every tenant needs, so nothing has to exist before the first price can be written. Almost nobody calls it: the app runs it by itself on `app.installed`, and the route is the manual re-run — for a tenant installed before that hook existed, or one whose standard list was deleted. Because it is idempotent it is also safe to call from a provisioning script that cannot know which of the two is the case.
        
        What it writes comes from settings, not from constants: the code is the tenant's `default_price_list_code`, the currency its `default_currency`, and the seeded list STATES its tax basis from `tax_inclusive_default` instead of inheriting it, because the one list every tenant gets should not be the ambiguous one.
        
        Idempotent twice over — by that code, and by the existence of ANY default list. So calling it repeatedly is free, changing `default_price_list_code` later never produces a second list, and a tenant that has made some other list the default is left exactly as it is (the answer names that list under `existing`). It writes nothing else: it never demotes, never touches entries, and never repairs a list that is already there.

        Returns
        -------
        PriceListDefaultsResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=PriceListDefaultsResponse)


    def prices_lists_delete(
        self,
        id: str
    ) -> Error:
        """
        Deletes the list AND every price in it. `price_entries.price_list_id` references this row ON DELETE CASCADE, so the entries go in the same statement: nothing asks, nothing blocks, a book of 40 000 prices deletes exactly as fast as an empty one, and the answer is a bare `{deleted, id}` that never says how many prices went with it.
        
        What that means while a storefront is quoting: from the next resolve call the items this list priced fall through to the next candidate list, and where there is none the answer is `on_request` — "price on request" for something that had a price a second ago, never €0. If the deleted list held the default flag the tenant has no default until one is moved onto another list; re-running `POST /prices/lists/defaults` recreates the standard list only while no other default exists.
        
        This is not the way to take a list out of circulation. `status: "inactive"` does that immediately and reversibly and keeps the prices; deleting is for a list whose contents you are prepared to import again, because nothing here is recoverable.

        Parameters
        ----------
        id : str
            The price list, by id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_lists_get(
        self,
        id: str
    ) -> Error:
        """
        The list HEADER, never its prices: currency, tax basis, buyer scope, priority, validity window and the default flag — the settings that decide WHETHER this list prices a given buyer, before any amount is looked at. Its entries are a separate page (`GET /prices/lists/{list_id}/entries`), because a price book runs to thousands of rows and no read of a list should carry them. This is the admin view and it reads the base table rather than the market-scoped one the resolve call uses, so a list that is invisible in the active market is still returned here.

        Parameters
        ----------
        id : str
            The price list, by id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_lists_update(
        self,
        id: str,
        channel_id: Optional[str] = None,
        code: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        priority: Optional[float] = None,
        requires_auth: Optional[bool] = None,
        status: Optional[PriceListStatus] = None,
        tax_basis: Optional[PriceListTaxBasis] = None,
        tax_included: Optional[bool] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> Error:
        """
        A partial update: send only what changes, omitted fields keep their value, and a payload with no updatable column at all is refused rather than answered with an unchanged row. There is no draft and no publish step — the next resolve call reads what this one wrote.
        
        Three edits do more than their field names suggest. `currency` re-denominates without converting: entries carry no currency of their own, so 19.90 EUR becomes 19.90 CHF and the whole book is re-priced by one edit. `status: "inactive"` takes the list out of every quote immediately while keeping its prices — the reversible way to stop selling on a list, and the one to reach for instead of deleting it. `code` is the handle imports and integrations address the list by, and a code another list already holds is a 409.
        
        `is_default` behaves here exactly as it does on create: setting it true leaves the incumbent default in place, so use `POST /prices/lists/{list_id}/make-default`, which demotes in the same call.

        Parameters
        ----------
        id : str
            The price list, by id.
        channel_id : Optional[str]
            Scope: only this sales channel. Beats the open lists, loses to contact and organization.
        code : Optional[str]
            Unique list code per tenant — the handle every import and integration addresses this list by. A code already in use answers 409.
        contact_id : Optional[str]
            Scope: only this contact. The most specific scope there is — it beats organization, channel and every open list, whatever their priority.
        currency : Optional[str]
            ISO 4217 code (default EUR) — the currency of EVERY amount in this list, since entries carry none of their own. Resolution only considers lists matching the currency of the call; nothing is ever converted.
        description : Optional[str]
            Free text for whoever maintains the list — why it exists and who it is for. Never shown to a buyer.
        is_default : Optional[bool]
            The fallback list. Within its group it sorts LAST, so it wins only where nothing more specific priced the item. Use prices.lists.make-default to move the flag rather than setting it here — two defaults leave a tie to row order.
        labels : Optional[Dict[str, Any]]
            Localised names, keyed by language tag — {"de": "Händlerpreise", "en": "Dealer prices"}. Omit to show `name` everywhere.
        metadata : Optional[Dict[str, Any]]
            Free-form bag: whatever JSON object you write round-trips exactly, and this app never reads it. Its keys are yours — ERP provenance is the usual content.
        name : Optional[str]
            Operator-facing name, shown wherever a human picks a list.
        organization_id : Optional[str]
            Scope: only buyers of this organization. Beats channel-scoped and open lists.
        priority : Optional[float]
            Tie-break WITHIN a specificity group (higher wins, default 0). It never beats scope: an organization list at 0 still wins over an open list at 100.
        requires_auth : Optional[bool]
            Gate: when true the list resolves only for an authenticated buyer (contact or organization context); anonymous resolve calls get on_request. Default false (open to everyone).
        status : Optional[PriceListStatus]
            Default 'active' — only active lists resolve. 'inactive' retires a list without deleting its prices.
        tax_basis : Optional[PriceListTaxBasis]
            Whether the amounts in this list are net (tax excluded) or gross (tax included) — the one fact a price cannot be without. Omit (null) to inherit the tenant's tax_inclusive_default setting; the resolve answer names which of the two decided under tax_basis_source.
        tax_included : Optional[bool]
            LEGACY mirror of tax_basis. false is the column default and is NOT read as a statement of intent; true is read as gross, and only where tax_basis is null. Prefer tax_basis.
        valid_from : Optional[str]
            Start of the validity window of the WHOLE list (ISO 8601); null = open-ended. Outside it the list is not a candidate at all.
        valid_until : Optional[str]
            End of the validity window of the whole list; null = open-ended. Lets a season expire on its own instead of being deactivated by hand.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['channel_id'] = self._normalize_value(channel_id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if requires_auth is not None:
            api_params['requires_auth'] = self._normalize_value(requires_auth)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['tax_basis'] = self._normalize_value(tax_basis)
        if tax_included is not None:
            api_params['tax_included'] = self._normalize_value(tax_included)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_list(
        self,
        list_id: str,
        id: Optional[str] = None,
        product_id: Optional[str] = None,
        sku: Optional[str] = None,
        price_type: Optional[PriceEntryType] = None,
        quantity_min: Optional[float] = None,
        unit_price: Optional[float] = None,
        unit: Optional[str] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        The prices inside one list, a page at a time. An entry is a rung rather than "the price of a product": it carries a quantity threshold, an amount and a unit, its own validity window, and — where the answer is deliberately no number at all — an `on_request` marker instead of one. So this page is where the quantity tiers, the promo windows and the "ask us" markers of a book are read.
        
        The ladder of one item is the set of entries sharing an identity, so `?product_id=…` (or `?sku=…`) is how a caller reads the Staffel a resolve answer was built from, and `?price_type=on_request` is how the markers are audited. The response also carries `page` and `filter` like every other list, and an unknown list_id answers 404 instead of an empty page.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        id : Optional[str]
            Filter to one entry by id, within this list.
        product_id : Optional[str]
            Filter to one product — the whole tier ladder that prices it, in this list.
        sku : Optional[str]
            Filter by exact SKU. Not a prefix and not case-insensitive — the bulk adjust route is where `sku_prefix` lives.
        price_type : Optional[PriceEntryType]
            Filter by entry type. `on_request` selects the explicit no-price markers, which is how to audit what a list refuses to quote.
        quantity_min : Optional[float]
            Filter to one exact tier threshold — `?quantity_min=1` is the base rung of every ladder in the list.
        unit_price : Optional[float]
            Filter to entries at one exact amount, in the list’s currency and on its tax basis. Equality, not a range — `?unit_price=0` finds the rows nobody has priced yet.
        unit : Optional[str]
            Filter by exact unit of measure.
        valid_from : Optional[str]
            Exact equality on the start of the entry’s own validity — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        valid_until : Optional[str]
            Exact equality on the end of the entry’s own validity — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        created_at : Optional[str]
            Exact equality on the creation instant — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        updated_at : Optional[str]
            Exact equality on the last change — a bulk adjust only writes the rows whose price actually moved — matched to the stored microsecond, not a range. This app publishes no from/until query; narrow a period client-side, or by `order` plus `limit`.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if product_id is not None:
            api_params['product_id'] = self._normalize_value(product_id)
        if sku is not None:
            api_params['sku'] = self._normalize_value(sku)
        if price_type is not None:
            api_params['price_type'] = self._normalize_value(price_type)
        if quantity_min is not None:
            api_params['quantity_min'] = self._normalize_value(quantity_min)
        if unit_price is not None:
            api_params['unit_price'] = self._normalize_value(unit_price)
        if unit is not None:
            api_params['unit'] = self._normalize_value(unit)
        if valid_from is not None:
            api_params['valid_from'] = self._normalize_value(valid_from)
        if valid_until is not None:
            api_params['valid_until'] = self._normalize_value(valid_until)
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

        return self._parse_response(response, model=Error)


    def prices_entries_create(
        self,
        list_id: str,
        metadata: Optional[Dict[str, Any]] = None,
        price_type: Optional[PriceEntryType] = None,
        product_id: Optional[str] = None,
        quantity_min: Optional[float] = None,
        sku: Optional[str] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> Error:
        """
        Adds ONE rung to one item's quantity ladder in this list. The only thing an entry must have is an identity — `product_id` or `sku`, which the row CHECK enforces; everything else defaults, and one of those defaults deserves a warning.
        
        `unit_price` defaults to **0**. That is the one door through which a zero price enters an app whose whole doctrine is that a missing price is `on_request` and never €0: a create that forgets the amount publishes a free item, and the storefront shows 0.00 instead of "price on request". Send the amount, or send `price_type: "on_request"` where there genuinely is none. The amount is per ONE unit of `unit`, in the LIST's currency (entries carry none) and on the LIST's tax basis, as a decimal in major units — 19.90, never 1990.
        
        Nothing enforces one rung per (item, quantity): create the same `quantity_min` twice and both rows come back in the resolved `tiers`, with the last of them setting the price — an ambiguous ladder no error ever mentions. `quantity_min` defaults to 1 and `price_type` to `standard`.
        
        This route is for a rung at a time. A whole ladder in one call is `POST …/entries/ladder`, an import is `POST …/entries/bulk`, and a complete rewrite of the book is `PUT …/entries`. An unknown `list_id` answers 404 rather than attaching a price to nothing.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        metadata : Optional[Dict[str, Any]]
            Free-form bag: whatever JSON object you write round-trips exactly, and this app never reads it. Its keys are yours.
        price_type : Optional[PriceEntryType]
            Default 'standard'; 'on_request' is the explicit no-price marker — it STOPS resolution for this item on this list and answers "price on request" even where a cheaper list exists.
        product_id : Optional[str]
            The product this rung prices. An entry needs product_id or sku — the row CHECK enforces it.
        quantity_min : Optional[float]
            Tier threshold (Staffelpreis): this price applies from this quantity upwards (default 1). The rungs of one item are the entries sharing its identity; the highest threshold at or below the requested quantity wins.
        sku : Optional[str]
            The article number this rung prices (alternative to product_id). Matched exactly on resolve — never normalised or case-folded.
        unit : Optional[str]
            Unit of measure the price is per — free text, neither validated nor converted here. A resolve call’s `quantity` is counted in it.
        unit_price : Optional[float]
            Price for ONE unit of `unit`, in the LIST’s currency and on the LIST’s tax basis — a decimal amount in major units (19.90), never minor units/cents. Stored at 4 decimals and echoed back exactly as sent (default 0).
        valid_from : Optional[str]
            Start of this entry’s own validity (ISO 8601) — how a promo price is expressed: a second rung, live only for its window. null = open-ended.
        valid_until : Optional[str]
            End of this entry’s own validity; null = open-ended. Outside it the rung is skipped and the ladder resolves as if it were not there.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        api_params['metadata'] = self._normalize_value(metadata)
        if price_type is not None:
            api_params['price_type'] = self._normalize_value(price_type)
        api_params['product_id'] = self._normalize_value(product_id)
        if quantity_min is not None:
            api_params['quantity_min'] = self._normalize_value(quantity_min)
        api_params['sku'] = self._normalize_value(sku)
        api_params['unit'] = self._normalize_value(unit)
        if unit_price is not None:
            api_params['unit_price'] = self._normalize_value(unit_price)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_replace(
        self,
        list_id: str,
        entries: List[PriceEntryReplaceItem]
    ) -> Error:
        """
        Set semantics over the WHOLE list, not over one item: every entry of the list is deleted and the payload becomes the complete new book. It exists for the two callers that genuinely hold the whole book in hand — the Cockpit's table editor, whose save is this call, and a small import. `entries: []` is a legal payload and empties the list — the items it priced then resolve from the next candidate list, or come back `on_request`.
        
        Two consequences of "delete, then insert". Every row is inserted fresh, so all entry ids change and anything holding one is stale afterwards. And it is not a transaction: the deletes go out before the inserts, so a payload that fails part-way through leaves the list holding the rows that landed and none of the ones it had. What protects you is that the whole payload is normalized and validated BEFORE the first delete — a malformed row is a 400 with the list untouched.
        
        For a book of any size, or for adding to one you want to keep, use `POST …/entries/bulk`: it upserts in chunks and never wipes.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        entries : List[PriceEntryReplaceItem]
            The complete new entry set (set semantics).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if entries is None:
            raise RevenexxException('Missing required parameter: "entries"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        api_params['entries'] = self._normalize_value(entries)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_adjust(
        self,
        list_id: str,
        amount: Optional[float] = None,
        dry_run: Optional[bool] = None,
        percent: Optional[float] = None,
        rounding: Optional[PriceEndingRule] = None,
        sku_prefix: Optional[str] = None
    ) -> Error:
        """
        Moves every priced entry of the list at once, in whichever of the two ways a merchant thinks about a price change: `percent` for a relative one (5 raises everything by 5 %) or `amount` for a flat one added to every unit price. One or the other, never both, and `sku_prefix` narrows the change to part of the book. On-request entries are never touched, because a percentage of "ask us" is not a number.
        
        The other half of a bulk change is what the arithmetic leaves behind: a 7 % increase turns 19.90 into 21.293, which no merchant prints. Results are therefore rounded to the tenant's price_precision/rounding_mode and then snapped to a declared merchant price ending — x.99, x.95, a whole number — either the one this call names or the tenant's `bulk_adjust_rounding`. dry_run answers the same preview and writes nothing, which is what the Cockpit dialog shows before it commits.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        amount : Optional[float]
            Absolute change added to every unit price, in the list's currency.
        dry_run : Optional[bool]
            true writes nothing and answers the same preview — what the Cockpit dialog shows before it commits.
        percent : Optional[float]
            Relative change in percent: 5 raises by 5 %, -10 cuts by 10 %.
        rounding : Optional[PriceEndingRule]
            Ending the computed prices snap to (nearest match). Omit to use the tenant's bulk_adjust_rounding setting.
        sku_prefix : Optional[str]
            Restrict the change to entries whose SKU starts with this (a prefix, case-sensitive, no wildcards). Entries identified only by product_id never match a prefix. Omit to change the whole list.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/adjust'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        api_params['amount'] = self._normalize_value(amount)
        api_params['dry_run'] = self._normalize_value(dry_run)
        api_params['percent'] = self._normalize_value(percent)
        api_params['rounding'] = self._normalize_value(rounding)
        api_params['sku_prefix'] = self._normalize_value(sku_prefix)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_bulk(
        self,
        list_id: str,
        entries: List[PriceEntryReplaceItem],
        mode: Optional[PriceEntriesBulkMode] = None
    ) -> Error:
        """
        Adds entries to a list without wiping it, and UPSERTS rather than inserts: a row naming a rung the list already has (same product_id/sku AND quantity_min) updates that rung, so re-running an import corrects prices instead of duplicating the ladder. `mode: 'append'` keeps the old insert-everything behaviour. Inserts go out as one PostgREST bulk write per 1000 rows.
        
        This is the route for a large price book, and a large book arrives in chunks: a call carries at most 5000 entries and a longer payload is refused with 400 rather than truncated, so an importer of 200 000 prices sends forty calls. Because the upsert is keyed on the rung rather than on a row id, the chunks may be re-sent and re-ordered freely — a chunk that lands twice writes the same prices twice.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        entries : List[PriceEntryReplaceItem]
            At most 5000 rows per call — send a large book in chunks.
        mode : Optional[PriceEntriesBulkMode]
            Default 'upsert': a row naming a rung the list already has (same product/sku AND quantity_min) updates it. 'append' always inserts — a re-run then duplicates the ladder, which is what makes an ambiguous tier table.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/bulk'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if entries is None:
            raise RevenexxException('Missing required parameter: "entries"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        api_params['entries'] = self._normalize_value(entries)
        api_params['mode'] = self._normalize_value(mode)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_ladder(
        self,
        list_id: str,
        base_price: float,
        discount_percent: Optional[float] = None,
        product_id: Optional[str] = None,
        quantities: Optional[List[float]] = None,
        replace: Optional[bool] = None,
        rounding: Optional[PriceEndingRule] = None,
        sku: Optional[str] = None,
        unit: Optional[str] = None
    ) -> Error:
        """
        Writes a whole quantity-tier ladder (Staffelpreise) for ONE item in one call, instead of typing a rung at a time. Tiers are a flat quantity_min column on purpose — the ladder IS the set of entries sharing an identity, and resolve returns it sorted as one array. What was missing was the gesture: "19.90 from 1, 5 % off per tier at 10 and 50". Prices are rounded and snapped exactly as a bulk adjust is.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        base_price : float
            Price for ONE unit at the FIRST tier, in the list’s currency and on the list’s tax basis — a decimal amount in major units (19.90), never minor units/cents.
        discount_percent : Optional[float]
            Discount applied per tier, COMPOUNDED down the ladder rather than off the base price: 5 gives 19.90 / 18.91 / 17.96. Default 0.
        product_id : Optional[str]
            The item the ladder prices.
        quantities : Optional[List[float]]
            Tier thresholds, ascending — an array of numbers or a comma-separated string ('1, 10, 50'). Duplicates are collapsed and the set is sorted. Default [1, 10, 50], at most 50 tiers.
        replace : Optional[bool]
            Default true: the item's existing entries in this list are removed first, so the ladder IS the ladder. false appends.
        rounding : Optional[PriceEndingRule]
            Ending the computed prices snap to (nearest match). Omit to use the tenant's bulk_adjust_rounding setting.
        sku : Optional[str]
            The item the ladder prices (alternative to product_id).
        unit : Optional[str]
            Unit of measure carried onto every generated tier. Free text, neither validated nor converted.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/ladder'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if base_price is None:
            raise RevenexxException('Missing required parameter: "base_price"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        api_params['base_price'] = self._normalize_value(base_price)
        api_params['discount_percent'] = self._normalize_value(discount_percent)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantities'] = self._normalize_value(quantities)
        api_params['replace'] = self._normalize_value(replace)
        api_params['rounding'] = self._normalize_value(rounding)
        api_params['sku'] = self._normalize_value(sku)
        api_params['unit'] = self._normalize_value(unit)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_delete(
        self,
        list_id: str,
        id: str
    ) -> Error:
        """
        Removes ONE rung. The item keeps its other rungs and stays priced — which is exactly what makes the lowest rung the dangerous one to delete.
        
        Below the first threshold the FIRST rung's price applies (a minimum quantity belongs to the catalog, not to the price ladder). So deleting the "from 1" rung of a 1/10/50 ladder does not make single units unpriced: it sells them at the 10-up volume price, silently, from the next resolve call onwards. Nothing in the answer marks that the ladder no longer starts where it used to.
        
        Delete an item's LAST rung and this list stops pricing it altogether: the item falls through to the next candidate list, or comes back `on_request` — never €0. To retire a price without losing it, set the rung's `price_type` to `on_request` instead, or deactivate the list. An entry belonging to another list answers 404 rather than being deleted through the wrong parent.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        id : str
            The price entry, by id. An entry that belongs to a different list answers 404.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/{id}'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_get(
        self,
        list_id: str,
        id: str
    ) -> Error:
        """
        One rung of one ladder, exactly as stored — nothing is rounded, converted or taxed on the way out. `unit_price` is per ONE unit of `unit`, in the LIST's currency and on the LIST's tax basis; the entry itself carries neither, which is why a rung read on its own is not yet a price you can show a buyer. `POST /prices/resolve` is what turns it into one: it picks the rung that applies to a quantity, names the basis, and adds the net/gross pair and the tax rate. The id is checked against the list in the path, so an entry belonging to another list answers 404 rather than being read through the wrong parent.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        id : str
            The price entry, by id. An entry that belongs to a different list answers 404.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/{id}'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_entries_update(
        self,
        list_id: str,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        price_type: Optional[PriceEntryType] = None,
        product_id: Optional[str] = None,
        quantity_min: Optional[float] = None,
        sku: Optional[str] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> Error:
        """
        A partial update of one rung: send only what changes, a payload with no updatable column at all is refused, and the next resolve call reads what this one wrote.
        
        Two edits reach further than the field they touch. Moving `quantity_min` moves the rung within the ladder and may land on a threshold the item already has — nothing stops it, and both rows then sit in the resolved `tiers`. Setting `price_type: "on_request"` on ONE rung takes the WHOLE item off price in this list: resolution stops there and answers "price on request" even though the other rungs still carry amounts, and even where a less specific list would have priced it. That is the intended way to say "ask us" for an item, and a surprise if you meant to retire a single tier.
        
        What this route cannot change is what the amount MEANS: currency and tax basis belong to the list, so re-denominating or switching net/gross is a list edit, not an entry edit. An entry of another list answers 404.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        id : str
            The price entry, by id. An entry that belongs to a different list answers 404.
        metadata : Optional[Dict[str, Any]]
            Free-form bag: whatever JSON object you write round-trips exactly, and this app never reads it. Its keys are yours.
        price_type : Optional[PriceEntryType]
            Default 'standard'; 'on_request' is the explicit no-price marker — it STOPS resolution for this item on this list and answers "price on request" even where a cheaper list exists.
        product_id : Optional[str]
            The product this rung prices. An entry needs product_id or sku — the row CHECK enforces it.
        quantity_min : Optional[float]
            Tier threshold (Staffelpreis): this price applies from this quantity upwards (default 1). The rungs of one item are the entries sharing its identity; the highest threshold at or below the requested quantity wins.
        sku : Optional[str]
            The article number this rung prices (alternative to product_id). Matched exactly on resolve — never normalised or case-folded.
        unit : Optional[str]
            Unit of measure the price is per — free text, neither validated nor converted here. A resolve call’s `quantity` is counted in it.
        unit_price : Optional[float]
            Price for ONE unit of `unit`, in the LIST’s currency and on the LIST’s tax basis — a decimal amount in major units (19.90), never minor units/cents. Stored at 4 decimals and echoed back exactly as sent (default 0).
        valid_from : Optional[str]
            Start of this entry’s own validity (ISO 8601) — how a promo price is expressed: a second rung, live only for its window. null = open-ended.
        valid_until : Optional[str]
            End of this entry’s own validity; null = open-ended. Outside it the rung is skipped and the ladder resolves as if it were not there.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/{id}'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['metadata'] = self._normalize_value(metadata)
        if price_type is not None:
            api_params['price_type'] = self._normalize_value(price_type)
        api_params['product_id'] = self._normalize_value(product_id)
        if quantity_min is not None:
            api_params['quantity_min'] = self._normalize_value(quantity_min)
        api_params['sku'] = self._normalize_value(sku)
        api_params['unit'] = self._normalize_value(unit)
        if unit_price is not None:
            api_params['unit_price'] = self._normalize_value(unit_price)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_lists_make_default(
        self,
        list_id: str,
        data: Dict[str, Any]
    ) -> Error:
        """
        Promotes this list AND demotes whoever held the flag, in one call. The flag is a single answer, not a per-row opinion: resolution uses it as the last tie-break, so two defaults leave the winner to row order and none leaves a tie unsettled. Promote-then-demote as two PATCHes from a client produces exactly those two states whenever the second call does not land.
        
        The write is as small as the change: exactly one write per row whose flag was wrong, and none at all for the rows that were already right. A tenant already in this state is therefore not written to, which is what makes repeating the call free. The answer is this list as it now stands plus the codes it demoted — empty when it already held the flag.

        Parameters
        ----------
        list_id : str
            The price list the entries belong to. An id no list in this tenant has answers 404 rather than an empty page.
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/make-default'
        api_params = {}
        if list_id is None:
            raise RevenexxException('Missing required parameter: "list_id"')

        if data is None:
            raise RevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{list_id}', str(self._normalize_value(list_id)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_resolve(
        self,
        items: List[PriceResolveItem],
        at: Optional[str] = None,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        market_id: Optional[str] = None,
        organization_id: Optional[str] = None
    ) -> Error:
        """
        The live price call. Everything else in this app configures prices; this is the one route that ANSWERS them, and a storefront reaches it on every listing, every product page and every cart. Send up to 200 items and the buyer context they are for — contact, organization, market and channel — and get back, per item, the unit price this buyer pays, the net/gross pair, the tax rate, the list that decided it and that item's full quantity ladder.
        
        Which price wins when several match is the whole value of this app, and it is not guessable from the field types. The order, in full:
        
        1. **Candidates.** A list is a candidate when it is `active`, its currency EQUALS the currency of the call (nothing is ever converted — a list in another currency simply does not price the item), the instant `at` falls inside its validity window, it is visible in the buyer’s market (the `X-Revenexx-Market` header scopes the list view; lists assigned to no market are global and always visible), and its buyer scope matches or is open. A `requires_auth` list is dropped for a buyer with neither `contact_id` nor `organization_id`.
        2. **Specificity decides first, and priority never overrules it.** contact-scoped (4) beats organization-scoped (3) beats channel-scoped (2) beats open (0). An organization list at `priority: 0` therefore wins over an open list at `priority: 100`.
        3. **Within one specificity level:** `priority` descending, then non-default before default — the default list is deliberately last, so it prices only what nothing else did.
        4. **A genuine tie** (same specificity, same priority, same default flag) is settled by the tenant’s `price_list_priority_tiebreak` setting — `lowest_price`, `highest_price`, `newest` or `code` — never by the order the database happened to return rows in. The setting in force is echoed in `basis.price_list_priority_tiebreak`.
        5. **The first list that prices the item wins, and the search stops there** — even if a later, less specific list is cheaper. Its FULL tier ladder comes back in `tiers`; the rung with the highest `quantity_min` at or below the requested `quantity` sets `unit_price`, and below the first rung the first rung applies.
        6. **An `on_request` entry stops the search too**, and inside a tie it outranks every price: a list that says "ask us" for this buyer is authoritative, and cannot be undercut by a list that happens to sort after it.
        7. **Nothing found → `on_request`, never 0**, with a reason (`not_priced`, `on_request_entry`, `anonymous_denied`, `no_identity`). A storefront shows "price on request"; it must never show €0.
        
        Amounts: `unit_price` is per ONE unit of the entry’s `unit`, in `currency`, as a decimal in MAJOR units (19.90) — never minor units/cents — and on the basis `tax_basis` names. `tax_basis` comes from the list’s own column, else from a legacy `tax_included: true` on it, else from the tenant’s `tax_inclusive_default`; `tax_basis_source` says which of the three. Read `unit_price_net`/`unit_price_gross` where you need an unambiguous number.
        
        Tax is never guessed. The market comes from the `X-Revenexx-Market` header (a market CODE) or from `market_id` in the body; with several markets whose rates differ and no signal, the answer is `tax.resolved: false`, `reason: market_required` rather than another market’s VAT. `tax_rate: null` means UNKNOWN, not 0 %.
        
        An item that cannot be priced never fails the call: it comes back on_request with its reason, so one bad line in a cart does not cost the other lines their prices.
        
        One last thing worth knowing before you build on it. This is the most customised surface this app has in the field: pricing is where a tenant's ERP usually has the last word, and a tenant whose prices are computed there does not want this app's resolution order at all. So the route is deliberately shaped to be REPLACED — one required field, no rejection of an item the caller got wrong, an answer that stands on its own — and it is designed to be swapped 1:1 for a custom app through the gateway's capability override. An ERP-priced tenant overrides `prices.resolve` alone: the same path, the same request and the same response, answered by their own service, while every configuration route here (lists, entries, ladders, bulk changes, vocabularies) stays standard and keeps working. That is why the contract below is smaller than the machinery behind it, and why it changes reluctantly.

        Parameters
        ----------
        items : List[PriceResolveItem]
            Items to price, at most 200 per call — a whole cart or a whole product listing in one round trip. The answer holds one entry per item, in this order.
        at : Optional[str]
            The instant every validity window — list and entry — is evaluated at (ISO 8601). Default now. This is how a promo price is previewed before it starts, and it is echoed as `basis.evaluated_at`.
        channel_id : Optional[str]
            Buyer context: the sales channel. Third scope — beats the open lists, loses to contact and organization.
        contact_id : Optional[str]
            Buyer context: the contact this quote is for. The most specific scope — a list naming this contact beats every other list, whatever their priority. Sending it (or organization_id) is also what makes the buyer AUTHENTICATED for `requires_auth` lists and for the tenant’s anonymous_resolve_allowed setting.
        currency : Optional[str]
            ISO 4217 code the quote is wanted in. ONLY lists in this currency are candidates and nothing is ever converted, so a wrong value here is not a rounding difference — it is no price at all. Omit to take the buyer market’s currency, then the tenant’s default_currency; `basis.currency_source` names which applied.
        market_id : Optional[str]
            Buyer context: the market, as a uuid pin for older callers. Prefer the `X-Revenexx-Market` header, which carries a market CODE and is what scopes the visible price lists. The market decides the tax rates AND which per-market settings (rounding, tie-break, anonymous access) apply — with several markets and no signal at all the answer says `tax.resolved: false`, `reason: market_required` rather than quoting another market’s VAT.
        organization_id : Optional[str]
            Buyer context: the organization the buyer belongs to. Second most specific scope; also counts as authenticated.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/resolve'
        api_params = {}
        if items is None:
            raise RevenexxException('Missing required parameter: "items"')


        api_params['at'] = self._normalize_value(at)
        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['items'] = self._normalize_value(items)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['organization_id'] = self._normalize_value(organization_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def prices_vocabularies_list(
        self
    ) -> PriceVocabularyIndex:
        """
        Discovery for the vocabulary routes: the enums this app enforces, each with its name, its title and its description — and deliberately WITHOUT its values, so a UI can cache this one small answer and then fetch only the value sets it actually renders. Names: list-statuses, price-types, tax-bases. Fetch one with GET /prices/vocabularies/{name}; a client holding the qualified pair 'prices.<name>' builds that URL from the pair alone.

        Returns
        -------
        PriceVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PriceVocabularyIndex)


    def prices_vocabularies_get(
        self,
        name: PricesVocabulariesGetName
    ) -> Error:
        """
        One vocabulary in full: every permitted value, each with the title and description a human reads for it and the badge tone a UI colours it with — enough to render a select or a status chip without keeping a private copy of an enum this app enforces. The values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift — a value added to the constraint appears here even before anyone labels it, titled from its own key. Values come back in constraint order, which is the order a select should offer. 'closed' says the set is exhaustive, so a value outside it is stale data rather than a missing label. Answers 404 for an unknown name. Names: list-statuses, price-types, tax-bases.

        Parameters
        ----------
        name : PricesVocabulariesGetName
            The vocabulary name — the part after the dot in the qualified id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/prices/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

