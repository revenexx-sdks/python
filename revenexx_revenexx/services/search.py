from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.collection import Collection;

class Search(Service):

    def __init__(self, client) -> None:
        super(Search, self).__init__(client)

    def search_list_collections(
        self
    ) -> Dict[str, Any]:
        """
        The collections the tenant's installed apps have provisioned.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/search/collections'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def search_search_documents_get(
        self,
        collection: Collection,
        q: Optional[str] = None,
        query_by: Optional[str] = None,
        filter_by: Optional[str] = None,
        sort_by: Optional[str] = None,
        page: Optional[float] = None,
        per_page: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Full-text search within one collection using Typesense query parameters as the query string.

        Parameters
        ----------
        collection : Collection
            Collection key (one the tenant has installed).
        q : Optional[str]
            Query text. Use `*` to match all.
        query_by : Optional[str]
            Comma-separated fields to search.
        filter_by : Optional[str]
            Filter expression.
        sort_by : Optional[str]
            Sort expression.
        page : Optional[float]
            1-based page.
        per_page : Optional[float]
            Hits per page (max 250).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}/documents/search'
        api_params = {}
        if collection is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "collection"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))

        if q is not None:
            api_params['q'] = self._normalize_value(q)
        if query_by is not None:
            api_params['query_by'] = self._normalize_value(query_by)
        if filter_by is not None:
            api_params['filter_by'] = self._normalize_value(filter_by)
        if sort_by is not None:
            api_params['sort_by'] = self._normalize_value(sort_by)
        if page is not None:
            api_params['page'] = self._normalize_value(page)
        if per_page is not None:
            api_params['per_page'] = self._normalize_value(per_page)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def search_search_documents(
        self,
        collection: Collection,
        facet_by: Optional[str] = None,
        filter_by: Optional[str] = None,
        page: Optional[float] = None,
        per_page: Optional[float] = None,
        q: Optional[str] = None,
        query_by: Optional[str] = None,
        sort_by: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Full-text search within one collection. The body holds Typesense search parameters.

        Parameters
        ----------
        collection : Collection
            Collection key (one the tenant has installed).
        facet_by : Optional[str]
            Comma-separated fields to facet on.
        filter_by : Optional[str]
            Filter expression, e.g. `in_stock:=true`.
        page : Optional[float]
            
        per_page : Optional[float]
            
        q : Optional[str]
            Query text. Use `*` to match all.
        query_by : Optional[str]
            Comma-separated fields to search.
        sort_by : Optional[str]
            Sort expression, e.g. `price:desc`.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}/documents/search'
        api_params = {}
        if collection is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "collection"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))

        if facet_by is not None:
            api_params['facet_by'] = self._normalize_value(facet_by)
        if filter_by is not None:
            api_params['filter_by'] = self._normalize_value(filter_by)
        if page is not None:
            api_params['page'] = self._normalize_value(page)
        if per_page is not None:
            api_params['per_page'] = self._normalize_value(per_page)
        if q is not None:
            api_params['q'] = self._normalize_value(q)
        if query_by is not None:
            api_params['query_by'] = self._normalize_value(query_by)
        if sort_by is not None:
            api_params['sort_by'] = self._normalize_value(sort_by)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def search_get_document(
        self,
        collection: Collection,
        document_id: str
    ) -> Dict[str, Any]:
        """
        Fetch a single document by id from a collection the tenant has installed.

        Parameters
        ----------
        collection : Collection
            Collection key (one the tenant has installed).
        document_id : str
            Document id within the collection.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/search/collections/{collection}/documents/{documentId}'
        api_params = {}
        if collection is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "collection"')

        if document_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{collection}', str(self._normalize_value(collection)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def search_multi_search(
        self,
        searches: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Run several searches in one request (the InstantSearch adapter uses this). Each entry names its collection.

        Parameters
        ----------
        searches : List[Dict[str, Any]]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/search/multi_search'
        api_params = {}
        if searches is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "searches"')


        api_params['searches'] = self._normalize_value(searches)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

