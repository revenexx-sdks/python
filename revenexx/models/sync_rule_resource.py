from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SyncRuleResource(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    enabled : bool
        Typed model field.
    id : str
        Typed model field.
    last_run_at : Optional[str]
        Typed model field.
    options : List[Any]
        Typed model field.
    schedule : str
        Typed model field.
    sftp_account_id : str
        Typed model field.
    source_path : str
        Typed model field.
    target_folder_id : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    """
    created_at: Optional[str] = Field(..., alias='created_at')
    enabled: bool = Field(..., alias='enabled')
    id: str = Field(..., alias='id')
    last_run_at: Optional[str] = Field(..., alias='last_run_at')
    options: List[Any] = Field(..., alias='options')
    schedule: str = Field(..., alias='schedule')
    sftp_account_id: str = Field(..., alias='sftp_account_id')
    source_path: str = Field(..., alias='source_path')
    target_folder_id: Optional[str] = Field(..., alias='target_folder_id')
    tenant_id: str = Field(..., alias='tenant_id')
