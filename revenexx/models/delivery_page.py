from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DeliveryPage(AppwriteModel):
    """
    One published page resolved for one language, ready to render: i18n fallback applied per field, blocks outside their publish window removed, library references expanded inline.

    Attributes
    ----------
    fields : Optional[Dict[str, Any]]
        The page&#039;s block tree, keyed by field name — `{ &quot;content&quot;: [ … ] }`. A theme renders the field it knows and ignores the rest.
    page : Optional[Dict[str, Any]]
        The page frame — everything a theme needs before it starts rendering blocks.
    """
    fields: Optional[Dict[str, Any]] = Field(default=None, alias='fields')
    page: Optional[Dict[str, Any]] = Field(default=None, alias='page')
