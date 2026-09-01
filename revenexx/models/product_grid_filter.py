from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductGridFilter(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        The attribute code to filter on.
    label : Optional[Dict[str, Any]]
        The attribute&#039;s i18n labels, for the filter&#039;s own caption.
    type : Optional[str]
        Which control the filter asks for — the same widget vocabulary the columns use.
    """
    code: Optional[str] = Field(default=None, alias='code')
    label: Optional[Dict[str, Any]] = Field(default=None, alias='label')
    type: Optional[str] = Field(default=None, alias='type')
