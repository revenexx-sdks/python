from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class RolePermissionsResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    key : Optional[str]
        The role that was written.
    permissions : Optional[List[Any]]
        Its complete new set, after de-duplication.
    """
    key: Optional[str] = Field(default=None, alias='key')
    permissions: Optional[List[Any]] = Field(default=None, alias='permissions')
