from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .variable import Variable

class Function(AppwriteModel):
    """
    Function

    Attributes
    ----------
    createdat : str
        Function creation date in ISO 8601 format.
    id : str
        Function ID.
    updatedat : str
        Function update date in ISO 8601 format.
    commands : str
        The build command used to build the deployment.
    deploymentcreatedat : str
        Active deployment creation date in ISO 8601 format.
    deploymentid : str
        Function&#039;s active deployment ID.
    enabled : bool
        Function enabled.
    entrypoint : str
        The entrypoint file used to execute the deployment.
    events : List[Any]
        Function trigger events.
    execute : List[Any]
        Execution permissions.
    installationid : str
        Function VCS (Version Control System) installation id.
    latestdeploymentcreatedat : str
        Latest deployment creation date in ISO 8601 format.
    latestdeploymentid : str
        Function&#039;s latest deployment ID.
    latestdeploymentstatus : str
        Status of latest deployment. Possible values are &quot;waiting&quot;, &quot;processing&quot;, &quot;building&quot;, &quot;ready&quot;, and &quot;failed&quot;.
    live : bool
        Is the function deployed with the latest configuration? This is set to false if you&#039;ve changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the function to update it with the latest configuration.
    logging : bool
        When disabled, executions will exclude logs and errors, and will be slightly faster.
    name : str
        Function name.
    providerbranch : str
        VCS (Version Control System) branch name
    providerrepositoryid : str
        VCS (Version Control System) Repository ID
    providerrootdirectory : str
        Path to function in VCS (Version Control System) repository
    providersilentmode : bool
        Is VCS (Version Control System) connection is in silent mode? When in silence mode, no comments will be posted on the repository pull or merge requests
    runtime : str
        Function execution and build runtime.
    schedule : str
        Function execution schedule in CRON format.
    scopes : List[Any]
        Allowed permission scopes.
    specification : str
        Machine specification for builds and executions.
    timeout : float
        Function execution timeout in seconds.
    vars : List[Variable]
        Function variables.
    version : str
        Version of Open Runtimes used for the function.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    commands: str = Field(..., alias='commands')
    deploymentcreatedat: str = Field(..., alias='deploymentCreatedAt')
    deploymentid: str = Field(..., alias='deploymentId')
    enabled: bool = Field(..., alias='enabled')
    entrypoint: str = Field(..., alias='entrypoint')
    events: List[Any] = Field(..., alias='events')
    execute: List[Any] = Field(..., alias='execute')
    installationid: str = Field(..., alias='installationId')
    latestdeploymentcreatedat: str = Field(..., alias='latestDeploymentCreatedAt')
    latestdeploymentid: str = Field(..., alias='latestDeploymentId')
    latestdeploymentstatus: str = Field(..., alias='latestDeploymentStatus')
    live: bool = Field(..., alias='live')
    logging: bool = Field(..., alias='logging')
    name: str = Field(..., alias='name')
    providerbranch: str = Field(..., alias='providerBranch')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
    providersilentmode: bool = Field(..., alias='providerSilentMode')
    runtime: str = Field(..., alias='runtime')
    schedule: str = Field(..., alias='schedule')
    scopes: List[Any] = Field(..., alias='scopes')
    specification: str = Field(..., alias='specification')
    timeout: float = Field(..., alias='timeout')
    vars: List[Variable] = Field(..., alias='vars')
    version: str = Field(..., alias='version')
