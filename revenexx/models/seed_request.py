from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SeedRequest(AppwriteModel):
    """
    A theme&#039;s starting content. Both lists are optional; sending neither is a no-op.

    Attributes
    ----------
    menus : Optional[List[Any]]
        The menus to create. One with no key or no label is reported under `skipped`.
    pages : Optional[List[Any]]
        The pages to create. One that has no `slug` or no `title` is reported under `skipped` rather than refused, so one bad entry never loses the rest.
    """
    menus: Optional[List[Any]] = Field(default=None, alias='menus')
    pages: Optional[List[Any]] = Field(default=None, alias='pages')
