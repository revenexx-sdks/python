from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingTaxClassUsage(AppwriteModel):
    """
    What in this app still points at a market tax class, by code.

    Attributes
    ----------
    code : Optional[str]
        The tax-class code that was asked about, echoed back.
    fallback_setting : Optional[bool]
        True when this market&#039;s shipping_tax_class setting names the code — the class every method that names none falls back to.
    in_use : Optional[bool]
        True when at least one method or the market fallback setting names it. The single field a caller deciding whether to allow a delete needs; the rest is so it can word the refusal.
    methods : Optional[List[Any]]
        The first 20 of them, so a refusal can name names instead of a number.
    shipping_methods : Optional[float]
        How many methods name this code as their own tax_class. Capped at 500 — a tenant with more shipping methods than that has a bigger problem than an imprecise count.
    """
    code: Optional[str] = Field(default=None, alias='code')
    fallback_setting: Optional[bool] = Field(default=None, alias='fallback_setting')
    in_use: Optional[bool] = Field(default=None, alias='in_use')
    methods: Optional[List[Any]] = Field(default=None, alias='methods')
    shipping_methods: Optional[float] = Field(default=None, alias='shipping_methods')
