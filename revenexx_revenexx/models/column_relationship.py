from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.column_relationship_status import ColumnRelationshipStatus

class ColumnRelationship(AppwriteModel):
    """
    ColumnRelationship

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
    ondelete : str
        How deleting the parent document will propagate to child documents.
    relatedtable : str
        The ID of the related table.
    relationtype : str
        The type of the relationship.
    required : bool
        Is column required?
    side : str
        Whether this is the parent or child side of the relationship
    status : ColumnRelationshipStatus
        Column status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    twoway : bool
        Is the relationship two-way?
    twowaykey : str
        The key of the two-way relationship.
    type : str
        Column type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    error: str = Field(..., alias='error')
    key: str = Field(..., alias='key')
    ondelete: str = Field(..., alias='onDelete')
    relatedtable: str = Field(..., alias='relatedTable')
    relationtype: str = Field(..., alias='relationType')
    required: bool = Field(..., alias='required')
    side: str = Field(..., alias='side')
    status: ColumnRelationshipStatus = Field(..., alias='status')
    twoway: bool = Field(..., alias='twoWay')
    twowaykey: str = Field(..., alias='twoWayKey')
    type: str = Field(..., alias='type')
