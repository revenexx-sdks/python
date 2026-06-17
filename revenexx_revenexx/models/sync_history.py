from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SyncHistory(AppwriteModel):
    """
    

    Attributes
    ----------
    bytes_synced : Optional[float]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    duration_ms : Optional[float]
        Typed model field.
    error : Optional[str]
        Typed model field.
    id : float
        Typed model field.
    rule_id : str
        Typed model field.
    run_id : str
        Typed model field.
    source_path : str
        Typed model field.
    status : str
        Typed model field.
    target_asset_id : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    """
    bytes_synced: Optional[float] = Field(..., alias='bytes_synced')
    created_at: Optional[str] = Field(..., alias='created_at')
    duration_ms: Optional[float] = Field(..., alias='duration_ms')
    error: Optional[str] = Field(..., alias='error')
    id: float = Field(..., alias='id')
    rule_id: str = Field(..., alias='rule_id')
    run_id: str = Field(..., alias='run_id')
    source_path: str = Field(..., alias='source_path')
    status: str = Field(..., alias='status')
    target_asset_id: Optional[str] = Field(..., alias='target_asset_id')
    tenant_id: str = Field(..., alias='tenant_id')
