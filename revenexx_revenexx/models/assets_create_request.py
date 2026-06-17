from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    asset_family_id : str
        Typed model field.
    attribute_values : Optional[Dict[str, Any]]
        Typed model field.
    code : str
        Typed model field.
    media_uuid : Optional[str]
        Typed model field.
    """
    asset_family_id: str = Field(..., alias='asset_family_id')
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    code: str = Field(..., alias='code')
    media_uuid: Optional[str] = Field(default=None, alias='media_uuid')
