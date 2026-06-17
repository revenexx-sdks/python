from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReferenceEntitiesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    image : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    image: Optional[str] = Field(default=None, alias='image')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
