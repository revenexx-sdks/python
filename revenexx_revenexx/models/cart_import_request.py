from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartImportRequest(AppwriteModel):
    """
    Import into an existing cart (&#039;target_cart_id&#039;) or a new cart (owner &#039;contact_id&#039;/&#039;session_key&#039; required).

    Attributes
    ----------
    contact_id : Optional[str]
        Owner of a newly created cart.
    csv : Optional[str]
        Raw CSV content (alternative to payload for csv profiles).
    name : Optional[str]
        Name for a newly created cart.
    payload : Optional[Dict[str, Any]]
        The import payload: &#039;{cart, items}&#039; object, or a raw JSON/CSV string in the profile&#039;s format.
    profile_id : Optional[str]
        Import profile to run; ad-hoc import when omitted.
    session_key : Optional[str]
        Guest owner of a newly created cart.
    target_cart_id : Optional[str]
        Existing active cart to import into.
    """
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    csv: Optional[str] = Field(default=None, alias='csv')
    name: Optional[str] = Field(default=None, alias='name')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
    profile_id: Optional[str] = Field(default=None, alias='profile_id')
    session_key: Optional[str] = Field(default=None, alias='session_key')
    target_cart_id: Optional[str] = Field(default=None, alias='target_cart_id')
