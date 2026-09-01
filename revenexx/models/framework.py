from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .framework_adapter import FrameworkAdapter

class Framework(AppwriteModel):
    """
    Framework

    Attributes
    ----------
    adapters : List[FrameworkAdapter]
        List of supported adapters.
    buildruntime : str
        Default runtime version.
    key : str
        Framework key.
    name : str
        Framework Name.
    runtimes : List[Any]
        List of supported runtime versions.
    """
    adapters: List[FrameworkAdapter] = Field(..., alias='adapters')
    buildruntime: str = Field(..., alias='buildRuntime')
    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    runtimes: List[Any] = Field(..., alias='runtimes')
