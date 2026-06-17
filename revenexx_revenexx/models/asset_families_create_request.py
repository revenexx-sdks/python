from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetFamiliesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    naming_convention : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    naming_convention: Optional[Dict[str, Any]] = Field(default=None, alias='naming_convention')
