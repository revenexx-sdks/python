from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.payment_status import PaymentStatus;
from ..enums.payment_method_kind import PaymentMethodKind;
from ..enums.payment_dunning_stage import PaymentDunningStage;
from ..models.error import Error;
from ..enums.payments_vocabularies_get_name import PaymentsVocabulariesGetName;

class PaymentsLedger(Service):

    def __init__(self, client) -> None:
        super(PaymentsLedger, self).__init__(client)

    def payments_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        cart_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        status: Optional[PaymentStatus] = None,
        order_ref: Optional[str] = None,
        method_code: Optional[str] = None,
        kind: Optional[PaymentMethodKind] = None,
        provider: Optional[str] = None,
        dunning_stage: Optional[PaymentDunningStage] = None,
        idempotency_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The ledger, paged and filtered — the Payments screen, the reconciliation query and the way an order or a cart finds out what has been paid against it. Every column of the entity is an exact-match filter, which is what makes it useful: `?cart_id=` and `?contact_id=` are indexed, `?status=authorized&kind=self_managed` is the awaiting-payment queue the dunning scan classifies, and `?order_ref=` is the only way to resolve a payment by its external reference. Rows come back in the database's own order, so a newest-first list needs `?order=created_at.desc`. `error_message` is answered from the failure taxonomy rather than echoed out of the column, so what a driver or a PSP actually wrote is never serialized here.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        cart_id : Optional[str]
            The cart a payment pays for. Indexed.
        contact_id : Optional[str]
            The paying customer contact. Indexed.
        status : Optional[PaymentStatus]
            Restrict to one lifecycle state. Indexed.
        order_ref : Optional[str]
            Exact external order reference.
        method_code : Optional[str]
            Exact code of the method the payment was made with.
        kind : Optional[PaymentMethodKind]
            Restrict to self-managed or PSP-backed payments.
        provider : Optional[str]
            Exact PSP code.
        dunning_stage : Optional[PaymentDunningStage]
            Restrict to one dunning stage — what the daily scan wrote.
        idempotency_key : Optional[str]
            Exact idempotency key. Unique per tenant, so this answers at most one row.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if cart_id is not None:
            api_params['cart_id'] = self._normalize_value(cart_id)
        if contact_id is not None:
            api_params['contact_id'] = self._normalize_value(contact_id)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if order_ref is not None:
            api_params['order_ref'] = self._normalize_value(order_ref)
        if method_code is not None:
            api_params['method_code'] = self._normalize_value(method_code)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        if provider is not None:
            api_params['provider'] = self._normalize_value(provider)
        if dunning_stage is not None:
            api_params['dunning_stage'] = self._normalize_value(dunning_stage)
        if idempotency_key is not None:
            api_params['idempotency_key'] = self._normalize_value(idempotency_key)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def payments_create(
        self,
        amount: float,
        method_code: str,
        cart_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        country: Optional[str] = None,
        currency: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        order_ref: Optional[str] = None,
        return_url: Optional[str] = None
    ) -> Error:
        """
        The checkout's write: it opens the ledger row and takes it as far as the named method allows, in one call. A create cannot omit `method_code` and `amount`; every other column is optional or defaulted by the database. Nothing else about the money is the caller's to choose: `kind`, `provider` and `fee_amount` are read off the method that `method_code` names, so a caller can neither pick an acquirer nor discount its own fee. `amount: 0` is legal (free orders); negative is 400. Eligibility is enforced HERE and not only in the checkout UI — the same country and order-value rules POST /payments/methods/eligible applies answer 422 if the method does not apply to this buyer. What comes back depends on the method: a self-managed one (invoice, prepayment) is `authorized` at once with the dunning clock already started, and a PSP one is `captured` or `authorized`, or `requires_action` with `next_action` — the instruction the storefront must carry out, typically a redirect, set at that status and at no other. Send an `idempotency_key` and a repeat of the same call answers 200 with the payment that key already named, unchanged and not re-authorized. What is never stored: the `instrument`, `token` or `card` is handed to the driver in-process and no token or PAN is written to the row.

        Parameters
        ----------
        amount : float
            What the provider is asked to authorize, in `currency`. 0 is legal (a free order) and negative is refused by the handler and by the CHECK behind it. `fee_amount` is recorded beside this and is NOT added to it — a checkout that charges its payment surcharge sends a total that already includes it.
        method_code : str
            The `code` of the payment method this payment was made with, copied at creation. Deliberately a code and not a foreign key: the ledger records what happened and has to outlive the configuration it happened under. It must name a method this tenant has configured; eligibility for the buyer context below is re-checked here, whatever the checkout showed.
        cart_id : Optional[str]
            The cart this payment pays for. Not a foreign key: the payment is a record of what happened and outlives the cart. Indexed, so it is the cheap way to find the payment behind a checkout.
        contact_id : Optional[str]
            The paying customer contact. Not a foreign key — a payment must survive a contact being merged or erased. Indexed.
        country : Optional[str]
            The buyer's ISO 3166-1 alpha-2 country code, for the eligibility check. A method restricted to countries is refused with 422 without it.
        currency : Optional[str]
            ISO 4217 code the amount and the fee are in. The database bounds the length at three characters and nothing else, so lower case is stored as written. Defaults to EUR.
        idempotency_key : Optional[str]
            The caller's own key for this creation attempt. Sending it again answers the SAME payment with 200 instead of creating a second one — which is what makes a retried checkout safe. Unique per tenant, so a filter on it answers at most one row. The replay answers 200, not 201.
        metadata : Optional[Dict[str, Any]]
            Free-form data to keep on the payment. Merged with the keys this app writes itself (`provider_method`, `return_url`, later the cancel/refund reasons), which win on a collision.
        order_ref : Optional[str]
            The external order reference the checkout wrote onto the payment. It is what POST /payments/orders/{order_ref}/capture resolves and the fallback key a PSP webhook is matched on when it carries no transaction id — so an integration that leaves it null gives up both. Free text with no uniqueness: several payments may share one reference.
        return_url : Optional[str]
            Where the PSP sends the buyer back after a redirect or a 3-D Secure challenge. Kept in `metadata.return_url` and handed to the driver — a PSP method that needs a redirect and has none leaves the buyer stranded at the provider.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments'
        api_params = {}
        if amount is None:
            raise RevenexxException('Missing required parameter: "amount"')

        if method_code is None:
            raise RevenexxException('Missing required parameter: "method_code"')


        api_params['amount'] = self._normalize_value(amount)
        api_params['cart_id'] = self._normalize_value(cart_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['country'] = self._normalize_value(country)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['idempotency_key'] = self._normalize_value(idempotency_key)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['method_code'] = self._normalize_value(method_code)
        api_params['order_ref'] = self._normalize_value(order_ref)
        api_params['return_url'] = self._normalize_value(return_url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_dunning_scan(
        self
    ) -> Dict[str, Any]:
        """
        Classifies every unpaid self-managed payment (invoice, prepayment) as on time / reminder due / overdue from payment_reminder_after_days and overdue_after_days, writes the stage and the next due date, and reports PSP payments still waiting on a callback longer than webhook_stale_after_minutes. Pure function of each payment's age, so it is idempotent — it also runs daily as the 'dunning-scan' schedule. It classifies and does not send: a stage change emits payment.updated, and what a reminder looks like is the merchant's workflow.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/dunning/scan'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def payments_errors_redact(
        self,
        apply: Optional[bool] = None,
        limit: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Rows written before the failure taxonomy still store the provider's/runtime's raw text in error_message. API responses never repeat it (the read path projects), but the column is also read directly through Baseline, so it needs rewriting once per tenant. Dry-run by default — reports what it would touch and changes nothing until apply:true. Idempotent: rows already carrying a taxonomy message are skipped.

        Parameters
        ----------
        apply : Optional[bool]
            Write the reclassified values. Defaults to false, which reports what WOULD change and touches nothing.
        limit : Optional[float]
            How many payments to scan, oldest first. Defaults to 500, capped at 5000 — a tenant with more pre-taxonomy rows needs several runs, and re-running is free.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/errors/redact'
        api_params = {}

        api_params['apply'] = self._normalize_value(apply)
        api_params['limit'] = self._normalize_value(limit)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def payments_orders_capture(
        self,
        order_ref: str
    ) -> Error:
        """
        This is the hook the tenant's `auto_capture_policy: 'on_ship'` was written for: fulfilment knows the order it shipped and not the payment ids behind it, so the shipment calls this one route with the reference it already holds and the money for that order is collected in a single request. Resolves payments by their order_ref (the same key the PSP webhooks fall back to), captures every authorized one and reports the rest instead of failing — an order whose payment was already captured is a successful no-op, and a provider that refuses one payment lands in `skipped` rather than failing the call. Note that payments.order_ref is nullable with no foreign key: this route is exactly as good as the reference the checkout writes onto the payment.

        Parameters
        ----------
        order_ref : str
            The external order reference the checkout wrote onto the payment, trimmed before it is resolved. Free text — the example is an invented shape, not a reference any tenant holds, and one no payment carries answers 404.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/orders/{order_ref}/capture'
        api_params = {}
        if order_ref is None:
            raise RevenexxException('Missing required parameter: "order_ref"')

        api_path = api_path.replace('{order_ref}', str(self._normalize_value(order_ref)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_vocabularies_list(
        self
    ) -> Dict[str, Any]:
        """
        The enums this app owns, four of them: statuses, method kinds, fee types and dunning stages. This is the index and carries a name and a title per set and nothing more — the values themselves, with their labels and badge tones, are one call further down at GET /payments/vocabularies/{name}, so a client that only needs to know which sets exist does not pay for all of them. Values come out of the CHECK constraints, so what is served is what the database enforces — a client renders a status this app adds without a release of its own.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def payments_vocabularies_get(
        self,
        name: PaymentsVocabulariesGetName
    ) -> Error:
        """
        One set in full: every value it permits, the label to show for each and the badge tone to render it in, which is what a client needs to draw a status chip without hard-coding this app's enums. The value set is parsed out of the CHECK constraint in schema.json, so what is served IS what the database enforces. Labels are curated on top and can only add words and colour — a permitted value nobody labelled still appears, titled from its own key, which is why `title` and `description` are a locale map on a labelled value and a plain string on an unlabelled one.

        Parameters
        ----------
        name : PaymentsVocabulariesGetName
            Which vocabulary to read. The set is closed: GET /payments/vocabularies lists exactly these.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_webhooks_ingest(
        self,
        provider: str,
        id: Optional[Any] = None,
        request: Optional[Dict[str, Any]] = None,
        verified: Optional[Any] = None
    ) -> Error:
        """
        The sink a PSP callback ends up in, and an inbound ingress endpoint in the sense of ADR-0066: the provider never posts here directly, it posts to webhooks.revenexx.com, which verifies and captures the delivery and dispatches its envelope to this route through the gateway. That indirection is also what makes this the one override point for PSP callback handling — everything a callback does to the ledger happens here and nowhere else, so a deployment that needs a provider's callbacks normalized differently replaces this operation instead of touching the lifecycle routes. Consumes the dispatch envelope from webhooks.revenexx.com: normalizes the provider callback (stripe payment intents + a generic shape), resolves the payment by psp_payment_id or order_ref and moves the ledger. Facts only move forward — provider retries and redeliveries are idempotent no-ops; unverified envelopes are refused.

        Parameters
        ----------
        provider : str
            The catalog provider code whose callback shape to normalize. Anything the normalizer does not recognise is read as the generic {event, psp_payment_id?, order_ref?, error?} envelope rather than refused.
        id : Optional[Any]
            The dispatcher's delivery id. Echoed back as `delivery_id` so a delivery and what the ledger did can be correlated.
        request : Optional[Dict[str, Any]]
            The captured HTTP request as the PSP sent it.
        verified : Optional[Any]
            Whether the ingress verified the callback signature against the provider's `webhook_secret`. An explicit false is refused with 422: an endpoint may run in annotate mode, and the ledger stays sovereign over one that does.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/webhooks/{provider}'
        api_params = {}
        if provider is None:
            raise RevenexxException('Missing required parameter: "provider"')

        api_path = api_path.replace('{provider}', str(self._normalize_value(provider)))

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if request is not None:
            api_params['request'] = self._normalize_value(request)
        if verified is not None:
            api_params['verified'] = self._normalize_value(verified)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_get(
        self,
        id: str
    ) -> Error:
        """
        One ledger row in full: the amount and the fee that were computed at creation, the method code and PSP it was made through, where it stands in the lifecycle, the timestamp of each transition it has been through (`authorized_at`, `captured_at`, `failed_at`, `refunded_at`), the dunning columns the daily scan maintains and, while the buyer still has something to do, `next_action`. This is the call to poll after sending a buyer to a PSP redirect. Two things it does not do: `error_message` is answered from the failure taxonomy and never carries the provider's or the runtime's own words, and there is no route that resolves a payment by `order_ref` — that column is nullable and not unique, so it is a filter on the list (`GET /payments?order_ref=…`) which may legitimately answer several rows.

        Parameters
        ----------
        id : str
            The payment. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_cancel(
        self,
        id: str,
        reason: Optional[str] = None
    ) -> Error:
        """
        Drops the claim before any money has been taken — the abandoned basket, the buyer who never came back from the redirect, the invoice an operator writes off. It is the only transition that starts from three statuses rather than one, because everything short of captured can still be released. A captured payment is not cancellable at all: that is a refund, and the lattice answers 400 rather than pretending. Unlike capture and refund this transition has no time window — the merchant's `capture_expiry_days` and `refund_window_days` do not apply, so a stale authorization can always be released even once it is too old to collect. On a PSP payment the provider is called and the `reason` in the body is passed to it, so it reaches the PSP's own cancellation-reason field as well as being stored under `metadata.cancel_reason`. Cancelling stops the dunning clock: the stage goes back to `none` and the due date is cleared.

        Parameters
        ----------
        id : str
            The payment. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        reason : Optional[str]
            The operator's own words for why. Kept on the payment (`metadata.cancel_reason` / `metadata.refund_reason`) AND handed to the provider's own cancellation or refund reason field, so it is readable in the PSP's dashboard too. Trimmed and cut at 500 characters.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/{id}/cancel'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_capture(
        self,
        id: str
    ) -> Error:
        """
        Collects money that is currently only reserved. It starts from `authorized` and from nothing else — under `auto_capture_policy: 'immediate'` a payment is captured in the same request that created it and never passes through here, so this is the route for the 'manual' and 'on_ship' policies, and POST /payments/orders/{order_ref}/capture is the same operation addressed by the order reference a warehouse actually holds. There is no request body and no amount: the ledger carries one amount and one status, so a capture is the whole authorization or nothing. On a self-managed payment it takes no PSP anywhere near it — it records that an invoice or a prepayment was paid, and stops the dunning clock. Refused with 422 once the authorization is older than the tenant's `capture_expiry_days` (the message carries both numbers), because an expired authorization is declined by the provider anyway and a 422 here is the cheap version of finding out later.

        Parameters
        ----------
        id : str
            The payment. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/{id}/capture'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_confirm(
        self,
        id: str
    ) -> Error:
        """
        The other half of a redirect. POST /payments answered `requires_action` with a `next_action` the storefront carried out — a 3-D Secure step, a wallet approval, a bank login — and this is the call that asks the PSP how it went and writes the answer to the ledger. It starts from `requires_action` and from nothing else, so a payment that already came back authorized needs no confirm and the lattice answers 400 rather than repeating one. `next_action` is cleared by this call whatever the outcome. Where the tenant's `auto_capture_policy` is 'immediate' the money is taken straight after the authorization, in the same request, so a successful confirm can come back `captured` rather than `authorized`; a failed auto-capture does not fail the confirm, because a good authorization is worth more than a tidy status.

        Parameters
        ----------
        id : str
            The payment. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/{id}/confirm'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_refund(
        self,
        id: str,
        reason: Optional[str] = None
    ) -> Error:
        """
        Gives captured money back. It starts from `captured` and from nothing else — money that was only authorized is cancelled, not refunded, and the lattice answers 400 rather than guessing which was meant. All or nothing: the ledger carries one amount and one status, so there is no partial refund and no second one to express — a refunded payment is refunded in full, and a repeat is a 400 because `refunded` is not a status a refund starts from. The `reason` in the body is handed to the driver in the same call, so it reaches the PSP's own refund-reason field rather than being a note only this database ever sees, and it is stored under `metadata.refund_reason`. On a self-managed payment nothing is sent anywhere: it records that the merchant paid the buyer back by their own means. Refused with 422 once the capture is older than the tenant's `refund_window_days` (the message carries both numbers) — past that the provider stops accepting a refund against the transaction and it has to be made by bank transfer.

        Parameters
        ----------
        id : str
            The payment. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        reason : Optional[str]
            The operator's own words for why. Kept on the payment (`metadata.cancel_reason` / `metadata.refund_reason`) AND handed to the provider's own cancellation or refund reason field, so it is readable in the PSP's dashboard too. Trimmed and cut at 500 characters.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/{id}/refund'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

