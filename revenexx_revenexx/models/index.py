from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.index_status import IndexStatus

class Index(AppwriteModel):
    """
    Index

    Attributes
    ----------
    createdat : str
        Index creation date in ISO 8601 format.
    id : str
        Index ID.
    updatedat : str
        Index update date in ISO 8601 format.
    attributes : List[Any]
        Index attributes.
    error : str
        Error message. Displays error generated on failure of creating or deleting an index.
    key : str
        Index key.
    lengths : List[Any]
        Index attributes length.
    orders : Optional[List[Any]]
        Index orders.
    status : IndexStatus
        Index status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    type : str
        Index type.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    attributes: List[Any] = Field(..., alias='attributes')
    error: str = Field(..., alias='error')
    key: str = Field(..., alias='key')
    lengths: List[Any] = Field(..., alias='lengths')
    orders: Optional[List[Any]] = Field(default=None, alias='orders')
    status: IndexStatus = Field(..., alias='status')
    type: str = Field(..., alias='type')
