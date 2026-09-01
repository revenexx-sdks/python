from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageTranslateRequest(AppwriteModel):
    """
    The strings to translate. They are forwarded to the tenant&#039;s provider verbatim.

    Attributes
    ----------
    items : Optional[List[Any]]
        The strings to translate. This app reads no element of the list — the provider defines the contract, and the blökkli adapter sends the fields below.
    """
    items: Optional[List[Any]] = Field(default=None, alias='items')
