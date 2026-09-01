from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductFamilyAssignRequest(AppwriteModel):
    """
    Name the family either way — `family_id` wins when both are sent. The family has to exist already; this route assigns one, it does not create one.

    Attributes
    ----------
    family_code : Optional[str]
        Alternative to family_id — a `families.code` this tenant holds, from `GET /products/families`. No example: a code is tenant data, and any value published here names a family somebody does not have.
    family_id : Optional[str]
        The family to assign.
    """
    family_code: Optional[str] = Field(default=None, alias='family_code')
    family_id: Optional[str] = Field(default=None, alias='family_id')
