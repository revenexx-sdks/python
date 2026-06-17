from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Organization(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    external_team_id : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    name : Optional[str]
        Typed model field.
    settings : Optional[Dict[str, Any]]
        Typed model field.
    status : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    vat_id : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    external_team_id: Optional[str] = Field(default=None, alias='external_team_id')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    settings: Optional[Dict[str, Any]] = Field(default=None, alias='settings')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    vat_id: Optional[str] = Field(default=None, alias='vat_id')
