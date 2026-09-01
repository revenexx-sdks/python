from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartPurgeSweep(AppwriteModel):
    """
    The second sweep, and the only destructive thing this app does: carts past their retention window are deleted, their lines with them. An ordered cart is never touched at any setting — it is the source record of a sale.

    Attributes
    ----------
    capped : Optional[bool]
        More carts were available to examine than one pass examines; the rest go next tick, oldest first.
    cart_ids : Optional[List[Any]]
        The carts this sweep touched, so a merchant can look at them before or after.
    cart_ttl_days : Optional[float]
        The tenant baseline&#039;s window for CUSTOMER carts, in days. 0 is &#039;never delete&#039; — the default, and also where an unparsable value lands, so no settings outage can start a purge.
    cutoff : Optional[str]
        The baseline cutoff, for carts belonging to no market. Null when the baseline keeps everything.
    deleted : Optional[float]
        Carts actually deleted. 0 on a dry run — see `found`.
    enabled : Optional[bool]
        Retention was in force for at least one cart this pass looked at — the baseline, or some market that sets a window while the baseline leaves it off. False means nothing could have been deleted.
    found : Optional[float]
        Carts past their retention window. On a dry run this is what the wet run would remove.
    guest_cart_ttl_days : Optional[float]
        The same for GUEST carts — a cart with a session key and no contact behind it. Kept separate because the two are worth different amounts: a named B2B cart may be a quote somebody is still thinking about.
    items_deleted : Optional[float]
        Lines actually deleted with them. 0 on a dry run.
    markets : Optional[List[Any]]
        The market codes this pass came across. Each cart was held against ITS market&#039;s window, not the baseline&#039;s.
    would_delete_items : Optional[float]
        Lines the wet run would remove. Always present, on a wet run too, so a client never has to tell &quot;nothing to delete&quot; apart from &quot;this build did not report it&quot;.
    """
    capped: Optional[bool] = Field(default=None, alias='capped')
    cart_ids: Optional[List[Any]] = Field(default=None, alias='cart_ids')
    cart_ttl_days: Optional[float] = Field(default=None, alias='cart_ttl_days')
    cutoff: Optional[str] = Field(default=None, alias='cutoff')
    deleted: Optional[float] = Field(default=None, alias='deleted')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    found: Optional[float] = Field(default=None, alias='found')
    guest_cart_ttl_days: Optional[float] = Field(default=None, alias='guest_cart_ttl_days')
    items_deleted: Optional[float] = Field(default=None, alias='items_deleted')
    markets: Optional[List[Any]] = Field(default=None, alias='markets')
    would_delete_items: Optional[float] = Field(default=None, alias='would_delete_items')
