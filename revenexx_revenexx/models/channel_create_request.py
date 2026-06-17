from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_status import ChannelStatus
from ..enums.channel_type import ChannelType

class ChannelCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Stable channel code, unique per tenant (e.g. shop, punchout-acme).
    is_default : Optional[bool]
        Mark as the default channel (default false).
    labels : Optional[Dict[str, Any]]
        Localized display names keyed by locale.
    name : str
        Display name.
    position : Optional[float]
        Sort position (default 0).
    status : Optional[ChannelStatus]
        Lifecycle status (default &#039;active&#039;).
    type : Optional[ChannelType]
        Where business happens (default &#039;storefront&#039;).
    """
    code: str = Field(..., alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: str = Field(..., alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    status: Optional[ChannelStatus] = Field(default=None, alias='status')
    type: Optional[ChannelType] = Field(default=None, alias='type')
