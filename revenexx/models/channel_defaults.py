from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .channel_type_defaults import ChannelTypeDefaults

class ChannelDefaults(AppwriteModel):
    """
    

    Attributes
    ----------
    created : Optional[List[Any]]
        Channel codes created by this call.
    existing : Optional[List[Any]]
        Default channel codes that already existed.
    types : Optional[ChannelTypeDefaults]
        The same answer for the channel types, which are seeded first because the seeded channel carries one.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
    types: Optional[ChannelTypeDefaults] = Field(default=None, alias='types')
