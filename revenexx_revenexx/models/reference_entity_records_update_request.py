from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReferenceEntityRecordsUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    attribute_values : Optional[Dict[str, Any]]
        Typed model field.
    code : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    reference_entity_id : Optional[str]
        Typed model field.
    """
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    code: Optional[str] = Field(default=None, alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    reference_entity_id: Optional[str] = Field(default=None, alias='reference_entity_id')
