from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.store_asset_request_visibility import StoreAssetRequestVisibility

class StoreAssetRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    alt_text : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    display_name : Optional[str]
        Typed model field.
    file : str
        Typed model field.
    folder_id : Optional[str]
        Typed model field.
    keep_archive : Optional[bool]
        Typed model field.
    tags : Optional[List[Any]]
        Typed model field.
    unpack : Optional[bool]
        Archives only: unpack the members after upload (see AssetController).
    visibility : Optional[StoreAssetRequestVisibility]
        Typed model field.
    """
    alt_text: Optional[str] = Field(default=None, alias='alt_text')
    description: Optional[str] = Field(default=None, alias='description')
    display_name: Optional[str] = Field(default=None, alias='display_name')
    file: str = Field(..., alias='file')
    folder_id: Optional[str] = Field(default=None, alias='folder_id')
    keep_archive: Optional[bool] = Field(default=None, alias='keep_archive')
    tags: Optional[List[Any]] = Field(default=None, alias='tags')
    unpack: Optional[bool] = Field(default=None, alias='unpack')
    visibility: Optional[StoreAssetRequestVisibility] = Field(default=None, alias='visibility')
