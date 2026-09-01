from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuditEntry(AppwriteModel):
    """
    

    Attributes
    ----------
    action : str
        Typed model field.
    changes : Optional[List[Any]]
        Typed model field.
    created_at : str
        Typed model field.
    id : str
        Typed model field.
    resource_id : str
        Typed model field.
    resource_key : Optional[str]
        Typed model field.
    resource_type : str
        Typed model field.
    subject : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    """
    action: str = Field(..., alias='action')
    changes: Optional[List[Any]] = Field(..., alias='changes')
    created_at: str = Field(..., alias='created_at')
    id: str = Field(..., alias='id')
    resource_id: str = Field(..., alias='resource_id')
    resource_key: Optional[str] = Field(..., alias='resource_key')
    resource_type: str = Field(..., alias='resource_type')
    subject: Optional[str] = Field(..., alias='subject')
    tenant_id: str = Field(..., alias='tenant_id')
