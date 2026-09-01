from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Specification(AppwriteModel):
    """
    Specification

    Attributes
    ----------
    cpus : float
        Number of CPUs.
    enabled : bool
        Is size enabled.
    memory : float
        Memory size in MB.
    slug : str
        Size slug.
    """
    cpus: float = Field(..., alias='cpus')
    enabled: bool = Field(..., alias='enabled')
    memory: float = Field(..., alias='memory')
    slug: str = Field(..., alias='slug')
