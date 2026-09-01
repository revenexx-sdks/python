from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageCommentTaskRequest(AppwriteModel):
    """
    Which checkbox to flip.

    Attributes
    ----------
    taskindex : float
        The task item to toggle, counted in document order from 0. A comment with fewer tasks than that answers 400, and so does anything that is not a whole number at or above 0.
    """
    taskindex: float = Field(..., alias='taskIndex')
