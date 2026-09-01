from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .reorder_scan_emit import ReorderScanEmit

class ReorderScan(AppwriteModel):
    """
    

    Attributes
    ----------
    emitted : List[ReorderScanEmit]
        One entry per published event, in the order they went out. Re-running the scan on the same day returns the SAME ids and publishes nothing a second time — the event id is derived from the row and the day, and the bus drops the repeat.
    enabled : bool
        false when reorder_alert_enabled is off — nothing was published, and not because nothing is low.
    scanned : float
        How many rows were at or below their point when the scan ran.
    """
    emitted: List[ReorderScanEmit] = Field(..., alias='emitted')
    enabled: bool = Field(..., alias='enabled')
    scanned: float = Field(..., alias='scanned')
