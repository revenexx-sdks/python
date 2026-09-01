from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .collection2 import Collection2

class CollectionList2(AppwriteModel):
    """
    Collections List

    Attributes
    ----------
    collections : List[Collection2]
        List of collections.
    total : float
        Total number of collections that matched your query.
    """
    collections: List[Collection2] = Field(..., alias='collections')
    total: float = Field(..., alias='total')
