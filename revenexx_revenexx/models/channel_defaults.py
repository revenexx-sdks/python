from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ChannelDefaults(AppwriteModel):
    """
    

    Attributes
    ----------
    created : Optional[List[Any]]
        Channel codes created by this call.
    existing : Optional[List[Any]]
        Default channel codes that already existed.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
