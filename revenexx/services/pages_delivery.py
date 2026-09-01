from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;

class PagesDelivery(Service):

    def __init__(self, client) -> None:
        super(PagesDelivery, self).__init__(client)

    def pages_delivery_menus(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        One call gives a theme its whole chrome: header, footer and account navigation, each under the key the theme looks it up by. This route reads no filter — fetch all of them once and index by `id`.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. A column this entity does not have, or any other shape, is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/delivery/menus'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_delivery_page(
        self,
        slug: Optional[str] = None,
        id: Optional[str] = None,
        langcode: Optional[str] = None
    ) -> Error:
        """
        What a storefront calls to render a URL: `GET /pages/delivery/page?slug=about-us&langcode=de`. Send exactly one selector — `slug` or `id`. `slug` is matched against the page and then against its translations, so a localized URL resolves to its page. Only the PUBLISHED revision is served, so an edit in progress never leaks. What comes back is finished rather than raw: `langcode` is resolved field by field with the page's source language behind it, blocks whose publish window has not opened or has already closed are left out, and every library reference is expanded into the subtree it points at — so a renderer walks the tree it is given and makes no second call for any of it.

        Parameters
        ----------
        slug : Optional[str]
            The page slug, or the slug of one of its translations, without a leading slash — the path segment the storefront routes. Either this or `id`.
        id : Optional[str]
            The page id, for a storefront that already holds one (from `GET /pages/delivery/pages`). Either this or `slug`.
        langcode : Optional[str]
            Language to resolve the tree for, e.g. `de`. Falls back to the page's source language per field, so a partly translated page still renders whole.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/delivery/page'
        api_params = {}

        if slug is not None:
            api_params['slug'] = self._normalize_value(slug)
        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if langcode is not None:
            api_params['langcode'] = self._normalize_value(langcode)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_delivery_pages(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        bundle: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The route a sitemap, a static build or a link picker is generated from. Only published pages, never a soft-deleted one — `filter` echoes both predicates the route applies on its own. A `?status=` of your own is ignored: this route is the published view by definition.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 100, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. A column this entity does not have, or any other shape, is refused with 400.
        bundle : Optional[str]
            Exact page type — how a theme asks for just its landing pages. The value set belongs to the active theme.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/delivery/pages'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if bundle is not None:
            api_params['bundle'] = self._normalize_value(bundle)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_delivery_preview(
        self,
        token: str,
        langcode: Optional[str] = None
    ) -> Error:
        """
        The same shape `GET /pages/delivery/page` answers, built from the UNPUBLISHED working copy instead of the published revision — so a reviewer without an editor account sees exactly what the storefront would render.

        Parameters
        ----------
        token : str
            The token handed out by POST /pages/editor/{page_id}/preview-grant.
        langcode : Optional[str]
            Language to resolve the tree for. Falls back to the page's source language, per field.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/delivery/preview/{token}'
        api_params = {}
        if token is None:
            raise RevenexxException('Missing required parameter: "token"')

        api_path = api_path.replace('{token}', str(self._normalize_value(token)))

        if langcode is not None:
            api_params['langcode'] = self._normalize_value(langcode)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

