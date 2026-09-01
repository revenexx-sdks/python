from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;
from ..models.page_menu_item import PageMenuItem;
from ..enums.page_status import PageStatus;
from ..models.seed_result import SeedResult;
from ..models.page_block_tree import PageBlockTree;
from ..models.pages_vocabulary_index import PagesVocabularyIndex;
from ..enums.pages_vocabularies_get_name import PagesVocabulariesGetName;

class Pages(Service):

    def __init__(self, client) -> None:
        super(Pages, self).__init__(client)

    def pages_library_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        bundles: Optional[str] = None,
        text: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The pool an editor picks a reusable block from. A library item is ONE block subtree that many pages share BY REFERENCE — edit the item and every page using it changes — which is what separates it from a template, the other reusable thing here, which copies instead and is at `GET /pages/templates`. So the two filters are the two questions the picker asks: `bundles` narrows to the block types that fit the field being filled, `text` matches the label a person gave the item.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 24, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. A column this entity does not have, or any other shape, is refused with 400.
        bundles : Optional[str]
            Comma-separated block types; an item matching any of them is returned. Note the plural — `?bundle=` (singular) is not read by this route and is ignored. Empty means no filter.
        text : Optional[str]
            Case-insensitive substring search over the item label. Runs in the query, so `page.total` counts the matches. Empty means no search.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/library'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if bundles is not None:
            api_params['bundles'] = self._normalize_value(bundles)
        if text is not None:
            api_params['text'] = self._normalize_value(text)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_library_delete(
        self,
        id: str
    ) -> Error:
        """
        Retires a reusable block. It leaves the picker and every list, but the blocks pointing at it keep their `library_item_id` — the FK's `set null` belongs to a hard delete, and this writes a tombstone. Delivery then skips the expansion for a struck item rather than failing on it, so a page that used it falls back to the block content stored in its own published revision: nothing breaks, but the pages quietly stop tracking each other. Nothing here tells you which pages those are, so establish that before striking it.

        Parameters
        ----------
        id : str
            The library item id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/library/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_library_get(
        self,
        id: str
    ) -> Error:
        """
        The stored subtree behind one reusable block, so a picker can preview what dropping it into a page would produce. Because delivery expands the reference against THIS row at read time, what comes back is also what every page already using the item is currently rendering — which makes this the call to make before editing one.

        Parameters
        ----------
        id : str
            The library item id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/library/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_library_update(
        self,
        id: str,
        bundle: Optional[str] = None,
        label: Optional[str] = None,
        tree: Optional[Dict[str, Any]] = None
    ) -> Error:
        """
        The one write in this app whose blast radius is not a single page. Delivery expands a library reference against this row every time it serves, so replacing `tree` re-renders every page that points at the item — published ones included — without any of them being edited, republished or even touched. Nothing warns you first and no revision records it, because the pages did not change; the item did. Changing `label` or `bundle` only moves the item around the picker. Detaching one page from the item, so it keeps a copy of its own, is an editor mutation and not this route.

        Parameters
        ----------
        id : str
            The library item id.
        bundle : Optional[str]
            The block type this item instantiates. Changing it moves the item to a different part of the picker.
        label : Optional[str]
            What the item is called in the picker.
        tree : Optional[Dict[str, Any]]
            A block and its whole subtree, serialized. Produced by the editor when a selection is made reusable or saved as a template, and instantiated back into real blocks when one is inserted.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/library/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if bundle is not None:
            api_params['bundle'] = self._normalize_value(bundle)
        if label is not None:
            api_params['label'] = self._normalize_value(label)
        if tree is not None:
            api_params['tree'] = self._normalize_value(tree)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_menus_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The management view of the menus a tenant keeps — `main`, `footer`, `account` and whatever else the theme asks for, each with the key it is looked up by. This route reads no filter at all — a `?menu_key=` is ignored, which the empty `filter` echo shows — so fetch a page and pick, or address one by id.

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

        api_path = '/v1/pages/menus'
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


    def pages_menus_upsert(
        self,
        label: str,
        menu_key: str,
        items: Optional[List[PageMenuItem]] = None
    ) -> Error:
        """
        Writes a menu by its KEY rather than by its id, which is what makes theme seeding safe to repeat: a key the tenant already has has its label and items replaced in place, a key it does not have is created. `items` is replaced wholesale and never merged, so sending an empty list empties the navigation. One caveat worth reading before you rely on the idempotence: the key's uniqueness is this route's doing and not the database's — `menu_key` carries an index but no unique constraint — so a duplicate key created any other way leaves this route updating whichever row it finds first.

        Parameters
        ----------
        label : str
            What this menu is called for the people who edit it. Required on a create; an update keeps the label it had when this is left out.
        menu_key : str
            The stable slot the theme asks for this menu by. Idempotency is keyed on it: sending an existing key replaces that menu instead of creating a second one.
        items : Optional[List[PageMenuItem]]
            The ordered navigation tree. Replaces the stored one completely.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/menus'
        api_params = {}
        if label is None:
            raise RevenexxException('Missing required parameter: "label"')

        if menu_key is None:
            raise RevenexxException('Missing required parameter: "menu_key"')


        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['label'] = self._normalize_value(label)
        api_params['menuKey'] = self._normalize_value(menu_key)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_menus_delete(
        self,
        id: str
    ) -> Error:
        """
        Writes the tombstone. The menu drops out of the management list and out of `GET /pages/delivery/menus` in the same moment, so a theme that reads its key gets nothing back and renders nothing — there is no fallback and no error a storefront could act on. The key is free immediately, which means re-seeding the theme is the way back. Check what reads the key before striking it.

        Parameters
        ----------
        id : str
            The menu row id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/menus/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_menus_get(
        self,
        id: str
    ) -> Error:
        """
        One menu and its whole item tree — the ordered links a theme renders as its header, footer or account navigation. `items` is nested, not one level, so this is the entire navigation for that key in a single read. Addressed by ROW ID here; the key a theme knows it by is `menu_key` on the body, and the route that works by key is the upsert.

        Parameters
        ----------
        id : str
            The menu row id — not the menu key.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/menus/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_menus_update(
        self,
        id: str,
        items: Optional[List[PageMenuItem]] = None,
        label: Optional[str] = None
    ) -> Error:
        """
        The same write as the upsert, for a caller that already holds the row id — use this when editing a menu a person picked from a list, and the upsert when reconciling a theme's defaults. `menu_key` is deliberately not editable here: the key is the handle every theme reads the menu by, so changing it would empty whatever is rendering that key without anything reporting an error.

        Parameters
        ----------
        id : str
            The menu row id.
        items : Optional[List[PageMenuItem]]
            The ordered navigation tree. Replaces the stored one completely.
        label : Optional[str]
            What this menu is called for the people who edit it.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/menus/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if items is not None:
            api_params['items'] = self._normalize_value(items)
        if label is not None:
            api_params['label'] = self._normalize_value(label)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_pages_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        bundle: Optional[str] = None,
        status: Optional[PageStatus] = None,
        q: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The EDITORIAL index — every live page of the tenant, whatever its status, newest change first. This is the list the Cockpit shows a person: drafts and archived pages are in it, and a row here says nothing about whether a visitor can see the page, because a published status without a published revision still delivers nothing. A storefront wants `GET /pages/delivery/pages` instead, which answers only what is actually servable. Soft-deleted pages are never returned and the predicate is this route's own, not something a caller can switch off.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. A column this entity does not have, or any other shape, is refused with 400.
        bundle : Optional[str]
            Exact page type. The value set belongs to the active theme, so this app constrains it to a non-empty string and nothing more.
        status : Optional[PageStatus]
            Exact lifecycle status.
        q : Optional[str]
            Case-insensitive substring search over the page title. Runs in the query, so `page.total` counts the matches. Empty means no search.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/pages'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if bundle is not None:
            api_params['bundle'] = self._normalize_value(bundle)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if q is not None:
            api_params['q'] = self._normalize_value(q)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_pages_create(
        self,
        title: str,
        bundle: Optional[str] = None,
        host_options: Optional[Dict[str, Any]] = None,
        meta: Optional[Dict[str, Any]] = None,
        slug: Optional[str] = None,
        source_language: Optional[str] = None
    ) -> Error:
        """
        Writes two rows, not one: the page itself and the translation row for its source language, so a page is never without the language it was authored in and `GET /pages/delivery/page?slug=` can match a localized URL from the first moment. Everything the caller leaves out comes from the tenant's settings, not from a literal in this app: `bundle` from default_page_bundle, `sourceLanguage` from default_source_language (resolved for the request's market), and the status of both the page and its source translation from default_page_status (draft | published).

        Parameters
        ----------
        title : str
            What the page is called, in its source language. Shown in the editorial list and searched by `?q=`.
        bundle : Optional[str]
            The page type. Omit to take the default_page_bundle setting.
        host_options : Optional[Dict[str, Any]]
            Page-level blökkli display options as a flat `option key → value` map. Theme-defined; usually left out and set later from the editor.
        meta : Optional[Dict[str, Any]]
            The page's metadata bag (SEO and social fields). Stored and handed back untouched — this app reads no key of it, so the theme decides what goes in.
        slug : Optional[str]
            The path segment the storefront routes it under, without a leading slash. Unique per tenant among live pages; omit or send null for a page reached only by id. Nothing here derives one from the title.
        source_language : Optional[str]
            The language you are authoring in, and the fallback for every later translation. Omit to take the default_source_language setting for the request market.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/pages'
        api_params = {}
        if title is None:
            raise RevenexxException('Missing required parameter: "title"')


        api_params['bundle'] = self._normalize_value(bundle)
        api_params['hostOptions'] = self._normalize_value(host_options)
        api_params['meta'] = self._normalize_value(meta)
        api_params['slug'] = self._normalize_value(slug)
        api_params['sourceLanguage'] = self._normalize_value(source_language)
        api_params['title'] = self._normalize_value(title)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_pages_delete(
        self,
        id: str
    ) -> Error:
        """
        Writes a tombstone. The page leaves every list, every read and all delivery at once, and its slug is immediately free for another page — the unique index counts live rows only. Nothing is erased: the translations, blocks, edit state, revisions, comments and preview grants that hang off the page all keep their rows, because their `on delete cascade` belongs to a hard delete and this is not one. So a page can be brought back intact by clearing `deleted_at` — but not through this app, which publishes no route that does it.

        Parameters
        ----------
        id : str
            The page id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_pages_get(
        self,
        id: str
    ) -> Error:
        """
        One page RECORD: what it is called, where it routes, what type it is, which revision is live. Not its content — the blocks are not on this row and no expansion here returns them. The editor reads them with `GET /pages/editor/{page_id}/state`, a renderer with `GET /pages/delivery/page`. A soft-deleted page answers 404 exactly like one that never existed, so this is also the check for whether an id is still good.

        Parameters
        ----------
        id : str
            The page id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_pages_update(
        self,
        id: str,
        bundle: Optional[str] = None,
        meta: Optional[Dict[str, Any]] = None,
        slug: Optional[str] = None,
        status: Optional[PageStatus] = None,
        title: Optional[str] = None
    ) -> Error:
        """
        Corrects the page RECORD — the five fields an editor changes without opening the visual editor, which are `title`, `slug`, `status`, `meta` and `bundle`, and no others. Anything else in the body is dropped rather than refused, and the block tree is unreachable from here by design: content moves only through the editor's mutation log, so a caller cannot half-edit a page behind the undo history's back. Two consequences worth knowing before you call it: a slug is unique among live pages, so claiming one that is held answers 409; and setting `status` to published does NOT put anything in front of a visitor — delivery needs a revision, which only `POST /pages/editor/{page_id}/publish` writes.

        Parameters
        ----------
        id : str
            The page id.
        bundle : Optional[str]
            The page type. Changing it changes which template the theme renders.
        meta : Optional[Dict[str, Any]]
            The page's metadata bag. Replaced wholesale, not merged.
        slug : Optional[str]
            The path segment the storefront routes it under. Sending a slug another live page holds answers 409; sending null makes the page unreachable by path.
        status : Optional[PageStatus]
            The lifecycle status. Setting `published` here does NOT publish content — delivery still needs a revision, which only `POST /pages/editor/{page_id}/publish` writes.
        title : Optional[str]
            The page title in its source language.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if bundle is not None:
            api_params['bundle'] = self._normalize_value(bundle)
        if meta is not None:
            api_params['meta'] = self._normalize_value(meta)
        api_params['slug'] = self._normalize_value(slug)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if title is not None:
            api_params['title'] = self._normalize_value(title)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_pages_revisions(
        self,
        id: str,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        label: Optional[str] = None,
        created_by: Optional[str] = None,
        created_by_name: Optional[str] = None,
        created_at: Optional[str] = None
    ) -> Error:
        """
        One entry per publication, newest first, which is the order a history is read in and the one this route sorts by unless `order` says otherwise. The `snapshot` — the whole published page, in every language — is deliberately not in the index: it is page-sized, and nothing that renders a history needs it.

        Parameters
        ----------
        id : str
            The page whose history to read.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. A column this entity does not have, or any other shape, is refused with 400.
        label : Optional[str]
            Exact revision label — the name a publication was made under. An equality, not a search.
        created_by : Optional[str]
            Exact user id of whoever published.
        created_by_name : Optional[str]
            Exact display name recorded at publish time.
        created_at : Optional[str]
            Exact publication timestamp, RFC 3339. Equality only — this data plane has no range operator, so walk the history with `order=created_at.desc` and `limit` instead.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}/revisions'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if label is not None:
            api_params['label'] = self._normalize_value(label)
        if created_by is not None:
            api_params['created_by'] = self._normalize_value(created_by)
        if created_by_name is not None:
            api_params['created_by_name'] = self._normalize_value(created_by_name)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_seed(
        self,
        menus: Optional[List[Dict[str, Any]]] = None,
        pages: Optional[List[Dict[str, Any]]] = None
    ) -> SeedResult:
        """
        The target of a theme activation hook: hand it the theme's default pages and menus and it creates whatever is missing. Idempotent by `slug` and by menu key — a slug or a key the tenant already holds is skipped rather than rewritten, so re-running after a theme update adds only the new ones and never overwrites what an editor has since changed. A seeded page is published on the spot, immediately servable by delivery: the default_page_status setting deliberately does not apply, because a theme that activates with invisible pages looks broken.

        Parameters
        ----------
        menus : Optional[List[Dict[str, Any]]]
            The menus to create. One with no key or no label is reported under `skipped`.
        pages : Optional[List[Dict[str, Any]]]
            The pages to create. One that has no `slug` or no `title` is reported under `skipped` rather than refused, so one bad entry never loses the rest.
        
        Returns
        -------
        SeedResult
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/seed'
        api_params = {}

        api_params['menus'] = self._normalize_value(menus)
        api_params['pages'] = self._normalize_value(pages)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=SeedResult)


    def pages_templates_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        id: Optional[str] = None,
        label: Optional[str] = None,
        description: Optional[str] = None,
        page_bundle: Optional[str] = None,
        field_name: Optional[str] = None,
        is_default: Optional[bool] = None,
        created_by: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Every column of a template is an exact-match filter here: `?page_bundle=standard&field_name=content` is how a picker asks for the templates offered in one place, and `?is_default=true` is how a "new page" flow finds the one to start from.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. A column this entity does not have, or any other shape, is refused with 400.
        id : Optional[str]
            Exact template id.
        label : Optional[str]
            Exact label. An equality, not a search — there is no substring search on this route.
        description : Optional[str]
            Exact description text. An equality, so it is the round-trip of the value a picker already showed, not a search.
        page_bundle : Optional[str]
            Exact page type the template is offered on. A template offered everywhere has no page_bundle and is not returned by this filter.
        field_name : Optional[str]
            Exact field the template is offered in.
        is_default : Optional[bool]
            Whether the template is the starting point for new pages of its bundle.
        created_by : Optional[str]
            Exact user id of whoever saved the template.
        created_at : Optional[str]
            Exact creation timestamp, RFC 3339. Equality only — there is no range operator here, so walk the list with `order` instead.
        updated_at : Optional[str]
            Exact last-change timestamp, RFC 3339. Equality only.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/templates'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if label is not None:
            api_params['label'] = self._normalize_value(label)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if page_bundle is not None:
            api_params['page_bundle'] = self._normalize_value(page_bundle)
        if field_name is not None:
            api_params['field_name'] = self._normalize_value(field_name)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if created_by is not None:
            api_params['created_by'] = self._normalize_value(created_by)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_templates_delete(
        self,
        id: str
    ) -> Error:
        """
        Removes the template row outright. This is the one delete in the app that is not a tombstone — `templates` carries no `deleted_at` — so it cannot be undone and the id will not come back. Nothing else breaks by it: pages built from the template hold their own copy of the blocks and never referenced the row.

        Parameters
        ----------
        id : str
            The template id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_templates_get(
        self,
        id: str
    ) -> Error:
        """
        The blocks a page would START from if an editor picked this template — read it to preview the insert. A template is a COPY source, the opposite of a library item: nothing links back from the pages already built from it, so this tells you what future pages get and nothing about existing ones.

        Parameters
        ----------
        id : str
            The template id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_templates_update(
        self,
        id: str,
        description: Optional[str] = None,
        field_name: Optional[str] = None,
        is_default: Optional[bool] = None,
        label: Optional[str] = None,
        page_bundle: Optional[str] = None,
        tree: Optional[List[PageBlockTree]] = None
    ) -> Error:
        """
        Edits what a future page will start from. Because templates copy rather than share, this reaches nothing that already exists — pages built from it keep the blocks they were handed, which is exactly the property that makes a template safe to edit and a library item dangerous. `is_default` is the one field with an effect past the picker: it decides what a new page of `page_bundle` starts with, and nothing here stops two templates of the same bundle from both claiming it, so which one wins is left to whoever reads the list.

        Parameters
        ----------
        id : str
            The template id.
        description : Optional[str]
            A sentence about when to reach for it, shown next to the label.
        field_name : Optional[str]
            The field this template is offered in. Null offers it in every field.
        is_default : Optional[bool]
            Whether a new page of this bundle starts from this template.
        label : Optional[str]
            What the template is called in the picker.
        page_bundle : Optional[str]
            The page type this template is offered on. Null offers it on every page type.
        tree : Optional[List[PageBlockTree]]
            The blocks the template inserts, in order. Replaces the stored tree completely.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['field_name'] = self._normalize_value(field_name)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if label is not None:
            api_params['label'] = self._normalize_value(label)
        api_params['page_bundle'] = self._normalize_value(page_bundle)
        if tree is not None:
            api_params['tree'] = self._normalize_value(tree)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_vocabularies_list(
        self
    ) -> PagesVocabularyIndex:
        """
        Discovery for the vocabulary routes: the enums this app publishes, each with its name, its title and what it is for, and none of them unpacked — the permitted values are not on this route, only on the one that serves a single vocabulary. Names: edit-state-statuses, page-statuses, translation-statuses. Fetch one with GET /pages/vocabularies/{name}; a client holding the qualified pair 'pages.<name>' builds that URL from the pair alone.

        Returns
        -------
        PagesVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PagesVocabularyIndex)


    def pages_vocabularies_get(
        self,
        name: PagesVocabulariesGetName
    ) -> Error:
        """
        One vocabulary unpacked: every value the column permits, each with the title to show for it, the sentence explaining it and the badge tone to render it in — everything a select or a status pill needs, so nothing downstream keeps its own copy of the labels. The values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift — a value added to the constraint appears here even before anyone labels it, titled from its own key. Values come back in constraint order, which is the order a select should offer. 'closed' says the set is exhaustive, so a value outside it is stale data rather than a missing label. Names: edit-state-statuses, page-statuses, translation-statuses.

        Parameters
        ----------
        name : PagesVocabulariesGetName
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

        api_path = '/v1/pages/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

