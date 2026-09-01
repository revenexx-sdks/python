from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrganizationMetricsRefreshRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    as_of : Optional[str]
        Anchor for the rolling windows — pass back the value the previous call returned.
    cursor : Optional[str]
        Continue an unfinished refresh: the value the previous call returned, verbatim. It is the id of the last organization processed, so only a value this API handed out ever resolves.
    organization_ids : Optional[List[Any]]
        Refresh exactly these organizations in one call instead of walking all of them.
    """
    as_of: Optional[str] = Field(default=None, alias='as_of')
    cursor: Optional[str] = Field(default=None, alias='cursor')
    organization_ids: Optional[List[Any]] = Field(default=None, alias='organization_ids')
