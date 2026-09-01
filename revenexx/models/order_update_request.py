from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderUpdateRequest(AppwriteModel):
    """
    Narrow modification — these six columns and no others. Anything else in the body is ignored, and a body with none of them at all is a 400 naming the allowed set. A whole key REPLACES the value it names; there is no merge into an existing snapshot. Nothing here moves the order: status, payment and fulfillment travel through the action routes.

    Attributes
    ----------
    billing_address : Optional[Dict[str, Any]]
        The invoice address, FROZEN at place-time. Changing the customer&#039;s address afterwards does not change what this order was billed to. Replaced wholesale — send the whole address, not a patch of it.
    buyer : Optional[Dict[str, Any]]
        The ordering party as it was at place-time, FROZEN: a copy, not a reference, so the order still reads correctly after the customer record is renamed, merged or deleted. The caller decides what goes in; this app stores it and reads nothing out of it. Replaced wholesale — send the whole snapshot, not a patch of it.
    customer_order_number : Optional[str]
        The BUYER&#039;s own reference — their purchase-order number. Free text, not unique, never generated here: it exists so the paperwork can carry the number the buyer&#039;s accounts payable will look for. One of the few fields PUT /orders/{id} may still change.
    metadata : Optional[Dict[str, Any]]
        Free-form data belonging to the INTEGRATION side — an ERP&#039;s own bookkeeping about this order. Stored and returned untouched; nothing here reads it. Replaced wholesale.
    shipping_address : Optional[Dict[str, Any]]
        The delivery address, FROZEN at place-time — what goes on the label of every shipment of this order. Null on an order that is never delivered (a service, a digital item, a collection). Replaced wholesale. This is the one correction that actually matters after placement: the label of every shipment still to go out is printed from it.
    user_data : Optional[Dict[str, Any]]
        Free-form data belonging to the ORDERING side — carried through from the storefront or the cart and handed back untouched. One of the few fields PUT /orders/{id} may still change. Replaced wholesale.
    """
    billing_address: Optional[Dict[str, Any]] = Field(default=None, alias='billing_address')
    buyer: Optional[Dict[str, Any]] = Field(default=None, alias='buyer')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, alias='shipping_address')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
