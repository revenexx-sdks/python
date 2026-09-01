from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class RolePermissionsRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    permissions : List[Any]
        The complete new set. Duplicates and blanks are ignored; an empty array revokes everything.
    """
    permissions: List[Any] = Field(..., alias='permissions')
