from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderAcknowledgeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    external_ref : Optional[str]
        The fulfilling system&#039;s order reference (e.g. the ERP order number).
    """
    external_ref: Optional[str] = Field(default=None, alias='external_ref')
