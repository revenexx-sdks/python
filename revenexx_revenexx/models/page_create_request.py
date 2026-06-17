from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    bundle : Optional[str]
        Typed model field.
    hostoptions : Optional[Dict[str, Any]]
        Typed model field.
    meta : Optional[Dict[str, Any]]
        Typed model field.
    slug : Optional[str]
        Typed model field.
    sourcelanguage : Optional[str]
        Typed model field.
    title : str
        Typed model field.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    hostoptions: Optional[Dict[str, Any]] = Field(default=None, alias='hostOptions')
    meta: Optional[Dict[str, Any]] = Field(default=None, alias='meta')
    slug: Optional[str] = Field(default=None, alias='slug')
    sourcelanguage: Optional[str] = Field(default=None, alias='sourceLanguage')
    title: str = Field(..., alias='title')
