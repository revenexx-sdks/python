from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.tone import Tone;
from ..models.error import Error;
from ..models.vocabulary_index import VocabularyIndex;
from ..enums.customers_vocabularies_get_name import CustomersVocabulariesGetName;

class CustomersValueLists(Service):

    def __init__(self, client) -> None:
        super(CustomersValueLists, self).__init__(client)

    def customers_address_types_list(
        self
    ) -> Dict[str, Any]:
        """
        What an address is used for. Billing and shipping are what a checkout needs; a works entrance or a central accounts office is the tenant's own. A fresh install is seeded with billing, shipping, and the set seeds on first read too, so the page is never empty and `addresses.type` always has a value it may carry. The whole set comes back in one page in the tenant's own order — this route takes no limit/offset/order and no column filters, so `page` describes the full set and `filter` is always empty.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/address-types'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_address_types_create(
        self,
        code: str,
        title: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Extends this tenant's address types set with a value of their own — the whole reason these four stopped being CHECK constraints. What an address is used for. Billing and shipping are what a checkout needs; a works entrance or a central accounts office is the tenant's own. The code is lowercase and becomes what `addresses.type` stores; it cannot be changed afterwards, because every record carrying it would be orphaned.

        Parameters
        ----------
        code : str
            What `addresses.type` will store. Lowercase, starting with a letter; immutable afterwards.
        title : str
            The fallback name shown when no locale matches.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted in the same call.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending. Default 0.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/address-types'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if title is None:
            raise RevenexxException('Missing required parameter: "title"')


        api_params['code'] = self._normalize_value(code)
        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_address_types_delete(
        self,
        id: str
    ) -> Error:
        """
        Takes a value out of the address types set. There is no foreign key behind `addresses.type` — one added to a table that starts empty fails the migration of every existing tenant — so this route IS the integrity: it refuses while any record still carries the code, and it refuses to empty the set. Retiring a value that is in use is therefore a two-step job: move the records onto another value first, then remove it.

        Parameters
        ----------
        id : str
            The address type to remove.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/address-types/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_address_types_get(
        self,
        id: str
    ) -> Error:
        """
        One value of the address types set, by its id — its code, its fallback title, the per-language `labels` an operator reads and the badge `tone` a client renders it with. What an address is used for. Billing and shipping are what a checkout needs; a works entrance or a central accounts office is the tenant's own. Reading one value is the rare path: `GET /customers/address-types` answers the whole set in a single page, which is what a select needs.

        Parameters
        ----------
        id : str
            The address type to read. Note that records store the CODE, not this id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/address-types/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_address_types_update(
        self,
        id: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        title: Optional[str] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Everything about a value except the value itself: its titles, its help text, its badge tone, its `position` in the select, and which one of the set is the default. The `code` is immutable, so no record carrying it is ever orphaned by an edit here — a merchant who retitles `shipping` to wording of their own changes what people READ and nothing about what `addresses.type` stores. Seeded values (`is_system`) are renameable like any other, and re-seeding leaves the rename alone.

        Parameters
        ----------
        id : str
            The address type to edit.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending.
        title : Optional[str]
            The fallback name shown when no locale matches.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/address-types/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contact_event_kinds_list(
        self
    ) -> Dict[str, Any]:
        """
        What kind of entry lands on a customer timeline. 'system' is the app's own decision trail and a caller may not file one, whatever the set says. A fresh install is seeded with system, note, call, email, meeting, visit, task, and the set seeds on first read too, so the page is never empty and `contact_events.kind` always has a value it may carry. The whole set comes back in one page in the tenant's own order — this route takes no limit/offset/order and no column filters, so `page` describes the full set and `filter` is always empty.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact-event-kinds'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_contact_event_kinds_create(
        self,
        code: str,
        title: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Extends this tenant's activity types set with a value of their own — the whole reason these four stopped being CHECK constraints. What kind of entry lands on a customer timeline. 'system' is the app's own decision trail and a caller may not file one, whatever the set says. The code is lowercase and becomes what `contact_events.kind` stores; it cannot be changed afterwards, because every record carrying it would be orphaned.

        Parameters
        ----------
        code : str
            What `contact_events.kind` will store. Lowercase, starting with a letter; immutable afterwards.
        title : str
            The fallback name shown when no locale matches.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted in the same call.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending. Default 0.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact-event-kinds'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if title is None:
            raise RevenexxException('Missing required parameter: "title"')


        api_params['code'] = self._normalize_value(code)
        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contact_event_kinds_delete(
        self,
        id: str
    ) -> Error:
        """
        Takes a value out of the activity types set. There is no foreign key behind `contact_events.kind` — one added to a table that starts empty fails the migration of every existing tenant — so this route IS the integrity: it refuses while any record still carries the code, and it refuses to empty the set. Retiring a value that is in use is therefore a two-step job: move the records onto another value first, then remove it.

        Parameters
        ----------
        id : str
            The activity type to remove.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact-event-kinds/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contact_event_kinds_get(
        self,
        id: str
    ) -> Error:
        """
        One value of the activity types set, by its id — its code, its fallback title, the per-language `labels` an operator reads and the badge `tone` a client renders it with. What kind of entry lands on a customer timeline. 'system' is the app's own decision trail and a caller may not file one, whatever the set says. Reading one value is the rare path: `GET /customers/contact-event-kinds` answers the whole set in a single page, which is what a select needs.

        Parameters
        ----------
        id : str
            The activity type to read. Note that records store the CODE, not this id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact-event-kinds/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contact_event_kinds_update(
        self,
        id: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        title: Optional[str] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Everything about a value except the value itself: its titles, its help text, its badge tone, its `position` in the select, and which one of the set is the default. The `code` is immutable, so no record carrying it is ever orphaned by an edit here — a merchant who retitles `call` to wording of their own changes what people READ and nothing about what `contact_events.kind` stores. Seeded values (`is_system`) are renameable like any other, and re-seeding leaves the rename alone.

        Parameters
        ----------
        id : str
            The activity type to edit.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending.
        title : Optional[str]
            The fallback name shown when no locale matches.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact-event-kinds/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_defaults(
        self,
        data: Dict[str, Any]
    ) -> Error:
        """
        What the app.installed event runs. It fills all four of the value sets a tenant needs before anything else works — the payment terms, the address types, the lifecycle stages and the activity types — in one call. Idempotent by code: a set that already has its rows is left completely alone, so a re-delivered event and a merchant's renames both survive. A tenant installed before these tables existed is seeded lazily instead, by the first read that finds one empty.

        Parameters
        ----------
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

        api_path = '/v1/customers/defaults'
        api_params = {}
        if data is None:
            raise RevenexxException('Missing required parameter: "data"')


        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_lifecycle_stages_list(
        self
    ) -> Dict[str, Any]:
        """
        Where a company stands in the sales pipeline — a separate axis from status, and one whose steps are a sales team's own. A fresh install is seeded with lead, prospect, customer, churned, and the set seeds on first read too, so the page is never empty and `organizations.lifecycle_stage` always has a value it may carry. The whole set comes back in one page in the tenant's own order — this route takes no limit/offset/order and no column filters, so `page` describes the full set and `filter` is always empty.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/lifecycle-stages'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_lifecycle_stages_create(
        self,
        code: str,
        title: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Extends this tenant's lifecycle stages set with a value of their own — the whole reason these four stopped being CHECK constraints. Where a company stands in the sales pipeline — a separate axis from status, and one whose steps are a sales team's own. The code is lowercase and becomes what `organizations.lifecycle_stage` stores; it cannot be changed afterwards, because every record carrying it would be orphaned.

        Parameters
        ----------
        code : str
            What `organizations.lifecycle_stage` will store. Lowercase, starting with a letter; immutable afterwards.
        title : str
            The fallback name shown when no locale matches.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted in the same call.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending. Default 0.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/lifecycle-stages'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if title is None:
            raise RevenexxException('Missing required parameter: "title"')


        api_params['code'] = self._normalize_value(code)
        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_lifecycle_stages_delete(
        self,
        id: str
    ) -> Error:
        """
        Takes a value out of the lifecycle stages set. There is no foreign key behind `organizations.lifecycle_stage` — one added to a table that starts empty fails the migration of every existing tenant — so this route IS the integrity: it refuses while any record still carries the code, and it refuses to empty the set. Retiring a value that is in use is therefore a two-step job: move the records onto another value first, then remove it.

        Parameters
        ----------
        id : str
            The lifecycle stage to remove.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/lifecycle-stages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_lifecycle_stages_get(
        self,
        id: str
    ) -> Error:
        """
        One value of the lifecycle stages set, by its id — its code, its fallback title, the per-language `labels` an operator reads and the badge `tone` a client renders it with. Where a company stands in the sales pipeline — a separate axis from status, and one whose steps are a sales team's own. Reading one value is the rare path: `GET /customers/lifecycle-stages` answers the whole set in a single page, which is what a select needs.

        Parameters
        ----------
        id : str
            The lifecycle stage to read. Note that records store the CODE, not this id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/lifecycle-stages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_lifecycle_stages_update(
        self,
        id: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        title: Optional[str] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Everything about a value except the value itself: its titles, its help text, its badge tone, its `position` in the select, and which one of the set is the default. The `code` is immutable, so no record carrying it is ever orphaned by an edit here — a merchant who retitles `customer` to wording of their own changes what people READ and nothing about what `organizations.lifecycle_stage` stores. Seeded values (`is_system`) are renameable like any other, and re-seeding leaves the rename alone.

        Parameters
        ----------
        id : str
            The lifecycle stage to edit.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending.
        title : Optional[str]
            The fallback name shown when no locale matches.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/lifecycle-stages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_payment_terms_list(
        self
    ) -> Dict[str, Any]:
        """
        When a company has to pay. A wholesaler who agrees net 45 with one customer used to need a release of this app to say so. A fresh install is seeded with prepayment, direct_debit, net_7, net_14, net_30, net_60, net_90, and the set seeds on first read too, so the page is never empty and `organizations.payment_terms` always has a value it may carry. The whole set comes back in one page in the tenant's own order — this route takes no limit/offset/order and no column filters, so `page` describes the full set and `filter` is always empty.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/payment-terms'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_payment_terms_create(
        self,
        code: str,
        title: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Extends this tenant's payment terms set with a value of their own — the whole reason these four stopped being CHECK constraints. When a company has to pay. A wholesaler who agrees net 45 with one customer used to need a release of this app to say so. The code is lowercase and becomes what `organizations.payment_terms` stores; it cannot be changed afterwards, because every record carrying it would be orphaned.

        Parameters
        ----------
        code : str
            What `organizations.payment_terms` will store. Lowercase, starting with a letter; immutable afterwards.
        title : str
            The fallback name shown when no locale matches.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted in the same call.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending. Default 0.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/payment-terms'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if title is None:
            raise RevenexxException('Missing required parameter: "title"')


        api_params['code'] = self._normalize_value(code)
        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_payment_terms_delete(
        self,
        id: str
    ) -> Error:
        """
        Takes a value out of the payment terms set. There is no foreign key behind `organizations.payment_terms` — one added to a table that starts empty fails the migration of every existing tenant — so this route IS the integrity: it refuses while any record still carries the code, and it refuses to empty the set. Retiring a value that is in use is therefore a two-step job: move the records onto another value first, then remove it.

        Parameters
        ----------
        id : str
            The payment term to remove.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/payment-terms/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_payment_terms_get(
        self,
        id: str
    ) -> Error:
        """
        One value of the payment terms set, by its id — its code, its fallback title, the per-language `labels` an operator reads and the badge `tone` a client renders it with. When a company has to pay. A wholesaler who agrees net 45 with one customer used to need a release of this app to say so. Reading one value is the rare path: `GET /customers/payment-terms` answers the whole set in a single page, which is what a select needs.

        Parameters
        ----------
        id : str
            The payment term to read. Note that records store the CODE, not this id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/payment-terms/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_payment_terms_update(
        self,
        id: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        title: Optional[str] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Everything about a value except the value itself: its titles, its help text, its badge tone, its `position` in the select, and which one of the set is the default. The `code` is immutable, so no record carrying it is ever orphaned by an edit here — a merchant who retitles `net_30` to wording of their own changes what people READ and nothing about what `organizations.payment_terms` stores. Seeded values (`is_system`) are renameable like any other, and re-seeding leaves the rename alone.

        Parameters
        ----------
        id : str
            The payment term to edit.
        description : Optional[str]
            One line of help for whoever picks this value.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `description`.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted.
        labels : Optional[Dict[str, Any]]
            Localized titles, keyed by language tag ({ "en": …, "de": … }). Null when nobody translated this value — a client then falls back to `title`.
        position : Optional[float]
            Where it sits in the set, ascending.
        title : Optional[str]
            The fallback name shown when no locale matches.
        tone : Optional[Tone]
            Semantic badge colour.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/payment-terms/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if tone is not None:
            api_params['tone'] = self._normalize_value(tone)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_vocabularies_list(
        self
    ) -> VocabularyIndex:
        """
        Discovery for the vocabulary routes: every enum this app publishes, each as a name, a title and a description. The VALUES are deliberately left out — this is the call that says which vocabularies exist, and the detail route is the one that answers what is in them. Names: address-types, contact-event-kinds, contact-statuses, lifecycle-stages, locales, organization-statuses, payment-terms, registration-statuses, roles, rule-matches, segment-sources. Fetch one with GET /customers/vocabularies/{name}; a client holding the qualified pair 'customers.<name>' builds that URL from the pair alone.

        Returns
        -------
        VocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VocabularyIndex)


    def customers_vocabularies_get(
        self,
        name: CustomersVocabulariesGetName
    ) -> Error:
        """
        One vocabulary in full: every permitted value, each with its title, its description and the badge tone a client renders it with — enough to build a select without a second call. Two kinds of set, and 'source' says which one answered. 'schema' — the values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift; a value added to the constraint appears here even before anyone labels it, titled from its own key. 'table' — the values are the TENANT's own rows (payment terms, address types, lifecycle stages, activity types, roles), so they carry labels/descriptions per locale, is_system and is_default, and a merchant may add to them without a release of this app. 'tenant'/'defaults' are the two answers for a set the merchant configures but may not extend. Either way 'closed' is true: the set is exhaustive at this moment, so a value outside it is stale data rather than a missing label. Values come back in the order a select should offer them — lifecycle order for a status, the merchant's own position for a table. Names: address-types, contact-event-kinds, contact-statuses, lifecycle-stages, locales, organization-statuses, payment-terms, registration-statuses, roles, rule-matches, segment-sources.

        Parameters
        ----------
        name : CustomersVocabulariesGetName
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

        api_path = '/v1/customers/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

