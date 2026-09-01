from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SeedResult(AppwriteModel):
    """
    What was created and what was already there. Nothing is ever overwritten, so a non-empty `skipped` is the normal answer to a second run.

    Attributes
    ----------
    menus : Optional[Dict[str, Any]]
        The menu half of the run.
    pages : Optional[Dict[str, Any]]
        The page half of the run.
    """
    menus: Optional[Dict[str, Any]] = Field(default=None, alias='menus')
    pages: Optional[Dict[str, Any]] = Field(default=None, alias='pages')
