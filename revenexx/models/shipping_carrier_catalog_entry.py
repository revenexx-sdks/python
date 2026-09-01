from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingCarrierCatalogEntry(AppwriteModel):
    """
    One carrier this app knows the facts for, exactly as it would be created.

    Attributes
    ----------
    code : Optional[str]
        The code the seeded row would carry, and the code a method&#039;s `carrier` text has to match to resolve to it.
    countries : Optional[List[Any]]
        The countries this carrier serves. ISO 3166-1 alpha-2 codes; null or an empty array means no restriction. Compared upper-cased, so a lower-case entry still matches. Declared as an array rather than the bare object a jsonb column derives to — this one is always a list.
    cutoff_time : Optional[str]
        This carrier&#039;s own daily pickup cut-off, HH:MM in 24-hour form, UTC. Overrides the tenant&#039;s cutoff_time for methods on this carrier — one shop-wide time cannot be both DHL&#039;s 16:00 and a forwarder&#039;s 12:00. Null or the empty string means this carrier declares none; any other shape is a 400, because a cut-off the estimator cannot read is a delivery promise silently computed without one.
    eta_days_max : Optional[float]
        Transit time upper bound, in calendar days from the ship date.
    eta_days_min : Optional[float]
        Transit time lower bound, in calendar days from the ship date — inherited by any method on this carrier that states no ETA of its own.
    handling_days : Optional[float]
        Days needed to make a consignment ready for THIS carrier, added to the ship date before the transit days. Overrides the tenant&#039;s handling_days.
    labels : Optional[Dict[str, Any]]
        Localized display names the seed would carry. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    name : Optional[str]
        The display name the seeded row would carry. An existing row keeps the merchant&#039;s own name — the seed never writes over one.
    seeded : Optional[bool]
        Whether a fresh install starts with this carrier. False means this app knows how to describe it but only creates it when asked.
    service_level : Optional[str]
        Service-level code the seeded row carries — one of the tenant&#039;s own values.
    tracking_url_template : Optional[str]
        Tracking page URL with {tracking_code} where the number goes; {postal_code} and {country} are also substituted, URL-encoded. Null for a carrier with no public tracking page.
    """
    code: Optional[str] = Field(default=None, alias='code')
    countries: Optional[List[Any]] = Field(default=None, alias='countries')
    cutoff_time: Optional[str] = Field(default=None, alias='cutoff_time')
    eta_days_max: Optional[float] = Field(default=None, alias='eta_days_max')
    eta_days_min: Optional[float] = Field(default=None, alias='eta_days_min')
    handling_days: Optional[float] = Field(default=None, alias='handling_days')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    seeded: Optional[bool] = Field(default=None, alias='seeded')
    service_level: Optional[str] = Field(default=None, alias='service_level')
    tracking_url_template: Optional[str] = Field(default=None, alias='tracking_url_template')
