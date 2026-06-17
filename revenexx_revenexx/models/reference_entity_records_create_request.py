from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReferenceEntityRecordsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_values : Optional[Dict[str, Any]]
        Typed model field.
    code : str
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    reference_entity_id : str
        Typed model field.
    """
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    reference_entity_id: str = Field(..., alias='reference_entity_id')
