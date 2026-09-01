from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageCommentCreateRequest(AppwriteModel):
    """
    A new comment. Send `blockUuids` for a thread anchored to blocks, `parentUuid` for a reply.

    Attributes
    ----------
    blockuuids : Optional[List[Any]]
        The blocks this thread is about, so the editor can draw a marker next to them. Leave empty for a comment about the page as a whole.
    body : str
        The comment, as editor HTML. `&lt;span data-type=&quot;mention&quot; data-id=&quot;USER_ID&quot;&gt;` is what this app reads to decide whom to notify; `&lt;li data-type=&quot;taskItem&quot; data-checked=&quot;false&quot;&gt;` makes a checkbox the toggle-task route can flip.
    parentuuid : Optional[str]
        The root comment this replies to. Omit for a new thread — only roots can be resolved.
    """
    blockuuids: Optional[List[Any]] = Field(default=None, alias='blockUuids')
    body: str = Field(..., alias='body')
    parentuuid: Optional[str] = Field(default=None, alias='parentUuid')
