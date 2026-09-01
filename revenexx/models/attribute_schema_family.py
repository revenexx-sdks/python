from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeSchemaFamily(AppwriteModel):
    """
    The family the fields belong to, or null when none was named — then the answer is every attribute of the `entity_type`, which is what a reference entity or an asset family has instead of a family.

    Attributes
    ----------
    code : Optional[str]
        The family&#039;s code — the value `?family_code=` takes.
    id : Optional[str]
        The family&#039;s id.
    label : Optional[str]
        The family name, resolved for the requested locale.
    label_attribute : Optional[str]
        Which of these fields is the product&#039;s display name.
    """
    code: Optional[str] = Field(default=None, alias='code')
    id: Optional[str] = Field(default=None, alias='id')
    label: Optional[str] = Field(default=None, alias='label')
    label_attribute: Optional[str] = Field(default=None, alias='label_attribute')
