from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingTrackingRequest(AppwriteModel):
    """
    One parcel, resolved into a tracking link by the carrier that owns the URL format.

    Attributes
    ----------
    carrier : str
        Carrier code (what an order shipment already stores) or the carrier row id — a value matching the uuid form is read as the id, anything else as a code, case-insensitively. Must name a carrier THIS tenant keeps; one that does not is a 404.
    country : Optional[str]
        Destination ISO 3166-1 alpha-2 code — only needed by a template that names {country}. Upper-cased before substitution.
    postal_code : Optional[str]
        Destination postcode — only needed by a template that names {postal_code}.
    tracking_code : Optional[str]
        The carrier&#039;s tracking number. Required by every template that names {tracking_code}, which is all of them in the shipped catalog. URL-encoded before substitution, so a code with a space or a slash cannot reshape the link.
    """
    carrier: str = Field(..., alias='carrier')
    country: Optional[str] = Field(default=None, alias='country')
    postal_code: Optional[str] = Field(default=None, alias='postal_code')
    tracking_code: Optional[str] = Field(default=None, alias='tracking_code')
