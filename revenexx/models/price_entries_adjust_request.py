from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_ending_rule import PriceEndingRule

class PriceEntriesAdjustRequest(AppwriteModel):
    """
    Change every priced entry of a list at once. Send &#039;percent&#039; OR &#039;amount&#039;, never both. On-request entries are never touched — a percentage of &quot;ask us&quot; is not a number.

    Attributes
    ----------
    amount : Optional[float]
        Absolute change added to every unit price, in the list&#039;s currency.
    dry_run : Optional[bool]
        true writes nothing and answers the same preview — what the Cockpit dialog shows before it commits.
    percent : Optional[float]
        Relative change in percent: 5 raises by 5 %, -10 cuts by 10 %.
    rounding : Optional[PriceEndingRule]
        Ending the computed prices snap to (nearest match). Omit to use the tenant&#039;s bulk_adjust_rounding setting.
    sku_prefix : Optional[str]
        Restrict the change to entries whose SKU starts with this (a prefix, case-sensitive, no wildcards). Entries identified only by product_id never match a prefix. Omit to change the whole list.
    """
    amount: Optional[float] = Field(default=None, alias='amount')
    dry_run: Optional[bool] = Field(default=None, alias='dry_run')
    percent: Optional[float] = Field(default=None, alias='percent')
    rounding: Optional[PriceEndingRule] = Field(default=None, alias='rounding')
    sku_prefix: Optional[str] = Field(default=None, alias='sku_prefix')
