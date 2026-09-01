from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamiliesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The family&#039;s stable identifier — which set of attributes a product of this family HAS. Unique per tenant, and the value `GET /products/attribute-schema?family_code=` resolves.
    image_attribute : Optional[str]
        Which attribute code carries the product&#039;s main image — the one a grid thumbnail and a picker read.
    label_attribute : Optional[str]
        Which attribute CODE carries the display name of a product in this family. A product&#039;s name is an attribute, not a column, and which attribute it is, is per family. Null falls back to the `default_label_attribute` setting and then to the conventional `name`.
    labels : Optional[Dict[str, Any]]
        What the family is called, per language tag — the name an operator picks from, while the code is what everything else joins on.
    """
    code: str = Field(..., alias='code')
    image_attribute: Optional[str] = Field(default=None, alias='image_attribute')
    label_attribute: Optional[str] = Field(default=None, alias='label_attribute')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
