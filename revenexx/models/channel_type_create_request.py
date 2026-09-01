from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_type_tone import ChannelTypeTone

class ChannelTypeCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        What `channels.type` will store. Lowercased and trimmed before it is written, and fixed from then on — a rename would orphan every channel carrying it.
    description : Optional[str]
        One sentence on what kind of place this type of channel is, for the merchant choosing between them. Plain text, in the tenant&#039;s primary language; `descriptions` carries the per-locale ones.
    descriptions : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    is_default : Optional[bool]
        Promote this type; the previous default is demoted. The default is the type a channel created without one gets.
    labels : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    position : Optional[float]
        Sort position (default 0). GET /channels/types answers in this order; ties fall back to the code.
    title : str
        The fallback name. `labels` carries the per-locale ones.
    tone : Optional[ChannelTypeTone]
        Badge colour (default &#039;neutral&#039;). A value outside the palette is ignored rather than refused.
    """
    code: str = Field(..., alias='code')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: str = Field(..., alias='title')
    tone: Optional[ChannelTypeTone] = Field(default=None, alias='tone')
