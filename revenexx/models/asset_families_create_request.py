from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetFamiliesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The asset family&#039;s stable identifier — a class of media with one shared shape. Unique per tenant.
    labels : Optional[Dict[str, Any]]
        What the asset family is called, per language tag.
    naming_convention : Optional[Dict[str, Any]]
        How a file of this family is named, so an import can bind a file to a product without a mapping table. `source` is the product value the file name is built from, `pattern` how it is assembled, `allowed_extensions` what may be uploaded.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    naming_convention: Optional[Dict[str, Any]] = Field(default=None, alias='naming_convention')
