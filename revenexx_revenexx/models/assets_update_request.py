from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetsUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    asset_family_id : Optional[str]
        Typed model field.
    attribute_values : Optional[Dict[str, Any]]
        Typed model field.
    code : Optional[str]
        Typed model field.
    media_uuid : Optional[str]
        Typed model field.
    """
    asset_family_id: Optional[str] = Field(default=None, alias='asset_family_id')
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    code: Optional[str] = Field(default=None, alias='code')
    media_uuid: Optional[str] = Field(default=None, alias='media_uuid')
