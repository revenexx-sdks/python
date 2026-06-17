from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceList(AppwriteModel):
    """
    

    Attributes
    ----------
    channel_id : Optional[str]
        Typed model field.
    code : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    market_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    organization_id : Optional[str]
        Typed model field.
    priority : Optional[float]
        Typed model field.
    status : Optional[str]
        Typed model field.
    tax_included : Optional[bool]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    valid_from : Optional[str]
        Typed model field.
    valid_until : Optional[str]
        Typed model field.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: Optional[str] = Field(default=None, alias='code')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    priority: Optional[float] = Field(default=None, alias='priority')
    status: Optional[str] = Field(default=None, alias='status')
    tax_included: Optional[bool] = Field(default=None, alias='tax_included')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
