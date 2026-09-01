from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketTaxClassDeleted(AppwriteModel):
    """
    Confirmation that the tax class of a market is gone. The row itself is not returned — read it before deleting if you need it.

    Attributes
    ----------
    deleted : Optional[bool]
        Always true — a row that was not there is a 404, not a false.
    id : Optional[str]
        The id of the row that was deleted.
    usage_checked : Optional[bool]
        False when the cross-app usage question could not be asked (shipping not installed, or unreachable) — the row was deleted without that guarantee.
    """
    deleted: Optional[bool] = Field(default=None, alias='deleted')
    id: Optional[str] = Field(default=None, alias='id')
    usage_checked: Optional[bool] = Field(default=None, alias='usage_checked')
