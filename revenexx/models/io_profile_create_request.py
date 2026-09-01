from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_io_apply_mode import CartIoApplyMode
from ..enums.cart_io_direction import CartIoDirection
from ..enums.cart_io_entity import CartIoEntity
from ..enums.cart_io_format import CartIoFormat
from .cart_io_mapping import CartIoMapping

class IoProfileCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    apply_mode : Optional[CartIoApplyMode]
        What an import does with the lines the target cart already has: &#039;replace&#039; clears them first, &#039;insert&#039; and &#039;append&#039; both add and behave identically today. Read only when the import names a target_cart_id. Default &#039;insert&#039;.
    direction : CartIoDirection
        Which way this profile runs. A profile only ever runs in the direction it declares: handing an import profile to carts.export is a 400, and the other way round.
    entity : Optional[CartIoEntity]
        What the profile carries: whole carts (the `{cart, items}` document) or bare cart lines. Default &#039;carts&#039;.
    format : Optional[CartIoFormat]
        The wire format. &#039;json&#039; is the canonical, re-importable document; &#039;csv&#039; is the spreadsheet form, and only line fields survive it. Default &#039;json&#039;.
    is_template : Optional[bool]
        One of the bundled templates. Set by carts.io.profiles.defaults; a profile a merchant writes is not one.
    mapping : Optional[CartIoMapping]
        Baseline-IO-compatible column mapping. An empty object (or null) is identity: the full canonical shape, every field under its own name.
    name : str
        What a merchant picks this profile by. Unique within the tenant — reusing a name is a 409.
    options : Optional[Dict[str, Any]]
        Free-form options carried with the profile. The four bundled templates put one human sentence under `description` and nothing else; no other key is read by this app, so anything a merchant needs alongside a profile can live here.
    """
    apply_mode: Optional[CartIoApplyMode] = Field(default=None, alias='apply_mode')
    direction: CartIoDirection = Field(..., alias='direction')
    entity: Optional[CartIoEntity] = Field(default=None, alias='entity')
    format: Optional[CartIoFormat] = Field(default=None, alias='format')
    is_template: Optional[bool] = Field(default=None, alias='is_template')
    mapping: Optional[CartIoMapping] = Field(default=None, alias='mapping')
    name: str = Field(..., alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
