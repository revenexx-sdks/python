from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_status import MarketStatus

class MarketCreateRequest(AppwriteModel):
    """
    A market needs a &#039;code&#039; and a &#039;name&#039; — currency defaults to EUR, status to active.

    Attributes
    ----------
    code : str
        Market code (unique per tenant).
    currency : Optional[str]
        ISO 4217 code (default &#039;EUR&#039;).
    is_default : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Localized display names ({locale: label}).
    name : str
        Typed model field.
    position : Optional[float]
        Sort position (default 0).
    status : Optional[MarketStatus]
        Default &#039;active&#039;.
    """
    code: str = Field(..., alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: str = Field(..., alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    status: Optional[MarketStatus] = Field(default=None, alias='status')
