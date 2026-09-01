from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderNumberRangesSeeded(AppwriteModel):
    """
    Which of the three standard codes this call had to create and which were already there.

    Attributes
    ----------
    created : Optional[List[Any]]
        The codes that were created just now, with the standard format ORD-/DEL-/RET- and padding 6. Empty on every call after the first.
    existing : Optional[List[Any]]
        The codes that were already there and were left EXACTLY as they are — a merchant who changed the prefix or the counter keeps their change. That is what makes this call safe to run again.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
