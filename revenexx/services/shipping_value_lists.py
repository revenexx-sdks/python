from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.tone import Tone;
from ..models.error import Error;
from ..models.shipping_vocabulary_index import ShippingVocabularyIndex;
from ..enums.shipping_vocabularies_get_name import ShippingVocabulariesGetName;

class ShippingValueLists(Service):

    def __init__(self, client) -> None:
        super(ShippingValueLists, self).__init__(client)

    def shipping_service_levels_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        What class of service a carrier row represents. This used to be a CHECK constraint, which meant a merchant with a night-courier tier or a two-man delivery service needed a release of this app to say so — and nothing in the app ever branched on the value, it only carried it. The set is the tenant's rows now, and the first read seeds it, so this never answers empty. Hand-rolled rather than a generic mount, because seeding is the point: it therefore honours limit/offset AND NOTHING ELSE. There is no `?code=` filter and no `order` — the rows always come back in `position` order, and a sort or a filter sent anyway is accepted, ignored, and answered 200.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200). A value outside the range is clamped rather than refused, and `page.limit` echoes what was applied.
        offset : Optional[float]
            Row offset for pagination (default 0). The next page is `page.offset + page.returned`.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/service-levels'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def shipping_service_levels_create(
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
        A service level is the class of service a carrier row represents, as one of the tenant's own codes. It is carried by `shipping_carriers.service_level` and reported on a rate as `carrier_service_level`; nothing in this app branches on it. A method never names one — it gets its level through the carrier it ships with. Reach for this when a merchant sells a class this app was not shipped with — a night courier, a two-man delivery, a same-day run. A create cannot omit `code` and `title`; every other column is optional or defaulted by the database. Two rows of this tenant may not share `code` — that is the 409. The code is lowercase and becomes what a carrier stores; it cannot be changed afterwards, because every carrier carrying it would be orphaned. Creating one changes nothing on its own: a carrier has to be moved onto it before it means anything.

        Parameters
        ----------
        code : str
            Lowercase letters, digits, - or _, starting with a letter. What `shipping_carriers.service_level` stores. Immutable once created — renaming it would orphan every row carrying it.
        title : str
            What an operator reads in a select. The name a merchant renames; the code underneath never moves.
        description : Optional[str]
            The sentence under the title, explaining when to pick this service level. Null when the title says enough.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        is_default : Optional[bool]
            Promote this value on creation; the previous default is demoted.
        labels : Optional[Dict[str, Any]]
            Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        position : Optional[float]
            Sort order in a select — the collection is returned in it.
        tone : Optional[Tone]
            Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/service-levels'
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


    def shipping_service_levels_delete(
        self,
        id: str
    ) -> Error:
        """
        There is no foreign key doing this: adding one to a table that starts empty would fail the migration of every existing tenant. The refusal lives in the handler instead.

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

        api_path = '/v1/shipping/service-levels/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_service_levels_get(
        self,
        id: str
    ) -> Error:
        """
        A service level is the class of service a carrier row represents, as one of the tenant's own codes. It is carried by `shipping_carriers.service_level` and reported on a rate as `carrier_service_level`; nothing in this app branches on it. A method never names one — it gets its level through the carrier it ships with. This reads one of them by ROW ID — which is what an editor holds after listing the set, and not what anything else in the platform stores. A caller holding the CODE (off a carrier row, or off a rate's `carrier_service_level`) cannot use this route: there is no `?code=` filter on the collection either, so read GET /shipping/vocabularies/service-levels, which is keyed the way the rest of the platform refers to these values.

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

        api_path = '/v1/shipping/service-levels/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_service_levels_update(
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
        A service level is the class of service a carrier row represents, as one of the tenant's own codes. It is carried by `shipping_carriers.service_level` and reported on a rate as `carrier_service_level`; nothing in this app branches on it. A method never names one — it gets its level through the carrier it ships with. This edits the DISPLAY half of one — title, description, their locale maps, badge tone, position, and the default flag. Everything a carrier or a filter joins on stays put: the code is immutable (a different one in the payload is a 400, not a silent no-op), and no carrier is moved onto or off this level by renaming it. Moving a row's `position` does not renumber its neighbours — the collection is returned in position order and ties fall back to whatever the database returns, so a deliberate order means writing every row's position.

        Parameters
        ----------
        id : str
            The row id.
        description : Optional[str]
            The sentence under the title, explaining when to pick this service level. Null when the title says enough.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted. POST …/make-default does the same thing without an edit.
        labels : Optional[Dict[str, Any]]
            Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        position : Optional[float]
            Sort order in a select — the collection is returned in it.
        title : Optional[str]
            What an operator reads in a select. The name a merchant renames; the code underneath never moves.
        tone : Optional[Tone]
            Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/service-levels/{id}'
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


    def shipping_service_levels_make_default(
        self,
        id: str,
        data: Dict[str, Any]
    ) -> Error:
        """
        The flag is a single answer, not a per-row opinion: it is what every fallback lands on, so two defaults leave the result to row order and none leaves it to the seeded value. This row takes it and whoever was holding it is demoted in the same call — there is no separate write to clear the old one, and no window in which both carry it. Only the rows whose flag is wrong are written, so repeating the call is free.

        Parameters
        ----------
        id : str
            The row id.
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

        api_path = '/v1/shipping/service-levels/{id}/make-default'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if data is None:
            raise RevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_vocabularies_list(
        self
    ) -> ShippingVocabularyIndex:
        """
        Discovery for the vocabulary routes: every enum this app publishes, each with its name, its title and its description, and deliberately without its values — an index stays an index, and the set a value belongs to is one further call. Names: carrier-statuses, matrix-bases, pricing-types, service-levels, weight-units. Fetch one with GET /shipping/vocabularies/{name}; a client holding the qualified pair 'shipping.<name>' builds that URL from the pair alone. `title` and `description` are either one string or a locale map keyed by locale — every entry here carries the map, because every one of them is curated copy.

        Returns
        -------
        ShippingVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ShippingVocabularyIndex)


    def shipping_vocabularies_get(
        self,
        name: ShippingVocabulariesGetName
    ) -> Error:
        """
        One vocabulary in full: every value it permits, each carrying the title to show, the description to explain it and the badge tone to draw it in — everything a select or a status chip needs, so nothing has to be labelled a second time in a client. Two sources, one guarantee: what is served is what is enforced, so no UI keeps a second copy. 'source: schema' means the values are read out of a CHECK constraint — a value added to the constraint appears here even before anyone labels it, titled from its own key, in constraint order. 'source: table' means the values are the TENANT's own rows (service-levels, weight-units), read per request and seeded on first use, so a merchant may add one without a release of this app; those values also carry labels/descriptions, is_system and is_default, and weight-units carries the conversion factor. 'closed' says the set is exhaustive either way, so a value outside it is stale data rather than a missing label. `title` and `description` — the vocabulary's and every value's — are either one string or a locale map keyed by locale: curated copy carries the map, a value titled from its own key carries the string. Names: carrier-statuses, matrix-bases, pricing-types, service-levels, weight-units.

        Parameters
        ----------
        name : ShippingVocabulariesGetName
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

        api_path = '/v1/shipping/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_weight_units_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Not a taxonomy: a unit is a code PLUS a factor, and the factor prices parcels. `factor` is how many kilograms one of this unit weighs, so a matrix keyed in one unit can price a request expressed in another. Exactly one row is the BASE (kg, factor 1) — the anchor every other factor and every stored rate tier is expressed in — and it is fixed at install. Seeded on first read, so this never answers empty. Like the service levels it is hand-rolled and honours limit/offset AND NOTHING ELSE: no column filter, no `order`, always `position` order, and a sort sent anyway is ignored rather than refused.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200). A value outside the range is clamped rather than refused, and `page.limit` echoes what was applied.
        offset : Optional[float]
            Row offset for pagination (default 0). The next page is `page.offset + page.returned`.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/weight-units'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def shipping_weight_units_create(
        self,
        code: str,
        factor: float,
        title: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Reach for this when a merchant weighs goods in something this app was not shipped with — a tonne for pallet freight, a carat for jewellery — and wants a rate matrix keyed in it. `factor` is required and must be greater than 0: zero does not convert a weight, it divides by it, and a negative factor turns a parcel into a credit. The new unit is never the base — which unit anchors the others is decided at install, and moving it would silently reprice every weight matrix in the shop.

        Parameters
        ----------
        code : str
            Lowercase letters, digits, - or _, starting with a letter. What a rate request names in `weight_unit`, and what a market's `weight_unit` setting stores. Immutable once created — renaming it would orphan every row carrying it.
        factor : float
            How many BASE units (kilograms) one of this unit weighs — a tonne is 1000, a gram 0.001, a pound 0.45359237. This number prices parcels: every weight matrix converts a request through it. Must be > 0; the base unit is fixed at 1 and rejects a change.
        title : str
            What an operator reads in a select. The name a merchant renames; the code underneath never moves.
        description : Optional[str]
            The sentence under the title, explaining when to pick this weight unit. Null when the title says enough.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        is_default : Optional[bool]
            Promote this value on creation; the previous default is demoted.
        labels : Optional[Dict[str, Any]]
            Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        position : Optional[float]
            Sort order in a select — the collection is returned in it.
        tone : Optional[Tone]
            Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/weight-units'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if factor is None:
            raise RevenexxException('Missing required parameter: "factor"')

        if title is None:
            raise RevenexxException('Missing required parameter: "title"')


        api_params['code'] = self._normalize_value(code)
        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        api_params['factor'] = self._normalize_value(factor)
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


    def shipping_weight_units_delete(
        self,
        id: str
    ) -> Error:
        """
        The market check is best effort by design — the setting is per market and this request carries one, so another market may still name the unit. That case degrades to the market falling back to the flagged unit rather than failing its quotes.

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

        api_path = '/v1/shipping/weight-units/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_weight_units_get(
        self,
        id: str
    ) -> Error:
        """
        A weight unit is a code PLUS a factor — how many kilograms one of this unit weighs — and the factor is what prices parcels: a rate request expressed in one unit is converted through the two factors into the unit the market's tiers are keyed in. Exactly one row is the base (kg, factor 1), fixed at install. This reads one of them by ROW ID, which is what an editor holds after listing the set; a caller holding the CODE (a market's `weight_unit` setting, a rate request's `weight_unit`) has no filter for it here and should read GET /shipping/vocabularies/weight-units instead. Reading the factor back is NOT how a past quote is checked: a rate answer echoes the factors it applied in `basis.weight_unit_factor` and `basis.request_weight_unit_factor` precisely so it stays re-derivable after this row has been edited.

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

        api_path = '/v1/shipping/weight-units/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def shipping_weight_units_update(
        self,
        id: str,
        description: Optional[str] = None,
        descriptions: Optional[Dict[str, Any]] = None,
        factor: Optional[float] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        title: Optional[str] = None,
        tone: Optional[Tone] = None
    ) -> Error:
        """
        Everything but the code and the base flag. A factor sent for the BASE unit is refused rather than silently ignored: it reads as 1 because every other factor is relative to it, so changing it would rescale the whole table without touching another row.

        Parameters
        ----------
        id : str
            The row id.
        description : Optional[str]
            The sentence under the title, explaining when to pick this weight unit. Null when the title says enough.
        descriptions : Optional[Dict[str, Any]]
            Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        factor : Optional[float]
            How many BASE units (kilograms) one of this unit weighs — a tonne is 1000, a gram 0.001, a pound 0.45359237. This number prices parcels: every weight matrix converts a request through it. Must be > 0; the base unit is fixed at 1 and rejects a change.
        is_default : Optional[bool]
            Promote this value; the previous default is demoted. POST …/make-default does the same thing without an edit.
        labels : Optional[Dict[str, Any]]
            Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
        position : Optional[float]
            Sort order in a select — the collection is returned in it.
        title : Optional[str]
            What an operator reads in a select. The name a merchant renames; the code underneath never moves.
        tone : Optional[Tone]
            Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/shipping/weight-units/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['descriptions'] = self._normalize_value(descriptions)
        if factor is not None:
            api_params['factor'] = self._normalize_value(factor)
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


    def shipping_weight_units_make_default(
        self,
        id: str,
        data: Dict[str, Any]
    ) -> Error:
        """
        The flag is a single answer, not a per-row opinion: it is what every fallback lands on, so two defaults leave the result to row order and none leaves it to the seeded value. This row takes it and whoever was holding it is demoted in the same call — there is no separate write to clear the old one, and no window in which both carry it. Only the rows whose flag is wrong are written, so repeating the call is free.

        Parameters
        ----------
        id : str
            The row id.
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

        api_path = '/v1/shipping/weight-units/{id}/make-default'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if data is None:
            raise RevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

