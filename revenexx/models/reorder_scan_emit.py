from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReorderScanEmit(AppwriteModel):
    """
    

    Attributes
    ----------
    event_id : str
        The event id on the bus. Stable per (row, day), which is what makes a re-run harmless.
    stock_level_id : str
        The stock row the event is about.
    """
    event_id: str = Field(..., alias='event_id')
    stock_level_id: str = Field(..., alias='stock_level_id')
