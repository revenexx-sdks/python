from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .bulk_job_status import BulkJobStatus
from .bulk_job_type import BulkJobType

class BulkJob(AppwriteModel):
    """
    A bulk job as returned by `/bulk-jobs`. Note that the row counts are
nested under `counts` — they are not top-level fields — and that the
response carries no `tenant_id` (the listing envelope does) and no
`updated_at`.


    Attributes
    ----------
    app : Optional[str]
        Typed model field.
    correlation_id : Optional[str]
        Typed model field.
    counts : Optional[Dict[str, Any]]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    created_by : Optional[str]
        Typed model field.
    duration_ms : Optional[float]
        Typed model field.
    entity : Optional[str]
        Typed model field.
    error_message : Optional[str]
        Typed model field.
    finished_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    profile_id : Optional[str]
        Typed model field.
    progress : Optional[Dict[str, Any]]
        Engine-reported progress. For an export this carries the
        `object_key` and `format` the result is written to.
        
    started_at : Optional[str]
        Typed model field.
    status : Optional[BulkJobStatus]
        Typed model field.
    type : Optional[BulkJobType]
        Typed model field.
    vendor : Optional[str]
        Typed model field.
    """
    app: Optional[str] = Field(default=None, alias='app')
    correlation_id: Optional[str] = Field(default=None, alias='correlation_id')
    counts: Optional[Dict[str, Any]] = Field(default=None, alias='counts')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    duration_ms: Optional[float] = Field(default=None, alias='duration_ms')
    entity: Optional[str] = Field(default=None, alias='entity')
    error_message: Optional[str] = Field(default=None, alias='error_message')
    finished_at: Optional[str] = Field(default=None, alias='finished_at')
    id: Optional[str] = Field(default=None, alias='id')
    profile_id: Optional[str] = Field(default=None, alias='profile_id')
    progress: Optional[Dict[str, Any]] = Field(default=None, alias='progress')
    started_at: Optional[str] = Field(default=None, alias='started_at')
    status: Optional[BulkJobStatus] = Field(default=None, alias='status')
    type: Optional[BulkJobType] = Field(default=None, alias='type')
    vendor: Optional[str] = Field(default=None, alias='vendor')
