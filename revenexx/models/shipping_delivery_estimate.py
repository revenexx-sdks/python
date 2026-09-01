from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingDeliveryEstimate(AppwriteModel):
    """
    The delivery window a checkout can print. Calendar days, cut-off evaluated in UTC (send `at` to control the instant).

    Attributes
    ----------
    cutoff_passed : Optional[bool]
        Whether the cut-off had passed at evaluation time, costing a day.
    cutoff_time : Optional[str]
        The cut-off applied (HH:MM, UTC), or null when none is configured — the carrier&#039;s own when it declares one, else the market&#039;s `cutoff_time` setting.
    earliest : Optional[str]
        ship_date + eta_days_min.
    handling_days : Optional[float]
        The tenant&#039;s handling_days setting, as applied.
    latest : Optional[str]
        ship_date + eta_days_max.
    ship_date : Optional[str]
        The day the parcel leaves — today plus handling days, plus one when the cut-off has passed.
    """
    cutoff_passed: Optional[bool] = Field(default=None, alias='cutoff_passed')
    cutoff_time: Optional[str] = Field(default=None, alias='cutoff_time')
    earliest: Optional[str] = Field(default=None, alias='earliest')
    handling_days: Optional[float] = Field(default=None, alias='handling_days')
    latest: Optional[str] = Field(default=None, alias='latest')
    ship_date: Optional[str] = Field(default=None, alias='ship_date')
