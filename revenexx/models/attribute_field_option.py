from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeFieldOption(AppwriteModel):
    """
    

    Attributes
    ----------
    label : Optional[str]
        What to show in the picker, already resolved for the requested locale.
    swatch : Optional[Dict[str, Any]]
        Colour/texture chip, when the option carries one — `{&quot;hex&quot;: &quot;#c0c0c0&quot;}`.
    value : Optional[str]
        The stored value — an `attribute_options.code`, or a `reference_entity_records.code` when the options ARE a reference entity. This, never the label, is what goes into `attribute_values`.
    """
    label: Optional[str] = Field(default=None, alias='label')
    swatch: Optional[Dict[str, Any]] = Field(default=None, alias='swatch')
    value: Optional[str] = Field(default=None, alias='value')
