from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_item_type import OrderItemType

class OrderItem(AppwriteModel):
    """
    One POSITION of an order, frozen at place-time: the article as it was, the price as it was, and three running quantities (shipped, cancelled, returned) that everything after placement books against. `quantity` itself never changes.

    Attributes
    ----------
    configuration : Optional[Dict[str, Any]]
        The chosen options of a configured line — what the configurator produced, in whatever shape it produces. Only meaningful for type &#039;configuration&#039;; null everywhere else.
    cost_center : Optional[str]
        The buyer&#039;s own cost centre for this line — a B2B field: the same order is split across several of them and the buyer&#039;s finance department needs the split per line, not per order.
    created_at : Optional[str]
        When the position was written — the moment the order was placed.
    id : Optional[str]
        Primary key of the position. This is the id every positions[] payload names: /ship, /items/cancel and /return all take order_item_id.
    line_total : Optional[float]
        quantity × unit_price, NET, always COMPUTED here — a caller cannot set it. The order&#039;s subtotal is the sum of these.
    metadata : Optional[Dict[str, Any]]
        Free-form data belonging to the integration side, per position. Stored and returned untouched.
    name : Optional[str]
        The article name as it stood at place-time, frozen. Falls back to the sku when the caller sent none — a position always reads as something.
    order_id : Optional[str]
        The order this position belongs to. Deleting the order deletes its positions.
    position : Optional[float]
        The line number a human reads, and what the order is sorted by. Numbered in steps of the range&#039;s position_step (10, 20, 30) unless the caller set it explicitly — the gap is what lets a line be inserted later without renumbering.
    position_text : Optional[str]
        A free note the buyer attached to this line — an engraving, a delivery instruction, the drawing number the line refers to. Printed on the paperwork, read by nothing.
    product : Optional[Dict[str, Any]]
        The product as it was at place-time, FROZEN: the copy that makes the order still correct after the catalog changes its price, its name or its attributes. The caller decides how much of the product to freeze; this app stores it and reads nothing out of it.
    product_id : Optional[str]
        The catalog product this line was taken from (the products app). Null on a custom line, and it stays a reference — the position keeps working after the product is retired.
    quantity : Optional[float]
        How much was ORDERED, in `unit`. Three decimal places, so 2.5 m of cable is a real order line. Never changed afterwards — cancelling or returning writes the quantity_* columns instead, which is what keeps the order a truthful record of what was asked for.
    quantity_cancelled : Optional[float]
        How much of this position was cancelled and will never ship. Written by /cancel (all of it) and /items/cancel (a named quantity). Cancelling reduces the effective quantity, so an order whose every position is fully cancelled becomes cancelled itself.
    quantity_returned : Optional[float]
        How much of this position came BACK, booked when a return is completed — not when it is registered or received. This is the goods accounting: it never reduces quantity_shipped, so a position can be shipped 3 and returned 3.
    quantity_shipped : Optional[float]
        How much of this position has GONE OUT, summed over the shipments. Written only by POST /orders/{id}/ship; it is what fulfillment_status is derived from, and what a return is guarded against.
    sku : Optional[str]
        The article number as it stood at place-time, frozen with the rest of the line. The value an ERP and a warehouse both join on, and the one field a picker reads. Null only on a line that never had one.
    tax_amount : Optional[float]
        Tax on this line in `currency`. Derived from line_total × tax_rate/100 when the caller sent none, which is the normal case — but a caller may send it, for a market whose rounding rules differ from ours.
    tax_rate : Optional[float]
        Tax percentage for this line, as a number (19 means 19 %). Frozen at place-time with everything else.
    type : Optional[OrderItemType]
        What kind of line this is: &#039;product&#039; is a catalog article, &#039;configuration&#039; a configured one carrying its configuration, &#039;custom&#039; a line typed by hand that no catalog knows.
    unit : Optional[str]
        The unit the quantity is counted in — piece, metre, kilogram, package. Free text as the catalog carries it; this app does no conversion.
    unit_price : Optional[float]
        NET price per unit, FROZEN at place-time. A later price change in the catalog does not reach this order.
    updated_at : Optional[str]
        When the position last changed, which in practice means the last time a quantity was booked onto it.
    user_data : Optional[Dict[str, Any]]
        Free-form data belonging to the ordering side, per position — carried through from the cart line and handed back untouched.
    """
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    cost_center: Optional[str] = Field(default=None, alias='cost_center')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    line_total: Optional[float] = Field(default=None, alias='line_total')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    position: Optional[float] = Field(default=None, alias='position')
    position_text: Optional[str] = Field(default=None, alias='position_text')
    product: Optional[Dict[str, Any]] = Field(default=None, alias='product')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    quantity_cancelled: Optional[float] = Field(default=None, alias='quantity_cancelled')
    quantity_returned: Optional[float] = Field(default=None, alias='quantity_returned')
    quantity_shipped: Optional[float] = Field(default=None, alias='quantity_shipped')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_amount: Optional[float] = Field(default=None, alias='tax_amount')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[OrderItemType] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
