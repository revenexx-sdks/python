from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.cart_status import CartStatus;
from ..models.error import Error;
from ..enums.cart_merge_strategy import CartMergeStrategy;
from ..models.cart_maintenance_result import CartMaintenanceResult;
from ..models.cart_vocabulary_index import CartVocabularyIndex;
from ..enums.name import Name;

class Carts(Service):

    def __init__(self, client) -> None:
        super(Carts, self).__init__(client)

    def carts_list(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        status: Optional[CartStatus] = None,
        contact_id: Optional[str] = None,
        session_key: Optional[str] = None,
        channel_id: Optional[str] = None,
        currency: Optional[str] = None,
        is_current: Optional[bool] = None,
        item_count: Optional[float] = None,
        subtotal: Optional[float] = None,
        abandoned_at: Optional[str] = None,
        ordered_at: Optional[str] = None,
        order_ref: Optional[str] = None,
        merged_into_cart_id: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        The cart index, and the route a storefront resumes a session with: `?contact_id=…` for a customer's carts, `?session_key=…` for a guest's, and `?is_current=true` alongside one of those two for the single cart carts.activate last marked — this list is the ONLY place that flag can be read back, and on its own the filter selects every current cart in the tenant. Filters are exact equality and never a search, unknown keys are dropped rather than refused, and `filter` echoes what was understood. Each row carries its own stored totals — `item_count` is the sum of the line QUANTITIES, not the number of lines — but never its lines: those are one call per cart. With no filter at all this is every cart the tenant holds, paged, which is a report rather than a session lookup.

        Parameters
        ----------
        id : Optional[str]
            One cart, in list form — the same row carts.get answers, but inside the page envelope.
        name : Optional[str]
            Exact name, not a search: 'Weekly' does not find 'Weekly order'. Useful with contact_id, to resume a named cart a buyer keeps.
        status : Optional[CartStatus]
            By lifecycle status — the abandoned queue, the ordered ones, the merged trail.
        contact_id : Optional[str]
            Every cart of one customer. With multi_cart_enabled this is a list, not a row.
        session_key : Optional[str]
            Every cart of one guest session — what a storefront asks for before anybody logs in, and what carts.claim then hands over.
        channel_id : Optional[str]
            Carts opened in one sales channel.
        currency : Optional[str]
            Carts priced in one currency.
        is_current : Optional[bool]
            The owner's current cart — the flag carts.activate sets, and the only way to read what it wrote. Pair it with contact_id or session_key; on its own it selects every current cart in the tenant.
        item_count : Optional[float]
            Exact total quantity. `?item_count=0` is the one that earns its place: the empty carts.
        subtotal : Optional[float]
            Exact subtotal. Equality only — there is no range form on this route, so this finds `0` and little else.
        abandoned_at : Optional[str]
            Exact instant, not a range. Of little use on its own; `status=abandoned` is the question people actually have.
        ordered_at : Optional[str]
            Exact instant, not a range. `status=ordered` is usually the question.
        order_ref : Optional[str]
            The cart behind an order number — the join order management and support both need.
        merged_into_cart_id : Optional[str]
            Every cart that was merged INTO this one: the other half of the trail, and the answer to "what did this cart absorb".
        created_at : Optional[str]
            Exact instant, not a range: this matches a timestamp to the microsecond, so it is for reproducing a row, not for reporting on a day.
        updated_at : Optional[str]
            Exact instant, not a range. Idleness is the sweep's business, not a filter's.
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

        api_path = '/v1/carts'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if contact_id is not None:
            api_params['contact_id'] = self._normalize_value(contact_id)
        if session_key is not None:
            api_params['session_key'] = self._normalize_value(session_key)
        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if is_current is not None:
            api_params['is_current'] = self._normalize_value(is_current)
        if item_count is not None:
            api_params['item_count'] = self._normalize_value(item_count)
        if subtotal is not None:
            api_params['subtotal'] = self._normalize_value(subtotal)
        if abandoned_at is not None:
            api_params['abandoned_at'] = self._normalize_value(abandoned_at)
        if ordered_at is not None:
            api_params['ordered_at'] = self._normalize_value(ordered_at)
        if order_ref is not None:
            api_params['order_ref'] = self._normalize_value(order_ref)
        if merged_into_cart_id is not None:
            api_params['merged_into_cart_id'] = self._normalize_value(merged_into_cart_id)
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


    def carts_create(
        self,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        is_current: Optional[bool] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        session_key: Optional[str] = None
    ) -> Error:
        """
        Opens an empty cart. The one thing it requires is an OWNER — `contact_id` for a signed-in customer or `session_key` for a guest, never neither: that is a database check on the table, and this route refuses it first with a 400 so the caller gets a sentence rather than a constraint name. Everything else is defaulted: the name 'Cart', currency EUR, status 'active', both totals 0. No column of a cart is unique, so one owner may hold as many carts as they like — unless the tenant's `multi_cart_enabled` is off, in which case a second ACTIVE cart for the same owner answers 409 naming the cart that already exists, because a storefront that hit that wants to fill THAT cart. Send `is_current: true` to have the new cart made current in the same call, which clears the flag on every sibling of the same owner. Lines are added afterwards, one call each or one bulk replace.

        Parameters
        ----------
        channel_id : Optional[str]
            The sales channel this cart is being opened in, as a channel of the channels app. Stored for attribution; nothing in this app reads it.
        contact_id : Optional[str]
            The customer who owns this cart, as a contact of the customers app. Send this OR session_key — a cart with neither owner is refused.
        currency : Optional[str]
            ISO 4217 code the cart is priced in (default EUR). Lines added without a currency inherit it.
        is_current : Optional[bool]
            Make this THE current cart of its owner as it is created — the same thing carts.activate does later, and it clears the flag on every sibling cart of the same owner.
        metadata : Optional[Dict[str, Any]]
            Free-form data the storefront hangs on the cart. Stored and returned verbatim; no key in here is read by this app, and none is indexed.
        name : Optional[str]
            What the buyer calls this cart (default 'Cart'). An empty string is legal and lands on the default.
        session_key : Optional[str]
            The guest session that owns this cart — the key the storefront already keeps in its own session or cookie. Any non-empty string is accepted; this app issues none and parses none, so the example shows a shape and not a format. Send this OR contact_id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts'
        api_params = {}

        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['is_current'] = self._normalize_value(is_current)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['session_key'] = self._normalize_value(session_key)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_claim(
        self,
        contact_id: str,
        session_key: str,
        strategy: Optional[CartMergeStrategy] = None,
        target_cart_id: Optional[str] = None
    ) -> Error:
        """
        The login call, and the one route that turns a guest into a customer: every ACTIVE cart of one session_key is handed to a contact_id, which is what a storefront fires the moment somebody signs in with a basket already filled. There are two ways it can land, and the body picks between them. Without a target_cart_id the session carts are ADOPTED as they stand — same carts, same lines, contact_id set and session_key cleared, nothing copied and nothing closed. With a target_cart_id they are instead folded into that cart, which survives while each session cart is closed as status merged; 'adopted' and 'merged' in the answer say which of the two happened to each one. With a target cart, cart_merge_strategy decides what happens to the target's OWN lines: 'merge' keeps them and folds the session lines in, 'replace' clears them first. 'strategy' overrides it for one call (merge | replace); the answer always echoes which one ran and how many lines a replace removed.

        Parameters
        ----------
        contact_id : str
            The contact taking ownership. Every active cart of that session ends up with this contact — adopted as it stands, or folded into `target_cart_id`.
        session_key : str
            The guest session whose active carts are handed over — the key the storefront keeps in its own session or cookie and has been sending on every anonymous call. This app neither issues nor parses it, so the example shows the shape of an opaque token and not a format anything enforces.
        strategy : Optional[CartMergeStrategy]
            Override the tenant's cart_merge_strategy for this call: 'merge' keeps the target cart's own lines, 'replace' clears them first. Omit to use the setting.
        target_cart_id : Optional[str]
            Merge the session carts into this cart instead of adopting them.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/claim'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        if session_key is None:
            raise RevenexxException('Missing required parameter: "session_key"')


        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['session_key'] = self._normalize_value(session_key)
        api_params['strategy'] = self._normalize_value(strategy)
        api_params['target_cart_id'] = self._normalize_value(target_cart_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_maintenance_run(
        self,
        dry_run: Optional[bool] = None
    ) -> CartMaintenanceResult:
        """
        Two sweeps in one pass. abandon_after_minutes marks active carts that have sat untouched past the window as abandoned (stamping abandoned_at, which nothing else in the platform ever sets — without this the abandonment funnel is empty by construction, not empty because nobody abandons carts). cart_ttl_days / guest_cart_ttl_days then DELETE carts past their retention window, line items included; both default to 0 (never), and an 'ordered' cart is never touched at any setting because it is the source record of a sale. Send dry_run to get the same counts and cart ids while writing nothing. The platform runs this per installed tenant on the schedule; it is idempotent, so calling it by hand between ticks is safe.

        Parameters
        ----------
        dry_run : Optional[bool]
            Report what the sweep WOULD do and write nothing. Worth doing before a first retention run: cart_ttl_days deletes carts and their lines.
        
        Returns
        -------
        CartMaintenanceResult
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/maintenance/run'
        api_params = {}

        api_params['dry_run'] = self._normalize_value(dry_run)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=CartMaintenanceResult)


    def carts_merge(
        self,
        source_cart_id: str,
        target_cart_id: str
    ) -> Error:
        """
        Which of the two carts survives is the whole question, and the answer is the TARGET: the source's lines are COPIED into the target, the target keeps every line it already had, its totals are recomputed, and it is the cart the caller goes on using. Nothing is replaced and nothing is moved — the source keeps its own line rows and is closed with status 'merged' and `merged_into_cart_id` pointing at the target, so a merged cart stays readable as the record of what went where. On the way in, a plain product line with the same product/sku AND the same `unit_price` as a line already in the target adds its quantity to that line; configured and custom lines always land as new ones. Both carts must be active and must differ, and the tenant's line limits are enforced on the target as the copies land (422). Reach for carts.merge_into where the caller holds one cart id and not two.

        Parameters
        ----------
        source_cart_id : str
            The cart being folded in. It must be active, and it does NOT survive as a workspace: its lines are copied into the target, it becomes status merged, and merged_into_cart_id points at the target. Its own lines stay on it as the record of what was moved.
        target_cart_id : str
            The cart that SURVIVES. Must be active; it gains the source's lines (identical product lines at the same price adding up) and its totals are recomputed.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/merge'
        api_params = {}
        if source_cart_id is None:
            raise RevenexxException('Missing required parameter: "source_cart_id"')

        if target_cart_id is None:
            raise RevenexxException('Missing required parameter: "target_cart_id"')


        api_params['source_cart_id'] = self._normalize_value(source_cart_id)
        api_params['target_cart_id'] = self._normalize_value(target_cart_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_vocabularies_list(
        self
    ) -> CartVocabularyIndex:
        """
        Discovery for the vocabulary routes: every enum this app publishes, each as its name, its title and its description and nothing else. The VALUES are deliberately not here — this is the index a client builds a menu from, and one call per vocabulary fills it. Names: io-apply-modes, io-directions, io-entities, io-formats, item-types, statuses. Fetch one with GET /carts/vocabularies/{name}; a client holding the qualified pair 'carts.<name>' builds that URL from the pair alone.

        Returns
        -------
        CartVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=CartVocabularyIndex)


    def carts_vocabularies_get(
        self,
        name: Name
    ) -> Error:
        """
        One vocabulary with its values filled in — every value permitted by the column behind it, each carrying the key the database stores, a human title, a description where one was written and the badge tone a UI should render it in, which is everything a select or a status chip needs from one call. The values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift — a value added to the constraint appears here even before anyone labels it, titled from its own key. Values come back in constraint order, which is the order a select should offer. 'closed' says the set is exhaustive, so a value outside it is stale data rather than a missing label. Names: io-apply-modes, io-directions, io-entities, io-formats, item-types, statuses.

        Parameters
        ----------
        name : Name
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

        api_path = '/v1/carts/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_delete(
        self,
        id: str
    ) -> Error:
        """
        Removes the cart row and, through the `on delete cascade` on `cart_items.cart_id`, every line in it. There is no soft delete and no undo. One status is protected and it is protected permanently: an 'ordered' cart is the source record of a sale — the order carries its id in `cart_id` and the order.placed event records it — so this route refuses it with 400 and there is no flag, no force and no lifecycle route that makes it deletable. Do not go looking for one. 'active', 'abandoned' and 'merged' are all deletable, which is deliberate and is the same set the cart-maintenance sweep removes on a retention window: clearing out abandoned guest carts is the main thing anyone deletes a cart for, and a merged cart's lines were COPIED into the target, which still holds them. What the delete does NOT take with it is the trail: `merged_into_cart_id` is a plain uuid column and not a foreign key, so deleting a cart that other carts were merged INTO leaves those carts pointing at a row that no longer exists, and nothing refuses the delete or clears the pointer — the retention sweep does the same, so this is a property of the column and not of this route. For a cart a buyer simply walked away from, carts.abandon keeps the row and the funnel; for deleting on a retention window, the cart-maintenance sweep does it per market and can be asked first with `dry_run`.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_get(
        self,
        id: str
    ) -> Error:
        """
        One cart with its owner, its totals and its lifecycle stamps — and none of its lines: those are a separate call (`GET /carts/{cart_id}/items`), because a cart row is small and a filled cart is not. The two totals are derived and stored, never taken from a caller: `item_count` is the sum of the line QUANTITIES rather than the number of lines (two lines of five pieces answer 10, not 2) and `subtotal` the sum of the line totals, net of shipping and tax; both are recomputed after every line write. `status` says what may still be done — only an 'active' cart accepts a write of any kind, 'abandoned' is the one reversible ending, and a 'merged' cart carries `merged_into_cart_id`, which is the trail to the cart its lines were copied into.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_update(
        self,
        id: str,
        channel_id: Optional[str] = None,
        currency: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None
    ) -> Error:
        """
        The four columns a cart's own editing screen owns, and only those: `name`, `currency`, `channel_id` and `metadata`. Everything else about a cart is either derived or a lifecycle move, and both are deliberately out of reach here — `item_count` and `subtotal` are recomputed from the lines, `status` travels through the action routes (activate, abandon, reopen, order, merge) so that every transition is guarded, and `market_id` is the platform's scope on the row rather than a column this app writes. A payload carrying none of the four answers 400 rather than storing nothing quietly, so a caller never believes an ignored field was saved. The owner is not updatable either: a guest cart becomes a customer's through carts.claim.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        channel_id : Optional[str]
            Move the cart to another sales channel.
        currency : Optional[str]
            ISO 4217 code. Changes what NEW lines inherit; lines already in the cart keep the currency they were added with.
        metadata : Optional[Dict[str, Any]]
            Free-form data the storefront hangs on the cart. Stored and returned verbatim; no key in here is read by this app, and none is indexed.
        name : Optional[str]
            Rename the cart. Unlike on create, this is written verbatim — `null` and `''` are refused by the database.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_abandon(
        self,
        id: str
    ) -> Error:
        """
        The by-hand half of the abandonment funnel: an active cart becomes 'abandoned', `abandoned_at` is stamped, and `is_current` is cleared — so its owner is left with no current cart until another one is activated. Nothing else in the platform writes `abandoned_at`; the only other writer is the cart-maintenance sweep, which does exactly this once a cart has sat untouched past the market's `abandon_after_minutes`. This is the one reversible ending: the lines are untouched throughout and carts.reopen takes the cart back. Only an active cart can be abandoned — an ordered or merged cart is already finished and answers 400 naming the status it actually holds.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}/abandon'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_activate(
        self,
        id: str
    ) -> Error:
        """
        Activate writes exactly one thing: `is_current` on this cart, cleared on every other cart of the same owner (the same contact_id, or the same session_key). It does NOT change the status — an active cart stays active, and only an active cart may be made current. Read it back with `GET /carts?is_current=true` plus the owner: that filter is the only way to see what this route wrote, and a storefront resuming a session is its main caller. The flag is cleared again by abandoning, ordering or merging the cart, so an owner can legitimately have no current cart at all.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}/activate'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_merge_into(
        self,
        id: str,
        target_cart_id: str
    ) -> Error:
        """
        Identical to carts.merge, with the SOURCE taken from the path — which is what makes the merge reachable from anything holding one cart and only one: a Cockpit row action, a detail page, a storefront session. The cart in the path is therefore the one that ends: its lines are copied into the `target_cart_id` named in the body, that target keeps its own lines and survives, and the path cart is closed with status 'merged' and `merged_into_cart_id` pointing at it. Getting the two the wrong way round is the mistake this route exists to make hard, so read the path id as "the cart I am giving away". Both carts must be active and must differ.

        Parameters
        ----------
        id : str
            The SOURCE cart — the one whose lines move and which becomes status merged.
        target_cart_id : str
            Receiving cart (must be active). The cart in the path is the source and becomes status merged.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}/merge-into'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if target_cart_id is None:
            raise RevenexxException('Missing required parameter: "target_cart_id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['target_cart_id'] = self._normalize_value(target_cart_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_order(
        self,
        id: str,
        order_ref: Optional[str] = None
    ) -> Error:
        """
        The hand-over to order management, and the end of the cart as a workspace: an ACTIVE cart becomes 'ordered', ordered_at is stamped, and the order_ref the call carries — order management's own number for the order this cart became — is stored on the cart, which is what lets anyone filter their way from an order number back to the cart behind it. Nothing moves out of 'ordered' afterwards, and no route will delete it. The conversion applies the two tenant decisions a cart cannot make for itself. price_snapshot_mode (snapshot | live) settles which of a line's two prices is charged — the snapshot the buyer was shown, or the current unit_price — and the cart's subtotal is rewritten to match, so cart and order can never disagree; 'pricing' reports the mode, the lines it rewrote and the subtotal on both sides. convert_reserves_stock (never | request | require) decides whether inventories is asked to hold the lines; at 'require' a refusal answers 409 and the cart stays active and unchanged. The reservation is attempted BEFORE anything is written.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        order_ref : Optional[str]
            The order number this cart becomes, in order management's own numbering. Stored on the cart — filtering on it is how anyone gets from an order back to the cart behind it — and it is also the reference the stock reservation is booked under. Omit it and the cart id is used for the reservation instead.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}/order'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_reopen(
        self,
        id: str
    ) -> Error:
        """
        Takes an abandoned cart back to 'active' with its lines exactly as they were — what a storefront calls when a buyer follows a recovery mail, and the way out of the 400 a write gets on a cart the maintenance sweep closed while nobody was looking. It also CLEARS `abandoned_at`, so a cart that was abandoned and reopened leaves nothing behind in the funnel: the funnel counts carts that are still abandoned, not carts that ever were. It does not restore `is_current` — a reopened cart is active but not current until carts.activate says so. Only an abandoned cart may be reopened; 'ordered' and 'merged' are final and answer 400 naming the status the cart holds.

        Parameters
        ----------
        id : str
            The cart, by its id — the `id` every cart answer carries. A uuid: the data plane casts the segment, so a code or a slug is refused before the cart is looked up.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{id}/reopen'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

