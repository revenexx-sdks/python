from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.attribute_relationship_status import AttributeRelationshipStatus

class AttributeRelationship(AppwriteModel):
    """
    AttributeRelationship

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
    ondelete : str
        How deleting the parent document will propagate to child documents.
    relatedcollection : str
        The ID of the related collection.
    relationtype : str
        The type of the relationship.
    required : bool
        Is attribute required?
    side : str
        Whether this is the parent or child side of the relationship
    status : AttributeRelationshipStatus
        Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    twoway : bool
        Is the relationship two-way?
    twowaykey : str
        The key of the two-way relationship.
    type : str
        Attribute type.
    """
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    array: Optional[bool] = Field(default=None, alias='array')
    error: str = Field(..., alias='error')
    key: str = Field(..., alias='key')
    ondelete: str = Field(..., alias='onDelete')
    relatedcollection: str = Field(..., alias='relatedCollection')
    relationtype: str = Field(..., alias='relationType')
    required: bool = Field(..., alias='required')
    side: str = Field(..., alias='side')
    status: AttributeRelationshipStatus = Field(..., alias='status')
    twoway: bool = Field(..., alias='twoWay')
    twowaykey: str = Field(..., alias='twoWayKey')
    type: str = Field(..., alias='type')
