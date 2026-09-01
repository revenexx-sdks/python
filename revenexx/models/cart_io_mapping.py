from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_io_mapping_column import CartIoMappingColumn

class CartIoMapping(AppwriteModel):
    """
    Baseline-IO-compatible column mapping. An empty object (or null) is identity: the full canonical shape, every field under its own name.

    Attributes
    ----------
    columns : Optional[List[CartIoMappingColumn]]
        Renames, in order. On export the row is narrowed to these columns; on import a column that is not listed is ignored. Omit or leave empty for identity.
    keys : Optional[List[Any]]
        Fields that identify a line in the payload — what the bundled quick-order template sets to [&#039;sku&#039;].
    """
    columns: Optional[List[CartIoMappingColumn]] = Field(default=None, alias='columns')
    keys: Optional[List[Any]] = Field(default=None, alias='keys')
