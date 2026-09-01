from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class IoEntity(AppwriteModel):
    """
    One importable / exportable entity of an installed app.

    Attributes
    ----------
    app : Optional[str]
        Typed model field.
    entity : Optional[str]
        Typed model field.
    label : Optional[str]
        Humanised entity name for pickers.
    table : Optional[str]
        The physical table name Baseline provisioned.
    vendor : Optional[str]
        Typed model field.
    """
    app: Optional[str] = Field(default=None, alias='app')
    entity: Optional[str] = Field(default=None, alias='entity')
    label: Optional[str] = Field(default=None, alias='label')
    table: Optional[str] = Field(default=None, alias='table')
    vendor: Optional[str] = Field(default=None, alias='vendor')
