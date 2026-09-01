from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.resource_type import ResourceType;
from ..models.error import Error;
from ..enums.scope import Scope;
from ..enums.reason import Reason;
from ..enums.message_class import MessageClass;
from ..enums.whatsapp_category import WhatsappCategory;

class Messaging(Service):

    def __init__(self, client) -> None:
        super(Messaging, self).__init__(client)

    def audit_index(
        self,
        resource_type: Optional[ResourceType] = None,
        resource_id: Optional[str] = None,
        subject: Optional[str] = None,
        limit: Optional[float] = None
    ) -> Error:
        """
        Filterable by `resource_type`, `resource_id` and `subject` — the last one
        being the human-readable name a row was recorded under (a template's key,
        a layout's name), which is what an operator has to hand six weeks later
        when the id means nothing to them.
        
        There is no write route and no delete route: an append-only log with an
        editor is a log that says whatever the last editor wanted.

        Parameters
        ----------
        resource_type : Optional[ResourceType]
            
        resource_id : Optional[str]
            
        subject : Optional[str]
            
        limit : Optional[float]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/audit'
        api_params = {}

        if resource_type is not None:
            api_params['resource_type'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resource_id'] = self._normalize_value(resource_id)
        if subject is not None:
            api_params['subject'] = self._normalize_value(subject)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def binding_index(
        self,
        event_topic: Optional[str] = None
    ) -> Error:
        """
        `?event_topic=` narrows to one topic, which is the question worth asking
        of this list: "what does this event actually do".

        Parameters
        ----------
        event_topic : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/bindings'
        api_params = {}

        if event_topic is not None:
            api_params['event_topic'] = self._normalize_value(event_topic)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def binding_store(
        self,
        channel: str,
        event_topic: str,
        recipient: str,
        template_key: str,
        enabled: Optional[bool] = None,
        fallback_order: Optional[float] = None,
        locale: Optional[str] = None
    ) -> Error:
        """
        `recipient` is a template, not an address: `{{ customer.email }}` is
        rendered against the event payload when the event arrives, which is the
        only way one binding can serve every customer. An event that renders it
        empty is skipped and logged rather than sent to nobody.
        
        `locale` is what the OPERATOR said this route speaks, and it outranks the
        tenant's default. Leave it null when nobody has made that decision, so
        that the recipient's own language is still allowed to decide.

        Parameters
        ----------
        channel : str
            
        event_topic : str
            
        recipient : str
            
        template_key : str
            
        enabled : Optional[bool]
            
        fallback_order : Optional[float]
            
        locale : Optional[str]
            Nullable: a binding's locale is what the OPERATOR said this
            route speaks, and it outranks the tenant's own default
            (LocaleResolver). "No opinion" has to be expressible, or a route
            nobody made a language decision about silently makes one.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/bindings'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        if event_topic is None:
            raise RevenexxException('Missing required parameter: "event_topic"')

        if recipient is None:
            raise RevenexxException('Missing required parameter: "recipient"')

        if template_key is None:
            raise RevenexxException('Missing required parameter: "template_key"')


        api_params['channel'] = self._normalize_value(channel)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['event_topic'] = self._normalize_value(event_topic)
        if fallback_order is not None:
            api_params['fallback_order'] = self._normalize_value(fallback_order)
        api_params['locale'] = self._normalize_value(locale)
        api_params['recipient'] = self._normalize_value(recipient)
        api_params['template_key'] = self._normalize_value(template_key)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def binding_destroy(
        self,
        id: str
    ) -> Error:
        """
        The event it answered goes back to doing nothing. Prefer `enabled: false`
        when the intent is to pause rather than to forget.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/bindings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def binding_show(
        self,
        id: str
    ) -> Error:
        """
        404 for a binding belonging to another tenant, not 403 — an id that
        answered differently would say whether it exists.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/bindings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def binding_update_patch(
        self,
        id: str,
        channel: Optional[str] = None,
        enabled: Optional[bool] = None,
        event_topic: Optional[str] = None,
        fallback_order: Optional[float] = None,
        locale: Optional[str] = None,
        recipient: Optional[str] = None,
        template_key: Optional[str] = None
    ) -> Error:
        """
        Every field is optional; only what is sent is written. `enabled: false`
        is how a binding is taken out of service without losing what it said —
        the alternative is deleting it and typing the payload path back in
        correctly from memory later.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        id : str
            
        channel : Optional[str]
            
        enabled : Optional[bool]
            
        event_topic : Optional[str]
            
        fallback_order : Optional[float]
            
        locale : Optional[str]
            Nullable: a binding's locale is what the OPERATOR said this
            route speaks, and it outranks the tenant's own default
            (LocaleResolver). "No opinion" has to be expressible, or a route
            nobody made a language decision about silently makes one.
        recipient : Optional[str]
            
        template_key : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/bindings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if channel is not None:
            api_params['channel'] = self._normalize_value(channel)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if event_topic is not None:
            api_params['event_topic'] = self._normalize_value(event_topic)
        if fallback_order is not None:
            api_params['fallback_order'] = self._normalize_value(fallback_order)
        api_params['locale'] = self._normalize_value(locale)
        if recipient is not None:
            api_params['recipient'] = self._normalize_value(recipient)
        if template_key is not None:
            api_params['template_key'] = self._normalize_value(template_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def binding_update(
        self,
        id: str,
        channel: Optional[str] = None,
        enabled: Optional[bool] = None,
        event_topic: Optional[str] = None,
        fallback_order: Optional[float] = None,
        locale: Optional[str] = None,
        recipient: Optional[str] = None,
        template_key: Optional[str] = None
    ) -> Error:
        """
        Every field is optional; only what is sent is written. `enabled: false`
        is how a binding is taken out of service without losing what it said —
        the alternative is deleting it and typing the payload path back in
        correctly from memory later.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        id : str
            
        channel : Optional[str]
            
        enabled : Optional[bool]
            
        event_topic : Optional[str]
            
        fallback_order : Optional[float]
            
        locale : Optional[str]
            Nullable: a binding's locale is what the OPERATOR said this
            route speaks, and it outranks the tenant's own default
            (LocaleResolver). "No opinion" has to be expressible, or a route
            nobody made a language decision about silently makes one.
        recipient : Optional[str]
            
        template_key : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/bindings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if channel is not None:
            api_params['channel'] = self._normalize_value(channel)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if event_topic is not None:
            api_params['event_topic'] = self._normalize_value(event_topic)
        if fallback_order is not None:
            api_params['fallback_order'] = self._normalize_value(fallback_order)
        api_params['locale'] = self._normalize_value(locale)
        if recipient is not None:
            api_params['recipient'] = self._normalize_value(recipient)
        if template_key is not None:
            api_params['template_key'] = self._normalize_value(template_key)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def channel_credential_index(
        self,
        market: Optional[str] = None,
        markets: Optional[str] = None
    ) -> Error:
        """
        Answers per channel with: which fields the chosen provider wants and
        which of them are SET (never their values — secrets go in and do not come
        back), which markets hold an override, which providers this build offers,
        whether the deployment has the channel switched on at all, the URL to
        paste into the provider's own console so bounces and opens come back, and
        whether callbacks are actually arriving.
        
        Admin tier on the read as well as the write: the identifiers alone —
        which Twilio account, which sender number — are more than a read-only
        operator has reason to see, and the webhook URL served here contains the
        tenant's callback token.

        Parameters
        ----------
        market : Optional[str]
            Which market's credentials this call is about. Absent means the GLOBAL bag — what every
            send used before markets reached this path, and what a market with no override of its own
            still uses.
            
            Lowercase, opening with a letter, 63 characters at most (Baseline's market slug rule,
            mirrored exactly). A code that does not match is refused with 422 rather than read as
            "no market": on the write paths, silently falling back to global would have an operator
            point every market's traffic at one market's provider while looking at a screen that said
            they had not.
        markets : Optional[str]
            Set to `all` to get every market's credentials in one answer: each channel gains an
            `overrides` object keyed by market code, holding that market's own resolved view of the
            channel — its provider, which of that provider's fields are set, its callback URL, and
            whether callbacks are arriving. Only markets with credentials of their OWN appear; a market
            that inherits has nothing to add.
            
            The channel's top-level entry is the GLOBAL one whenever this is set, and `?market=` is
            ignored: `all` is not a market to resolve against, and honouring both would leave the
            base entry meaning something different depending on a header.
            
            The override entries carry no `providers` catalogue, `enabled` flag or `markets` list.
            Those are properties of the channel, identical in every market, and repeating
            twenty-six providers' field specifications per market would be most of the response.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/channel-credentials'
        api_params = {}

        if market is not None:
            api_params['market'] = self._normalize_value(market)
        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def channel_credential_destroy(
        self,
        channel: str,
        market: Optional[str] = None
    ) -> Error:
        """
        With `?market=`, only that market's override goes and the global
        credentials stand — the market then sends over the global provider again,
        which is what it did before anybody configured it. Without a market the
        channel goes entirely, overrides and all: a caller asking for a channel
        to hold no credentials means all of them.
        
        204 whether or not anything was there. The caller wants this channel to
        hold no credentials, and it does.

        Parameters
        ----------
        channel : str
            
        market : Optional[str]
            Which market's credentials this call is about. Absent means the GLOBAL bag — what every
            send used before markets reached this path, and what a market with no override of its own
            still uses.
            
            Lowercase, opening with a letter, 63 characters at most (Baseline's market slug rule,
            mirrored exactly). A code that does not match is refused with 422 rather than read as
            "no market": on the write paths, silently falling back to global would have an operator
            point every market's traffic at one market's provider while looking at a screen that said
            they had not.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/channel-credentials/{channel}'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        api_path = api_path.replace('{channel}', str(self._normalize_value(channel)))

        if market is not None:
            api_params['market'] = self._normalize_value(market)

        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def channel_credential_update_patch(
        self,
        channel: str,
        market: Optional[str] = None,
        driver: Optional[str] = None
    ) -> Error:
        """
        A PATCH in spirit whichever verb is used: only the fields present in the
        body are written, and the answer says which of them actually CHANGED, so
        a form that resent everything it had on screen does not report a change
        that did not happen.
        
        Three refusals, all 422 and all deliberate rather than ignored. A field
        the channel's provider does not have (`unknown_credential_field`) — a
        typo sitting in the bag looking like configuration fails later with a
        message about a MISSING field the operator can see they filled in. A
        field the platform issues (`managed_credential`) — ignoring it would have
        the caller believe they set something. A channel with nothing to
        configure (`channel_not_configurable`), which is push: its VAPID keypair
        is generated at provisioning, and pasting a new one would orphan every
        browser registration the tenant has collected.
        
        Switching provider is `driver`, and the fields in the same request are
        validated against the provider being switched TO — validating Postmark's
        key against Mailgun's field list is how a switch loses everything the
        operator just typed.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        channel : str
            
        market : Optional[str]
            Which market's credentials this call is about. Absent means the GLOBAL bag — what every
            send used before markets reached this path, and what a market with no override of its own
            still uses.
            
            Lowercase, opening with a letter, 63 characters at most (Baseline's market slug rule,
            mirrored exactly). A code that does not match is refused with 422 rather than read as
            "no market": on the write paths, silently falling back to global would have an operator
            point every market's traffic at one market's provider while looking at a screen that said
            they had not.
        driver : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/channel-credentials/{channel}'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        api_path = api_path.replace('{channel}', str(self._normalize_value(channel)))

        if market is not None:
            api_params['market'] = self._normalize_value(market)
        api_params['driver'] = self._normalize_value(driver)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def channel_credential_update(
        self,
        channel: str,
        market: Optional[str] = None,
        driver: Optional[str] = None
    ) -> Error:
        """
        A PATCH in spirit whichever verb is used: only the fields present in the
        body are written, and the answer says which of them actually CHANGED, so
        a form that resent everything it had on screen does not report a change
        that did not happen.
        
        Three refusals, all 422 and all deliberate rather than ignored. A field
        the channel's provider does not have (`unknown_credential_field`) — a
        typo sitting in the bag looking like configuration fails later with a
        message about a MISSING field the operator can see they filled in. A
        field the platform issues (`managed_credential`) — ignoring it would have
        the caller believe they set something. A channel with nothing to
        configure (`channel_not_configurable`), which is push: its VAPID keypair
        is generated at provisioning, and pasting a new one would orphan every
        browser registration the tenant has collected.
        
        Switching provider is `driver`, and the fields in the same request are
        validated against the provider being switched TO — validating Postmark's
        key against Mailgun's field list is how a switch loses everything the
        operator just typed.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        channel : str
            
        market : Optional[str]
            Which market's credentials this call is about. Absent means the GLOBAL bag — what every
            send used before markets reached this path, and what a market with no override of its own
            still uses.
            
            Lowercase, opening with a letter, 63 characters at most (Baseline's market slug rule,
            mirrored exactly). A code that does not match is refused with 422 rather than read as
            "no market": on the write paths, silently falling back to global would have an operator
            point every market's traffic at one market's provider while looking at a screen that said
            they had not.
        driver : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/channel-credentials/{channel}'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        api_path = api_path.replace('{channel}', str(self._normalize_value(channel)))

        if market is not None:
            api_params['market'] = self._normalize_value(market)
        api_params['driver'] = self._normalize_value(driver)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def channel_credential_verify(
        self,
        channel: str,
        market: Optional[str] = None
    ) -> Error:
        """
        The one thing that turns this screen from a form into a tool. Credentials
        that only fail at send time cost a customer their first order
        confirmation, and by then nobody connects the failure to the afternoon
        somebody pasted a key with a trailing space.
        
        **Always 200.** The answer is `{ok, message}` in the body, including when
        the credentials are wrong: the REQUEST was fine, the credentials are not,
        and a 4xx here would have the cockpit's own error handling swallow the
        one sentence worth reading. A channel that asks for no credentials at all
        (push, in-app) answers `ok: true` — "nothing to verify" is a finished
        check, not a failed one, and reporting it as an error painted a channel
        that has worked since provisioning in the same red as a wrong token.

        Parameters
        ----------
        channel : str
            
        market : Optional[str]
            Which market's credentials this call is about. Absent means the GLOBAL bag — what every
            send used before markets reached this path, and what a market with no override of its own
            still uses.
            
            Lowercase, opening with a letter, 63 characters at most (Baseline's market slug rule,
            mirrored exactly). A code that does not match is refused with 422 rather than read as
            "no market": on the write paths, silently falling back to global would have an operator
            point every market's traffic at one market's provider while looking at a screen that said
            they had not.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/channel-credentials/{channel}/verify'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        api_path = api_path.replace('{channel}', str(self._normalize_value(channel)))

        if market is not None:
            api_params['market'] = self._normalize_value(market)

        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def channel_index(
        self
    ) -> Error:
        """
        Each entry says whether the channel is switched on and which provider
        carries it by default. A channel that is off will refuse a send, so a UI
        that offers a channel picker should build it from this rather than from a
        list of its own — a channel added to the service then appears without a
        release of the client.

        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/channels'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def config_show(
        self
    ) -> Error:
        """
        A tenant that was never provisioned has no row and still gets an answer:
        an empty shape rather than a 404, so the Cockpit's panels open on
        editable blanks instead of an error.
        
        `meta.push_public_key` is the VAPID public key, and only the public one.
        A storefront cannot call `PushManager.subscribe()` without it, so it has
        to leave the service; the private half and every provider secret stay
        hidden on the model, where they are protected on every route rather than
        on this one.

        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/config'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def config_update_patch(
        self,
        default_locale: Optional[str] = None,
        defaults: Optional[List[str]] = None,
        product: Optional[str] = None,
        quiet_hours: Optional[List[str]] = None,
        support_email: Optional[str] = None
    ) -> Error:
        """
        Reaches every message this tenant sends, including templates saved months
        ago — content placeholders resolve at send time, not at save time — which
        is why writing is admin tier while reading is not.
        
        Two refusals worth knowing about. `defaults.brand` is 422, not ignored:
        the letterhead moved to /v1/layouts when a tenant gained more than one of
        them, and a letterhead edit that appears to save and changes nothing is
        the worst of the three possible behaviours. A half-written `quiet_hours`
        is 422 as well — a tenant that typed a start and forgot the end has an
        opinion about when not to message people, and silently sending through
        the night is the one answer that is definitely wrong.
        
        Provider credentials cannot be written here. That path is
        /v1/channel-credentials, so the one route that handles secrets stays the
        one that was built for it.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        default_locale : Optional[str]
            The house language — step 4 of the send path's resolution order,
            reached only when neither the caller, the event payload nor the
            binding said anything. A column of its own and not a key in
            `defaults` below, because everything in that bag is merged into
            the render model: a `locale` key there would start filling
            `{{ locale }}` inside template bodies, which is a routing
            decision leaking into content.
        defaults : Optional[List[str]]
            The saved modules live in here. The shape is the Cockpit's
            contract and is not pinned down further: adding a block type
            would otherwise be a service deploy. The one key that IS pinned
            down is `brand`, because it moved out — and it is refused with a
            closure rather than a `defaults.brand` rule, since a nested rule
            makes the validator drop the parent and quietly discard every
            other key in the bag along with it.
        product : Optional[str]
            
        quiet_hours : Optional[List[str]]
            
        support_email : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/config'
        api_params = {}

        api_params['default_locale'] = self._normalize_value(default_locale)
        api_params['defaults'] = self._normalize_value(defaults)
        api_params['product'] = self._normalize_value(product)
        api_params['quiet_hours'] = self._normalize_value(quiet_hours)
        api_params['support_email'] = self._normalize_value(support_email)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def config_update(
        self,
        default_locale: Optional[str] = None,
        defaults: Optional[List[str]] = None,
        product: Optional[str] = None,
        quiet_hours: Optional[List[str]] = None,
        support_email: Optional[str] = None
    ) -> Error:
        """
        Reaches every message this tenant sends, including templates saved months
        ago — content placeholders resolve at send time, not at save time — which
        is why writing is admin tier while reading is not.
        
        Two refusals worth knowing about. `defaults.brand` is 422, not ignored:
        the letterhead moved to /v1/layouts when a tenant gained more than one of
        them, and a letterhead edit that appears to save and changes nothing is
        the worst of the three possible behaviours. A half-written `quiet_hours`
        is 422 as well — a tenant that typed a start and forgot the end has an
        opinion about when not to message people, and silently sending through
        the night is the one answer that is definitely wrong.
        
        Provider credentials cannot be written here. That path is
        /v1/channel-credentials, so the one route that handles secrets stays the
        one that was built for it.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        default_locale : Optional[str]
            The house language — step 4 of the send path's resolution order,
            reached only when neither the caller, the event payload nor the
            binding said anything. A column of its own and not a key in
            `defaults` below, because everything in that bag is merged into
            the render model: a `locale` key there would start filling
            `{{ locale }}` inside template bodies, which is a routing
            decision leaking into content.
        defaults : Optional[List[str]]
            The saved modules live in here. The shape is the Cockpit's
            contract and is not pinned down further: adding a block type
            would otherwise be a service deploy. The one key that IS pinned
            down is `brand`, because it moved out — and it is refused with a
            closure rather than a `defaults.brand` rule, since a nested rule
            makes the validator drop the parent and quietly discard every
            other key in the bag along with it.
        product : Optional[str]
            
        quiet_hours : Optional[List[str]]
            
        support_email : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/config'
        api_params = {}

        api_params['default_locale'] = self._normalize_value(default_locale)
        api_params['defaults'] = self._normalize_value(defaults)
        api_params['product'] = self._normalize_value(product)
        api_params['quiet_hours'] = self._normalize_value(quiet_hours)
        api_params['support_email'] = self._normalize_value(support_email)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def layout_index(
        self,
        markets: Optional[str] = None
    ) -> Error:
        """
        The order is the list's purpose: it is a picker, and the entry most
        templates are actually on belongs at the top of it.
        
        Market-scoped as a browsing filter — see the parameters. `GET /layouts/{id}`
        deliberately is not: somebody holding an id may read it.

        Parameters
        ----------
        markets : Optional[str]
            Set to `all` for the unscoped read: every row whatever its markets, ignoring the `X-Revenexx-Market` header. The deliberate admin case, spelled in the query string so it is asked for rather than fallen into. No other value has any effect.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/layouts'
        api_params = {}

        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def layout_store(
        self
    ) -> Error:
        """
        A tenant's FIRST layout becomes the default whatever the request says: a
        tenant with no default cannot compile a template that does not name one.
        
        The default may hold neither a validity window nor `enabled: false`, and
        asking for both in one request is refused with 422
        `layout_default_always_in_force`. There is no fallback behind the default
        — every template that names no layout is framed by it — so a window set
        today would take a tenant's whole letterhead away on a morning months
        from now, with nobody left who remembers typing the date.

        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/layouts'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def layout_destroy(
        self,
        id: str
    ) -> Error:
        """
        Answers 200 with a body rather than the 204 the other resources use: the
        count of reassigned templates is the part an operator needs, and a
        deletion that silently moved eleven templates onto another letterhead is
        one they would only discover from the next mail that went out.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/layouts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def layout_show(
        self,
        id: str
    ) -> Error:
        """
        Not market-filtered, deliberately: market scoping is a browsing concern,
        and somebody holding an id may read the row. A template pinned to a
        layout keeps mailing on it whatever market the reader is looking at.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/layouts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def layout_update(
        self,
        id: str
    ) -> Error:
        """
        The change reaches every template on this layout, including ones saved
        months ago and never opened since — which is exactly the change nobody
        remembers making when the mails start looking wrong. It is audited for
        that reason, and only when something actually changed: an audit line on
        every save teaches its readers to ignore the log.
        
        Two 422s. Clearing `is_default` on the current default is
        `layout_default_required` — promoting another layout is the operation
        that exists for this, and it clears this one as a side effect, which is
        the only way the count stays at exactly one. Giving the default a
        validity window or switching it off is `layout_default_always_in_force`,
        and the check is made of the OUTCOME, so promoting a layout and dating it
        in the same request is caught.
        
        The structural half of a layout — colours, width, font — is baked into
        each template's compiled body, so templates already on it keep the old
        one until they are recompiled.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/layouts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('patch', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def library_index(
        self,
        channel: Optional[str] = None,
        locale: Optional[str] = None
    ) -> Error:
        """
        What the Cockpit's "start from a template" gallery is built from. These
        are not the tenant's rows and cannot be edited here: provisioning clones
        them into `/v1/templates`, and it is the clone that a tenant owns.

        Parameters
        ----------
        channel : Optional[str]
            
        locale : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/library'
        api_params = {}

        if channel is not None:
            api_params['channel'] = self._normalize_value(channel)
        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def message_index(
        self,
        channel: Optional[str] = None,
        status: Optional[str] = None
    ) -> Error:
        """
        `?channel=` and `?status=` narrow it; `?limit=` is clamped to 200 and
        defaults to 50. `?channel=inapp` is the tenant's in-app inbox — the
        Message row IS the inbox item, so there is no second store for it.
        
        Rows are subject to the deployment's retention window and to erasure
        requests, so this is not an archive.

        Parameters
        ----------
        channel : Optional[str]
            
        status : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/messages'
        api_params = {}

        if channel is not None:
            api_params['channel'] = self._normalize_value(channel)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def message_show(
        self,
        id: str
    ) -> Error:
        """
        Carries the render model it was sent with, so "why did this mail say
             * that" is answerable after the fact. That is also why the row is personal
        data and why it can be erased — see POST /v1/privacy/erasures.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/messages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def send_preview(
        self,
        channel: str,
        template: str,
        data: Optional[Dict[str, Any]] = None,
        locale: Optional[str] = None
    ) -> Error:
        """
        Answers with the resolved subject, HTML and text exactly as a real send
        would produce them, so an editor can show a faithful preview without a
        message row, a provider call or a suppression check.
        
        Takes no `market`, deliberately: rendering picks no provider, so there is
        nothing here for a market to change. Nor `send_at`, `draft` or
        `attachments` — all of them are properties of a dispatch, not of a render.

        Parameters
        ----------
        channel : str
            
        template : str
            
        data : Optional[Dict[str, Any]]
            The render model: a free map of variable name to value, resolved against the template's
            placeholders. Values may be strings, numbers, booleans, or nested objects and arrays —
            `{{ order.number }}` reads a nested one.
            
            Not the only source. A tenant's `defaults`, its layout, and the template's own
            `variable_defaults` are merged underneath, so a placeholder an event did not carry can
            still resolve. Anything named here wins over all of them.
        locale : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/preview'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        if template is None:
            raise RevenexxException('Missing required parameter: "template"')


        api_params['channel'] = self._normalize_value(channel)
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        api_params['locale'] = self._normalize_value(locale)
        api_params['template'] = self._normalize_value(template)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def erasure_store(
        self,
        address: str,
        channel: str
    ) -> Error:
        """
        Per (channel, address), because an address is channel-shaped and the rows
        it has to line up with are keyed that way. Matching is done on the
        normalised form on both sides, so a request for `ada@acme.test` finds a
        log written for `Ada@Acme.test` — an erasure that misses on
        capitalisation is an erasure that did not happen and reports success.
        
        Message rows and unsubscribe tokens are DELETED. Suppressions are KEPT
        with the clear-text address nulled: matching runs on a keyed hash, so the
        row can still block and can no longer identify. Deleting it instead is
        the obvious reading of "erase everything about them", and it is the
        reading that mails a dead address again next week — or mails somebody who
        complained, which is how a sending domain gets blocked.
        
        Answers with the counts, `suppressions_kept` among them, so the design is
        stated in the response rather than only in this paragraph.

        Parameters
        ----------
        address : str
            
        channel : str
            Per (channel, address), not per address: an address is
            channel-shaped, and the suppression and token rows it has to line
            up with are keyed that way.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/privacy/erasures'
        api_params = {}
        if address is None:
            raise RevenexxException('Missing required parameter: "address"')

        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')


        api_params['address'] = self._normalize_value(address)
        api_params['channel'] = self._normalize_value(channel)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def push_subscription_destroy(
        self,
        endpoint: str
    ) -> Error:
        """
        By endpoint and not by id, because the browser knows its endpoint and has
        never seen our id — this is called from a service worker reacting to
        `pushsubscriptionchange`, or from a "turn off notifications" button.

        Parameters
        ----------
        endpoint : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/push/subscriptions'
        api_params = {}
        if endpoint is None:
            raise RevenexxException('Missing required parameter: "endpoint"')


        api_params['endpoint'] = self._normalize_value(endpoint)

        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def push_subscription_index(
        self,
        subscriber_id: str
    ) -> Error:
        """
        `subscriber_id` is required: this is not a list of everybody, and there
        is no route that is. The caller is a storefront acting for one visitor
        and has no business enumerating the rest.
        
        The client key material is never returned — see the `$hidden` list on the
        model. A registration that can be read back is a registration somebody
        else can push with.

        Parameters
        ----------
        subscriber_id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/push/subscriptions'
        api_params = {}
        if subscriber_id is None:
            raise RevenexxException('Missing required parameter: "subscriber_id"')


        api_params['subscriber_id'] = self._normalize_value(subscriber_id)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def push_subscription_store(
        self,
        endpoint: str,
        keys: Dict[str, Any],
        subscriber_id: str,
        user_agent: Optional[str] = None
    ) -> Error:
        """
        Send what `PushManager.subscribe()` handed back — the endpoint and the
        two keys — plus the id you know that person by. The VAPID public key the
        browser needs to produce it comes from `GET /v1/config`
        (`meta.push_public_key`).
        
        **Idempotent by endpoint**, and the two statuses say which happened: 201
        for a browser seen for the first time, 200 for one already registered. A
        browser calls `subscribe()` on every page load and hands back the same
        endpoint each time; treating that as a new device would give one laptop a
        thousand rows and push to it a thousand times.

        Parameters
        ----------
        endpoint : str
            
        keys : Dict[str, Any]
            
        subscriber_id : str
            
        user_agent : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/push/subscriptions'
        api_params = {}
        if endpoint is None:
            raise RevenexxException('Missing required parameter: "endpoint"')

        if keys is None:
            raise RevenexxException('Missing required parameter: "keys"')

        if subscriber_id is None:
            raise RevenexxException('Missing required parameter: "subscriber_id"')


        api_params['endpoint'] = self._normalize_value(endpoint)
        api_params['keys'] = self._normalize_value(keys)
        api_params['subscriber_id'] = self._normalize_value(subscriber_id)
        api_params['user_agent'] = self._normalize_value(user_agent)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def send_send(
        self,
        channel: str,
        template: str,
        to: str,
        attachments: Optional[List[Dict[str, Any]]] = None,
        data: Optional[Dict[str, Any]] = None,
        draft: Optional[bool] = None,
        locale: Optional[str] = None,
        market: Optional[str] = None,
        send_at: Optional[str] = None
    ) -> Error:
        """
        Renders a tenant template and dispatches it — now, at `send_at`, or at
        the end of the tenant's quiet hours.
        
        The first line is deliberately a title, not a sentence about the
        mechanism: Scramble takes it as the operation's `summary`, and a summary
        is what an API explorer prints in its route list. The paragraph that used
        to be here ran to 119 characters across two lines, which the gateway's
        fragment tests reject for exactly that reason.
        
        Retry-safe when the caller sends an `Idempotency-Key` header. The two
        answers are deliberately different:
        
          201 — a message was created by THIS call
          200 — this key was already used; here is the message it produced
        
        A caller has to be able to tell those apart. "Your mail went out" and
        "your mail had already gone out" are the same outcome and different
        facts, and a client reconciling its own records needs the second one.
        Same key with a different body is a 422 — see IdempotencyConflict.
        
        A recipient on the tenant's suppression list is not sent to, and that is
        reported as a refusal rather than as a silent success.

        Parameters
        ----------
        channel : str
            
        template : str
            
        to : str
            
        attachments : Optional[List[Dict[str, Any]]]
            Files travelling with the message. Base64 content, never a URL:
            fetching an address that arrives in a request body would make
            this service a request-forwarder inside the platform network —
            see App\Support\Attachment.
        data : Optional[Dict[str, Any]]
            The render model: a free map of variable name to value, resolved against the template's
            placeholders. Values may be strings, numbers, booleans, or nested objects and arrays —
            `{{ order.number }}` reads a nested one.
            
            Not the only source. A tenant's `defaults`, its layout, and the template's own
            `variable_defaults` are merged underneath, so a placeholder an event did not carry can
            still resolve. Anything named here wins over all of them.
        draft : Optional[bool]
            A TEST SEND. Renders the draft instead of the published snapshot,
            which is the only way an author can check a correction in a real
            mail client before it goes live to everybody. Deliberately a flag on this route and not a route of its own:
            everything else about it — suppression, quiet hours, the
            language chain, idempotency — has to behave exactly as a real
            send, and a second endpoint is a second set of those rules that
            drifts. The one difference is which fassung is rendered.
        locale : Optional[str]
            The language the CALLER states — step 1 of the resolution order,
            ahead of anything in the payload. Absent is normal and is not
            "English": it means the recipient's own language decides.
        market : Optional[str]
            Which market this send belongs to. Absent means the GLOBAL
            market, which is what every send was before markets reached this
            path — so a caller that never heard of them keeps working and
            gets the credentials it always had. The caller states it; nothing here derives it. A country code on
            a phone number is a fact and a domain on an address is a guess,
            and a guess that decides which carrier carries a message would
            look exactly like a decision somebody made.
            
            Not on `preview`: rendering picks no provider, so there is
            nothing there for a market to change.
        send_at : Optional[str]
            Send later. A time in the past is accepted and means now — a
            client retrying a request it built ten minutes ago is asking for
            the same send, and refusing it turns a late retry into a lost
            message.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/send'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        if template is None:
            raise RevenexxException('Missing required parameter: "template"')

        if to is None:
            raise RevenexxException('Missing required parameter: "to"')


        if attachments is not None:
            api_params['attachments'] = self._normalize_value(attachments)
        api_params['channel'] = self._normalize_value(channel)
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        api_params['locale'] = self._normalize_value(locale)
        api_params['market'] = self._normalize_value(market)
        api_params['send_at'] = self._normalize_value(send_at)
        api_params['template'] = self._normalize_value(template)
        api_params['to'] = self._normalize_value(to)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def stats_index(
        self,
        days: Optional[float] = None,
        xfrom: Optional[str] = None,
        to: Optional[str] = None
    ) -> Error:
        """
        Either `days` (a window ending now, default 30) or an explicit `from`/`to`
        span. Both ends of the span or neither: `from` alone would be an open
        range and the service would have to guess which end was meant.
        
        Three numbers are deliberately not the naive ones, and the `window` block
        says so rather than leaving a chart to imply otherwise. The window is
        CLAMPED to the tenant's retention, and `clamped_by_retention` says when
        that happened — 90 days on a 30-day retention is 30 days of data wearing
        a 90-day label, and the trend line it draws invents a collapse that never
        happened. Opens are counted only over channels that can report them; SMS
        and push have no such thing, so dividing opens by all messages would
        quietly halve every open rate the moment a tenant adds a second channel.
        The delivery rate is sent ÷ (sent + failed): suppressed is the service
        doing what it was told, and counting it as a failure would punish a
        tenant for having a working unsubscribe list.
        
        `previous` is the same window again immediately before this one, which is
        what turns a figure into a direction. **It is null** whenever the
        preceding window is not entirely inside retention: the query would answer
        zero rather than fail, and zero against 1,337 renders as a triumphant
        +100 % beside every tile on the screen. Show no trend rather than a
        flattering one.
        
        Nothing here names a recipient. That is the delivery log, which is a
        different endpoint with a different question.

        Parameters
        ----------
        days : Optional[float]
            Clamped and possibly shortened by retention inside the service,
            which reports what it actually used.
        xfrom : Optional[str]
            An explicit span, for a window that does not end today. Both
            ends or neither: `from` alone would be an open range, and the
            service would have to guess which end was meant.
            `nullable` rather than `sometimes`, so `required_with` still
            runs when the OTHER end is missing. With `sometimes` an absent
            field is skipped entirely, and `?from=` alone sailed through to
            become a window nobody asked for.
        to : Optional[str]
            The other end of the same span, inclusive: the whole of this day
            is inside the window whatever time its rows carry. A span running
            past today ends today — there is no data ahead of now, and a
            window with a future edge draws the series short against an axis
            claiming a month nobody has lived through.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/stats'
        api_params = {}

        if days is not None:
            api_params['days'] = self._normalize_value(days)
        api_params['from'] = self._normalize_value(xfrom)
        api_params['to'] = self._normalize_value(to)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def suppression_index(
        self,
        channel: Optional[str] = None,
        scope: Optional[Scope] = None,
        reason: Optional[Reason] = None,
        address: Optional[str] = None,
        limit: Optional[float] = None
    ) -> Error:
        """
        Filterable by `channel`, `scope`, `reason` and `address`. The address
        filter is looked up by FINGERPRINT rather than against the address
        column, which is what makes "why did this person stop getting our mail"
        answerable for somebody who has since been erased: the row has no
        address left to match on, and the question is still the same question.

        Parameters
        ----------
        channel : Optional[str]
            
        scope : Optional[Scope]
            
        reason : Optional[Reason]
            
        address : Optional[str]
            
        limit : Optional[float]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/suppressions'
        api_params = {}

        if channel is not None:
            api_params['channel'] = self._normalize_value(channel)
        if scope is not None:
            api_params['scope'] = self._normalize_value(scope)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)
        if address is not None:
            api_params['address'] = self._normalize_value(address)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def suppression_store(
        self,
        address: str,
        channel: str,
        reason: Reason,
        expires_at: Optional[str] = None,
        note: Optional[str] = None,
        scope: Optional[Scope] = None
    ) -> Error:
        """
        201 for a row this call created, 200 for an address that was already on
        the list — so a client can tell whether it changed anything.
        
        The `scope` follows from the `reason` for every reason but `manual`, and
        asking for a different one is 422 `suppression_scope_fixed` rather than
        being quietly corrected: a caller who asked for `marketing` on a hard
        bounce has the model wrong, and a silent upgrade to `all` would leave
        them believing transactional mail still flows to an address that does not
        exist.

        Parameters
        ----------
        address : str
            
        channel : str
            
        reason : Reason
            
        expires_at : Optional[str]
            
        note : Optional[str]
            
        scope : Optional[Scope]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/suppressions'
        api_params = {}
        if address is None:
            raise RevenexxException('Missing required parameter: "address"')

        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        if reason is None:
            raise RevenexxException('Missing required parameter: "reason"')


        api_params['address'] = self._normalize_value(address)
        api_params['channel'] = self._normalize_value(channel)
        api_params['expires_at'] = self._normalize_value(expires_at)
        api_params['note'] = self._normalize_value(note)
        api_params['reason'] = self._normalize_value(reason)
        if scope is not None:
            api_params['scope'] = self._normalize_value(scope)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def suppression_destroy(
        self,
        id: str
    ) -> Error:
        """
        Audited, unlike most deletes in this service. Removing a row here is the
        one operation that makes the service mail an address something decided
        not to mail — if a complaint turns into a spam report later, "who took
             * this off the list, and when" is the whole investigation.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/suppressions/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def suppression_show(
        self,
        id: str
    ) -> Error:
        """
        `address` may be null: that is a person who has been erased
        (POST /v1/privacy/erasures). The row survives as a hash, which is the
        point — the clear text is gone and the address is still blocked.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/suppressions/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_index(
        self,
        channel: Optional[str] = None,
        markets: Optional[str] = None
    ) -> Error:
        """
        `?channel=` narrows to one channel. Market-scoped as a BROWSING filter:
        with `X-Revenexx-Market` the list is the global rows plus that market's,
        without it the global rows only, and `?markets=all` is the unscoped read.
        Never a boundary — the tenant is fixed by the credential and by row-level
        security, and no value of either parameter reaches another tenant's rows.

        Parameters
        ----------
        channel : Optional[str]
            
        markets : Optional[str]
            Set to `all` for the unscoped read: every row whatever its markets, ignoring the `X-Revenexx-Market` header. The deliberate admin case, spelled in the query string so it is asked for rather than fallen into. No other value has any effect.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates'
        api_params = {}

        if channel is not None:
            api_params['channel'] = self._normalize_value(channel)
        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_store(
        self,
        channel: str,
        key: str,
        body_html: Optional[str] = None,
        body_text: Optional[str] = None,
        content_sid: Optional[str] = None,
        design: Optional[List[str]] = None,
        enabled: Optional[bool] = None,
        layout_id: Optional[str] = None,
        locale: Optional[str] = None,
        markets: Optional[List[str]] = None,
        message_class: Optional[MessageClass] = None,
        subject: Optional[str] = None,
        test_mode: Optional[bool] = None,
        title: Optional[str] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None,
        variable_defaults: Optional[List[str]] = None,
        variables: Optional[List[str]] = None,
        whatsapp_category: Optional[WhatsappCategory] = None
    ) -> Error:
        """
        Send a `design` document and the service compiles it against the
        template's layout — or send `body_html` and `body_text` yourself and skip
        compilation entirely.
        
        A design that the compiler refuses is 422 and NOTHING is written, with
        `error.details` naming the offending block. That order is deliberate: a
        save whose compile failed must leave the row alone, because storing the
        design while keeping a stale body would hand the next send a mail that no
        longer matches the document it claims to be built from, and nothing would
        ever surface it. A sidecar that is down is 503 `mjml_unavailable`, which
        is worth retrying; a rejected design is not.
        
        The row this creates is a DRAFT and sends nothing until it is published.

        Parameters
        ----------
        channel : str
            
        key : str
            
        body_html : Optional[str]
            
        body_text : Optional[str]
            
        content_sid : Optional[str]
            The Meta-approved template this one is sent as. Outside the
            24-hour service window it is the only thing WhatsApp carries.
        design : Optional[List[str]]
            The design document (v2). Validated as "an array" and no further:
            the compiler is the authority on the block schema and answers with
            the offending block, which is a better error than anything a
            validation rule list could restate here.
        enabled : Optional[bool]
            
        layout_id : Optional[str]
            Which letterhead this template is mailed on. Null (or absent) is
            not "no layout" — it means the tenant's default, resolved on
            every compile and every send, so the template keeps following
            that default when it changes.
        locale : Optional[str]
            
        markets : Optional[List[str]]
            Which markets this template is browsed in. `[]` — the default —
            is global, so this is never nullable: null would be a second
            empty next to the one that already carries the meaning.
        message_class : Optional[MessageClass]
            What messages from this template ARE. Defaulted in the column
            rather than here, so a client that has never heard of the field
            keeps sending transactional mail — which is what every template
            written before this field existed was.
        subject : Optional[str]
            
        test_mode : Optional[bool]
            When this template is in force — see App\Models\Template. `after_or_equal` and not `after`: a window of a single instant is
            a legitimate thing to write while somebody is lining two
            templates up back to back, and rejecting it would only make them
            add a second nobody can see. A window that runs BACKWARDS is
            refused, because it is a template that can never send and looks
            from the list exactly like one that can.
        title : Optional[str]
            What the template is CALLED, as opposed to `key`, which is what
            it is addressed by. Without it a list has to derive a name from
            the key, and `order-confirmation` becomes "Order Confirmation" —
            passable English by accident and wrong in every other language.
        valid_from : Optional[str]
            
        valid_until : Optional[str]
            
        variable_defaults : Optional[List[str]]
            Fallbacks for the placeholders an event did not fill — a map of
            variable name → string. Nullable, unlike `markets`: an empty map
            and no map are the same thing (nothing to fall back to), so there
            is no second state for a null to confuse anybody with.
        variables : Optional[List[str]]
            
        whatsapp_category : Optional[WhatsappCategory]
            What a WhatsApp template is to Meta, which is what every message
            from it COSTS: marketing runs about five times utility, and in
            Germany that is roughly $0.12 against $0.025 a message. Refused
            rather than coerced when it is not one of Meta's four — a
            misspelled category that quietly became the default would be
            wrong on an invoice nobody reads until the quarter closes.
            Nullable: it is not a fact about an e-mail template, and what an
            unset one means is decided on read (Template::whatsappCategory).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates'
        api_params = {}
        if channel is None:
            raise RevenexxException('Missing required parameter: "channel"')

        if key is None:
            raise RevenexxException('Missing required parameter: "key"')


        api_params['body_html'] = self._normalize_value(body_html)
        api_params['body_text'] = self._normalize_value(body_text)
        api_params['channel'] = self._normalize_value(channel)
        api_params['content_sid'] = self._normalize_value(content_sid)
        api_params['design'] = self._normalize_value(design)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['key'] = self._normalize_value(key)
        api_params['layout_id'] = self._normalize_value(layout_id)
        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)
        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)
        if message_class is not None:
            api_params['message_class'] = self._normalize_value(message_class)
        api_params['subject'] = self._normalize_value(subject)
        if test_mode is not None:
            api_params['test_mode'] = self._normalize_value(test_mode)
        api_params['title'] = self._normalize_value(title)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)
        api_params['variable_defaults'] = self._normalize_value(variable_defaults)
        api_params['variables'] = self._normalize_value(variables)
        api_params['whatsapp_category'] = self._normalize_value(whatsapp_category)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_destroy(
        self,
        id: str
    ) -> Error:
        """
        Any binding still naming this template's key will find nothing when its
        event next arrives. Audited under the KEY as well as the id: after the
        delete the id resolves to nothing, and "deleted tmpl_01J…" is not
        something an operator can act on six weeks later.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_show(
        self,
        id: str
    ) -> Error:
        """
        What customers are receiving is the published snapshot; see
        `GET /v1/templates/{id}/versions`, whose `meta.has_unpublished_changes`
        says whether the two differ.
        
        Not market-filtered, deliberately: market scoping is a browsing concern
        and somebody holding an id may read the row.

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_update_patch(
        self,
        id: str,
        body_html: Optional[str] = None,
        body_text: Optional[str] = None,
        content_sid: Optional[str] = None,
        design: Optional[List[str]] = None,
        enabled: Optional[bool] = None,
        layout_id: Optional[str] = None,
        markets: Optional[List[str]] = None,
        message_class: Optional[MessageClass] = None,
        subject: Optional[str] = None,
        test_mode: Optional[bool] = None,
        title: Optional[str] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None,
        variable_defaults: Optional[List[str]] = None,
        variables: Optional[List[str]] = None,
        whatsapp_category: Optional[WhatsappCategory] = None
    ) -> Error:
        """
        Only the fields sent are written, and the change is audited only when
        something actually changed — a PATCH that resent the same values records
        nothing, because an audit line on every save teaches its readers to
        ignore the log.
        
        Moving a template to another layout recompiles it against the NEW one,
        even when nothing else changed: colours, width and font come from the
        layout and are already inlined, so a template that merely changed hands
        would otherwise keep showing the old letterhead until somebody happened
        to press save on it again.
        
        Changes nothing customers receive until the template is published.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        id : str
            
        body_html : Optional[str]
            
        body_text : Optional[str]
            
        content_sid : Optional[str]
            
        design : Optional[List[str]]
            
        enabled : Optional[bool]
            
        layout_id : Optional[str]
            
        markets : Optional[List[str]]
            
        message_class : Optional[MessageClass]
            
        subject : Optional[str]
            
        test_mode : Optional[bool]
            When this template is in force — see App\Models\Template. `after_or_equal` and not `after`: a window of a single instant is
            a legitimate thing to write while somebody is lining two
            templates up back to back, and rejecting it would only make them
            add a second nobody can see. A window that runs BACKWARDS is
            refused, because it is a template that can never send and looks
            from the list exactly like one that can.
        title : Optional[str]
            Reclassifying is allowed and changes nothing that already went
            out: `messages.message_class` was copied onto each row at
            dispatch, so the log keeps saying what each message was.
        valid_from : Optional[str]
            
        valid_until : Optional[str]
            
        variable_defaults : Optional[List[str]]
            
        variables : Optional[List[str]]
            
        whatsapp_category : Optional[WhatsappCategory]
            Recategorising is allowed and takes effect on the next send: Meta
            move templates between categories on their own schedule, and a
            row that could not follow them would go on quoting a price that
            stopped being true.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['body_html'] = self._normalize_value(body_html)
        api_params['body_text'] = self._normalize_value(body_text)
        api_params['content_sid'] = self._normalize_value(content_sid)
        api_params['design'] = self._normalize_value(design)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['layout_id'] = self._normalize_value(layout_id)
        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)
        if message_class is not None:
            api_params['message_class'] = self._normalize_value(message_class)
        api_params['subject'] = self._normalize_value(subject)
        if test_mode is not None:
            api_params['test_mode'] = self._normalize_value(test_mode)
        api_params['title'] = self._normalize_value(title)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)
        api_params['variable_defaults'] = self._normalize_value(variable_defaults)
        api_params['variables'] = self._normalize_value(variables)
        api_params['whatsapp_category'] = self._normalize_value(whatsapp_category)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_update(
        self,
        id: str,
        body_html: Optional[str] = None,
        body_text: Optional[str] = None,
        content_sid: Optional[str] = None,
        design: Optional[List[str]] = None,
        enabled: Optional[bool] = None,
        layout_id: Optional[str] = None,
        markets: Optional[List[str]] = None,
        message_class: Optional[MessageClass] = None,
        subject: Optional[str] = None,
        test_mode: Optional[bool] = None,
        title: Optional[str] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None,
        variable_defaults: Optional[List[str]] = None,
        variables: Optional[List[str]] = None,
        whatsapp_category: Optional[WhatsappCategory] = None
    ) -> Error:
        """
        Only the fields sent are written, and the change is audited only when
        something actually changed — a PATCH that resent the same values records
        nothing, because an audit line on every save teaches its readers to
        ignore the log.
        
        Moving a template to another layout recompiles it against the NEW one,
        even when nothing else changed: colours, width and font come from the
        layout and are already inlined, so a template that merely changed hands
        would otherwise keep showing the old letterhead until somebody happened
        to press save on it again.
        
        Changes nothing customers receive until the template is published.
        
        This path answers on `PUT` and `PATCH`, both routed to the same action.

        Parameters
        ----------
        id : str
            
        body_html : Optional[str]
            
        body_text : Optional[str]
            
        content_sid : Optional[str]
            
        design : Optional[List[str]]
            
        enabled : Optional[bool]
            
        layout_id : Optional[str]
            
        markets : Optional[List[str]]
            
        message_class : Optional[MessageClass]
            
        subject : Optional[str]
            
        test_mode : Optional[bool]
            When this template is in force — see App\Models\Template. `after_or_equal` and not `after`: a window of a single instant is
            a legitimate thing to write while somebody is lining two
            templates up back to back, and rejecting it would only make them
            add a second nobody can see. A window that runs BACKWARDS is
            refused, because it is a template that can never send and looks
            from the list exactly like one that can.
        title : Optional[str]
            Reclassifying is allowed and changes nothing that already went
            out: `messages.message_class` was copied onto each row at
            dispatch, so the log keeps saying what each message was.
        valid_from : Optional[str]
            
        valid_until : Optional[str]
            
        variable_defaults : Optional[List[str]]
            
        variables : Optional[List[str]]
            
        whatsapp_category : Optional[WhatsappCategory]
            Recategorising is allowed and takes effect on the next send: Meta
            move templates between categories on their own schedule, and a
            row that could not follow them would go on quoting a price that
            stopped being true.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['body_html'] = self._normalize_value(body_html)
        api_params['body_text'] = self._normalize_value(body_text)
        api_params['content_sid'] = self._normalize_value(content_sid)
        api_params['design'] = self._normalize_value(design)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['layout_id'] = self._normalize_value(layout_id)
        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)
        if message_class is not None:
            api_params['message_class'] = self._normalize_value(message_class)
        api_params['subject'] = self._normalize_value(subject)
        if test_mode is not None:
            api_params['test_mode'] = self._normalize_value(test_mode)
        api_params['title'] = self._normalize_value(title)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)
        api_params['variable_defaults'] = self._normalize_value(variable_defaults)
        api_params['variables'] = self._normalize_value(variables)
        api_params['whatsapp_category'] = self._normalize_value(whatsapp_category)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_version_store(
        self,
        template_id: str,
        note: Optional[str] = None
    ) -> Error:
        """
        Answers 200 with the version already live when there was nothing to
        publish, and 201 when a new one was written — so a client can tell
        whether its press did anything without diffing the payload.

        Parameters
        ----------
        template_id : str
            
        note : Optional[str]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{templateId}/publish'
        api_params = {}
        if template_id is None:
            raise RevenexxException('Missing required parameter: "template_id"')

        api_path = api_path.replace('{templateId}', str(self._normalize_value(template_id)))

        api_params['note'] = self._normalize_value(note)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_version_index(
        self,
        template_id: str
    ) -> Error:
        """
        Summaries only: version, subject, message class, layout, who published it
        and when, and their note. The BODIES are deliberately absent — a compiled
        `body_html` runs to tens of kilobytes, and a template with forty versions
        would make this a several-megabyte download that nobody scrolls to the
        end of. `GET /v1/templates/{id}/versions/{version}` serves the full
        snapshot for the one somebody actually opened.
        
        `meta.published_version_id` says which of them is live — a property of
        the template, said once, rather than a flag repeated on every row that
        two rows could then claim. `meta.has_unpublished_changes` says whether
        the draft has moved on since.

        Parameters
        ----------
        template_id : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{templateId}/versions'
        api_params = {}
        if template_id is None:
            raise RevenexxException('Missing required parameter: "template_id"')

        api_path = api_path.replace('{templateId}', str(self._normalize_value(template_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_version_show(
        self,
        template_id: str,
        version: str
    ) -> Error:
        """
        Addressed by its VERSION NUMBER — the small integer on the history row,
        not the snapshot's id — because that is the number an author has in front
        of them.
        
        This is what sends actually rendered while that version was live, so it
        is the thing to read when the question is "what did the mail we sent in
             * March say".

        Parameters
        ----------
        template_id : str
            
        version : str
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{templateId}/versions/{version}'
        api_params = {}
        if template_id is None:
            raise RevenexxException('Missing required parameter: "template_id"')

        if version is None:
            raise RevenexxException('Missing required parameter: "version"')

        api_path = api_path.replace('{templateId}', str(self._normalize_value(template_id)))
        api_path = api_path.replace('{version}', str(self._normalize_value(version)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def template_version_restore(
        self,
        template_id: str,
        version: str,
        publish: Optional[bool] = None
    ) -> Error:
        """
        `publish: true` makes it live in the same transaction — see
        TemplatePublisher::restore for why that flag exists rather than asking
        the caller for a second round trip.

        Parameters
        ----------
        template_id : str
            
        version : str
            
        publish : Optional[bool]
            
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/messaging/templates/{templateId}/versions/{version}/restore'
        api_params = {}
        if template_id is None:
            raise RevenexxException('Missing required parameter: "template_id"')

        if version is None:
            raise RevenexxException('Missing required parameter: "version"')

        api_path = api_path.replace('{templateId}', str(self._normalize_value(template_id)))
        api_path = api_path.replace('{version}', str(self._normalize_value(version)))

        if publish is not None:
            api_params['publish'] = self._normalize_value(publish)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

