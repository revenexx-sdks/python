from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MutationRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    langcode : Optional[str]
        Typed model field.
    payload : Optional[Dict[str, Any]]
        Typed model field.
    plugin : str
        Mutation plugin id (add, move, delete, duplicate, update_field_value, ...).
    """
    langcode: Optional[str] = Field(default=None, alias='langcode')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
    plugin: str = Field(..., alias='plugin')
