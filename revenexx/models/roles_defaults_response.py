from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class RolesDefaultsResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    created : Optional[List[Any]]
        Role keys created by this call.
    existing : Optional[List[Any]]
        Role keys that were already there and were left untouched, permissions included.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
