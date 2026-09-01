from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_list_item_input import OrderListItemInput

class OrderListCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : Optional[List[OrderListItemInput]]
        Optional initial positions. Every one is validated — and article-checked where `reject_unknown_articles` is on — BEFORE the list row is written, so a rejected position never leaves an empty list behind.
    kind : Optional[str]
        List kind — the `code` of one of the tenant&#039;s own kinds (GET /orderlists/kinds); defaults to the flagged one, or the market&#039;s &#039;default_kind&#039; setting.
    metadata : Optional[Dict[str, Any]]
        Free-form data the tenant keeps on the list — an ERP requisition number, a department, whatever an integration needs to recognise the list again. Never read by this app, and never merged: a write replaces the whole document.
    name : str
        What the buyer calls this list. Free text, at least one character, and not unique: two contacts may both keep a &quot;Weekly office supplies&quot;. It is also the name a NEW cart gets when POST /orderlists/{id}/cart creates one.
    organization_id : Optional[str]
        The organization the sharing is scoped to. Null means the list can only ever be the owner&#039;s own: `shared` is meaningless without it, because there is no set of people to share with. It is also what the order conversion hands the orders app as the buying organization.
    owner_id : str
        The contact who owns the list. Ownership IS the authorization here: a caller the gateway resolved to a contact sees their own lists plus their organization&#039;s shared ones, and may write only their own — unless `shared_lists_editable` opens a shared list to the whole owning organization. Set once at create; no route moves a list to another owner.
    owner_name : str
        The owner&#039;s display name as it stood when the list was created — a snapshot, so renaming the contact does not rewrite it. Carried so a shared list can say whose it is without a call to the contacts app.
    shared : Optional[bool]
        Whether the OWNING ORGANIZATION may see this list. False — the default — keeps it private to `owner_id`, and a foreign private list answers 404 rather than 403, so an outsider learns nothing from the difference. True lets every contact of `organization_id` READ it, and write it only where the tenant turned on the `shared_lists_editable` setting. A list with no `organization_id` shares with nobody however this is set.
    """
    items: Optional[List[OrderListItemInput]] = Field(default=None, alias='items')
    kind: Optional[str] = Field(default=None, alias='kind')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: str = Field(..., alias='name')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    owner_id: str = Field(..., alias='owner_id')
    owner_name: str = Field(..., alias='owner_name')
    shared: Optional[bool] = Field(default=None, alias='shared')
