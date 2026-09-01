from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.attribute_value_bucket import AttributeValueBucket

class AttributeFieldStorage(AppwriteModel):
    """
    Where the value lives. Absent on an app whose custom fields are plain columns — then the field name IS the column.

    Attributes
    ----------
    bucket : Optional[AttributeValueBucket]
        Which scope bucket this attribute writes to, implied by localizable/scopable.
    column : Optional[str]
        The jsonb column holding the values (`attribute_values`).
    path : Optional[List[Any]]
        The exact key path for the requested context, or null when the request named no locale/channel and the bucket needs one. Null means: read-only until a context is chosen.
    """
    bucket: Optional[AttributeValueBucket] = Field(default=None, alias='bucket')
    column: Optional[str] = Field(default=None, alias='column')
    path: Optional[List[Any]] = Field(default=None, alias='path')
