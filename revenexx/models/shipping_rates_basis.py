from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_free_above_basis import ShippingFreeAboveBasis
from ..enums.shipping_rates_basis_matrix_basis_default import ShippingRatesBasisMatrixBasisDefault

class ShippingRatesBasis(AppwriteModel):
    """
    How this answer was measured — the tenant settings that shaped it, echoed so the numbers can be re-derived.

    Attributes
    ----------
    evaluated_at : Optional[str]
        The instant the delivery estimates were computed from.
    free_above_compares : Optional[ShippingFreeAboveBasis]
        Whether free-above thresholds were compared against the net or the gross order value.
    matrix_basis_default : Optional[ShippingRatesBasisMatrixBasisDefault]
        The measure a matrix method without its own basis priced over.
    request_weight_unit : Optional[str]
        The unit the request expressed its weight in; converted to weight_unit before any tier was matched.
    request_weight_unit_factor : Optional[float]
        Kilograms per unit of `request_weight_unit`, as applied.
    weight_unit : Optional[str]
        The unit the rate tiers are keyed in — this market&#039;s `weight_unit` setting, else the unit the tenant flagged as default.
    weight_unit_factor : Optional[float]
        Kilograms per unit of `weight_unit`, as applied. Echoed because a unit is a code PLUS a number and the number is what priced the parcel — a quote has to be re-derivable from its own payload, not from a table the merchant may since have edited.
    """
    evaluated_at: Optional[str] = Field(default=None, alias='evaluated_at')
    free_above_compares: Optional[ShippingFreeAboveBasis] = Field(default=None, alias='free_above_compares')
    matrix_basis_default: Optional[ShippingRatesBasisMatrixBasisDefault] = Field(default=None, alias='matrix_basis_default')
    request_weight_unit: Optional[str] = Field(default=None, alias='request_weight_unit')
    request_weight_unit_factor: Optional[float] = Field(default=None, alias='request_weight_unit_factor')
    weight_unit: Optional[str] = Field(default=None, alias='weight_unit')
    weight_unit_factor: Optional[float] = Field(default=None, alias='weight_unit_factor')
