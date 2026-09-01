from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.attribute_mediumtext_status import AttributeMediumtextStatus

class AttributeMediumtext(AppwriteModel):
    """
    AttributeMediumtext

    Attributes
    ----------
    createdat : str
        Attribute creation date in ISO 8601 format.
    updatedat : str
        Attribute update date in ISO 8601 format.
    array : Optional[bool]
        Is attribute an array?
    error : str
        Error message. Displays error generated on failure of creating or deleting an attribute.
    key : str
        Attribute Key.
    required : bool
        Is attribute required?
    status : AttributeMediumtextStatus
        Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    type : str
        Attribute type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    error: str = Field(..., alias='error')
    key: str = Field(..., alias='key')
    required: bool = Field(..., alias='required')
    status: AttributeMediumtextStatus = Field(..., alias='status')
    type: str = Field(..., alias='type')
