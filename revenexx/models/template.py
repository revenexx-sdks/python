from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Template(AppwriteModel):
    """
    

    Attributes
    ----------
    body_html : Optional[str]
        Typed model field.
    body_text : Optional[str]
        Typed model field.
    channel : str
        Typed model field.
    content_sid : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    design : Optional[List[Any]]
        Typed model field.
    enabled : bool
        Typed model field.
    has_unpublished_changes : str
        Typed model field.
    id : str
        Typed model field.
    is_published : str
        Typed model field.
    key : str
        Typed model field.
    layout_id : Optional[str]
        Typed model field.
    lifecycle_state : str
        Typed model field.
    locale : str
        Typed model field.
    markets : List[Any]
        Typed model field.
    message_class : str
        Typed model field.
    published_version_id : Optional[str]
        Typed model field.
    source_library_key : Optional[str]
        Typed model field.
    subject : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    test_mode : bool
        Typed model field.
    title : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    uses_raw_html : str
        Typed model field.
    valid_from : Optional[str]
        Typed model field.
    valid_until : Optional[str]
        Typed model field.
    variable_defaults : Optional[List[Any]]
        Typed model field.
    variables : Optional[List[Any]]
        Typed model field.
    whatsapp_category : Optional[str]
        Typed model field.
    """
    body_html: Optional[str] = Field(..., alias='body_html')
    body_text: Optional[str] = Field(..., alias='body_text')
    channel: str = Field(..., alias='channel')
    content_sid: Optional[str] = Field(..., alias='content_sid')
    created_at: Optional[str] = Field(..., alias='created_at')
    design: Optional[List[Any]] = Field(..., alias='design')
    enabled: bool = Field(..., alias='enabled')
    has_unpublished_changes: str = Field(..., alias='has_unpublished_changes')
    id: str = Field(..., alias='id')
    is_published: str = Field(..., alias='is_published')
    key: str = Field(..., alias='key')
    layout_id: Optional[str] = Field(..., alias='layout_id')
    lifecycle_state: str = Field(..., alias='lifecycle_state')
    locale: str = Field(..., alias='locale')
    markets: List[Any] = Field(..., alias='markets')
    message_class: str = Field(..., alias='message_class')
    published_version_id: Optional[str] = Field(..., alias='published_version_id')
    source_library_key: Optional[str] = Field(..., alias='source_library_key')
    subject: Optional[str] = Field(..., alias='subject')
    tenant_id: str = Field(..., alias='tenant_id')
    test_mode: bool = Field(..., alias='test_mode')
    title: Optional[str] = Field(..., alias='title')
    updated_at: Optional[str] = Field(..., alias='updated_at')
    uses_raw_html: str = Field(..., alias='uses_raw_html')
    valid_from: Optional[str] = Field(..., alias='valid_from')
    valid_until: Optional[str] = Field(..., alias='valid_until')
    variable_defaults: Optional[List[Any]] = Field(..., alias='variable_defaults')
    variables: Optional[List[Any]] = Field(..., alias='variables')
    whatsapp_category: Optional[str] = Field(..., alias='whatsapp_category')
