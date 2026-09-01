from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderListUpdateRequest(AppwriteModel):
    """
    Partial update — rename, visibility or kind. Positions go through the items routes, and the owner cannot be changed.

    Attributes
    ----------
    kind : Optional[str]
        List kind — the `code` of one of the tenant&#039;s own kinds (GET /orderlists/kinds); defaults to the flagged one, or the market&#039;s &#039;default_kind&#039; setting.
    metadata : Optional[Dict[str, Any]]
        Free-form data the tenant keeps on the list — an ERP requisition number, a department, whatever an integration needs to recognise the list again. Never read by this app, and never merged: a write replaces the whole document.
    name : Optional[str]
        What the buyer calls this list. Free text, at least one character, and not unique: two contacts may both keep a &quot;Weekly office supplies&quot;. It is also the name a NEW cart gets when POST /orderlists/{id}/cart creates one.
    shared : Optional[bool]
        Whether the OWNING ORGANIZATION may see this list. False — the default — keeps it private to `owner_id`, and a foreign private list answers 404 rather than 403, so an outsider learns nothing from the difference. True lets every contact of `organization_id` READ it, and write it only where the tenant turned on the `shared_lists_editable` setting. A list with no `organization_id` shares with nobody however this is set.
    """
    kind: Optional[str] = Field(default=None, alias='kind')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    shared: Optional[bool] = Field(default=None, alias='shared')
