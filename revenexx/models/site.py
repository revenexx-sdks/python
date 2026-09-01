from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .variable import Variable

class Site(AppwriteModel):
    """
    Site

    Attributes
    ----------
    createdat : str
        Site creation date in ISO 8601 format.
    id : str
        Site ID.
    updatedat : str
        Site update date in ISO 8601 format.
    adapter : str
        Site framework adapter.
    buildcommand : str
        The build command used to build the site.
    buildruntime : str
        Site build runtime.
    deploymentcreatedat : str
        Active deployment creation date in ISO 8601 format.
    deploymentid : str
        Site&#039;s active deployment ID.
    deploymentscreenshotdark : str
        Screenshot of active deployment with dark theme preference file ID.
    deploymentscreenshotlight : str
        Screenshot of active deployment with light theme preference file ID.
    enabled : bool
        Site enabled.
    fallbackfile : str
        Name of the fallback file to serve instead of a 404 page. If null, the site runtime&#039;s built-in 404 page is served.
    framework : str
        Site framework.
    installcommand : str
        The install command used to install the site dependencies.
    installationid : str
        Site VCS (Version Control System) installation id.
    latestdeploymentcreatedat : str
        Latest deployment creation date in ISO 8601 format.
    latestdeploymentid : str
        Site&#039;s latest deployment ID.
    latestdeploymentstatus : str
        Status of latest deployment. Possible values are &quot;waiting&quot;, &quot;processing&quot;, &quot;building&quot;, &quot;ready&quot;, and &quot;failed&quot;.
    live : bool
        Is the site deployed with the latest configuration? This is set to false if you&#039;ve changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the site to update it with the latest configuration.
    logging : bool
        When disabled, request logs will exclude logs and errors, and site responses will be slightly faster.
    name : str
        Site name.
    outputdirectory : str
        The directory where the site build output is located.
    providerbranch : str
        VCS (Version Control System) branch name
    providerrepositoryid : str
        VCS (Version Control System) Repository ID
    providerrootdirectory : str
        Path to site in VCS (Version Control System) repository
    providersilentmode : bool
        Is VCS (Version Control System) connection is in silent mode? When in silence mode, no comments will be posted on the repository pull or merge requests
    specification : str
        Machine specification for builds and executions.
    timeout : float
        Site request timeout in seconds.
    vars : List[Variable]
        Site variables.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    adapter: str = Field(..., alias='adapter')
    buildcommand: str = Field(..., alias='buildCommand')
    buildruntime: str = Field(..., alias='buildRuntime')
    deploymentcreatedat: str = Field(..., alias='deploymentCreatedAt')
    deploymentid: str = Field(..., alias='deploymentId')
    deploymentscreenshotdark: str = Field(..., alias='deploymentScreenshotDark')
    deploymentscreenshotlight: str = Field(..., alias='deploymentScreenshotLight')
    enabled: bool = Field(..., alias='enabled')
    fallbackfile: str = Field(..., alias='fallbackFile')
    framework: str = Field(..., alias='framework')
    installcommand: str = Field(..., alias='installCommand')
    installationid: str = Field(..., alias='installationId')
    latestdeploymentcreatedat: str = Field(..., alias='latestDeploymentCreatedAt')
    latestdeploymentid: str = Field(..., alias='latestDeploymentId')
    latestdeploymentstatus: str = Field(..., alias='latestDeploymentStatus')
    live: bool = Field(..., alias='live')
    logging: bool = Field(..., alias='logging')
    name: str = Field(..., alias='name')
    outputdirectory: str = Field(..., alias='outputDirectory')
    providerbranch: str = Field(..., alias='providerBranch')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
    providersilentmode: bool = Field(..., alias='providerSilentMode')
    specification: str = Field(..., alias='specification')
    timeout: float = Field(..., alias='timeout')
    vars: List[Variable] = Field(..., alias='vars')
