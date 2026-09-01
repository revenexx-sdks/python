from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class TenantConfig(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    default_locale : Optional[str]
        Typed model field.
    defaults : Optional[List[Any]]
        Typed model field.
    delivery_reporting : Optional[List[Any]]
        Typed model field.
    locales : Optional[List[Any]]
        Typed model field.
    product : Optional[str]
        Typed model field.
    provisioned_at : Optional[str]
        Typed model field.
    quiet_hours : Optional[List[Any]]
        Typed model field.
    quotas : Optional[List[Any]]
        Typed model field.
    retention_days : Optional[float]
        Typed model field.
    support_email : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(..., alias='created_at')
    default_locale: Optional[str] = Field(..., alias='default_locale')
    defaults: Optional[List[Any]] = Field(..., alias='defaults')
    delivery_reporting: Optional[List[Any]] = Field(..., alias='delivery_reporting')
    locales: Optional[List[Any]] = Field(..., alias='locales')
    product: Optional[str] = Field(..., alias='product')
    provisioned_at: Optional[str] = Field(..., alias='provisioned_at')
    quiet_hours: Optional[List[Any]] = Field(..., alias='quiet_hours')
    quotas: Optional[List[Any]] = Field(..., alias='quotas')
    retention_days: Optional[float] = Field(..., alias='retention_days')
    support_email: Optional[str] = Field(..., alias='support_email')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: Optional[str] = Field(..., alias='updated_at')
