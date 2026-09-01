from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_list_skipped_position import OrderListSkippedPosition

class OrderListToOrderResult(AppwriteModel):
    """
    

    Attributes
    ----------
    list_id : Optional[str]
        The list that was ordered. Unchanged by the call — the list stays, so it can be ordered again next month.
    order : Optional[Dict[str, Any]]
        The orders app&#039;s answer, verbatim and unreshaped — the whole created order, whose shape is the orders app&#039;s own `Order` schema (GET /v1/orders/{id}) and is deliberately not restated here, because a copy would be the thing that goes stale. `order_id`, `order_number` and `status` are lifted out of it for a client that needs nothing else.
    order_id : Optional[str]
        The order the orders app created. Null only when that app answered without one, which is a fault worth reporting rather than a normal outcome.
    order_number : Optional[str]
        The order number a human quotes, drawn from the tenant&#039;s order range by the orders app. It is NOT the id: every orders route addresses an order by uuid.
    positions : Optional[float]
        Positions handed to the orders app — the list&#039;s count minus `skipped`.
    skipped : Optional[List[OrderListSkippedPosition]]
        Positions left out because the catalogue no longer knows their article. Only ever non-empty when &#039;on_missing_article&#039; is &#039;skip&#039;.
    status : Optional[str]
        Where the new order stands, as the orders app decided: &#039;placed&#039; when it was accepted outright, &#039;pending&#039; when it awaits approval — a contact holding only orders.request, or an order above the tenant&#039;s approval threshold. This app does not choose it and cannot override it.
    """
    list_id: Optional[str] = Field(default=None, alias='list_id')
    order: Optional[Dict[str, Any]] = Field(default=None, alias='order')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    order_number: Optional[str] = Field(default=None, alias='order_number')
    positions: Optional[float] = Field(default=None, alias='positions')
    skipped: Optional[List[OrderListSkippedPosition]] = Field(default=None, alias='skipped')
    status: Optional[str] = Field(default=None, alias='status')
