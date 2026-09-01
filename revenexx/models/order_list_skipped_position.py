from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderListSkippedPosition(AppwriteModel):
    """
    A position left out of the conversion because the catalogue no longer knows its article (only ever non-empty when the tenant&#039;s &#039;on_missing_article&#039; setting is &#039;skip&#039;).

    Attributes
    ----------
    id : Optional[str]
        The position that was left out, so a client can point at the row in the list.
    name : Optional[str]
        The saved article name, so the omission can be reported to the buyer in words they recognise.
    product_id : Optional[str]
        The catalogue product the position named, if it named one.
    sku : Optional[str]
        The article number the position named, if it named one.
    """
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    sku: Optional[str] = Field(default=None, alias='sku')
