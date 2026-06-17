from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetFamiliesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    naming_convention : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    naming_convention: Optional[Dict[str, Any]] = Field(default=None, alias='naming_convention')
