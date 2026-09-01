from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BulkJobStatus(AppwriteModel):
    """
    Lifecycle of a `baseline.bulk_jobs` row:
`pending → running → completed`, or `partial` (finished with
`counts.rejected &gt; 0`), `failed`, or `canceled`.

    """
    pass
