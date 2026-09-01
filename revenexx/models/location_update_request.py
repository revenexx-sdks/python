from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.location_type import LocationType

class LocationUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    address : Optional[Dict[str, Any]]
        Where the location physically is. Free-form, and one key is READ: `country`, an ISO country code, which POST /inventories/reserve compares (case-insensitively) against `ship_to.country` when `allocation_strategy` is &#039;nearest&#039; — that is what stops a German order pulling from the US warehouse because it happens to sort first. The keys the cockpit form writes are `street`, `postal_code`, `city`, `country`; anything else a tenant stores is kept and ignored.
    code : Optional[str]
        The location&#039;s stable identifier, and the name every stock call uses instead of an id: `location_code` on receive / adjust / restock / reserve, and the `default_location_code` setting. Unique per tenant, at least one character (CHECK `length(code) &gt; 0`). Every tenant starts with `main` — POST /inventories/locations/defaults seeds it and the app.installed event runs the same seed — so `main` is the one code that resolves everywhere.
    enabled : Optional[bool]
        Whether this location takes part in stock at all. POST /inventories/availability and POST /inventories/reserve look at enabled locations and nothing else, so switching this off hides a location&#039;s stock from the storefront without deleting a row or losing a single ledger booking; its stock stays readable through GET /inventories/stock. Defaults to true.
    labels : Optional[Dict[str, Any]]
        The location name per language tag, for a UI that has to render it in the reader&#039;s language. Falls back to `name` when a tag is missing. Keys are language tags, values plain strings.
    metadata : Optional[Dict[str, Any]]
        Free-form data the tenant keeps on the location — an ERP site number, a contact, a cut-off time. No route in this app reads it; it is stored and handed back unchanged.
    name : Optional[str]
        What the place is called for an operator, in the tenant&#039;s working language. At least one character (CHECK `length(name) &gt; 0`). It is a label only: nothing addresses a location by name.
    priority : Optional[float]
        Sourcing order for POST /inventories/reserve while `allocation_strategy` is &#039;priority&#039;: the enabled locations are walked ASCENDING and the first that can cover the item wins, so a LOWER number is preferred. Locations that tie keep the order the database returns them in — give every location a distinct priority if the order matters. Defaults to 0.
    type : Optional[LocationType]
        What kind of place holds the stock. &#039;warehouse&#039; — own stock, the default. &#039;store&#039; — a retail floor, the stock a click-and-collect order draws on. &#039;dropship&#039; — a supplier ships it and this row tracks what they say they hold. &#039;virtual&#039; — a bucket that is not a building (pre-orders, consignment, a quarantine shelf). Descriptive only: sourcing order comes from `priority`, and no route in this app treats one type differently from another. Defaults to &#039;warehouse&#039;.
    """
    address: Optional[Dict[str, Any]] = Field(default=None, alias='address')
    code: Optional[str] = Field(default=None, alias='code')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    priority: Optional[float] = Field(default=None, alias='priority')
    type: Optional[LocationType] = Field(default=None, alias='type')
