from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrganizationMetricsRefreshResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    as_of : Optional[str]
        The instant the rolling windows are measured from. Send it back on every continuation — that is what stops the 30/90/365-day windows sliding while a multi-call refresh runs.
    batched : Optional[bool]
        False if an insert had to fall back to row-at-a-time. A performance fact, not an error.
    batches : Optional[float]
        Rollup calls made to the orders app — the cross-app cost of this pass.
    cursor : Optional[str]
        Where to resume: the id of the last organization this call processed. Send it back verbatim; null when the pass finished. No example is published — the value names a row in THIS tenant, and `cursor: &quot;sample cursor&quot;` reaches PostgREST as a malformed uuid and comes back as a 400 nobody can read.
    done : Optional[bool]
        False means the budget ran out with work left — POST again with the returned `cursor` AND `as_of`.
    inserted : Optional[float]
        Metrics rows created — organizations that had none yet.
    orders_scanned : Optional[float]
        Orders the orders app counted while answering this call.
    orders_without_organization : Optional[float]
        Orders the orders app could not attribute to a company (B2C/guest). They belong to no organization and land in no metrics row.
    organizations : Optional[float]
        Organizations processed by THIS call.
    unchanged : Optional[float]
        Rows that already said the same thing — no write was issued. A routine refresh is almost all of these.
    updated : Optional[float]
        Metrics rows whose numbers actually changed.
    with_orders : Optional[float]
        Of those, how many have at least one counted order.
    """
    as_of: Optional[str] = Field(default=None, alias='as_of')
    batched: Optional[bool] = Field(default=None, alias='batched')
    batches: Optional[float] = Field(default=None, alias='batches')
    cursor: Optional[str] = Field(default=None, alias='cursor')
    done: Optional[bool] = Field(default=None, alias='done')
    inserted: Optional[float] = Field(default=None, alias='inserted')
    orders_scanned: Optional[float] = Field(default=None, alias='orders_scanned')
    orders_without_organization: Optional[float] = Field(default=None, alias='orders_without_organization')
    organizations: Optional[float] = Field(default=None, alias='organizations')
    unchanged: Optional[float] = Field(default=None, alias='unchanged')
    updated: Optional[float] = Field(default=None, alias='updated')
    with_orders: Optional[float] = Field(default=None, alias='with_orders')
