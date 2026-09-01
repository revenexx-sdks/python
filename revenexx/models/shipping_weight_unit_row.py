from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_weight_unit_row_tone import ShippingWeightUnitRowTone

class ShippingWeightUnitRow(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        What a rate request names in `weight_unit`, and what a market&#039;s `weight_unit` setting stores. Immutable once created — renaming it would orphan every row carrying it.
    created_at : Optional[str]
        When the row was created (UTC).
    description : Optional[str]
        The sentence under the title, explaining when to pick this weight unit. Null when the title says enough.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    factor : Optional[float]
        How many BASE units (kilograms) one of this unit weighs — a tonne is 1000, a gram 0.001, a pound 0.45359237. This number prices parcels: every weight matrix converts a request through it. Must be &gt; 0; the base unit is fixed at 1 and rejects a change.
    id : Optional[str]
        Row id, assigned by the database on insert.
    is_base : Optional[bool]
        The anchor every other factor is expressed in. Exactly one row, fixed at install, not writable and not deletable — moving it would silently reprice every weight matrix.
    is_default : Optional[bool]
        The unit a market whose `weight_unit` setting is unset keys its tiers in. Exactly one row carries it.
    is_system : Optional[bool]
        Seeded on install rather than typed by the merchant. Still renameable and still deletable; it only says where the row came from.
    labels : Optional[Dict[str, Any]]
        Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    position : Optional[float]
        Sort order in a select — the collection is returned in it.
    title : Optional[str]
        What an operator reads in a select. The name a merchant renames; the code underneath never moves.
    tone : Optional[ShippingWeightUnitRowTone]
        Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
    updated_at : Optional[str]
        When the row was last written (UTC).
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    factor: Optional[float] = Field(default=None, alias='factor')
    id: Optional[str] = Field(default=None, alias='id')
    is_base: Optional[bool] = Field(default=None, alias='is_base')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    is_system: Optional[bool] = Field(default=None, alias='is_system')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[ShippingWeightUnitRowTone] = Field(default=None, alias='tone')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
