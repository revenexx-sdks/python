from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Layout(AppwriteModel):
    """
    

    Attributes
    ----------
    color_accent : Optional[str]
        Typed model field.
    color_bg : Optional[str]
        Typed model field.
    color_text : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    enabled : bool
        Typed model field.
    font_family : Optional[str]
        Typed model field.
    footer_note : Optional[str]
        Typed model field.
    id : str
        Typed model field.
    is_default : bool
        Typed model field.
    legal_name : Optional[str]
        Typed model field.
    lifecycle_state : str
        Typed model field.
    logo_url : Optional[str]
        Typed model field.
    markets : List[Any]
        Typed model field.
    menu_links : Optional[List[Any]]
        Typed model field.
    name : str
        Typed model field.
    postal_address : Optional[str]
        Typed model field.
    sender_name : Optional[str]
        Typed model field.
    social_links : Optional[List[Any]]
        Typed model field.
    support_email : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    valid_from : Optional[str]
        Typed model field.
    valid_until : Optional[str]
        Typed model field.
    width : Optional[str]
        Typed model field.
    """
    color_accent: Optional[str] = Field(..., alias='color_accent')
    color_bg: Optional[str] = Field(..., alias='color_bg')
    color_text: Optional[str] = Field(..., alias='color_text')
    created_at: Optional[str] = Field(..., alias='created_at')
    enabled: bool = Field(..., alias='enabled')
    font_family: Optional[str] = Field(..., alias='font_family')
    footer_note: Optional[str] = Field(..., alias='footer_note')
    id: str = Field(..., alias='id')
    is_default: bool = Field(..., alias='is_default')
    legal_name: Optional[str] = Field(..., alias='legal_name')
    lifecycle_state: str = Field(..., alias='lifecycle_state')
    logo_url: Optional[str] = Field(..., alias='logo_url')
    markets: List[Any] = Field(..., alias='markets')
    menu_links: Optional[List[Any]] = Field(..., alias='menu_links')
    name: str = Field(..., alias='name')
    postal_address: Optional[str] = Field(..., alias='postal_address')
    sender_name: Optional[str] = Field(..., alias='sender_name')
    social_links: Optional[List[Any]] = Field(..., alias='social_links')
    support_email: Optional[str] = Field(..., alias='support_email')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: Optional[str] = Field(..., alias='updated_at')
    valid_from: Optional[str] = Field(..., alias='valid_from')
    valid_until: Optional[str] = Field(..., alias='valid_until')
    width: Optional[str] = Field(..., alias='width')
