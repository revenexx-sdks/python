from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PagePreviewGrantRequest(AppwriteModel):
    """
    How long the link should live.

    Attributes
    ----------
    ttlhours : Optional[float]
        Hours until the link expires. Defaults to 72. After that `GET /pages/delivery/preview/{token}` answers 410 rather than 404, so the holder can tell &quot;expired&quot; from &quot;wrong link&quot;.
    """
    ttlhours: Optional[float] = Field(default=None, alias='ttlHours')
