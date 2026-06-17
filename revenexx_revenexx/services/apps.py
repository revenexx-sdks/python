from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.function_list import FunctionList;
from ..enums.runtime import Runtime;
from ..enums.scopes import Scopes;
from ..models.function import Function;
from ..models.runtime_list import RuntimeList;
from ..models.specification_list import SpecificationList;
from ..enums.runtimes import Runtimes;
from ..enums.use_cases import UseCases;
from ..models.template_function_list import TemplateFunctionList;
from ..models.template_function import TemplateFunction;
from ..enums.range import Range;
from ..models.usage_functions import UsageFunctions;
from ..models.deployment_list import DeploymentList;
from ..models.deployment import Deployment;
from ..enums.type import Type;
from ..models.execution_list import ExecutionList;
from ..enums.method import Method;
from ..models.execution import Execution;
from ..models.usage_function import UsageFunction;
from ..models.variable_list import VariableList;
from ..models.variable import Variable;

class Apps(Service):

    def __init__(self, client) -> None:
        super(Apps, self).__init__(client)

    def apps_list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> FunctionList:
        """
        List all Apps in the active project. Pass `search` to filter by name.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, runtime, deploymentId, schedule, scheduleNext, schedulePrevious, timeout, entrypoint, commands, installationId
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        FunctionList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=FunctionList)


    def apps_create(
        self,
        function_id: str,
        name: str,
        runtime: Runtime,
        commands: Optional[str] = None,
        enabled: Optional[bool] = None,
        entrypoint: Optional[str] = None,
        events: Optional[List[str]] = None,
        execute: Optional[List[str]] = None,
        installation_id: Optional[str] = None,
        logging: Optional[bool] = None,
        provider_branch: Optional[str] = None,
        provider_repository_id: Optional[str] = None,
        provider_root_directory: Optional[str] = None,
        provider_silent_mode: Optional[bool] = None,
        schedule: Optional[str] = None,
        scopes: Optional[List[Scopes]] = None,
        specification: Optional[str] = None,
        timeout: Optional[float] = None
    ) -> Function:
        """
        Create a new revenexx App. An App is the deployment surface for code that runs on the platform — backend jobs, APIs, integrations. The created App owns subsequent deployments and executions.
        
        Phase 1 mirrors the underlying Functions runtime 1:1; future phases will add manifest validation, registry coupling and schema migrations.

        Parameters
        ----------
        function_id : str
            Function ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Function name. Max length: 128 chars.
        runtime : Runtime
            Execution runtime.
        commands : Optional[str]
            Build Commands.
        enabled : Optional[bool]
            Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
        entrypoint : Optional[str]
            Entrypoint File. This path is relative to the "providerRootDirectory".
        events : Optional[List[str]]
            Events list. Maximum of 100 events are allowed.
        execute : Optional[List[str]]
            An array of role strings with execution permissions. By default no user is granted with any execute permissions. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        installation_id : Optional[str]
            Appwrite Installation ID for VCS (Version Control System) deployment.
        logging : Optional[bool]
            When disabled, executions will exclude logs and errors, and will be slightly faster.
        provider_branch : Optional[str]
            Production branch for the repo linked to the function.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the function.
        provider_root_directory : Optional[str]
            Path to function code in the linked repo.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
        schedule : Optional[str]
            Schedule CRON syntax.
        scopes : Optional[List[Scopes]]
            List of scopes allowed for API key auto-generated for every execution. Maximum of 100 scopes are allowed.
        specification : Optional[str]
            Runtime specification for the function and builds.
        timeout : Optional[float]
            Function maximum execution time in seconds.
        
        Returns
        -------
        Function
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if runtime is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "runtime"')


        if commands is not None:
            api_params['commands'] = self._normalize_value(commands)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if entrypoint is not None:
            api_params['entrypoint'] = self._normalize_value(entrypoint)
        if events is not None:
            api_params['events'] = self._normalize_value(events)
        if execute is not None:
            api_params['execute'] = self._normalize_value(execute)
        api_params['functionId'] = self._normalize_value(function_id)
        if installation_id is not None:
            api_params['installationId'] = self._normalize_value(installation_id)
        if logging is not None:
            api_params['logging'] = self._normalize_value(logging)
        api_params['name'] = self._normalize_value(name)
        if provider_branch is not None:
            api_params['providerBranch'] = self._normalize_value(provider_branch)
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = self._normalize_value(provider_repository_id)
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = self._normalize_value(provider_root_directory)
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = self._normalize_value(provider_silent_mode)
        api_params['runtime'] = self._normalize_value(runtime)
        if schedule is not None:
            api_params['schedule'] = self._normalize_value(schedule)
        if scopes is not None:
            api_params['scopes'] = self._normalize_value(scopes)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Function)


    def apps_list_marketplace(
        self,
        search: Optional[str] = None,
        per_page: Optional[float] = None,
        page: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        List apps published to the Marketplace. Proxies the App Registry on Console with `?published=true` filter.

        Parameters
        ----------
        search : Optional[str]
            Search by app name, title or vendor.
        per_page : Optional[float]
            Items per page.
        page : Optional[float]
            Page number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/marketplace'
        api_params = {}

        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if per_page is not None:
            api_params['per_page'] = self._normalize_value(per_page)
        if page is not None:
            api_params['page'] = self._normalize_value(page)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def apps_install_from_marketplace(
        self,
        name: str,
        owner: str
    ) -> Dict[str, Any]:
        """
        Install a Marketplace app on the calling project's tenant. Body: { owner, name }.

        Parameters
        ----------
        name : str
            App name.
        owner : str
            Owner tenant slug of the app being installed.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/marketplace/install'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if owner is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "owner"')


        api_params['name'] = self._normalize_value(name)
        api_params['owner'] = self._normalize_value(owner)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def apps_list_runtimes(
        self
    ) -> RuntimeList:
        """
        Get a list of all runtimes available for an App. Identical content to `functions.listRuntimes()`.

        Returns
        -------
        RuntimeList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/runtimes'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=RuntimeList)


    def apps_list_specifications(
        self
    ) -> SpecificationList:
        """
        List the compute specifications (CPU + memory) available to Apps in this project.

        Returns
        -------
        SpecificationList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/specifications'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SpecificationList)


    def apps_list_templates(
        self,
        runtimes: Optional[List[Runtimes]] = None,
        use_cases: Optional[List[UseCases]] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        total: Optional[bool] = None
    ) -> TemplateFunctionList:
        """
        List the curated catalogue of App templates that can be used as starting points.

        Parameters
        ----------
        runtimes : Optional[List[Runtimes]]
            List of runtimes allowed for filtering function templates. Maximum of 100 runtimes are allowed.
        use_cases : Optional[List[UseCases]]
            List of use cases allowed for filtering function templates. Maximum of 100 use cases are allowed.
        limit : Optional[float]
            Limit the number of templates returned in the response. Default limit is 25, and maximum limit is 5000.
        offset : Optional[float]
            Offset the list of returned templates. Maximum offset is 5000.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        TemplateFunctionList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/templates'
        api_params = {}

        if runtimes is not None:
            api_params['runtimes'] = self._normalize_value(runtimes)
        if use_cases is not None:
            api_params['useCases'] = self._normalize_value(use_cases)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TemplateFunctionList)


    def apps_get_template(
        self,
        template_id: str
    ) -> TemplateFunction:
        """
        Get a single App template by its ID.

        Parameters
        ----------
        template_id : str
            Template ID.
        
        Returns
        -------
        TemplateFunction
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/templates/{templateId}'
        api_params = {}
        if template_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "template_id"')

        api_path = api_path.replace('{templateId}', str(self._normalize_value(template_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TemplateFunction)


    def apps_list_usage(
        self,
        range: Optional[Range] = None
    ) -> UsageFunctions:
        """
        Get aggregated usage stats across all Apps in the project for the requested time range.

        Parameters
        ----------
        range : Optional[Range]
            Date range.
        
        Returns
        -------
        UsageFunctions
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/usage'
        api_params = {}

        if range is not None:
            api_params['range'] = self._normalize_value(range)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=UsageFunctions)


    def apps_delete(
        self,
        function_id: str
    ) -> Dict[str, Any]:
        """
        Delete an App and all of its deployments. Cascades to the App Registry — Console removes the matching `RegisteredApp` row.

        Parameters
        ----------
        function_id : str
            App ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def apps_get(
        self,
        function_id: str
    ) -> Function:
        """
        Get an App by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        
        Returns
        -------
        Function
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Function)


    def apps_update(
        self,
        function_id: str,
        name: str,
        commands: Optional[str] = None,
        enabled: Optional[bool] = None,
        entrypoint: Optional[str] = None,
        events: Optional[List[str]] = None,
        execute: Optional[List[str]] = None,
        installation_id: Optional[str] = None,
        logging: Optional[bool] = None,
        provider_branch: Optional[str] = None,
        provider_repository_id: Optional[str] = None,
        provider_root_directory: Optional[str] = None,
        provider_silent_mode: Optional[bool] = None,
        runtime: Optional[Runtime] = None,
        schedule: Optional[str] = None,
        scopes: Optional[List[Scopes]] = None,
        specification: Optional[str] = None,
        timeout: Optional[float] = None
    ) -> Function:
        """
        Update an App. Use this endpoint to rename, change runtime, schedule, environment variables and other configuration.

        Parameters
        ----------
        function_id : str
            Function ID.
        name : str
            Function name. Max length: 128 chars.
        commands : Optional[str]
            Build Commands.
        enabled : Optional[bool]
            Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
        entrypoint : Optional[str]
            Entrypoint File. This path is relative to the "providerRootDirectory".
        events : Optional[List[str]]
            Events list. Maximum of 100 events are allowed.
        execute : Optional[List[str]]
            An array of role strings with execution permissions. By default no user is granted with any execute permissions. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        installation_id : Optional[str]
            Appwrite Installation ID for VCS (Version Controle System) deployment.
        logging : Optional[bool]
            When disabled, executions will exclude logs and errors, and will be slightly faster.
        provider_branch : Optional[str]
            Production branch for the repo linked to the function
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the function
        provider_root_directory : Optional[str]
            Path to function code in the linked repo.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
        runtime : Optional[Runtime]
            Execution runtime.
        schedule : Optional[str]
            Schedule CRON syntax.
        scopes : Optional[List[Scopes]]
            List of scopes allowed for API Key auto-generated for every execution. Maximum of 100 scopes are allowed.
        specification : Optional[str]
            Runtime specification for the function and builds.
        timeout : Optional[float]
            Maximum execution time in seconds.
        
        Returns
        -------
        Function
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if commands is not None:
            api_params['commands'] = self._normalize_value(commands)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if entrypoint is not None:
            api_params['entrypoint'] = self._normalize_value(entrypoint)
        if events is not None:
            api_params['events'] = self._normalize_value(events)
        if execute is not None:
            api_params['execute'] = self._normalize_value(execute)
        if installation_id is not None:
            api_params['installationId'] = self._normalize_value(installation_id)
        if logging is not None:
            api_params['logging'] = self._normalize_value(logging)
        api_params['name'] = self._normalize_value(name)
        if provider_branch is not None:
            api_params['providerBranch'] = self._normalize_value(provider_branch)
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = self._normalize_value(provider_repository_id)
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = self._normalize_value(provider_root_directory)
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = self._normalize_value(provider_silent_mode)
        if runtime is not None:
            api_params['runtime'] = self._normalize_value(runtime)
        if schedule is not None:
            api_params['schedule'] = self._normalize_value(schedule)
        if scopes is not None:
            api_params['scopes'] = self._normalize_value(scopes)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Function)


    def apps_update_deployment(
        self,
        function_id: str,
        deployment_id: str
    ) -> Function:
        """
        Set the active deployment for an App. The chosen deployment must already be `ready`.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Function
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployment'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        api_params['deploymentId'] = self._normalize_value(deployment_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Function)


    def apps_list_deployments(
        self,
        function_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> DeploymentList:
        """
        List the deployment history of an App.

        Parameters
        ----------
        function_id : str
            Function ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: buildSize, sourceSize, totalSize, buildDuration, status, activate, type
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        DeploymentList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=DeploymentList)


    def apps_create_deployment(
        self,
        function_id: str,
        activate: bool,
        code: str,
        commands: Optional[str] = None,
        entrypoint: Optional[str] = None,
        on_progress = None
    ) -> Deployment:
        """
        Upload a new code deployment for an App. Accepts a `.tar.gz`
        archive containing the App source. Phase 2 will extract the
        manifest from this archive and validate it against the App
        Registry before kicking off the build.

        Parameters
        ----------
        function_id : str
            Function ID.
        activate : bool
            Automatically activate the deployment when it is finished building.
        code : str
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
        commands : Optional[str]
            Build Commands.
        entrypoint : Optional[str]
            Entrypoint File.
                on_progress : callable, optional
            Optional callback for upload progress
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if activate is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "activate"')

        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        api_params['activate'] = self._normalize_value(str(activate).lower() if type(activate) is bool else activate)
        api_params['code'] = self._normalize_value(code)
        if commands is not None:
            api_params['commands'] = self._normalize_value(commands)
        if entrypoint is not None:
            api_params['entrypoint'] = self._normalize_value(entrypoint)


        upload_id = ''

        response = self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

        return self._parse_response(response, model=Deployment)


    def apps_create_duplicate_deployment(
        self,
        function_id: str,
        deployment_id: str,
        build_id: Optional[str] = None
    ) -> Deployment:
        """
        Re-deploy an existing build under a new deployment ID. Useful for promoting a known-good preview build to production without rebuilding.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        build_id : Optional[str]
            Build unique ID.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/duplicate'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if build_id is not None:
            api_params['buildId'] = self._normalize_value(build_id)
        api_params['deploymentId'] = self._normalize_value(deployment_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def apps_create_template_deployment(
        self,
        function_id: str,
        owner: str,
        reference: str,
        repository: str,
        root_directory: str,
        type: Type,
        activate: Optional[bool] = None
    ) -> Deployment:
        """
        Create a new App deployment from a template in the App Templates catalogue.

        Parameters
        ----------
        function_id : str
            Function ID.
        owner : str
            The name of the owner of the template.
        reference : str
            Reference value, can be a commit hash, branch name, or release tag
        repository : str
            Repository name of the template.
        root_directory : str
            Path to function code in the template repo.
        type : Type
            Type for the reference provided. Can be commit, branch, or tag
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/template'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if owner is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "owner"')

        if reference is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "reference"')

        if repository is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "repository"')

        if root_directory is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "root_directory"')

        if type is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "type"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if activate is not None:
            api_params['activate'] = self._normalize_value(activate)
        api_params['owner'] = self._normalize_value(owner)
        api_params['reference'] = self._normalize_value(reference)
        api_params['repository'] = self._normalize_value(repository)
        api_params['rootDirectory'] = self._normalize_value(root_directory)
        api_params['type'] = self._normalize_value(type)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def apps_create_vcs_deployment(
        self,
        function_id: str,
        reference: str,
        type: Type,
        activate: Optional[bool] = None
    ) -> Deployment:
        """
        Trigger a new deployment from the App's connected Git repository.

        Parameters
        ----------
        function_id : str
            Function ID.
        reference : str
            VCS reference to create deployment from. Depending on type this can be: branch name, commit hash
        type : Type
            Type of reference passed. Allowed values are: branch, commit
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/vcs'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if reference is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "reference"')

        if type is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "type"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if activate is not None:
            api_params['activate'] = self._normalize_value(activate)
        api_params['reference'] = self._normalize_value(reference)
        api_params['type'] = self._normalize_value(type)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def apps_delete_deployment(
        self,
        function_id: str,
        deployment_id: str
    ) -> Dict[str, Any]:
        """
        Delete a deployment. The active deployment cannot be deleted while it is active — switch first via the deployment-update endpoint.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def apps_get_deployment(
        self,
        function_id: str,
        deployment_id: str
    ) -> Deployment:
        """
        Get a deployment by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def apps_get_deployment_download(
        self,
        function_id: str,
        deployment_id: str,
        type: Optional[Type] = None
    ) -> Dict[str, Any]:
        """
        Get a redirect URL to download the source archive of an App deployment. Useful for re-running a build locally or auditing what was deployed.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        type : Optional[Type]
            Deployment file to download. Can be: "source", "output".
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/{deploymentId}/download'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))

        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def apps_update_deployment_status(
        self,
        function_id: str,
        deployment_id: str
    ) -> Deployment:
        """
        Cancel an in-progress deployment build. Used by the Cockpit "Cancel build" affordance.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/deployments/{deploymentId}/status'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('patch', api_path, {
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def apps_list_executions(
        self,
        function_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ExecutionList:
        """
        List the execution history of an App.

        Parameters
        ----------
        function_id : str
            Function ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: trigger, status, responseStatusCode, duration, requestMethod, requestPath, deploymentId
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ExecutionList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/executions'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ExecutionList)


    def apps_create_execution(
        self,
        function_id: str,
        xasync: Optional[bool] = None,
        body: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        method: Optional[Method] = None,
        path: Optional[str] = None,
        scheduled_at: Optional[str] = None
    ) -> Execution:
        """
        Trigger an App execution. Use the optional `body`, `path`, `method` and `headers` parameters to invoke the App as if from an HTTP request.

        Parameters
        ----------
        function_id : str
            Function ID.
        xasync : Optional[bool]
            Execute code in the background. Default value is false.
        body : Optional[str]
            HTTP body of execution. Default value is empty string.
        headers : Optional[Dict[str, Any]]
            HTTP headers of execution. Defaults to empty.
        method : Optional[Method]
            HTTP method of execution. Default value is POST.
        path : Optional[str]
            HTTP path of execution. Path can include query params. Default value is /
        scheduled_at : Optional[str]
            Scheduled execution time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future with precision in minutes.
        
        Returns
        -------
        Execution
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/executions'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if xasync is not None:
            api_params['async'] = self._normalize_value(xasync)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if headers is not None:
            api_params['headers'] = self._normalize_value(headers)
        if method is not None:
            api_params['method'] = self._normalize_value(method)
        if path is not None:
            api_params['path'] = self._normalize_value(path)
        if scheduled_at is not None:
            api_params['scheduledAt'] = self._normalize_value(scheduled_at)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Execution)


    def apps_delete_execution(
        self,
        function_id: str,
        execution_id: str
    ) -> Dict[str, Any]:
        """
        Delete an App execution by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        execution_id : str
            Execution ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/executions/{executionId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "execution_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{executionId}', str(self._normalize_value(execution_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def apps_get_execution(
        self,
        function_id: str,
        execution_id: str
    ) -> Execution:
        """
        Get an App execution by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        execution_id : str
            Execution ID.
        
        Returns
        -------
        Execution
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/executions/{executionId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "execution_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{executionId}', str(self._normalize_value(execution_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Execution)


    def apps_get_marketplace_status(
        self,
        function_id: str
    ) -> Dict[str, Any]:
        """
        Read-through view of the App's App Registry row — visibility + Marketplace publish flag. Used by Cockpit to render the Publish/Unpublish button correctly on cold load.

        Parameters
        ----------
        function_id : str
            App ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/marketplace-status'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def apps_unpublish(
        self,
        function_id: str
    ) -> Dict[str, Any]:
        """
        Remove this App from the Marketplace listing. Existing tenant installations are unaffected. Idempotent.

        Parameters
        ----------
        function_id : str
            App ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/publish'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def apps_publish(
        self,
        function_id: str
    ) -> Dict[str, Any]:
        """
        Publish this App to the Marketplace. The App must have at
        least one `ready` deployment with a registered manifest,
        and its visibility (derived from `billing.json`) must be
        `public` or `included`. Idempotent.

        Parameters
        ----------
        function_id : str
            App ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/publish'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def apps_get_usage(
        self,
        function_id: str,
        range: Optional[Range] = None
    ) -> UsageFunction:
        """
        Get usage stats for a single App over the requested time range.

        Parameters
        ----------
        function_id : str
            Function ID.
        range : Optional[Range]
            Date range.
        
        Returns
        -------
        UsageFunction
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/usage'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        if range is not None:
            api_params['range'] = self._normalize_value(range)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=UsageFunction)


    def apps_list_variables(
        self,
        function_id: str
    ) -> VariableList:
        """
        List all environment variables defined for the App.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        
        Returns
        -------
        VariableList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/variables'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VariableList)


    def apps_create_variable(
        self,
        function_id: str,
        key: str,
        value: str,
        secret: Optional[bool] = None
    ) -> Variable:
        """
        Create a new App environment variable. These are passed into the App at runtime as `process.env.*`.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        key : str
            Variable key. Max length: 255 chars.
        value : str
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only functions can read them during build and runtime.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/variables'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if key is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "key"')

        if value is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "value"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))

        api_params['key'] = self._normalize_value(key)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)
        api_params['value'] = self._normalize_value(value)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def apps_delete_variable(
        self,
        function_id: str,
        variable_id: str
    ) -> Dict[str, Any]:
        """
        Delete an App environment variable.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        variable_id : str
            Variable unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def apps_get_variable(
        self,
        function_id: str,
        variable_id: str
    ) -> Variable:
        """
        Get an App variable by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        variable_id : str
            Variable unique ID.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Variable)


    def apps_update_variable(
        self,
        function_id: str,
        variable_id: str,
        key: str,
        secret: Optional[bool] = None,
        value: Optional[str] = None
    ) -> Variable:
        """
        Update an App environment variable.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        variable_id : str
            Variable unique ID.
        key : str
            Variable key. Max length: 255 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only functions can read them during build and runtime.
        value : Optional[str]
            Variable value. Max length: 8192 chars.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/apps/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "variable_id"')

        if key is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "key"')

        api_path = api_path.replace('{functionId}', str(self._normalize_value(function_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))

        api_params['key'] = self._normalize_value(key)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)
        if value is not None:
            api_params['value'] = self._normalize_value(value)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)

