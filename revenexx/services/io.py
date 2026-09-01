from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.validation_failed_response import ValidationFailedResponse;
from ..enums.format import Format;
from ..enums.mode import Mode;
from ..enums.create_import_target import CreateImportTarget;
from ..enums.direction import Direction;
from ..enums.apply_mode import ApplyMode;

class Io(Service):

    def __init__(self, client) -> None:
        super(Io, self).__init__(client)

    def list_bulk_jobs(
        self,
        type: Optional[Any] = None,
        status: Optional[Any] = None,
        vendor: Optional[str] = None,
        app: Optional[str] = None,
        entity: Optional[str] = None,
        limit: Optional[float] = None
    ) -> ValidationFailedResponse:
        """
        The calling tenant's bulk jobs, newest first. Jobs are created by the
        feature blocks (import / export / A/B swap / tenant copy / sample) —
        never here; this surface is read-only.
        

        Parameters
        ----------
        type : Optional[Any]
            
        status : Optional[Any]
            
        vendor : Optional[str]
            
        app : Optional[str]
            
        entity : Optional[str]
            
        limit : Optional[float]
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/bulk-jobs'
        api_params = {}

        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if vendor is not None:
            api_params['vendor'] = self._normalize_value(vendor)
        if app is not None:
            api_params['app'] = self._normalize_value(app)
        if entity is not None:
            api_params['entity'] = self._normalize_value(entity)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def get_bulk_job(
        self,
        id: str
    ) -> ValidationFailedResponse:
        """
        Status, row counts, and progress for one bulk job.
        
        Tenant-scoped: an id belonging to another tenant is filtered out and
        is therefore indistinguishable from a non-existent one — which is the
        intent.
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/bulk-jobs/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def list_io_entities(
        self
    ) -> ValidationFailedResponse:
        """
        Flat list of the entities the calling tenant's installed apps expose,
        sorted by vendor, app, entity. Feeds the entity pickers of the
        Integration Studio I/O nodes.
        
        The app set comes from `baseline.tenant_app_versions`. Per app the
        entity list is resolved from the tenant's pinned schema version; when
        that pointer is stale (missing or not applied) it falls back to the
        latest applied version of `(vendor, app)`. Apps with no applied
        schema at all contribute no entities.
        

        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/entities'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def create_export(
        self,
        app: str,
        entity: str,
        vendor: str,
        format: Optional[Format] = None,
        profile_id: Optional[str] = None
    ) -> ValidationFailedResponse:
        """
        Creates a `bulk_job` and dispatches the engine to export the tenant's
        rows for an entity. CSV/XML stream row-by-row into an S3 multipart
        upload (flat RAM); JSON/XLSX are buffered. The response carries the
        object key the result will be written to.
        

        Parameters
        ----------
        app : str
            
        entity : str
            
        vendor : str
            
        format : Optional[Format]
            
        profile_id : Optional[str]
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/exports'
        api_params = {}
        if app is None:
            raise RevenexxException('Missing required parameter: "app"')

        if entity is None:
            raise RevenexxException('Missing required parameter: "entity"')

        if vendor is None:
            raise RevenexxException('Missing required parameter: "vendor"')


        api_params['app'] = self._normalize_value(app)
        api_params['entity'] = self._normalize_value(entity)
        if format is not None:
            api_params['format'] = self._normalize_value(format)
        if profile_id is not None:
            api_params['profile_id'] = self._normalize_value(profile_id)
        api_params['vendor'] = self._normalize_value(vendor)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def get_export_url(
        self,
        id: str
    ) -> ValidationFailedResponse:
        """
        Mints a short-TTL signed S3 `GET` URL for the object a completed
        export wrote. Tenant-scoped: an id belonging to another tenant — or
        to a job that is not an export — is indistinguishable from a
        non-existent one and answers `404`.
        
        The job must have reached `completed` or `partial`; any earlier
        state answers `409` and carries the current `job_status`.
        

        Parameters
        ----------
        id : str
            The export job's id.
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/exports/{id}/url'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def create_import(
        self,
        app: str,
        entity: str,
        object_key: str,
        vendor: str,
        format: Optional[Format] = None,
        keys: Optional[List[str]] = None,
        max_rejects: Optional[float] = None,
        mode: Optional[Mode] = None,
        profile_id: Optional[str] = None,
        target: Optional[CreateImportTarget] = None
    ) -> ValidationFailedResponse:
        """
        Creates a `bulk_job` and dispatches the engine to import a previously
        uploaded object into the named entity. The engine streams CSV
        row-by-row (flat RAM at 1M+ rows) and COPYs into the entity's staging
        sibling before a merge / content-hash delta into the target.
        

        Parameters
        ----------
        app : str
            
        entity : str
            
        object_key : str
            
        vendor : str
            
        format : Optional[Format]
            
        keys : Optional[List[str]]
            Natural-key columns for upsert / delta.
        max_rejects : Optional[float]
            Rejected rows tolerated before the import fails. Omit for
            unlimited (reject-and-continue); `0` = fail-fast.
            
        mode : Optional[Mode]
            
        profile_id : Optional[str]
            
        target : Optional[CreateImportTarget]
            `shadow` stages the dataset into the A/B `{table}__shadow`
            sibling for diff + switch-over instead of writing live.
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/imports'
        api_params = {}
        if app is None:
            raise RevenexxException('Missing required parameter: "app"')

        if entity is None:
            raise RevenexxException('Missing required parameter: "entity"')

        if object_key is None:
            raise RevenexxException('Missing required parameter: "object_key"')

        if vendor is None:
            raise RevenexxException('Missing required parameter: "vendor"')


        api_params['app'] = self._normalize_value(app)
        api_params['entity'] = self._normalize_value(entity)
        if format is not None:
            api_params['format'] = self._normalize_value(format)
        if keys is not None:
            api_params['keys'] = self._normalize_value(keys)
        if max_rejects is not None:
            api_params['max_rejects'] = self._normalize_value(max_rejects)
        if mode is not None:
            api_params['mode'] = self._normalize_value(mode)
        api_params['object_key'] = self._normalize_value(object_key)
        if profile_id is not None:
            api_params['profile_id'] = self._normalize_value(profile_id)
        if target is not None:
            api_params['target'] = self._normalize_value(target)
        api_params['vendor'] = self._normalize_value(vendor)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def list_profiles(
        self
    ) -> ValidationFailedResponse:
        """
        The calling tenant's saved profiles, ordered by name.
        
        When `X-Revenexx-Market` is present the listing is filtered to the
        profiles offered for that market — global profiles (`markets: null`)
        plus those whose `markets` contain it. Omit the header to get every
        profile, which is what the management view wants.
        

        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/profiles'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def create_profile(
        self,
        app: str,
        direction: Direction,
        entity: str,
        format: str,
        name: str,
        vendor: str,
        apply_mode: Optional[ApplyMode] = None,
        mapping: Optional[Dict[str, Any]] = None,
        markets: Optional[List[str]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ValidationFailedResponse:
        """
        A tenant-secured, reusable mapping (field rename + transforms + keys)
        for a direction (`import`/`export`), format, and entity. Runnable
        on-click via `/io/profiles/{id}/run`.
        

        Parameters
        ----------
        app : str
            
        direction : Direction
            
        entity : str
            
        format : str
            
        name : str
            
        vendor : str
            
        apply_mode : Optional[ApplyMode]
            
        mapping : Optional[Dict[str, Any]]
            Field mapping. `fields[]` carry `target` (DB column),
            `source` (external name) and ordered `transforms`; `keys[]`
            are natural-key columns. Optional `max_rejects`/`target`
            ride along for import runs.
            
        markets : Optional[List[str]]
            Markets this profile applies to (n:m). Omitted, `null` or
            empty means global — offered for every market.
            
        options : Optional[Dict[str, Any]]
            Free-form per-profile engine options.
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/profiles'
        api_params = {}
        if app is None:
            raise RevenexxException('Missing required parameter: "app"')

        if direction is None:
            raise RevenexxException('Missing required parameter: "direction"')

        if entity is None:
            raise RevenexxException('Missing required parameter: "entity"')

        if format is None:
            raise RevenexxException('Missing required parameter: "format"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        if vendor is None:
            raise RevenexxException('Missing required parameter: "vendor"')


        api_params['app'] = self._normalize_value(app)
        if apply_mode is not None:
            api_params['apply_mode'] = self._normalize_value(apply_mode)
        api_params['direction'] = self._normalize_value(direction)
        api_params['entity'] = self._normalize_value(entity)
        api_params['format'] = self._normalize_value(format)
        if mapping is not None:
            api_params['mapping'] = self._normalize_value(mapping)
        api_params['markets'] = self._normalize_value(markets)
        api_params['name'] = self._normalize_value(name)
        if options is not None:
            api_params['options'] = self._normalize_value(options)
        api_params['vendor'] = self._normalize_value(vendor)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def delete_profile(
        self,
        id: str
    ) -> ValidationFailedResponse:
        """
        Permanently remove a saved profile owned by the calling tenant.
        
        Idempotent, and deliberately not a `404` path: deleting an id that
        does not belong to the tenant still answers `200`, with `deleted: 0`.
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/profiles/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def show_profile(
        self,
        id: str
    ) -> ValidationFailedResponse:
        """
        A single saved profile. Tenant-scoped: an id owned by another tenant
        is indistinguishable from a non-existent one and answers `404`.
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/profiles/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def update_profile(
        self,
        id: str,
        app: str,
        direction: Direction,
        entity: str,
        format: str,
        name: str,
        vendor: str,
        apply_mode: Optional[ApplyMode] = None,
        mapping: Optional[Dict[str, Any]] = None,
        markets: Optional[List[str]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> ValidationFailedResponse:
        """
        Replace a saved profile's mapping, format, or apply mode (tenant-scoped).

        Parameters
        ----------
        id : str
            
        app : str
            
        direction : Direction
            
        entity : str
            
        format : str
            
        name : str
            
        vendor : str
            
        apply_mode : Optional[ApplyMode]
            
        mapping : Optional[Dict[str, Any]]
            Field mapping. `fields[]` carry `target` (DB column),
            `source` (external name) and ordered `transforms`; `keys[]`
            are natural-key columns. Optional `max_rejects`/`target`
            ride along for import runs.
            
        markets : Optional[List[str]]
            Markets this profile applies to (n:m). Omitted, `null` or
            empty means global — offered for every market.
            
        options : Optional[Dict[str, Any]]
            Free-form per-profile engine options.
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/profiles/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if app is None:
            raise RevenexxException('Missing required parameter: "app"')

        if direction is None:
            raise RevenexxException('Missing required parameter: "direction"')

        if entity is None:
            raise RevenexxException('Missing required parameter: "entity"')

        if format is None:
            raise RevenexxException('Missing required parameter: "format"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        if vendor is None:
            raise RevenexxException('Missing required parameter: "vendor"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['app'] = self._normalize_value(app)
        if apply_mode is not None:
            api_params['apply_mode'] = self._normalize_value(apply_mode)
        api_params['direction'] = self._normalize_value(direction)
        api_params['entity'] = self._normalize_value(entity)
        api_params['format'] = self._normalize_value(format)
        if mapping is not None:
            api_params['mapping'] = self._normalize_value(mapping)
        api_params['markets'] = self._normalize_value(markets)
        api_params['name'] = self._normalize_value(name)
        if options is not None:
            api_params['options'] = self._normalize_value(options)
        api_params['vendor'] = self._normalize_value(vendor)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def run_profile(
        self,
        id: str,
        markets: Optional[List[str]] = None,
        object_key: Optional[str] = None
    ) -> ValidationFailedResponse:
        """
        Dispatches the engine using the saved profile. An import run requires
        `object_key` (upload first); an export run writes a generated key.
        

        Parameters
        ----------
        id : str
            
        markets : Optional[List[str]]
            Target market(s) the imported rows are assigned to (n:m).
            Overrides the profile's own `markets` for this run; an
            empty array means global (no assignment).
            
        object_key : Optional[str]
            The uploaded object to import. Required for an import
            run; ignored for an export run, which generates its own
            key. Omitting it on an import answers `422` with
            `RUN_NO_OBJECT`.
            
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/profiles/{id}/run'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if markets is not None:
            api_params['markets'] = self._normalize_value(markets)
        if object_key is not None:
            api_params['object_key'] = self._normalize_value(object_key)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)


    def create_upload(
        self,
        extension: Optional[str] = None
    ) -> ValidationFailedResponse:
        """
        Returns a short-lived signed S3 `PUT` URL (+ required headers) and
        the `object_key` to reference in a subsequent `/io/imports`. The
        client uploads bytes directly to object storage — never through
        Baseline.
        

        Parameters
        ----------
        extension : Optional[str]
            File extension for the generated key.
        
        Returns
        -------
        ValidationFailedResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/io/uploads'
        api_params = {}

        if extension is not None:
            api_params['extension'] = self._normalize_value(extension)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ValidationFailedResponse)

