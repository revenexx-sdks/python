from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SegmentRuleRecomputeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    cursor : Optional[str]
        Continuation token from a previous response — the id of the last organization the pass touched. Omit to resume or start automatically; pass null to force a restart from the beginning.
    """
    cursor: Optional[str] = Field(default=None, alias='cursor')
