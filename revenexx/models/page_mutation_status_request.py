from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageMutationStatusRequest(AppwriteModel):
    """
    Which entry of the history to switch, and to what.

    Attributes
    ----------
    enabled : bool
        Whether the entry takes part in the replay.
    index : float
        The position in the mutation log to switch. Unknown positions answer 404.
    langcode : Optional[str]
        Which language the returned state should be resolved for.
    """
    enabled: bool = Field(..., alias='enabled')
    index: float = Field(..., alias='index')
    langcode: Optional[str] = Field(default=None, alias='langcode')
