from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .template_runtime import TemplateRuntime
from .template_variable import TemplateVariable

class TemplateFunction(AppwriteModel):
    """
    Template Function

    Attributes
    ----------
    cron : str
        Function execution schedult in CRON format.
    events : List[Any]
        Function trigger events.
    icon : str
        Function Template Icon.
    id : str
        Function Template ID.
    instructions : str
        Function Template Instructions.
    name : str
        Function Template Name.
    permissions : List[Any]
        Execution permissions.
    providerowner : str
        VCS (Version Control System) Owner.
    providerrepositoryid : str
        VCS (Version Control System) Repository ID
    providerversion : str
        VCS (Version Control System) branch version (tag).
    runtimes : List[TemplateRuntime]
        List of runtimes that can be used with this template.
    scopes : List[Any]
        Function scopes.
    tagline : str
        Function Template Tagline.
    timeout : float
        Function execution timeout in seconds.
    usecases : List[Any]
        Function use cases.
    variables : List[TemplateVariable]
        Function variables.
    vcsprovider : str
        VCS (Version Control System) Provider.
    """
    cron: str = Field(..., alias='cron')
    events: List[Any] = Field(..., alias='events')
    icon: str = Field(..., alias='icon')
    id: str = Field(..., alias='id')
    instructions: str = Field(..., alias='instructions')
    name: str = Field(..., alias='name')
    permissions: List[Any] = Field(..., alias='permissions')
    providerowner: str = Field(..., alias='providerOwner')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerversion: str = Field(..., alias='providerVersion')
    runtimes: List[TemplateRuntime] = Field(..., alias='runtimes')
    scopes: List[Any] = Field(..., alias='scopes')
    tagline: str = Field(..., alias='tagline')
    timeout: float = Field(..., alias='timeout')
    usecases: List[Any] = Field(..., alias='useCases')
    variables: List[TemplateVariable] = Field(..., alias='variables')
    vcsprovider: str = Field(..., alias='vcsProvider')
