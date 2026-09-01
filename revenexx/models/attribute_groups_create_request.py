from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeGroupsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The group&#039;s stable identifier, and the value an `AttributeField` carries as its `group` — a SECTION of the product form, not a label. Unique per tenant and the key an import joins on.
    labels : Optional[Dict[str, Any]]
        The section heading a person sees, keyed by language tag. The code is never shown to an operator; a tag nobody translated falls back to the next filled one, then to English.
    position : Optional[float]
        Where this section sits in a form, ascending. Sections that tie keep the order the database returns them in.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
