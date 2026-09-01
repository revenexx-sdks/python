from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeOptionsUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    attribute_id : Optional[str]
        The select / multi-select attribute these are the permitted values of. Deleting the attribute deletes its options with it.
    code : Optional[str]
        The value actually STORED in a record&#039;s `attribute_values` when this option is picked — never the label. Unique within the attribute.
    labels : Optional[Dict[str, Any]]
        What the option is called, per language tag. Two tenants may label the same code differently; only the code is ever written into a record.
    position : Optional[float]
        Order in the dropdown, ascending. Options that tie keep the order the database returns them in, so give every option a position if the order matters.
    swatch : Optional[Dict[str, Any]]
        A colour or texture chip for the picker. Null for an option that is not visual.
    """
    attribute_id: Optional[str] = Field(default=None, alias='attribute_id')
    code: Optional[str] = Field(default=None, alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    swatch: Optional[Dict[str, Any]] = Field(default=None, alias='swatch')
