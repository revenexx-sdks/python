from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductLabelsRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    ids : Optional[List[Any]]
        Product ids to name. At most 500.
    skus : Optional[List[Any]]
        Product SKUs to name. At most 500.
    """
    ids: Optional[List[Any]] = Field(default=None, alias='ids')
    skus: Optional[List[Any]] = Field(default=None, alias='skus')
