from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderDeleted(AppwriteModel):
    """
    The row is gone. Deleting is not idempotent here: a second call answers 404, because the row no longer resolves.

    Attributes
    ----------
    deleted : Optional[bool]
        Always true — a failed delete is a status code, not a false here.
    id : Optional[str]
        The id of the row that was deleted, echoed back.
    """
    deleted: Optional[bool] = Field(default=None, alias='deleted')
    id: Optional[str] = Field(default=None, alias='id')
