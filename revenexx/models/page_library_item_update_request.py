from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_block_tree import PageBlockTree

class PageLibraryItemUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value. Every page that references this item renders the new tree the next time it is delivered, which is the whole point of the library and the whole risk of editing one.

    Attributes
    ----------
    bundle : Optional[str]
        The block type this item instantiates. Changing it moves the item to a different part of the picker.
    label : Optional[str]
        What the item is called in the picker.
    tree : Optional[PageBlockTree]
        A block and its whole subtree, serialized. Produced by the editor when a selection is made reusable or saved as a template, and instantiated back into real blocks when one is inserted.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    label: Optional[str] = Field(default=None, alias='label')
    tree: Optional[PageBlockTree] = Field(default=None, alias='tree')
