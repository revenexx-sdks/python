from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .attribute_field_option import AttributeFieldOption
from .attribute_field_storage import AttributeFieldStorage
from .attribute_field_validation import AttributeFieldValidation

class AttributeField(AppwriteModel):
    """
    One renderable field. A superset of the manifest&#039;s `Field`: the three additions (`localized`, `channel_scoped`, `storage`) carry what a static manifest never has to say, because a manifest&#039;s fields are columns and these are keys inside one.

    Attributes
    ----------
    channel_scoped : Optional[bool]
        One value per channel rather than one value.
    xfrom : Optional[List[Any]]
        Dotted read paths, most specific first — the documented precedence (channel+locale → locale → channel → common). `common` is always last and always present, because early imports wrote there whatever the attribute&#039;s flags say.
    group : Optional[str]
        Attribute-group code — the section this field belongs in.
    group_label : Optional[str]
        That section&#039;s heading, resolved for the requested locale — so a form can be built without reading `attribute_groups` as well.
    label : Optional[str]
        Resolved for the requested locale, falling back to English, then to the code.
    localized : Optional[bool]
        One value per locale rather than one value.
    name : Optional[str]
        The attribute code — the key the value is stored under.
    options : Optional[List[AttributeFieldOption]]
        Present on select / multi-select. Two sources, one shape: rows of `attribute_options` for an enumeration the attribute owns, or the records of a reference entity for an attribute that points at one. Empty is an answer: the list has no members yet.
    position : Optional[float]
        The family&#039;s ordering of this attribute, falling back to the attribute&#039;s own.
    readonly : Optional[bool]
        The field must not be edited in this context. Today the one cause is a variant axis on a product model; `readonly_reason` says which.
    readonly_reason : Optional[str]
        Why the field is locked — a variant axis on a product model is set on its variants.
    reference_entity : Optional[str]
        Present when the options ARE a reference entity&#039;s records: the code of that entity, so a client can offer to manage the values rather than only pick from them.
    required : Optional[bool]
        The family&#039;s `is_required`, narrowed to the requested channel when `required_channels` names any.
    storage : Optional[AttributeFieldStorage]
        Where the value lives. Absent on an app whose custom fields are plain columns — then the field name IS the column.
    type : Optional[str]
        The control to draw. Mapped from `attributes.type`, which carries no CHECK on purpose — an unknown type answers &#039;text&#039; rather than nothing.
    unique : Optional[bool]
        The attribute&#039;s `is_unique` — the value is meant to identify the product. Advisory: no index enforces it, so a client that cares has to check.
    units : Optional[List[Any]]
        Offered units of a `measure` field, from the attribute&#039;s `config.units`.
    validation : Optional[AttributeFieldValidation]
        The limits the value has to satisfy, ready to hand to a form validator. Only the seven keys below are republished; anything else the tenant stored in `attributes.validation` stays there.
    """
    channel_scoped: Optional[bool] = Field(default=None, alias='channel_scoped')
    xfrom: Optional[List[Any]] = Field(default=None, alias='from')
    group: Optional[str] = Field(default=None, alias='group')
    group_label: Optional[str] = Field(default=None, alias='group_label')
    label: Optional[str] = Field(default=None, alias='label')
    localized: Optional[bool] = Field(default=None, alias='localized')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[List[AttributeFieldOption]] = Field(default=None, alias='options')
    position: Optional[float] = Field(default=None, alias='position')
    readonly: Optional[bool] = Field(default=None, alias='readonly')
    readonly_reason: Optional[str] = Field(default=None, alias='readonly_reason')
    reference_entity: Optional[str] = Field(default=None, alias='reference_entity')
    required: Optional[bool] = Field(default=None, alias='required')
    storage: Optional[AttributeFieldStorage] = Field(default=None, alias='storage')
    type: Optional[str] = Field(default=None, alias='type')
    unique: Optional[bool] = Field(default=None, alias='unique')
    units: Optional[List[Any]] = Field(default=None, alias='units')
    validation: Optional[AttributeFieldValidation] = Field(default=None, alias='validation')
