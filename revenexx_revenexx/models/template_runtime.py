from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class TemplateRuntime(AppwriteModel):
    """
    Template Runtime

    Attributes
    ----------
    commands : str
        The build command used to build the deployment.
    entrypoint : str
        The entrypoint file used to execute the deployment.
    name : str
        Runtime Name.
    providerrootdirectory : str
        Path to function in VCS (Version Control System) repository
    """
    commands: str = Field(..., alias='commands')
    entrypoint: str = Field(..., alias='entrypoint')
    name: str = Field(..., alias='name')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
