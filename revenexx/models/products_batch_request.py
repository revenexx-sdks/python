from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductsBatchRequest(AppwriteModel):
    """
    Name the products either way, or both ways. Send at least one non-empty list; the two are unioned and a product named twice comes back once.

    Attributes
    ----------
    ids : Optional[List[Any]]
        Product ids, when the caller already holds them.
    skus : Optional[List[Any]]
        Product SKUs — the identifier a foreign system carries, which is why this route exists at all.
    """
    ids: Optional[List[Any]] = Field(default=None, alias='ids')
    skus: Optional[List[Any]] = Field(default=None, alias='skus')
