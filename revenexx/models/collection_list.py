from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CollectionList(AppwriteModel):
    """
    

    Attributes
    ----------
    collections : List[Any]
        Public collection names the tenant owns. These are the values accepted for the `collection` path parameter.
    """
    collections: List[Any] = Field(..., alias='collections')
