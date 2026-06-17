from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class EligiblePaymentMethod(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    fee : Optional[float]
        Typed model field.
    fee_type : Optional[str]
        Typed model field.
    kind : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    provider : Optional[str]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    fee: Optional[float] = Field(default=None, alias='fee')
    fee_type: Optional[str] = Field(default=None, alias='fee_type')
    kind: Optional[str] = Field(default=None, alias='kind')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    provider: Optional[str] = Field(default=None, alias='provider')
