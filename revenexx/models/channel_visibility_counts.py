from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ChannelVisibilityCounts(AppwriteModel):
    """
    The three tallies, so a caller can log or alert on a batch without walking it.

    Attributes
    ----------
    hidden : Optional[float]
        How many must not be. A batch where this equals `total` and the reason is no_channel_context means the channel did not resolve, not that the assortment is empty.
    total : Optional[float]
        How many rows were decided — the length of the `items` sent.
    visible : Optional[float]
        How many may be shown.
    """
    hidden: Optional[float] = Field(default=None, alias='hidden')
    total: Optional[float] = Field(default=None, alias='total')
    visible: Optional[float] = Field(default=None, alias='visible')
