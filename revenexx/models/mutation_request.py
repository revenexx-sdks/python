from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MutationRequest(AppwriteModel):
    """
    One change to the page.

    Attributes
    ----------
    langcode : Optional[str]
        Which language the returned state should be resolved for. Not the language the change is written in — that lives in the payload.
    payload : Optional[Dict[str, Any]]
        The arguments of that change; the keys depend on the plugin (`add` takes `{ bundle, hostEntityType, hostEntityUuid, hostField }`, `move` takes `{ uuid, preceedingUuid }`, and so on). Anything non-deterministic in it — new uuids, a library item&#039;s tree, a copied subtree — is resolved once here and stored, so replaying the log is deterministic forever.
    plugin : str
        Which kind of change this is — `add`, `move`, `delete`, `duplicate`, `update_field_value`, `update_options`, … An id this app does not implement is refused with 400 rather than stored, because the log has to replay.
    """
    langcode: Optional[str] = Field(default=None, alias='langcode')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
    plugin: str = Field(..., alias='plugin')
