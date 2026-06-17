from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetResource(AppwriteModel):
    """
    

    Attributes
    ----------
    alt_text : Optional[str]
        Typed model field.
    content_hash : Optional[str]
        Typed model field.
    created_at : str
        Typed model field.
    deleted_at : str
        Typed model field.
    description : Optional[str]
        Typed model field.
    display_name : Optional[str]
        Typed model field.
    dominant_color : Optional[str]
        Typed model field.
    duration_ms : Optional[float]
        Typed model field.
    folder_id : Optional[str]
        Typed model field.
    height : Optional[float]
        Typed model field.
    id : str
        Typed model field.
    kind : str
        Typed model field.
    metadata : List[Any]
        Typed model field.
    mime_type : str
        Typed model field.
    original_name : str
        Typed model field.
    page_count : Optional[float]
        Typed model field.
    path_name : str
        Typed model field.
    processed_at : str
        Typed model field.
    size_bytes : float
        Typed model field.
    status : str
        Typed model field.
    tags : List[Any]
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : str
        Typed model field.
    url : str
        Typed model field.
    visibility : str
        Typed model field.
    width : Optional[float]
        Typed model field.
    """
    alt_text: Optional[str] = Field(..., alias='alt_text')
    content_hash: Optional[str] = Field(..., alias='content_hash')
    created_at: str = Field(..., alias='created_at')
    deleted_at: str = Field(..., alias='deleted_at')
    description: Optional[str] = Field(..., alias='description')
    display_name: Optional[str] = Field(..., alias='display_name')
    dominant_color: Optional[str] = Field(..., alias='dominant_color')
    duration_ms: Optional[float] = Field(..., alias='duration_ms')
    folder_id: Optional[str] = Field(..., alias='folder_id')
    height: Optional[float] = Field(..., alias='height')
    id: str = Field(..., alias='id')
    kind: str = Field(..., alias='kind')
    metadata: List[Any] = Field(..., alias='metadata')
    mime_type: str = Field(..., alias='mime_type')
    original_name: str = Field(..., alias='original_name')
    page_count: Optional[float] = Field(..., alias='page_count')
    path_name: str = Field(..., alias='path_name')
    processed_at: str = Field(..., alias='processed_at')
    size_bytes: float = Field(..., alias='size_bytes')
    status: str = Field(..., alias='status')
    tags: List[Any] = Field(..., alias='tags')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: str = Field(..., alias='updated_at')
    url: str = Field(..., alias='url')
    visibility: str = Field(..., alias='visibility')
    width: Optional[float] = Field(..., alias='width')
