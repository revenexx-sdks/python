from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageScheduleRequest(AppwriteModel):
    """
    When this working copy should go live.

    Attributes
    ----------
    scheduledat : str
        The moment to publish at. Stored on the edit state and echoed back normalized to UTC.
    """
    scheduledat: str = Field(..., alias='scheduledAt')
