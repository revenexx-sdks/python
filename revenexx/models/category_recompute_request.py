from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CategoryRecomputeRequest(AppwriteModel):
    """
    Omit the body entirely to resume an unfinished pass, or start a fresh one when the last completed.

    Attributes
    ----------
    cursor : Optional[str]
        The `cursor` a previous call returned, to continue that pass. Send `null` explicitly to restart from the beginning; omit the field to let the app decide (resume if a pass is in flight, otherwise start fresh). Anything that is not a string or null is a 400.
    """
    cursor: Optional[str] = Field(default=None, alias='cursor')
