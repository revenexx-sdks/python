from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_weight_unit_create_request_tone import ShippingWeightUnitCreateRequestTone

class ShippingWeightUnitCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Lowercase letters, digits, - or _, starting with a letter. What a rate request names in `weight_unit`, and what a market&#039;s `weight_unit` setting stores. Immutable once created — renaming it would orphan every row carrying it.
    description : Optional[str]
        The sentence under the title, explaining when to pick this weight unit. Null when the title says enough.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    factor : float
        How many BASE units (kilograms) one of this unit weighs — a tonne is 1000, a gram 0.001, a pound 0.45359237. This number prices parcels: every weight matrix converts a request through it. Must be &gt; 0; the base unit is fixed at 1 and rejects a change.
    is_default : Optional[bool]
        Promote this value on creation; the previous default is demoted.
    labels : Optional[Dict[str, Any]]
        Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    position : Optional[float]
        Sort order in a select — the collection is returned in it.
    title : str
        What an operator reads in a select. The name a merchant renames; the code underneath never moves.
    tone : Optional[ShippingWeightUnitCreateRequestTone]
        Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
    """
    code: str = Field(..., alias='code')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    factor: float = Field(..., alias='factor')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: str = Field(..., alias='title')
    tone: Optional[ShippingWeightUnitCreateRequestTone] = Field(default=None, alias='tone')
