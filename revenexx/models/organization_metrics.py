from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrganizationMetrics(AppwriteModel):
    """
    What an organization has BOUGHT, materialized from the orders app. One row per organization — including all-zero rows for companies that never ordered, so a &#039;never bought anything&#039; rule has something to match.

    Attributes
    ----------
    avg_order_value : Optional[float]
        revenue_total / order_count, computed here from the sums rather than averaged upstream. Zero when there are no orders.
    avg_order_value_365d : Optional[float]
        revenue_365d / order_count_365d. Zero when there were none in the window.
    computed_at : Optional[str]
        When this row was last written. The projection is materialized, so this is how stale the numbers are.
    created_at : Optional[str]
        When the projection row first appeared.
    currency : Optional[str]
        The single ISO 4217 currency all counted orders were in. NULL when there were none, and also when there were several — read `currency_mixed` to tell those two apart.
    currency_mixed : Optional[bool]
        True when this company ordered in more than one currency. The sums are still stored (dropping money is worse), but they are not comparable against a threshold, and a rule reading revenue should say so.
    first_order_at : Optional[str]
        When this company first ordered. Null if it never has — that is what makes it usable as &quot;is this a customer at all?&quot;.
    id : Optional[str]
        Primary key of the projection row.
    last_order_at : Optional[str]
        When this company last ordered. Null if it never has, which is why the virtual `days_since_last_order` rule field never matches those companies: use `last_order_at is_empty` for them.
    order_count : Optional[float]
        Orders ever counted for this company.
    order_count_30d : Optional[float]
        Orders in the 30 days before `orders_as_of`. A rolling window, not a calendar month.
    order_count_365d : Optional[float]
        Orders in the 365 days before `orders_as_of`.
    order_count_90d : Optional[float]
        Orders in the 90 days before `orders_as_of`.
    orders_as_of : Optional[str]
        The instant the rolling windows were measured from. Pinned across a chunked refresh, so a multi-call pass cannot let the windows slide underneath it.
    organization_id : Optional[str]
        The company these numbers describe. One row per organization, and rows exist for companies that never ordered — all zeros rather than missing, so a &quot;never bought&quot; rule matches something.
    revenue_30d : Optional[float]
        Revenue in the 30 days before `orders_as_of`.
    revenue_365d : Optional[float]
        Revenue in the 365 days before `orders_as_of`. The usual &quot;how big is this customer&quot; number, and the one a key-account rule should read.
    revenue_90d : Optional[float]
        Revenue in the 90 days before `orders_as_of`.
    revenue_total : Optional[float]
        Revenue ever counted, in `currency`. Which orders count is the orders app&#039;s decision, not this app&#039;s.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    updated_at : Optional[str]
        When the row last changed. Unchanged numbers are not rewritten, so this can lag `computed_at`.
    """
    avg_order_value: Optional[float] = Field(default=None, alias='avg_order_value')
    avg_order_value_365d: Optional[float] = Field(default=None, alias='avg_order_value_365d')
    computed_at: Optional[str] = Field(default=None, alias='computed_at')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    currency_mixed: Optional[bool] = Field(default=None, alias='currency_mixed')
    first_order_at: Optional[str] = Field(default=None, alias='first_order_at')
    id: Optional[str] = Field(default=None, alias='id')
    last_order_at: Optional[str] = Field(default=None, alias='last_order_at')
    order_count: Optional[float] = Field(default=None, alias='order_count')
    order_count_30d: Optional[float] = Field(default=None, alias='order_count_30d')
    order_count_365d: Optional[float] = Field(default=None, alias='order_count_365d')
    order_count_90d: Optional[float] = Field(default=None, alias='order_count_90d')
    orders_as_of: Optional[str] = Field(default=None, alias='orders_as_of')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    revenue_30d: Optional[float] = Field(default=None, alias='revenue_30d')
    revenue_365d: Optional[float] = Field(default=None, alias='revenue_365d')
    revenue_90d: Optional[float] = Field(default=None, alias='revenue_90d')
    revenue_total: Optional[float] = Field(default=None, alias='revenue_total')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
