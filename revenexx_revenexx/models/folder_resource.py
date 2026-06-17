from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FolderResource(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : str
        Typed model field.
    id : str
        Typed model field.
    is_system : bool
        Typed model field.
    name : str
        Typed model field.
    parent_id : Optional[str]
        Typed model field.
    path : str
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : str
        Typed model field.
    """
    created_at: str = Field(..., alias='created_at')
    id: str = Field(..., alias='id')
    is_system: bool = Field(..., alias='is_system')
    name: str = Field(..., alias='name')
    parent_id: Optional[str] = Field(..., alias='parent_id')
    path: str = Field(..., alias='path')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: str = Field(..., alias='updated_at')
