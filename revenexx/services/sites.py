from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.site_list import SiteList;
from ..enums.build_runtime import BuildRuntime;
from ..enums.framework import Framework;
from ..enums.adapter import Adapter;
from ..models.site import Site;
from ..models.framework_list import FrameworkList;
from ..models.specification_list import SpecificationList;
from ..models.deployment_list import DeploymentList;
from ..input_file import InputFile
from ..models.deployment import Deployment;
from ..enums.sites_create_template_deployment_type import SitesCreateTemplateDeploymentType;
from ..enums.apps_get_deployment_download_type import AppsGetDeploymentDownloadType;
from ..models.execution_list import ExecutionList;
from ..models.execution import Execution;
from ..models.variable_list import VariableList;
from ..models.variable import Variable;

class Sites(Service):

    def __init__(self, client) -> None:
        super(Sites, self).__init__(client)

    def sites_list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> SiteList:
        """
        Get a list of all the project's sites. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Result filters, paging and ordering. Repeat the parameter once per query — `?queries=…&queries=…` — and make each value a JSON object, e.g. `{"method":"limit","values":[25]}`. The bracketed spellings `queries[]=` and `queries[0]=` are accepted too; the `limit(25)` call syntax is not. See “Query parameters” in this document's introduction. Filterable attributes, besides `$id`, `$createdAt`, `$updatedAt` and `$sequence`: name, enabled, framework, deploymentId, buildCommand, installCommand, outputDirectory, installationId
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        SiteList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SiteList)


    def sites_create(
        self,
        build_runtime: BuildRuntime,
        framework: Framework,
        name: str,
        site_id: str,
        adapter: Optional[Adapter] = None,
        build_command: Optional[str] = None,
        enabled: Optional[bool] = None,
        fallback_file: Optional[str] = None,
        install_command: Optional[str] = None,
        installation_id: Optional[str] = None,
        logging: Optional[bool] = None,
        output_directory: Optional[str] = None,
        provider_branch: Optional[str] = None,
        provider_repository_id: Optional[str] = None,
        provider_root_directory: Optional[str] = None,
        provider_silent_mode: Optional[bool] = None,
        specification: Optional[str] = None,
        timeout: Optional[float] = None
    ) -> Site:
        """
        Create a new site.

        Parameters
        ----------
        build_runtime : BuildRuntime
            Runtime to use during build step.
        framework : Framework
            Sites framework.
        name : str
            Site name. Max length: 128 chars.
        site_id : str
            Site ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        adapter : Optional[Adapter]
            Framework adapter defining rendering strategy. Allowed values are: static, ssr
        build_command : Optional[str]
            Build Command.
        enabled : Optional[bool]
            Is site enabled? When set to 'disabled', users cannot access the site but Server SDKs with and API key can still access the site. No data is lost when this is toggled.
        fallback_file : Optional[str]
            Fallback file for single page application sites.
        install_command : Optional[str]
            Install Command.
        installation_id : Optional[str]
            Installation ID of the platform's VCS (Version Control System) integration to deploy from.
        logging : Optional[bool]
            When disabled, request logs will exclude logs and errors, and site responses will be slightly faster.
        output_directory : Optional[str]
            Output Directory for site.
        provider_branch : Optional[str]
            Production branch for the repo linked to the site.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the site.
        provider_root_directory : Optional[str]
            Path to site code in the linked repo.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the site? In silent mode, comments will not be made on commits and pull requests.
        specification : Optional[str]
            Framework specification for the site and builds.
        timeout : Optional[float]
            Maximum request time in seconds.
        
        Returns
        -------
        Site
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites'
        api_params = {}
        if build_runtime is None:
            raise RevenexxException('Missing required parameter: "build_runtime"')

        if framework is None:
            raise RevenexxException('Missing required parameter: "framework"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')


        if adapter is not None:
            api_params['adapter'] = self._normalize_value(adapter)
        if build_command is not None:
            api_params['buildCommand'] = self._normalize_value(build_command)
        api_params['buildRuntime'] = self._normalize_value(build_runtime)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if fallback_file is not None:
            api_params['fallbackFile'] = self._normalize_value(fallback_file)
        api_params['framework'] = self._normalize_value(framework)
        if install_command is not None:
            api_params['installCommand'] = self._normalize_value(install_command)
        if installation_id is not None:
            api_params['installationId'] = self._normalize_value(installation_id)
        if logging is not None:
            api_params['logging'] = self._normalize_value(logging)
        api_params['name'] = self._normalize_value(name)
        if output_directory is not None:
            api_params['outputDirectory'] = self._normalize_value(output_directory)
        if provider_branch is not None:
            api_params['providerBranch'] = self._normalize_value(provider_branch)
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = self._normalize_value(provider_repository_id)
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = self._normalize_value(provider_root_directory)
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = self._normalize_value(provider_silent_mode)
        api_params['siteId'] = self._normalize_value(site_id)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Site)


    def sites_list_frameworks(
        self
    ) -> FrameworkList:
        """
        Get a list of all frameworks that are currently available on the server instance.

        Returns
        -------
        FrameworkList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/frameworks'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=FrameworkList)


    def sites_list_specifications(
        self
    ) -> SpecificationList:
        """
        List allowed site specifications for this instance.

        Returns
        -------
        SpecificationList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/specifications'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SpecificationList)


    def sites_delete(
        self,
        site_id: str
    ) -> Dict[str, Any]:
        """
        Delete a site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def sites_get(
        self,
        site_id: str
    ) -> Site:
        """
        Get a site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        
        Returns
        -------
        Site
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Site)


    def sites_update(
        self,
        site_id: str,
        framework: Framework,
        name: str,
        adapter: Optional[Adapter] = None,
        build_command: Optional[str] = None,
        build_runtime: Optional[BuildRuntime] = None,
        enabled: Optional[bool] = None,
        fallback_file: Optional[str] = None,
        install_command: Optional[str] = None,
        installation_id: Optional[str] = None,
        logging: Optional[bool] = None,
        output_directory: Optional[str] = None,
        provider_branch: Optional[str] = None,
        provider_repository_id: Optional[str] = None,
        provider_root_directory: Optional[str] = None,
        provider_silent_mode: Optional[bool] = None,
        specification: Optional[str] = None,
        timeout: Optional[float] = None
    ) -> Site:
        """
        Update site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        framework : Framework
            Sites framework.
        name : str
            Site name. Max length: 128 chars.
        adapter : Optional[Adapter]
            Framework adapter defining rendering strategy. Allowed values are: static, ssr
        build_command : Optional[str]
            Build Command.
        build_runtime : Optional[BuildRuntime]
            Runtime to use during build step.
        enabled : Optional[bool]
            Is site enabled? When set to 'disabled', users cannot access the site but Server SDKs with and API key can still access the site. No data is lost when this is toggled.
        fallback_file : Optional[str]
            Fallback file for single page application sites.
        install_command : Optional[str]
            Install Command.
        installation_id : Optional[str]
            Installation ID of the platform's VCS (Version Control System) integration to deploy from.
        logging : Optional[bool]
            When disabled, request logs will exclude logs and errors, and site responses will be slightly faster.
        output_directory : Optional[str]
            Output Directory for site.
        provider_branch : Optional[str]
            Production branch for the repo linked to the site.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the site.
        provider_root_directory : Optional[str]
            Path to site code in the linked repo.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the site? In silent mode, comments will not be made on commits and pull requests.
        specification : Optional[str]
            Framework specification for the site and builds.
        timeout : Optional[float]
            Maximum request time in seconds.
        
        Returns
        -------
        Site
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if framework is None:
            raise RevenexxException('Missing required parameter: "framework"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if adapter is not None:
            api_params['adapter'] = self._normalize_value(adapter)
        if build_command is not None:
            api_params['buildCommand'] = self._normalize_value(build_command)
        if build_runtime is not None:
            api_params['buildRuntime'] = self._normalize_value(build_runtime)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if fallback_file is not None:
            api_params['fallbackFile'] = self._normalize_value(fallback_file)
        api_params['framework'] = self._normalize_value(framework)
        if install_command is not None:
            api_params['installCommand'] = self._normalize_value(install_command)
        if installation_id is not None:
            api_params['installationId'] = self._normalize_value(installation_id)
        if logging is not None:
            api_params['logging'] = self._normalize_value(logging)
        api_params['name'] = self._normalize_value(name)
        if output_directory is not None:
            api_params['outputDirectory'] = self._normalize_value(output_directory)
        if provider_branch is not None:
            api_params['providerBranch'] = self._normalize_value(provider_branch)
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = self._normalize_value(provider_repository_id)
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = self._normalize_value(provider_root_directory)
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = self._normalize_value(provider_silent_mode)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Site)


    def sites_update_site_deployment(
        self,
        site_id: str,
        deployment_id: str
    ) -> Site:
        """
        Update the site active deployment. Use this endpoint to switch the code deployment that should be used when visitor opens your site.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Site
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployment'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise RevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['deploymentId'] = self._normalize_value(deployment_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Site)


    def sites_list_deployments(
        self,
        site_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> DeploymentList:
        """
        Get a list of all the site's code deployments. You can use the query params to filter your results.

        Parameters
        ----------
        site_id : str
            Site ID.
        queries : Optional[List[str]]
            Result filters, paging and ordering. Repeat the parameter once per query — `?queries=…&queries=…` — and make each value a JSON object, e.g. `{"method":"limit","values":[25]}`. The bracketed spellings `queries[]=` and `queries[0]=` are accepted too; the `limit(25)` call syntax is not. See “Query parameters” in this document's introduction. Filterable attributes, besides `$id`, `$createdAt`, `$updatedAt` and `$sequence`: buildSize, sourceSize, totalSize, buildDuration, status, activate, type
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
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=DeploymentList)


    def sites_create_deployment(
        self,
        site_id: str,
        activate: bool,
        code: InputFile,
        build_command: Optional[str] = None,
        install_command: Optional[str] = None,
        output_directory: Optional[str] = None,
        on_progress = None
    ) -> Deployment:
        """
        Create a new site code deployment. Use this endpoint to upload a new version of your site code. To activate your newly uploaded code, you'll need to update the site's deployment to use your new deployment ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        activate : bool
            Automatically activate the deployment when it is finished building.
        code : InputFile
            Your source directory packaged as a gzipped tar archive (`.tar.gz`), sent as the file part of the multipart request.
        build_command : Optional[str]
            Build Commands.
        install_command : Optional[str]
            Install Commands.
        output_directory : Optional[str]
            Output Directory.
                on_progress : callable, optional
            Optional callback for upload progress
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if activate is None:
            raise RevenexxException('Missing required parameter: "activate"')

        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['activate'] = self._normalize_value(str(activate).lower() if type(activate) is bool else activate)
        if build_command is not None:
            api_params['buildCommand'] = self._normalize_value(build_command)
        api_params['code'] = self._normalize_value(code)
        if install_command is not None:
            api_params['installCommand'] = self._normalize_value(install_command)
        if output_directory is not None:
            api_params['outputDirectory'] = self._normalize_value(output_directory)

        param_name = 'code'


        upload_id = ''

        response = self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

        return self._parse_response(response, model=Deployment)


    def sites_create_duplicate_deployment(
        self,
        site_id: str,
        deployment_id: str
    ) -> Deployment:
        """
        Create a new build for an existing site deployment. This endpoint allows you to rebuild a deployment with the updated site configuration, including its commands and output directory if they have been modified. The build process will be queued and executed asynchronously. The original deployment's code will be preserved and used for the new build.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/duplicate'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise RevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['deploymentId'] = self._normalize_value(deployment_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def sites_create_template_deployment(
        self,
        site_id: str,
        owner: str,
        reference: str,
        repository: str,
        root_directory: str,
        type: SitesCreateTemplateDeploymentType,
        activate: Optional[bool] = None
    ) -> Deployment:
        """
        Create a deployment based on a template.
        
        Unlike app templates, site templates have no listing on this API — that catalogue is the vendor's and is not reproduced here. Take `repository`, `owner`, `rootDirectory` and `reference` from wherever the template is published.

        Parameters
        ----------
        site_id : str
            Site ID.
        owner : str
            The name of the owner of the template.
        reference : str
            Reference value, can be a commit hash, branch name, or release tag
        repository : str
            Repository name of the template.
        root_directory : str
            Path to site code in the template repo.
        type : SitesCreateTemplateDeploymentType
            Type for the reference provided. Can be commit, branch, or tag
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/template'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if owner is None:
            raise RevenexxException('Missing required parameter: "owner"')

        if reference is None:
            raise RevenexxException('Missing required parameter: "reference"')

        if repository is None:
            raise RevenexxException('Missing required parameter: "repository"')

        if root_directory is None:
            raise RevenexxException('Missing required parameter: "root_directory"')

        if type is None:
            raise RevenexxException('Missing required parameter: "type"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

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


    def sites_create_vcs_deployment(
        self,
        site_id: str,
        reference: str,
        type: SitesCreateTemplateDeploymentType,
        activate: Optional[bool] = None
    ) -> Deployment:
        """
        Create a deployment when a site is connected to VCS.
        
        This endpoint lets you create deployment from a branch, commit, or a tag.

        Parameters
        ----------
        site_id : str
            Site ID.
        reference : str
            VCS reference to create deployment from. Depending on type this can be: branch name, commit hash
        type : SitesCreateTemplateDeploymentType
            Type of reference passed. Allowed values are: branch, commit
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/vcs'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if reference is None:
            raise RevenexxException('Missing required parameter: "reference"')

        if type is None:
            raise RevenexxException('Missing required parameter: "type"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if activate is not None:
            api_params['activate'] = self._normalize_value(activate)
        api_params['reference'] = self._normalize_value(reference)
        api_params['type'] = self._normalize_value(type)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def sites_delete_deployment(
        self,
        site_id: str,
        deployment_id: str
    ) -> Dict[str, Any]:
        """
        Delete a site deployment by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/{deploymentId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise RevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def sites_get_deployment(
        self,
        site_id: str,
        deployment_id: str
    ) -> Deployment:
        """
        Get a site deployment by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/{deploymentId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise RevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def sites_get_deployment_download(
        self,
        site_id: str,
        deployment_id: str,
        type: Optional[AppsGetDeploymentDownloadType] = None
    ) -> Dict[str, Any]:
        """
        Get a site deployment content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        type : Optional[AppsGetDeploymentDownloadType]
            Deployment file to download. Can be: "source", "output".
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/{deploymentId}/download'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise RevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))

        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def sites_update_deployment_status(
        self,
        site_id: str,
        deployment_id: str
    ) -> Deployment:
        """
        Cancel an ongoing site deployment build. If the build is already in progress, it will be stopped and marked as canceled. If the build hasn't started yet, it will be marked as canceled without executing. You cannot cancel builds that have already completed (status 'ready') or failed. The response includes the final build status and details.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Deployment
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/deployments/{deploymentId}/status'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise RevenexxException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('patch', api_path, {
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def sites_list_logs(
        self,
        site_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ExecutionList:
        """
        Get a list of all site logs. You can use the query params to filter your results.

        Parameters
        ----------
        site_id : str
            Site ID.
        queries : Optional[List[str]]
            Result filters, paging and ordering. Repeat the parameter once per query — `?queries=…&queries=…` — and make each value a JSON object, e.g. `{"method":"limit","values":[25]}`. The bracketed spellings `queries[]=` and `queries[0]=` are accepted too; the `limit(25)` call syntax is not. See “Query parameters” in this document's introduction. Filterable attributes, besides `$id`, `$createdAt`, `$updatedAt` and `$sequence`: trigger, status, responseStatusCode, duration, requestMethod, requestPath, deploymentId
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ExecutionList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/logs'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ExecutionList)


    def sites_delete_log(
        self,
        site_id: str,
        log_id: str
    ) -> Dict[str, Any]:
        """
        Delete a site log by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        log_id : str
            Log ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/logs/{logId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if log_id is None:
            raise RevenexxException('Missing required parameter: "log_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{logId}', str(self._normalize_value(log_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def sites_get_log(
        self,
        site_id: str,
        log_id: str
    ) -> Execution:
        """
        Get a site request log by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        log_id : str
            Log ID.
        
        Returns
        -------
        Execution
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/logs/{logId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if log_id is None:
            raise RevenexxException('Missing required parameter: "log_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{logId}', str(self._normalize_value(log_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Execution)


    def sites_list_variables(
        self,
        site_id: str
    ) -> VariableList:
        """
        Get a list of all variables of a specific site.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        
        Returns
        -------
        VariableList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/variables'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VariableList)


    def sites_create_variable(
        self,
        site_id: str,
        key: str,
        value: str,
        secret: Optional[bool] = None
    ) -> Variable:
        """
        Create a new site variable. These variables can be accessed during build and runtime (server-side rendering) as environment variables.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        key : str
            Variable key. Max length: 255 chars.
        value : str
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only sites can read them during build and runtime.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/variables'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if key is None:
            raise RevenexxException('Missing required parameter: "key"')

        if value is None:
            raise RevenexxException('Missing required parameter: "value"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['key'] = self._normalize_value(key)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)
        api_params['value'] = self._normalize_value(value)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def sites_delete_variable(
        self,
        site_id: str,
        variable_id: str
    ) -> Dict[str, Any]:
        """
        Delete a variable by its unique ID.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        variable_id : str
            Variable unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/variables/{variableId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if variable_id is None:
            raise RevenexxException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def sites_get_variable(
        self,
        site_id: str,
        variable_id: str
    ) -> Variable:
        """
        Get a variable by its unique ID.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        variable_id : str
            Variable unique ID.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/variables/{variableId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if variable_id is None:
            raise RevenexxException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Variable)


    def sites_update_variable(
        self,
        site_id: str,
        variable_id: str,
        key: str,
        secret: Optional[bool] = None,
        value: Optional[str] = None
    ) -> Variable:
        """
        Update variable by its unique ID.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        variable_id : str
            Variable unique ID.
        key : str
            Variable key. Max length: 255 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only sites can read them during build and runtime.
        value : Optional[str]
            Variable value. Max length: 8192 chars.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/sites/{siteId}/variables/{variableId}'
        api_params = {}
        if site_id is None:
            raise RevenexxException('Missing required parameter: "site_id"')

        if variable_id is None:
            raise RevenexxException('Missing required parameter: "variable_id"')

        if key is None:
            raise RevenexxException('Missing required parameter: "key"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
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

