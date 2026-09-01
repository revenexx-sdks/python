from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageCommentUpdateRequest(AppwriteModel):
    """
    The new body. Nothing else about a comment is editable.

    Attributes
    ----------
    body : str
        The comment, as editor HTML. Replaces the old body completely.
    """
    body: str = Field(..., alias='body')
