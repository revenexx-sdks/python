from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_tracking_carrier_status import ShippingTrackingCarrierStatus

class ShippingTrackingCarrier(AppwriteModel):
    """
    The carrier row that owns the URL format, identified so the caller can show who is carrying the parcel without a second read. Resolved whatever its status — a retired carrier still answers here.

    Attributes
    ----------
    code : Optional[str]
        Stable carrier code, unique per tenant (e.g. dhl, dpd, gls). A method whose `carrier` text equals this code resolves to this carrier — that is the migration path off the free-text field. Deliberately no slug pattern: the column asks only for a non-empty string, and a contract stricter than the implementation would refuse codes merchants already keep.
    id : Optional[str]
        Row id, assigned by the database on insert.
    name : Optional[str]
        Display name, for the line that reads &quot;shipped with …&quot;.
    service_level : Optional[str]
        The class of service this row represents (default &#039;standard&#039;), as a CODE into the tenant&#039;s own service levels (GET /shipping/service-levels). One row is one class: a carrier selling both a parcel and an express product is two rows. Deliberately not an enum here — the set is the merchant&#039;s, so a fixed list in this contract would make the gateway reject a level they created. A code the tenant does not keep is a 400 naming the codes they do.
    status : Optional[ShippingTrackingCarrierStatus]
        Whether this carrier may be quoted (default &#039;active&#039;). Anything else excludes every method that ships with it from POST /shipping/rates, with a reason. Tracking links are NOT gated on it — a retired carrier&#039;s old shipments stay resolvable. Reported here so a UI can mark a link as belonging to a carrier nobody quotes any more.
    """
    code: Optional[str] = Field(default=None, alias='code')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    service_level: Optional[str] = Field(default=None, alias='service_level')
    status: Optional[ShippingTrackingCarrierStatus] = Field(default=None, alias='status')
