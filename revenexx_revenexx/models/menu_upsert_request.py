from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MenuUpsertRequest(AppwriteModel):
    """
    Create or update the menu identified by menuKey (idempotent per tenant). `items` is the ordered nav tree ([{ label, to, items? }]).

    Attributes
    ----------
    items : Optional[List[Any]]
        Ordered menu entries ({ label, to?, items? }).
    label : str
        Typed model field.
    menukey : str
        Stable menu identifier, e.g. &quot;main&quot;, &quot;footer&quot;, &quot;account&quot;.
    """
    items: Optional[List[Any]] = Field(default=None, alias='items')
    label: str = Field(..., alias='label')
    menukey: str = Field(..., alias='menuKey')
