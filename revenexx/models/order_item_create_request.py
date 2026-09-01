from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_item_type import OrderItemType

class OrderItemCreateRequest(AppwriteModel):
    """
    A position of the placed order — needs an identity: &#039;name&#039; or &#039;sku&#039;. Items are SNAPSHOTS: carry the product copy, prices are frozen at place-time.

    Attributes
    ----------
    configuration : Optional[Dict[str, Any]]
        The chosen options of a configured line — what the configurator produced, in whatever shape it produces. Only meaningful for type &#039;configuration&#039;; null everywhere else.
    cost_center : Optional[str]
        The buyer&#039;s own cost centre for this line — a B2B field: the same order is split across several of them and the buyer&#039;s finance department needs the split per line, not per order.
    metadata : Optional[Dict[str, Any]]
        Free-form data belonging to the integration side, per position. Stored and returned untouched.
    name : Optional[str]
        The article name as it stood at place-time, frozen. Falls back to the sku when the caller sent none — a position always reads as something. Falls back to &#039;sku&#039; when omitted; one of the two is required.
    position : Optional[float]
        The line number a human reads, and what the order is sorted by. Numbered in steps of the range&#039;s position_step (10, 20, 30) unless the caller set it explicitly — the gap is what lets a line be inserted later without renumbering. Omitted = numbered in steps of the order range&#039;s position_step.
    position_text : Optional[str]
        A free note the buyer attached to this line — an engraving, a delivery instruction, the drawing number the line refers to. Printed on the paperwork, read by nothing.
    product : Optional[Dict[str, Any]]
        The product as it was at place-time, FROZEN: the copy that makes the order still correct after the catalog changes its price, its name or its attributes. The caller decides how much of the product to freeze; this app stores it and reads nothing out of it. &#039;snapshot&#039; is accepted as an alias for this key.
    product_id : Optional[str]
        The catalog product this line was taken from (the products app). Null on a custom line, and it stays a reference — the position keeps working after the product is retired.
    quantity : Optional[float]
        How much was ORDERED, in `unit`. Three decimal places, so 2.5 m of cable is a real order line. Never changed afterwards — cancelling or returning writes the quantity_* columns instead, which is what keeps the order a truthful record of what was asked for. Defaults to 1.
    sku : Optional[str]
        The article number as it stood at place-time, frozen with the rest of the line. The value an ERP and a warehouse both join on, and the one field a picker reads. Null only on a line that never had one.
    snapshot : Optional[Dict[str, Any]]
        The product as it was at place-time, FROZEN: the copy that makes the order still correct after the catalog changes its price, its name or its attributes. The caller decides how much of the product to freeze; this app stores it and reads nothing out of it. Alias for &#039;product&#039; — send one or the other, not both.
    tax_amount : Optional[float]
        Tax on this line in `currency`. Derived from line_total × tax_rate/100 when the caller sent none, which is the normal case — but a caller may send it, for a market whose rounding rules differ from ours. Send it only where your market rounds differently from line_total × tax_rate/100.
    tax_rate : Optional[float]
        Tax percentage for this line, as a number (19 means 19 %). Frozen at place-time with everything else. Defaults to 0.
    type : Optional[OrderItemType]
        What kind of line this is: &#039;product&#039; is a catalog article, &#039;configuration&#039; a configured one carrying its configuration, &#039;custom&#039; a line typed by hand that no catalog knows. Defaults to &#039;product&#039;.
    unit : Optional[str]
        The unit the quantity is counted in — piece, metre, kilogram, package. Free text as the catalog carries it; this app does no conversion.
    unit_price : Optional[float]
        NET price per unit, FROZEN at place-time. A later price change in the catalog does not reach this order. Defaults to 0. line_total is always derived from it and never taken from the body.
    user_data : Optional[Dict[str, Any]]
        Free-form data belonging to the ordering side, per position — carried through from the cart line and handed back untouched.
    """
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    cost_center: Optional[str] = Field(default=None, alias='cost_center')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    position_text: Optional[str] = Field(default=None, alias='position_text')
    product: Optional[Dict[str, Any]] = Field(default=None, alias='product')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    snapshot: Optional[Dict[str, Any]] = Field(default=None, alias='snapshot')
    tax_amount: Optional[float] = Field(default=None, alias='tax_amount')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[OrderItemType] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
