from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Runtime(AppwriteModel):
    """
    Runtime

    Attributes
    ----------
    id : str
        Runtime ID.
    base : str
        Base Docker image used to build the runtime.
    image : str
        Image name of Docker Hub.
    key : str
        Parent runtime key.
    logo : str
        Name of the logo image.
    name : str
        Runtime Name.
    supports : List[Any]
        List of supported architectures.
    version : str
        Runtime version.
    """
    id: str = Field(..., alias='$id')
    base: str = Field(..., alias='base')
    image: str = Field(..., alias='image')
    key: str = Field(..., alias='key')
    logo: str = Field(..., alias='logo')
    name: str = Field(..., alias='name')
    supports: List[Any] = Field(..., alias='supports')
    version: str = Field(..., alias='version')
