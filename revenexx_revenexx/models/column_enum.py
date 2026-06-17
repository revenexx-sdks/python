from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.column_enum_status import ColumnEnumStatus

class ColumnEnum(AppwriteModel):
    """
    ColumnEnum

    Attributes
    ----------
    createdat : str
        Column creation date in ISO 8601 format.
    updatedat : str
        Column update date in ISO 8601 format.
    array : Optional[bool]
        Is column an array?
    elements : List[Any]
        Array of elements in enumerated type.
    error : str
        Error message. Displays error generated on failure of creating or deleting an column.
    format : str
        String format.
    key : str
        Column Key.
    required : bool
        Is column required?
    status : ColumnEnumStatus
        Column status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    type : str
        Column type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    elements: List[Any] = Field(..., alias='elements')
    error: str = Field(..., alias='error')
    format: str = Field(..., alias='format')
    key: str = Field(..., alias='key')
    required: bool = Field(..., alias='required')
    status: ColumnEnumStatus = Field(..., alias='status')
    type: str = Field(..., alias='type')
