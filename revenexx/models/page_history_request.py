from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageHistoryRequest(AppwriteModel):
    """
    Where to put the undo pointer.

    Attributes
    ----------
    index : float
        The position in the mutation log to materialize at. `-1` undoes everything; the last position redoes everything. Values outside the log are clamped rather than refused.
    langcode : Optional[str]
        Which language the returned state should be resolved for.
    """
    index: float = Field(..., alias='index')
    langcode: Optional[str] = Field(default=None, alias='langcode')
