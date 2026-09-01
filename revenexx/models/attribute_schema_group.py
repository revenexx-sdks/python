from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeSchemaGroup(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        The group code, which is what every field in the section carries as its `group`.
    label : Optional[str]
        The section heading, resolved for the requested locale.
    position : Optional[float]
        Where the section sits, ascending. The array is already in this order.
    """
    code: Optional[str] = Field(default=None, alias='code')
    label: Optional[str] = Field(default=None, alias='label')
    position: Optional[float] = Field(default=None, alias='position')
