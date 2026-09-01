from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.column_float_status import ColumnFloatStatus

class ColumnFloat(AppwriteModel):
    """
    ColumnFloat

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
    max : Optional[float]
        Maximum value to enforce for new documents.
    min : Optional[float]
        Minimum value to enforce for new documents.
    required : bool
        Is column required?
    status : ColumnFloatStatus
        Column status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    type : str
        Column type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    error: str = Field(..., alias='error')
    key: str = Field(..., alias='key')
    max: Optional[float] = Field(default=None, alias='max')
    min: Optional[float] = Field(default=None, alias='min')
    required: bool = Field(..., alias='required')
    status: ColumnFloatStatus = Field(..., alias='status')
    type: str = Field(..., alias='type')
