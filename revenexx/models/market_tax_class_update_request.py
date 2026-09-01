from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketTaxClassUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Tax class code, unique per market — the rate bucket a product or a shipping method is assigned to (&#039;standard&#039;, &#039;reduced&#039;, &#039;zero&#039;). Other apps name a class by THIS and by nothing else: there is no foreign key behind it and there cannot be (ADR-0055), which is why the delete route asks the shipping app what still points at the code before removing it.
    is_default : Optional[bool]
        The class applied to a line that names none. At most one per market. A market that stores GROSS prices and marks no default cannot break those prices back down into net, which is why readiness turns that combination from a warning into a blocking failure.
    labels : Optional[Dict[str, Any]]
        Localized display names for storefronts and invoices, keyed by locale: a flat {locale: label} map, one level deep, string values. The key to write is the `locale_policy.write` from GET /markets/{id}/context, exactly as for a market&#039;s labels. Null means nothing is translated and `name` is all there is.
    name : Optional[str]
        Display name of the rate bucket, in the operator&#039;s own language.
    position : Optional[float]
        Sort position among this market&#039;s tax classes, ascending, default 0 — and the tie-break that picks a class when none is flagged default.
    rate : Optional[float]
        Tax rate in PERCENT, 0–100 (default 0) — 20 means 20 %, not 0.2. Whether a stored price already contains it is a separate question, answered per market by `pricing.tax_basis` on the context.
    """
    code: Optional[str] = Field(default=None, alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    rate: Optional[float] = Field(default=None, alias='rate')
