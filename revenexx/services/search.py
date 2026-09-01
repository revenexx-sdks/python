from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;
from ..enums.collection import Collection;
from ..models.multi_search_entry import MultiSearchEntry;

class Search(Service):

    def __init__(self, client) -> None:
        super(Search, self).__init__(client)

    def search_list_collections(
        self
    ) -> Error:
        """
        The collections the tenant's installed apps have provisioned. Available on the API-gateway-trust path only — a `revx_` key authorises a single collection, so discovery is a gateway concern and a key-authenticated caller gets 403.

        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/collections'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def search_get_collection(
        self,
        collection: Collection
    ) -> Error:
        """
        Returns the Typesense collection definition (fields, defaults, document count). Requires the `collections:read` action.

        Parameters
        ----------
        collection : Collection
            A collection the tenant owns (see `GET /api/v1/collections`). Resolved to its namespaced Typesense name server-side; a collection the tenant does not own is a 404.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}'
        api_params = {}
        if collection is None:
            raise RevenexxException('Missing required parameter: "collection"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def search_search_documents_get(
        self,
        collection: Collection,
        q: Optional[str] = None,
        query_by: Optional[str] = None,
        filter_by: Optional[str] = None,
        sort_by: Optional[str] = None,
        facet_by: Optional[str] = None,
        max_facet_values: Optional[float] = None,
        group_by: Optional[str] = None,
        include_fields: Optional[str] = None,
        exclude_fields: Optional[str] = None,
        highlight_full_fields: Optional[str] = None,
        num_typos: Optional[float] = None,
        prefix: Optional[str] = None,
        page: Optional[float] = None,
        per_page: Optional[float] = None
    ) -> Error:
        """
        Full-text search within one collection. Typesense search parameters are passed through verbatim as the query string, so parameters not listed here still reach Typesense. Requires the `documents:search` action.

        Parameters
        ----------
        collection : Collection
            A collection the tenant owns (see `GET /api/v1/collections`). Resolved to its namespaced Typesense name server-side; a collection the tenant does not own is a 404.
        q : Optional[str]
            Query text. Use `*` to match everything.
        query_by : Optional[str]
            Comma-separated fields to search, in weight order.
        filter_by : Optional[str]
            Filter expression, e.g. `in_stock:=true && price:<100`. ANDed with the tenant filter the proxy injects.
        sort_by : Optional[str]
            Sort expression, e.g. `price:desc`.
        facet_by : Optional[str]
            Comma-separated fields to facet on.
        max_facet_values : Optional[float]
            Facet values to return per field.
        group_by : Optional[str]
            Comma-separated fields to group results by.
        include_fields : Optional[str]
            Comma-separated document fields to return.
        exclude_fields : Optional[str]
            Comma-separated document fields to omit.
        highlight_full_fields : Optional[str]
            Comma-separated fields to highlight in full.
        num_typos : Optional[float]
            Typos tolerated per query token.
        prefix : Optional[str]
            Whether the last token is a prefix; per-field when comma-separated.
        page : Optional[float]
            1-based page number.
        per_page : Optional[float]
            Hits per page.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}/documents/search'
        api_params = {}
        if collection is None:
            raise RevenexxException('Missing required parameter: "collection"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))

        if q is not None:
            api_params['q'] = self._normalize_value(q)
        if query_by is not None:
            api_params['query_by'] = self._normalize_value(query_by)
        if filter_by is not None:
            api_params['filter_by'] = self._normalize_value(filter_by)
        if sort_by is not None:
            api_params['sort_by'] = self._normalize_value(sort_by)
        if facet_by is not None:
            api_params['facet_by'] = self._normalize_value(facet_by)
        if max_facet_values is not None:
            api_params['max_facet_values'] = self._normalize_value(max_facet_values)
        if group_by is not None:
            api_params['group_by'] = self._normalize_value(group_by)
        if include_fields is not None:
            api_params['include_fields'] = self._normalize_value(include_fields)
        if exclude_fields is not None:
            api_params['exclude_fields'] = self._normalize_value(exclude_fields)
        if highlight_full_fields is not None:
            api_params['highlight_full_fields'] = self._normalize_value(highlight_full_fields)
        if num_typos is not None:
            api_params['num_typos'] = self._normalize_value(num_typos)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if page is not None:
            api_params['page'] = self._normalize_value(page)
        if per_page is not None:
            api_params['per_page'] = self._normalize_value(per_page)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def search_search_documents(
        self,
        collection: Collection,
        exclude_fields: Optional[str] = None,
        facet_by: Optional[str] = None,
        filter_by: Optional[str] = None,
        group_by: Optional[str] = None,
        highlight_full_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        max_facet_values: Optional[float] = None,
        num_typos: Optional[float] = None,
        page: Optional[float] = None,
        per_page: Optional[float] = None,
        prefix: Optional[str] = None,
        q: Optional[str] = None,
        query_by: Optional[str] = None,
        sort_by: Optional[str] = None
    ) -> Error:
        """
        Full-text search within one collection, with the Typesense search parameters in the body. Requires the `documents:search` action.

        Parameters
        ----------
        collection : Collection
            A collection the tenant owns (see `GET /api/v1/collections`). Resolved to its namespaced Typesense name server-side; a collection the tenant does not own is a 404.
        exclude_fields : Optional[str]
            Comma-separated document fields to omit.
        facet_by : Optional[str]
            Comma-separated fields to facet on.
        filter_by : Optional[str]
            Filter expression, e.g. `in_stock:=true && price:<100`. ANDed with the tenant filter the proxy injects.
        group_by : Optional[str]
            Comma-separated fields to group results by.
        highlight_full_fields : Optional[str]
            Comma-separated fields to highlight in full.
        include_fields : Optional[str]
            Comma-separated document fields to return.
        max_facet_values : Optional[float]
            Facet values to return per field.
        num_typos : Optional[float]
            Typos tolerated per query token.
        page : Optional[float]
            1-based page number.
        per_page : Optional[float]
            Hits per page.
        prefix : Optional[str]
            Whether the last token is a prefix; per-field when comma-separated.
        q : Optional[str]
            Query text. Use `*` to match everything.
        query_by : Optional[str]
            Comma-separated fields to search, in weight order.
        sort_by : Optional[str]
            Sort expression, e.g. `price:desc`.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}/documents/search'
        api_params = {}
        if collection is None:
            raise RevenexxException('Missing required parameter: "collection"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))

        if exclude_fields is not None:
            api_params['exclude_fields'] = self._normalize_value(exclude_fields)
        if facet_by is not None:
            api_params['facet_by'] = self._normalize_value(facet_by)
        if filter_by is not None:
            api_params['filter_by'] = self._normalize_value(filter_by)
        if group_by is not None:
            api_params['group_by'] = self._normalize_value(group_by)
        if highlight_full_fields is not None:
            api_params['highlight_full_fields'] = self._normalize_value(highlight_full_fields)
        if include_fields is not None:
            api_params['include_fields'] = self._normalize_value(include_fields)
        if max_facet_values is not None:
            api_params['max_facet_values'] = self._normalize_value(max_facet_values)
        if num_typos is not None:
            api_params['num_typos'] = self._normalize_value(num_typos)
        if page is not None:
            api_params['page'] = self._normalize_value(page)
        if per_page is not None:
            api_params['per_page'] = self._normalize_value(per_page)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if q is not None:
            api_params['q'] = self._normalize_value(q)
        if query_by is not None:
            api_params['query_by'] = self._normalize_value(query_by)
        if sort_by is not None:
            api_params['sort_by'] = self._normalize_value(sort_by)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def search_get_document(
        self,
        collection: Collection,
        document_id: str
    ) -> Error:
        """
        Fetch a single document by id. The document shape is the collection's own schema, so it is described as a free-form object. Requires the `documents:get` action.

        Parameters
        ----------
        collection : Collection
            A collection the tenant owns (see `GET /api/v1/collections`). Resolved to its namespaced Typesense name server-side; a collection the tenant does not own is a 404.
        document_id : str
            The document's `id` within the collection.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}/documents/{documentId}'
        api_params = {}
        if collection is None:
            raise RevenexxException('Missing required parameter: "collection"')

        if document_id is None:
            raise RevenexxException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def gateway_facet_resync(
        self,
        app: Optional[str] = None,
        vendor: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Idempotent, and bounded by the tenant's own configuration: it can add
        no field for an attribute the tenant has not marked `is_filterable`,
        and drops only fields whose attribute it has itself un-marked. A run
        that changes nothing makes zero calls to Typesense.
        
        Body (optional) narrows the sweep to one app:
        
            {"vendor": "revenexx", "app": "products"}
        
        Omitted, every app the tenant has installed is swept. Apps outside the
        facet-sync allowlist are included in the response with
        `skipped: app_not_enabled` rather than silently dropped — a caller
        asking for an app that cannot have facets deserves to be told so.
        
        The response shape below is DECLARED rather than inferred. Its entries
        are built by spreading AttributeFacetSyncer::syncForCollection()'s
        summary, and the generator cannot see through an array spread: left to
        itself it emits an unnamed property and a null in `required`, which
        Spectral rejects as `"1" property must be string`.
        AppController::resyncFacets() carries the same declaration for the same
        reason — keep both in step with syncForApp()'s return type.

        Parameters
        ----------
        app : Optional[str]
            
        vendor : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/facets/resync'
        api_params = {}

        if app is not None:
            api_params['app'] = self._normalize_value(app)
        if vendor is not None:
            api_params['vendor'] = self._normalize_value(vendor)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def search_multi_search(
        self,
        searches: List[MultiSearchEntry]
    ) -> Error:
        """
        Run several searches in one round trip — the endpoint the typesense-js `multiSearch` helper and the InstantSearch adapter use for every query. On the gateway-trust path each entry must name a collection the tenant owns. With a `revx_` key `collection_name` is optional and is forced to the key's own collection. Requires the `documents:search` action.

        Parameters
        ----------
        searches : List[MultiSearchEntry]
            The searches to run, in order. Must not be empty.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/search/multi_search'
        api_params = {}
        if searches is None:
            raise RevenexxException('Missing required parameter: "searches"')


        api_params['searches'] = self._normalize_value(searches)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

