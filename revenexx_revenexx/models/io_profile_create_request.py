from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_io_apply_mode import CartIoApplyMode
from ..enums.cart_io_direction import CartIoDirection
from ..enums.cart_io_entity import CartIoEntity
from ..enums.cart_io_format import CartIoFormat

class IoProfileCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    apply_mode : Optional[CartIoApplyMode]
        Default &#039;insert&#039;.
    direction : CartIoDirection
        Typed model field.
    entity : Optional[CartIoEntity]
        Default &#039;carts&#039;.
    format : Optional[CartIoFormat]
        Default &#039;json&#039;.
    is_template : Optional[bool]
        Typed model field.
    mapping : Optional[Dict[str, Any]]
        Column mapping (Baseline-IO-compatible).
    name : str
        Typed model field.
    options : Optional[Dict[str, Any]]
        Typed model field.
    """
    apply_mode: Optional[CartIoApplyMode] = Field(default=None, alias='apply_mode')
    direction: CartIoDirection = Field(..., alias='direction')
    entity: Optional[CartIoEntity] = Field(default=None, alias='entity')
    format: Optional[CartIoFormat] = Field(default=None, alias='format')
    is_template: Optional[bool] = Field(default=None, alias='is_template')
    mapping: Optional[Dict[str, Any]] = Field(default=None, alias='mapping')
    name: str = Field(..., alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
