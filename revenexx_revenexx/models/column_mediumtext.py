from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.column_mediumtext_status import ColumnMediumtextStatus

class ColumnMediumtext(AppwriteModel):
    """
    ColumnMediumtext

    Attributes
    ----------
    createdat : str
        Column creation date in ISO 8601 format.
    updatedat : str
        Column update date in ISO 8601 format.
    array : Optional[bool]
        Is column an array?
    error : str
        Error message. Displays error generated on failure of creating or deleting an column.
    key : str
        Column Key.
    required : bool
        Is column required?
    status : ColumnMediumtextStatus
        Column status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    type : str
        Column type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    error: str = Field(..., alias='error')
    key: str = Field(..., alias='key')
    required: bool = Field(..., alias='required')
    status: ColumnMediumtextStatus = Field(..., alias='status')
    type: str = Field(..., alias='type')
