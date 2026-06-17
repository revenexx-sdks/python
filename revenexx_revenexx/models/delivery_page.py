from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DeliveryPage(AppwriteModel):
    """
    Published page resolved for one language: nested block tree with i18n fallback applied and scheduled blocks filtered.

    Attributes
    ----------
    fields : Optional[Dict[str, Any]]
        Field name → ordered block list ({ uuid, bundle, props, options, children }).
    page : Optional[Dict[str, Any]]
        Typed model field.
    """
    fields: Optional[Dict[str, Any]] = Field(default=None, alias='fields')
    page: Optional[Dict[str, Any]] = Field(default=None, alias='page')
