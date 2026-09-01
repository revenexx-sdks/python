from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeOptionsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_id : str
        The select / multi-select attribute these are the permitted values of. Deleting the attribute deletes its options with it.
    code : str
        The value actually STORED in a record&#039;s `attribute_values` when this option is picked — never the label. Unique within the attribute.
    labels : Optional[Dict[str, Any]]
        What the option is called, per language tag. Two tenants may label the same code differently; only the code is ever written into a record.
    position : Optional[float]
        Order in the dropdown, ascending. Options that tie keep the order the database returns them in, so give every option a position if the order matters.
    swatch : Optional[Dict[str, Any]]
        A colour or texture chip for the picker. Null for an option that is not visual.
    """
    attribute_id: str = Field(..., alias='attribute_id')
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    swatch: Optional[Dict[str, Any]] = Field(default=None, alias='swatch')
