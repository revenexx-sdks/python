from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductsBatchRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    ids : Optional[List[Any]]
        Typed model field.
    skus : Optional[List[Any]]
        Typed model field.
    """
    ids: Optional[List[Any]] = Field(default=None, alias='ids')
    skus: Optional[List[Any]] = Field(default=None, alias='skus')
