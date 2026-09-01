from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_list_kind_tone import OrderListKindTone

class OrderListKindUpdateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[str]
        What this kind is for, in one sentence. Explicit null clears it.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions, keyed by language tag. Replaces the whole map rather than merging into it.
    is_default : Optional[bool]
        True promotes this kind and demotes the previous default — the same move POST /orderlists/kinds/{id}/make-default makes on its own.
    labels : Optional[Dict[str, Any]]
        Localized titles, keyed by language tag. Replaces the whole map rather than merging into it.
    position : Optional[float]
        Where the kind sits in a select, ascending.
    title : Optional[str]
        What a person reads. A blank title is ignored rather than stored — a kind with no words is unreadable in every UI.
    tone : Optional[OrderListKindTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[OrderListKindTone] = Field(default=None, alias='tone')
