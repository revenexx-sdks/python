from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderUpdateRequest(AppwriteModel):
    """
    Narrow modification — only these columns are touchable, and only until the order is acknowledged. Status moves through the action routes.

    Attributes
    ----------
    billing_address : Optional[Dict[str, Any]]
        Typed model field.
    buyer : Optional[Dict[str, Any]]
        Typed model field.
    customer_order_number : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    shipping_address : Optional[Dict[str, Any]]
        Typed model field.
    user_data : Optional[Dict[str, Any]]
        Free-form user data.
    """
    billing_address: Optional[Dict[str, Any]] = Field(default=None, alias='billing_address')
    buyer: Optional[Dict[str, Any]] = Field(default=None, alias='buyer')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, alias='shipping_address')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
