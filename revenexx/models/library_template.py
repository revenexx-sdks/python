from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class LibraryTemplate(AppwriteModel):
    """
    

    Attributes
    ----------
    body_html : Optional[str]
        Typed model field.
    body_text : Optional[str]
        Typed model field.
    channel : str
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    design : Optional[List[Any]]
        Typed model field.
    id : str
        Typed model field.
    key : str
        Typed model field.
    locale : str
        Typed model field.
    subject : Optional[str]
        Typed model field.
    suggested_event : Optional[str]
        Typed model field.
    suggested_recipient : Optional[str]
        Typed model field.
    title : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    variables : Optional[List[Any]]
        Typed model field.
    """
    body_html: Optional[str] = Field(..., alias='body_html')
    body_text: Optional[str] = Field(..., alias='body_text')
    channel: str = Field(..., alias='channel')
    created_at: Optional[str] = Field(..., alias='created_at')
    description: Optional[str] = Field(..., alias='description')
    design: Optional[List[Any]] = Field(..., alias='design')
    id: str = Field(..., alias='id')
    key: str = Field(..., alias='key')
    locale: str = Field(..., alias='locale')
    subject: Optional[str] = Field(..., alias='subject')
    suggested_event: Optional[str] = Field(..., alias='suggested_event')
    suggested_recipient: Optional[str] = Field(..., alias='suggested_recipient')
    title: Optional[str] = Field(..., alias='title')
    updated_at: Optional[str] = Field(..., alias='updated_at')
    variables: Optional[List[Any]] = Field(..., alias='variables')
