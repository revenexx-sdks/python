from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_export_format import CartExportFormat

class CartExportRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    format : Optional[CartExportFormat]
        Ad-hoc export format (only without profile_id).
    profile_id : Optional[str]
        Export profile to run; ad-hoc JSON/CSV export when omitted.
    """
    format: Optional[CartExportFormat] = Field(default=None, alias='format')
    profile_id: Optional[str] = Field(default=None, alias='profile_id')
