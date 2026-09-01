from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_list_kind_tone import OrderListKindTone

class OrderListKindCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        What `lists.kind` will store. Lowercased on the way in and immutable afterwards — a merchant who wants a different code creates a new kind and moves the lists over.
    description : Optional[str]
        What this kind is for, in one sentence — the line a select shows under the title.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions, keyed by language tag.
    is_default : Optional[bool]
        Promote this kind; the previous default is demoted.
    labels : Optional[Dict[str, Any]]
        Localized titles, keyed by language tag.
    position : Optional[float]
        Where the kind sits in a select, ascending. Omitted means 0, which puts it first among the unpositioned.
    title : str
        What a person reads. `labels` adds the localized forms on top; this one is the fallback.
    tone : Optional[OrderListKindTone]
        Semantic badge colour. The client owns what each tone looks like; omitted means `neutral`.
    """
    code: str = Field(..., alias='code')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: str = Field(..., alias='title')
    tone: Optional[OrderListKindTone] = Field(default=None, alias='tone')
