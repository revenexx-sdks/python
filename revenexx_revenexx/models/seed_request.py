from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SeedRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    menus : Optional[List[Any]]
        Typed model field.
    pages : Optional[List[Any]]
        Typed model field.
    """
    menus: Optional[List[Any]] = Field(default=None, alias='menus')
    pages: Optional[List[Any]] = Field(default=None, alias='pages')
