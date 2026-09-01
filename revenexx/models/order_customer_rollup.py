from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderCustomerRollup(AppwriteModel):
    """
    Additive order facts for one organization. Average order value is revenue_total / order_count.

    Attributes
    ----------
    currencies : Optional[List[Any]]
        Every currency seen on the counted orders, sorted. MORE THAN ONE MEANS THE SUMS MIX CURRENCIES — nothing here converts, so a two-currency row&#039;s revenue_total is a sum of unlike numbers and should be shown per currency or not at all.
    first_order_at : Optional[str]
        When this company first ordered — placed_at where there is one, otherwise created_at. Null cannot happen on a row that exists, but the field is nullable because the columns behind it are.
    last_order_at : Optional[str]
        When they last ordered. Together with as_of this is the recency a churn rule reads.
    order_count : Optional[float]
        How many orders of this company were counted — orders in one of the counted statuses, over all time.
    order_count_30d : Optional[float]
        Orders in the 30 days before as_of.
    order_count_365d : Optional[float]
        Orders in the 365 days before as_of — the rolling year a &quot;still active&quot; rule usually asks about.
    order_count_90d : Optional[float]
        Orders in the 90 days before as_of.
    organization_id : Optional[str]
        The company these facts belong to — the id the customers app knows it by. Every row of the answer carries one; orders without an organization are counted in orders_without_organization instead.
    revenue_30d : Optional[float]
        Revenue in the 30 days before as_of.
    revenue_365d : Optional[float]
        Revenue in the 365 days before as_of.
    revenue_90d : Optional[float]
        Revenue in the 90 days before as_of.
    revenue_total : Optional[float]
        Sum of grand_total over the counted orders. Gross: it includes tax and shipping, because grand_total does.
    """
    currencies: Optional[List[Any]] = Field(default=None, alias='currencies')
    first_order_at: Optional[str] = Field(default=None, alias='first_order_at')
    last_order_at: Optional[str] = Field(default=None, alias='last_order_at')
    order_count: Optional[float] = Field(default=None, alias='order_count')
    order_count_30d: Optional[float] = Field(default=None, alias='order_count_30d')
    order_count_365d: Optional[float] = Field(default=None, alias='order_count_365d')
    order_count_90d: Optional[float] = Field(default=None, alias='order_count_90d')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    revenue_30d: Optional[float] = Field(default=None, alias='revenue_30d')
    revenue_365d: Optional[float] = Field(default=None, alias='revenue_365d')
    revenue_90d: Optional[float] = Field(default=None, alias='revenue_90d')
    revenue_total: Optional[float] = Field(default=None, alias='revenue_total')
