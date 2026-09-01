from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_export_format import CartExportFormat

class CartExportRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    format : Optional[CartExportFormat]
        Format of an ad-hoc export, read only when no profile_id is sent. &#039;json&#039; returns the whole `{cart, items}` document, &#039;csv&#039; the lines alone. Default &#039;json&#039;.
    profile_id : Optional[str]
        The export profile to run — one of the ids `GET /carts/io/profiles?direction=export` lists. Omit it for an ad-hoc export in the canonical shape, which is what `format` is for.
    """
    format: Optional[CartExportFormat] = Field(default=None, alias='format')
    profile_id: Optional[str] = Field(default=None, alias='profile_id')
