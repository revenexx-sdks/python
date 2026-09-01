from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_type_tone import ChannelTypeTone

class ChannelTypeUpdateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[str]
        Replace the one-sentence description. Sent as null it is cleared; omitted it is kept. `descriptions` carries the per-locale ones.
    descriptions : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    is_default : Optional[bool]
        Promote this type; the previous default is demoted. Only `true` does anything — sending false does not demote this type, because some type must hold the flag.
    labels : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    position : Optional[float]
        Move the type in the order GET /channels/types answers in.
    title : Optional[str]
        Rename the type. A blank or non-string title is ignored, not refused — the stored one is kept.
    tone : Optional[ChannelTypeTone]
        Change the badge colour. A value outside the palette is ignored rather than refused, and the stored tone is kept.
    """
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[ChannelTypeTone] = Field(default=None, alias='tone')
