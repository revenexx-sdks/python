from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class TemplateVariable(AppwriteModel):
    """
    Template Variable

    Attributes
    ----------
    description : str
        Variable Description.
    name : str
        Variable Name.
    placeholder : str
        Variable Placeholder.
    required : bool
        Is the variable required?
    secret : bool
        Variable secret flag. Secret variables can only be updated or deleted, but never read.
    type : str
        Variable Type.
    value : str
        Variable Value.
    """
    description: str = Field(..., alias='description')
    name: str = Field(..., alias='name')
    placeholder: str = Field(..., alias='placeholder')
    required: bool = Field(..., alias='required')
    secret: bool = Field(..., alias='secret')
    type: str = Field(..., alias='type')
    value: str = Field(..., alias='value')
