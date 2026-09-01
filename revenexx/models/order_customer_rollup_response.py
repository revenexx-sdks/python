from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_customer_rollup import OrderCustomerRollup
from ..enums.order_customer_rollup_response_statuses import OrderCustomerRollupResponseStatuses

class OrderCustomerRollupResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    as_of : Optional[str]
        The anchor the windows were measured from — echoed so a paging caller can pin it.
    cursor : Optional[str]
        Where to resume, when `done` is false — the id of the last order this call read. Null once the scan finished. Send it back unchanged, together with the same as_of.
    done : Optional[bool]
        True = the whole set was scanned and this answer is complete. False = the scan hit its time budget: send `cursor` back to continue, and MERGE the parts (every number is additive, min for first_order_at, max for last_order_at, union for currencies).
    items : Optional[List[OrderCustomerRollup]]
        One row per organization that appeared on a counted order, sorted by id. A company with no counted order is absent — this answer does not carry zero rows.
    orders_scanned : Optional[float]
        How many order rows this call read, attributed or not. It is the cost of the call, and on a partial answer the size of the part.
    orders_without_organization : Optional[float]
        Orders read that carry no organization_id — private and guest orders. They are real revenue and are deliberately not attributed to anybody, so they appear here and in no row of items.
    organizations : Optional[float]
        How many rows `items` carries. On a partial answer this counts what THIS part saw, not the whole tenant.
    statuses : Optional[List[OrderCustomerRollupResponseStatuses]]
        The statuses that were counted, echoed — the default set unless the request named its own.
    windows : Optional[List[Any]]
        The rolling windows the *_30d / *_90d / *_365d numbers were measured over, in days. Echoed so a caller reads the numbers with the right labels instead of hard-coding three of them.
    """
    as_of: Optional[str] = Field(default=None, alias='as_of')
    cursor: Optional[str] = Field(default=None, alias='cursor')
    done: Optional[bool] = Field(default=None, alias='done')
    items: Optional[List[OrderCustomerRollup]] = Field(default=None, alias='items')
    orders_scanned: Optional[float] = Field(default=None, alias='orders_scanned')
    orders_without_organization: Optional[float] = Field(default=None, alias='orders_without_organization')
    organizations: Optional[float] = Field(default=None, alias='organizations')
    statuses: Optional[List[OrderCustomerRollupResponseStatuses]] = Field(default=None, alias='statuses')
    windows: Optional[List[Any]] = Field(default=None, alias='windows')
