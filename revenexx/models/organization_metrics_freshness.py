from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrganizationMetricsFreshness(AppwriteModel):
    """
    

    Attributes
    ----------
    missing : Optional[float]
        Companies with no metrics row yet. A rule reading revenue silently skips them, so this is the number to watch after an import.
    oldest_computed_at : Optional[str]
        The OLDEST computed_at in the table — the floor, not an average. Null when there are no rows at all.
    orders_as_of : Optional[str]
        The anchor those oldest numbers were measured from.
    organizations : Optional[float]
        Companies in this tenant.
    rows : Optional[float]
        Metrics rows that exist — at most one per company.
    """
    missing: Optional[float] = Field(default=None, alias='missing')
    oldest_computed_at: Optional[str] = Field(default=None, alias='oldest_computed_at')
    orders_as_of: Optional[str] = Field(default=None, alias='orders_as_of')
    organizations: Optional[float] = Field(default=None, alias='organizations')
    rows: Optional[float] = Field(default=None, alias='rows')
