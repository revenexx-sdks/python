from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_block_tree import PageBlockTree

class LibraryItem(AppwriteModel):
    """
    One reusable block. Every page that references it renders THIS tree, so editing the item changes every placement at once.

    Attributes
    ----------
    bundle : Optional[str]
        The block type this item instantiates. The library picker filters by it, so an item only ever appears where its bundle is allowed. Theme-defined.
    created_at : Optional[str]
        When the item entered the library.
    created_by : Optional[str]
        The user id that made the block reusable.
    deleted_at : Optional[str]
        The tombstone. A soft-deleted item is never listed or handed out, and a block still referencing it keeps rendering its own last state rather than breaking.
    id : Optional[str]
        The library item id. A block references it to become an instance of the item rather than a copy.
    label : Optional[str]
        What the item is called in the library picker. This is the only thing an editor sees before inserting it, so it carries the whole description.
    tree : Optional[PageBlockTree]
        The block and everything under it, serialized. This is the payload: every page that references the item renders THIS tree, so editing it here changes every placement at once.
    updated_at : Optional[str]
        When the item last changed — i.e. when every page referencing it last changed with it.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    id: Optional[str] = Field(default=None, alias='id')
    label: Optional[str] = Field(default=None, alias='label')
    tree: Optional[PageBlockTree] = Field(default=None, alias='tree')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
