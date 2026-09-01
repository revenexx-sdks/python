from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReferenceEntityRecordsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_values : Optional[Dict[str, Any]]
        Every attribute value the record carries, in ONE jsonb document — the core of an attribute-driven PIM. A record&#039;s properties are not columns here: they are rows in `attributes`, selected per family by `family_attributes`, and their values live under their attribute CODE inside this object.
        
        Four buckets, and an attribute&#039;s own flags decide which one it writes to:
        
          `common`                    the attribute is neither localizable nor scopable — one value, full stop.
                                      `{&quot;common&quot;: {&quot;net_weight&quot;: 2.4, &quot;colour&quot;: &quot;black&quot;}}`
          `locale_specific`           `localizable`: one value per language tag.
                                      `{&quot;locale_specific&quot;: {&quot;de_DE&quot;: {&quot;name&quot;: &quot;Akku-Bohrschrauber&quot;}}}`
          `channel_specific`          `scopable`: one value per channel.
                                      `{&quot;channel_specific&quot;: {&quot;b2b&quot;: {&quot;minimum_order_quantity&quot;: 6}}}`
          `channel_locale_specific`   both: one value per channel AND language tag.
                                      `{&quot;channel_locale_specific&quot;: {&quot;b2b&quot;: {&quot;de_DE&quot;: {&quot;description&quot;: &quot;…&quot;}}}}`
        
        A reader takes the most specific bucket that carries the code and falls back through locale, then channel, then `common`. `common` is always last and always consulted, because early imports wrote everything there whatever an attribute&#039;s flags said — a reader that skipped it reports an imported catalog as empty. `GET /products/attribute-schema` answers, per field, the exact path a value belongs at (`storage.path`) and that full fallback order (`from`), so no client has to re-derive any of this.
        
        The value itself is whatever the attribute&#039;s `type` implies: a string, a number, a boolean, an option CODE for a select (never its label), a list of codes for a multi-select, `{&quot;amount&quot;: …, &quot;unit&quot;: …}` for a measure, a list of `{&quot;amount&quot;: …, &quot;currency&quot;: …}` for a price, an asset code for media.
        
        Defaults to `{}`, and an empty object is a normal state — a record nobody has enriched yet. The declared type also admits an array only because every jsonb column of this app shares one mapping; an array is not meaningful here and every reader in this app treats a non-object as empty.
        
        Which attributes a record of this entity has comes from `attributes` rows with `entity_type: &quot;reference_entity&quot;` and `entity_ref` equal to the entity&#039;s code — `GET /products/attribute-schema?entity_type=reference_entity&amp;entity_ref=brand` answers it in one call.
    code : str
        The record&#039;s stable identifier — the value a product stores when it points at this record, the same way a select stores an option code. Unique within the entity.
    labels : Optional[Dict[str, Any]]
        What the record is called, per language tag — the text a picker shows while the code is what gets written.
    reference_entity_id : str
        Which reference entity this record belongs to.
    """
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    reference_entity_id: str = Field(..., alias='reference_entity_id')
