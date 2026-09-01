from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceDeleted(AppwriteModel):
    """
    The row is gone. Deleting a price list cascades to its entries.

    Attributes
    ----------
    deleted : Optional[bool]
        Always true — a row that was not there answers 404 instead.
    id : Optional[str]
        The row that was removed.
    """
    deleted: Optional[bool] = Field(default=None, alias='deleted')
    id: Optional[str] = Field(default=None, alias='id')
