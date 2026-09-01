from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.deployment_status import DeploymentStatus

class Deployment(AppwriteModel):
    """
    Deployment

    Attributes
    ----------
    createdat : str
        Deployment creation date in ISO 8601 format.
    id : str
        Deployment ID.
    updatedat : str
        Deployment update date in ISO 8601 format.
    activate : bool
        Whether the deployment should be automatically activated.
    billingjson : str
        Raw billing.json bytes captured from the source archive at deploy time. Empty when no billing.json was shipped (private app).
    buildduration : float
        The current build time in seconds.
    buildid : str
        The current build ID.
    buildlogs : str
        The build logs.
    buildsize : float
        The build output size in bytes.
    entrypoint : str
        The entrypoint file to use to execute the deployment code.
    manifestjson : str
        Raw manifest.json bytes captured from the source archive at deploy time. Empty for legacy Function/Site deployments without a manifest.
    providerbranch : str
        The branch of the vcs repository
    providerbranchurl : str
        The branch of the vcs repository
    providercommitauthor : str
        The name of vcs commit author
    providercommitauthorurl : str
        The url of vcs commit author
    providercommithash : str
        The commit hash of the vcs commit
    providercommitmessage : str
        The commit message
    providercommiturl : str
        The url of the vcs commit
    providerrepositoryname : str
        The name of the vcs provider repository
    providerrepositoryowner : str
        The name of the vcs provider repository owner
    providerrepositoryurl : str
        The url of the vcs provider repository
    resourceid : str
        Resource ID.
    resourcetype : str
        Resource type.
    screenshotdark : str
        Screenshot with dark theme preference file ID.
    screenshotlight : str
        Screenshot with light theme preference file ID.
    sourcesize : float
        The code size in bytes.
    status : DeploymentStatus
        The deployment status. Possible values are &quot;waiting&quot;, &quot;processing&quot;, &quot;building&quot;, &quot;ready&quot;, &quot;canceled&quot; and &quot;failed&quot;.
    totalsize : float
        The total size in bytes (source and build output).
    type : str
        Type of deployment.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    activate: bool = Field(..., alias='activate')
    billingjson: str = Field(..., alias='billingJson')
    buildduration: float = Field(..., alias='buildDuration')
    buildid: str = Field(..., alias='buildId')
    buildlogs: str = Field(..., alias='buildLogs')
    buildsize: float = Field(..., alias='buildSize')
    entrypoint: str = Field(..., alias='entrypoint')
    manifestjson: str = Field(..., alias='manifestJson')
    providerbranch: str = Field(..., alias='providerBranch')
    providerbranchurl: str = Field(..., alias='providerBranchUrl')
    providercommitauthor: str = Field(..., alias='providerCommitAuthor')
    providercommitauthorurl: str = Field(..., alias='providerCommitAuthorUrl')
    providercommithash: str = Field(..., alias='providerCommitHash')
    providercommitmessage: str = Field(..., alias='providerCommitMessage')
    providercommiturl: str = Field(..., alias='providerCommitUrl')
    providerrepositoryname: str = Field(..., alias='providerRepositoryName')
    providerrepositoryowner: str = Field(..., alias='providerRepositoryOwner')
    providerrepositoryurl: str = Field(..., alias='providerRepositoryUrl')
    resourceid: str = Field(..., alias='resourceId')
    resourcetype: str = Field(..., alias='resourceType')
    screenshotdark: str = Field(..., alias='screenshotDark')
    screenshotlight: str = Field(..., alias='screenshotLight')
    sourcesize: float = Field(..., alias='sourceSize')
    status: DeploymentStatus = Field(..., alias='status')
    totalsize: float = Field(..., alias='totalSize')
    type: str = Field(..., alias='type')
