from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .reorder_alert import ReorderAlert

class ReorderAlerts(AppwriteModel):
    """
    

    Attributes
    ----------
    alerts : Optional[List[ReorderAlert]]
        The rows at or below their reorder point, worst first (by `shortfall`). Computed on read, so it is never stale — and never empty because of caching: an empty list means nothing is low, unless `enabled` is false.
    enabled : Optional[bool]
        false when reorder_alert_enabled is off — the list is then empty by policy, not because nothing is low.
    reorder_point_default : Optional[float]
        The threshold applied to rows carrying none of their own.
    """
    alerts: Optional[List[ReorderAlert]] = Field(default=None, alias='alerts')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    reorder_point_default: Optional[float] = Field(default=None, alias='reorder_point_default')
