from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_returned_position import OrderReturnedPosition
from .order_restock_position import OrderRestockPosition
from ..enums.order_return_status import OrderReturnStatus

class OrderReturnCompleted(AppwriteModel):
    """
    The completed return plus the restock report. Restocking itself is an explicit inventories.restock call by the orchestrator — this app books quantity_returned and says what came back, it does not write another app&#039;s stock.

    Attributes
    ----------
    completed_at : Optional[str]
        When the return was settled, stamped by the SERVER. Never taken from the body: a client clock records when a client thinks it acted, not when the goods were booked.
    created_at : Optional[str]
        When the return row was written.
    id : Optional[str]
        Primary key of the return. The {rid} segment of the return routes.
    metadata : Optional[Dict[str, Any]]
        Free-form data for the caller — the returns portal&#039;s own reference. Stored and returned untouched.
    number : Optional[str]
        The RETURN number — drawn from the tenant&#039;s return range, unique per tenant, and a third series alongside orders and delivery notes. What the customer writes on the parcel.
    order_id : Optional[str]
        The order the goods are coming back from. A return of another order is a 404 on these routes, not a cross-order write.
    positions : Optional[List[OrderReturnedPosition]]
        The positions and quantities this return covers, fixed when it was registered and guarded against the shipped-but-not-yet-returned quantity of each. Entries flagged restock are what the completion reports back for the inventories call.
    reason : Optional[str]
        Why the goods are coming back, free text as the customer or the desk stated it. Also what /reject stores when it is given no resolution out of the published set.
    received_at : Optional[str]
        When the goods physically arrived back. Null until POST …/receive — and null forever on a return that was completed straight out of registered, which is allowed.
    registered_at : Optional[str]
        When the return was announced. Defaults to now.
    rejected_at : Optional[str]
        When the return was refused. Null unless it was.
    resolution : Optional[str]
        How it ended, in one of the words this app publishes — the settlement words on a completion (refund, partial_refund, replacement, repair, store_credit), the refusal words on a rejection (wear_and_tear, not_returnable); GET /orders/vocabularies/return-resolutions carries both sets with the stage that accepts each. The column carries no database constraint; the ROUTES enforce the set, which is what stopped a client settling returns with a word nobody else knew. On a rejection that named no resolution, the free-text reason is stored here instead — which is the one case a value outside the two sets appears.
    restock : Optional[List[OrderRestockPosition]]
        One entry per returned position that carried restock: true. Empty when nothing was flagged.
    status : Optional[OrderReturnStatus]
        Where the return stands: &#039;registered&#039; = announced, nothing booked; &#039;received&#039; = the goods are back but not yet settled; &#039;completed&#039; = settled, and the only transition that books quantity_returned; &#039;rejected&#039; = refused, nothing booked. The last two are final.
    updated_at : Optional[str]
        When the return last changed — each of its transitions writes it.
    """
    completed_at: Optional[str] = Field(default=None, alias='completed_at')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    positions: Optional[List[OrderReturnedPosition]] = Field(default=None, alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
    received_at: Optional[str] = Field(default=None, alias='received_at')
    registered_at: Optional[str] = Field(default=None, alias='registered_at')
    rejected_at: Optional[str] = Field(default=None, alias='rejected_at')
    resolution: Optional[str] = Field(default=None, alias='resolution')
    restock: Optional[List[OrderRestockPosition]] = Field(default=None, alias='restock')
    status: Optional[OrderReturnStatus] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
