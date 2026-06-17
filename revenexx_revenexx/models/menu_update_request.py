from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MenuUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    items : Optional[List[Any]]
        Typed model field.
    label : Optional[str]
        Typed model field.
    """
    items: Optional[List[Any]] = Field(default=None, alias='items')
    label: Optional[str] = Field(default=None, alias='label')
