from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.page_edit_state_status import PageEditStateStatus;
from ..models.error import Error;
from ..models.mutation_response import MutationResponse;
from ..models.editor_state import EditorState;

class PagesEditor(Service):

    def __init__(self, client) -> None:
        super(PagesEditor, self).__init__(client)

    def pages_editor_edit_states(
        self,
        status: Optional[PageEditStateStatus] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        The drafts overview — the "what is unpublished right now" list, across every page: who holds it, since when, and whether it is parked for a date. Always newest-first — this route does not read `order`. An edit state whose page has been deleted is dropped from `items` but still counted in `total`.

        Parameters
        ----------
        status : Optional[PageEditStateStatus]
            Which kind of working copy to list. Omitted means `active` — the drafts somebody is actually holding, which is what this route is opened for.
        limit : Optional[float]
            Page size (default 50). Unlike the list routes this one applies no ceiling of its own.
        offset : Optional[float]
            Row offset for pagination (default 0).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/edit-states'
        api_params = {}

        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_translate(
        self,
        items: Optional[List[Dict[str, Any]]] = None
    ) -> Error:
        """
        The translation is the tenant's provider's, not this app's, and a tenant that has configured none gets no translation at all. The endpoint comes from the tenant setting `translate_endpoint` (PAGES_TRANSLATE_ENDPOINT remains a fallback). The bearer token does NOT: the gateway masks every setting flagged `sensitive`, so a key stored as one could never be read back — it stays the PAGES_TRANSLATE_KEY function secret. This app does not translate anything itself; it forwards `items` and hands the answer back.

        Parameters
        ----------
        items : Optional[List[Dict[str, Any]]]
            The strings to translate. This app reads no element of the list — the provider defines the contract, and the blökkli adapter sends the fields below.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/translate'
        api_params = {}

        api_params['items'] = self._normalize_value(items)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_user_settings_get(
        self
    ) -> Dict[str, Any]:
        """
        Per-user editor preferences — one row per user, scoped to this app. Not tenant configuration: nothing here changes what the API does, only how one person's editor looks.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/user-settings'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_user_settings_put(
        self,
        settings: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Replaces the caller's preferences wholesale — this is not a merge, so send the whole bag.

        Parameters
        ----------
        settings : Optional[Dict[str, Any]]
            The whole preferences bag — replaced, not merged, so send all of it. Its keys vary by the editor build and this app reads none of them. Null or omitted stores `{}`, which is how a user resets their editor.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/user-settings'
        api_params = {}

        api_params['settings'] = self._normalize_value(settings)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_history(
        self,
        page_id: str,
        index: float,
        langcode: Optional[str] = None
    ) -> MutationResponse:
        """
        Undo and redo. The pointer is the edit state's `current_index`, the position in the mutation log the page is materialized at, and this route is the only thing that moves it — `GET …/state?index=` looks at another position without going there. The log itself is never rewritten — only the pointer moves — so redo stays available until the next change is appended.

        Parameters
        ----------
        page_id : str
            The page being edited.
        index : float
            The position in the mutation log to materialize at. `-1` undoes everything; the last position redoes everything. Values outside the log are clamped rather than refused.
        langcode : Optional[str]
            Which language the returned state should be resolved for.
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/history'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if index is None:
            raise RevenexxException('Missing required parameter: "index"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['index'] = self._normalize_value(index)
        api_params['langcode'] = self._normalize_value(langcode)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_last_changed(
        self,
        page_id: str
    ) -> Dict[str, Any]:
        """
        The cheap poll behind "someone else is editing this page": one integer, the moment the open edit state last moved, in epoch seconds rather than as a timestamp so a comparison is a subtraction. Compare it with the `updatedAt` you last saw and re-fetch the state only when it moved.

        Parameters
        ----------
        page_id : str
            The page being edited.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/last-changed'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_mutation_status(
        self,
        page_id: str,
        enabled: bool,
        index: float,
        langcode: Optional[str] = None
    ) -> MutationResponse:
        """
        Take one change out of the replay without deleting it — "what would the page look like without this edit". The entry stays in the history and can be switched back on.

        Parameters
        ----------
        page_id : str
            The page being edited.
        enabled : bool
            Whether the entry takes part in the replay.
        index : float
            The position in the mutation log to switch. Unknown positions answer 404.
        langcode : Optional[str]
            Which language the returned state should be resolved for.
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/mutation-status'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if enabled is None:
            raise RevenexxException('Missing required parameter: "enabled"')

        if index is None:
            raise RevenexxException('Missing required parameter: "index"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['enabled'] = self._normalize_value(enabled)
        api_params['index'] = self._normalize_value(index)
        api_params['langcode'] = self._normalize_value(langcode)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_mutate(
        self,
        page_id: str,
        plugin: str,
        langcode: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None
    ) -> MutationResponse:
        """
        The one way page CONTENT changes. Each call appends one entry to the append-only log and answers the whole re-materialized state, so a client never re-fetches. A page nobody has opened yet needs no separate call to open it: the first mutation creates the edit state and takes ownership of it, and every later one asks for that ownership, so a second person editing the same page is refused until they take it over. Appending while the pointer sits mid-history discards the redo branch, exactly as an editor expects.

        Parameters
        ----------
        page_id : str
            The page being edited.
        plugin : str
            Which kind of change this is — `add`, `move`, `delete`, `duplicate`, `update_field_value`, `update_options`, … An id this app does not implement is refused with 400 rather than stored, because the log has to replay.
        langcode : Optional[str]
            Which language the returned state should be resolved for. Not the language the change is written in — that lives in the payload.
        payload : Optional[Dict[str, Any]]
            The arguments of that change; the keys depend on the plugin (`add` takes `{ bundle, hostEntityType, hostEntityUuid, hostField }`, `move` takes `{ uuid, preceedingUuid }`, and so on). Anything non-deterministic in it — new uuids, a library item's tree, a copied subtree — is resolved once here and stored, so replaying the log is deterministic forever.
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/mutations'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if plugin is None:
            raise RevenexxException('Missing required parameter: "plugin"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['langcode'] = self._normalize_value(langcode)
        api_params['payload'] = self._normalize_value(payload)
        api_params['plugin'] = self._normalize_value(plugin)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_preview_grant(
        self,
        page_id: str,
        ttl_hours: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Mints a link that shows this page's current edit state — the UNPUBLISHED one — to somebody without an editor account. The token is the whole credential — anyone holding it sees the page — so it expires, and a new one is cheap.

        Parameters
        ----------
        page_id : str
            The page being edited.
        ttl_hours : Optional[float]
            Hours until the link expires. Defaults to 72. After that `GET /pages/delivery/preview/{token}` answers 410 rather than 404, so the holder can tell "expired" from "wrong link".
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/preview-grant'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        if ttl_hours is not None:
            api_params['ttlHours'] = self._normalize_value(ttl_hours)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_publish(
        self,
        page_id: str,
        force: Optional[bool] = None,
        label: Optional[str] = None
    ) -> Error:
        """
        Four things in one call: the mutation log is replayed into a finished block tree, that tree is snapshotted into a new revision, the page's canonical blocks are replaced by it, and the edit state is archived — so the page comes out of this with nothing unpublished and the working copy behind it closed rather than deleted. The revision is written FIRST and the canonical blocks replaced after, so a failure mid-way leaves the page recoverable. Block uuids survive, which is why comments anchored to a block outlive the publish.

        Parameters
        ----------
        page_id : str
            The page being edited.
        force : Optional[bool]
            Publish despite violations. Without it a page with unresolved violations answers 422 and nothing is written.
        label : Optional[str]
            What to call this publication in the page's history — "Autumn campaign" rather than a timestamp.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/publish'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['force'] = self._normalize_value(force)
        api_params['label'] = self._normalize_value(label)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_revert(
        self,
        page_id: str
    ) -> MutationResponse:
        """
        Throws the whole working copy away: the edit state row is deleted and its mutation log with it, so the history goes too — this is not an undo and cannot itself be undone. Unlike publishing, which archives the edit state, nothing of it survives to be reopened. The published page is untouched.

        Parameters
        ----------
        page_id : str
            The page being edited.
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/revert'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_schedule(
        self,
        page_id: str,
        scheduled_at: str
    ) -> Error:
        """
        Gated on the tenant setting `enable_scheduled_publishing`, which is off by default: nothing in the platform publishes a scheduled edit state yet, so a date accepted here would be a promise the app cannot keep. Every editor state carries `features.scheduledPublishing` so the control can be hidden rather than the refusal discovered.

        Parameters
        ----------
        page_id : str
            The page being edited.
        scheduled_at : str
            The moment to publish at. Stored on the edit state and echoed back normalized to UTC.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/schedule'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if scheduled_at is None:
            raise RevenexxException('Missing required parameter: "scheduled_at"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['scheduledAt'] = self._normalize_value(scheduled_at)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_state(
        self,
        page_id: str,
        langcode: Optional[str] = None,
        index: Optional[float] = None
    ) -> EditorState:
        """
        The one call the visual editor boots on, and the only place the UNPUBLISHED page can be seen whole: the canonical blocks with every enabled mutation of the log replayed over them, the resulting field lists, the mutation history itself, who owns the edit state and where the undo pointer sits, and the tenant's editor feature flags. `langcode` decides which language the props resolve in, falling back to the page's source language. `index` replays the log up to a given position instead of the current one, which is how the editor previews an undo without performing it — it changes nothing, so it is safe to call at any position. Reading this creates nothing either: a page nobody has opened answers with a null `editState`, an empty history, and the published blocks as they stand.

        Parameters
        ----------
        page_id : str
            The page being edited.
        langcode : Optional[str]
            Language to resolve every field for. Falls back to the page's source language, per field, so a half-translated page still comes back whole.
        index : Optional[float]
            Materialize the state at this point of the undo history instead of at the pointer the edit state carries. `-1` is "before the first change". It is how a diff view shows what one step did, and it does NOT move the pointer — `POST …/history` does that.
        
        Returns
        -------
        EditorState
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/state'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        if langcode is not None:
            api_params['langcode'] = self._normalize_value(langcode)
        if index is not None:
            api_params['index'] = self._normalize_value(index)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=EditorState)


    def pages_editor_take_ownership(
        self,
        page_id: str
    ) -> MutationResponse:
        """
        One page has one writer. This is how the second person gets the pen — the previous owner is notified rather than silently locked out.

        Parameters
        ----------
        page_id : str
            The page being edited.
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/take-ownership'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_templates_create(
        self,
        page_id: str,
        label: str,
        uuids: List[str],
        description: Optional[str] = None,
        field_name: Optional[str] = None,
        is_default: Optional[bool] = None,
        page_bundle: Optional[str] = None
    ) -> Error:
        """
        Freezes a selection into a reusable starting point. The blocks are read out of the page's CURRENT edit state rather than out of what is published, so a template can be cut from work in progress and the uuids you send are the ones the editor is showing. Unlike making a block reusable, this COPIES: pages later made from the template are independent of it and of each other.

        Parameters
        ----------
        page_id : str
            The page being edited.
        label : str
            What the template is called in the picker.
        uuids : List[str]
            The blocks to serialize into the template, each with its whole subtree. They are read from the CURRENT edit state, so unpublished changes are included.
        description : Optional[str]
            A sentence about when to reach for it.
        field_name : Optional[str]
            The field this template should be offered in. Null offers it in every field.
        is_default : Optional[bool]
            Whether a new page of that type should start from this template.
        page_bundle : Optional[str]
            The page type this template should be offered on. Omit to take the current page's own type.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/templates'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if label is None:
            raise RevenexxException('Missing required parameter: "label"')

        if uuids is None:
            raise RevenexxException('Missing required parameter: "uuids"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['description'] = self._normalize_value(description)
        api_params['fieldName'] = self._normalize_value(field_name)
        api_params['isDefault'] = self._normalize_value(is_default)
        api_params['label'] = self._normalize_value(label)
        api_params['pageBundle'] = self._normalize_value(page_bundle)
        api_params['uuids'] = self._normalize_value(uuids)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_unschedule(
        self,
        page_id: str
    ) -> Dict[str, Any]:
        """
        Takes a parked edit state back to `active` and clears its date, so the scheduled publication simply does not happen. The work is not touched — the mutation log, the undo position and the owner all stay as they were — and the page can then be published by hand or scheduled again for a different date. Like every other write to an edit state it asks for ownership, and a page with no open edit state answers 404 rather than pretending to have cancelled something.

        Parameters
        ----------
        page_id : str
            The page being edited.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/unschedule'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response

