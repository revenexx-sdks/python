from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageCommentItem(AppwriteModel):
    """
    One comment, in the shape the editor renders — this is not the stored row: the id is `uuid`, the timestamps are `created`/`updated` and the author is nested under `user`.

    Attributes
    ----------
    blockuuids : Optional[List[Any]]
        The blocks this thread hangs on, so the editor can draw a marker next to them. Empty for a comment about the page as a whole.
    body : Optional[str]
        The comment itself, as editor HTML. @mentions are `&lt;span data-type=&quot;mention&quot; data-id=&quot;…&quot;&gt;` — that is what this app reads to decide whom to notify — and task checkboxes are `&lt;li data-type=&quot;taskItem&quot; data-checked=&quot;…&quot;&gt;`.
    created : Optional[str]
        When the comment was written.
    parentuuid : Optional[str]
        The root comment this is a reply to. Absent on a root — and only roots can be resolved.
    resolved : Optional[bool]
        Whether the thread was marked done. Replies inherit nothing: resolving is a property of the root.
    updated : Optional[str]
        When it was last edited. Absent when it never was.
    user : Optional[Dict[str, Any]]
        Who wrote it, or `null` when it was written without an identity.
    uuid : Optional[str]
        The comment id. Every comment route addresses one by it.
    """
    blockuuids: Optional[List[Any]] = Field(default=None, alias='blockUuids')
    body: Optional[str] = Field(default=None, alias='body')
    created: Optional[str] = Field(default=None, alias='created')
    parentuuid: Optional[str] = Field(default=None, alias='parentUuid')
    resolved: Optional[bool] = Field(default=None, alias='resolved')
    updated: Optional[str] = Field(default=None, alias='updated')
    user: Optional[Dict[str, Any]] = Field(default=None, alias='user')
    uuid: Optional[str] = Field(default=None, alias='uuid')
