from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        The attribute&#039;s stable identifier — the KEY its value is stored under inside `attribute_values`, and the name a category rule addresses as `attribute:&lt;code&gt;`. Unique per (`entity_type`, `entity_ref`) in this tenant.
    config : Optional[Dict[str, Any]]
        Type-specific settings; which keys apply depends on `type`. The ones this app reads: `units` (the unit list a measure attribute offers) and `reference_entity` (which entity a reference attribute draws its options from). The ones the cockpit edits alongside them: `unit`, `metric_family`, `decimals_allowed`, `asset_family`, `max_file_size`, `allowed_extensions`.
    entity_ref : Optional[str]
        Narrows `entity_type` to ONE reference entity or asset family, by its code — the attributes of `brand` rather than of every reference entity. Null for a plain product attribute.
    entity_type : Optional[str]
        Which kind of record carries this attribute: &#039;product&#039; for the catalog itself, &#039;reference_entity&#039;, &#039;asset&#039; or &#039;category&#039; for the other things in this app that have attributes. Deliberately carries no CHECK — a tenant that models a fifth kind is served on it too.
    group_id : Optional[str]
        The `attribute_groups` row this attribute is filed under — the form section it appears in. Null is ungrouped, and an ungrouped field is rendered after every section that has a name.
    is_filterable : Optional[bool]
        Offer this attribute as a filter in a product list. `GET /products/grid` reports exactly these attributes in its `filters` array, and nothing else reads the flag.
    is_unique : Optional[bool]
        Declares that the value identifies the product — an EAN, a manufacturer part number. It is metadata a form and an importer read: no database index enforces it, because the value lives inside jsonb rather than in a column.
    labels : Optional[Dict[str, Any]]
        The field label a person sees, keyed by language tag. Resolution falls back to English and then to the code, so an untranslated attribute is still renderable.
    localizable : Optional[bool]
        True → the record holds ONE VALUE PER LOCALE, under `attribute_values.locale_specific.&lt;locale&gt;.&lt;code&gt;`. False → one value, under `attribute_values.common.&lt;code&gt;`. This flag is what decides where a write goes.
    position : Optional[float]
        Where the field sits inside its group. A family may override it for its own form through `family_attributes.position`; this is the attribute&#039;s default.
    scopable : Optional[bool]
        True → one value PER CHANNEL, under `attribute_values.channel_specific.&lt;channel&gt;.&lt;code&gt;`. Set together with `localizable` it means one value per channel AND locale, in `channel_locale_specific`.
    type : Optional[str]
        Which editor the value asks for — &#039;text&#039;, &#039;select&#039;, &#039;metric&#039;, &#039;price&#039;, &#039;asset_collection&#039;, &#039;reference_entity&#039;. Carries no CHECK on purpose: an integrator adds a type, and `GET /products/attribute-schema` maps an unknown one onto a text field rather than refusing to answer.
    usable_in_grid : Optional[bool]
        Show this attribute as a COLUMN in the product grid. `GET /products/grid` returns a column definition and a per-row value for exactly these.
    validation : Optional[Dict[str, Any]]
        Limits a value has to satisfy, as a flat object. The seven keys a client can act on are `min`, `max`, `min_length`, `max_length`, `pattern`, `min_items`, `max_items` — `GET /products/attribute-schema` republishes those and leaves anything else the tenant stored untouched.
    """
    code: Optional[str] = Field(default=None, alias='code')
    config: Optional[Dict[str, Any]] = Field(default=None, alias='config')
    entity_ref: Optional[str] = Field(default=None, alias='entity_ref')
    entity_type: Optional[str] = Field(default=None, alias='entity_type')
    group_id: Optional[str] = Field(default=None, alias='group_id')
    is_filterable: Optional[bool] = Field(default=None, alias='is_filterable')
    is_unique: Optional[bool] = Field(default=None, alias='is_unique')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    localizable: Optional[bool] = Field(default=None, alias='localizable')
    position: Optional[float] = Field(default=None, alias='position')
    scopable: Optional[bool] = Field(default=None, alias='scopable')
    type: Optional[str] = Field(default=None, alias='type')
    usable_in_grid: Optional[bool] = Field(default=None, alias='usable_in_grid')
    validation: Optional[Dict[str, Any]] = Field(default=None, alias='validation')
