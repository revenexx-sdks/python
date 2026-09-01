from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_io_apply_mode import CartIoApplyMode
from ..enums.cart_io_direction import CartIoDirection
from ..enums.cart_io_entity import CartIoEntity
from ..enums.cart_io_format import CartIoFormat
from .cart_io_mapping import CartIoMapping

class IoProfile(AppwriteModel):
    """
    

    Attributes
    ----------
    apply_mode : Optional[CartIoApplyMode]
        What an import does with the lines the target cart already has. &#039;replace&#039; clears them first; &#039;insert&#039; and &#039;append&#039; both add, and behave identically today. Read only by carts.import, and only when the call names a target_cart_id — an import that creates its own cart has nothing to apply a mode to.
    created_at : Optional[str]
        When the profile was created — for the bundled templates, when the app was installed.
    direction : Optional[CartIoDirection]
        Which way this profile runs. A profile only ever runs in the direction it declares: handing an import profile to carts.export is a 400, and the other way round.
    entity : Optional[CartIoEntity]
        What the profile carries: whole carts (&#039;carts&#039; — the `{cart, items}` document) or bare cart lines (&#039;cart_items&#039; — the spreadsheet a buyer quick-orders from).
    format : Optional[CartIoFormat]
        The wire format. &#039;json&#039; is the canonical, re-importable document; &#039;csv&#039; is the spreadsheet form, and only line fields survive it.
    id : Optional[str]
        The profile, as carts.export and carts.import name it in `profile_id`.
    is_template : Optional[bool]
        One of the profiles this app ships with, seeded by carts.io.profiles.defaults. A profile a merchant wrote is not one, so this is how a UI separates &quot;what came with the app&quot; from &quot;what we built&quot;.
    mapping : Optional[CartIoMapping]
        Baseline-IO-compatible column mapping. An empty object (or null) is identity: the full canonical shape, every field under its own name.
    name : Optional[str]
        What a merchant picks this profile by. Unique within the tenant — reusing a name is a 409 — and the four bundled templates use it as their identity, so seeding is idempotent by name.
    options : Optional[Dict[str, Any]]
        Free-form options carried with the profile. The four bundled templates put one human sentence under `description` and nothing else; no other key is read by this app, so anything a merchant needs alongside a profile can live here.
    tenant_id : Optional[str]
        The tenant this row belongs to, echoed by the data plane.
    updated_at : Optional[str]
        When the profile last changed.
    """
    apply_mode: Optional[CartIoApplyMode] = Field(default=None, alias='apply_mode')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    direction: Optional[CartIoDirection] = Field(default=None, alias='direction')
    entity: Optional[CartIoEntity] = Field(default=None, alias='entity')
    format: Optional[CartIoFormat] = Field(default=None, alias='format')
    id: Optional[str] = Field(default=None, alias='id')
    is_template: Optional[bool] = Field(default=None, alias='is_template')
    mapping: Optional[CartIoMapping] = Field(default=None, alias='mapping')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
