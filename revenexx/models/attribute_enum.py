from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.attribute_enum_status import AttributeEnumStatus

class AttributeEnum(AppwriteModel):
    """
    AttributeEnum

    Attributes
    ----------
    createdat : str
        Attribute creation date in ISO 8601 format.
    updatedat : str
        Attribute update date in ISO 8601 format.
    array : Optional[bool]
        Is attribute an array?
    elements : List[Any]
        Array of elements in enumerated type.
    error : str
        Error message. Displays error generated on failure of creating or deleting an attribute.
    format : str
        String format.
    key : str
        Attribute Key.
    required : bool
        Is attribute required?
    status : AttributeEnumStatus
        Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    type : str
        Attribute type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    elements: List[Any] = Field(..., alias='elements')
    error: str = Field(..., alias='error')
    format: str = Field(..., alias='format')
    key: str = Field(..., alias='key')
    required: bool = Field(..., alias='required')
    status: AttributeEnumStatus = Field(..., alias='status')
    type: str = Field(..., alias='type')
