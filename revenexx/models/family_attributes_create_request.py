from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamilyAttributesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_id : str
        The attribute the family carries. One row per (family, attribute); deleting either side deletes the link.
    family_id : str
        The family this link belongs to — one side of the pair that makes an attribute part of a family&#039;s form.
    is_required : Optional[bool]
        The attribute has to carry a value for a product of this family to count as complete. `POST /products/{id}/completeness` measures exactly these and nothing else.
    position : Optional[float]
        The family&#039;s own ordering of this attribute, which overrides the attribute&#039;s default `position` in this family&#039;s form.
    required_channels : Optional[Dict[str, Any]]
        Narrows `is_required` to named channels. NULL or an empty list means required EVERYWHERE, not nowhere — that is how every required link in the wild is stored, and reading an empty list as &quot;nowhere&quot; reports a fully configured family as demanding nothing.
    """
    attribute_id: str = Field(..., alias='attribute_id')
    family_id: str = Field(..., alias='family_id')
    is_required: Optional[bool] = Field(default=None, alias='is_required')
    position: Optional[float] = Field(default=None, alias='position')
    required_channels: Optional[Dict[str, Any]] = Field(default=None, alias='required_channels')
