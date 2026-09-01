from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.assets_source import AssetsSource

class AssetsCreateRequest(AppwriteModel):
    """
    An asset is bound to its bytes on creation: source &#039;storage&#039; needs `storage_asset_id`, source &#039;external&#039; needs `external_url` AND an explicit `source` — the column defaults to &#039;storage&#039;, so an `external_url` on its own is refused by the database with a bare &quot;a value is not allowed here&quot;.

    Attributes
    ----------
    asset_family_id : str
        The asset family this asset belongs to — which attributes it carries and how its file is named. A create falls back to the `default_asset_family` tenant setting when the body names none.
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
        
        Which attributes an asset of this family has comes from `attributes` rows with `entity_type: &quot;asset&quot;` and `entity_ref` equal to the family&#039;s code — alt text, copyright, an expiry date.
    code : str
        The asset&#039;s stable identifier within its family — the value a product&#039;s media attribute stores. Unique per family.
    delivery_path : Optional[str]
        The path the CDN serves this asset under — the convenient value for rendering. It changes when the file is moved, so never join on it.
    external_url : Optional[str]
        Absolute URL of an externally hosted file. Required when `source` is `external`, and accepted only when the tenant has `allow_external_media` on and the host is on its `external_media_allowed_hosts` list — `POST /products/assets` is the only place an external URL can enter the catalog, so it is the only place those are enforced.
    source : Optional[AssetsSource]
        Where the bytes live: &#039;storage&#039; is this platform&#039;s object store and needs `storage_asset_id`, &#039;external&#039; is somebody else&#039;s host and needs `external_url`. The database enforces the pair, so neither half can be stored on its own.
    storage_asset_id : Optional[str]
        The stable `ast_…` id of the storage object. It survives a rename or a folder move, which is exactly why it and not the delivery path is the identifier. Required when `source` is `storage`.
    """
    asset_family_id: str = Field(..., alias='asset_family_id')
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    code: str = Field(..., alias='code')
    delivery_path: Optional[str] = Field(default=None, alias='delivery_path')
    external_url: Optional[str] = Field(default=None, alias='external_url')
    source: Optional[AssetsSource] = Field(default=None, alias='source')
    storage_asset_id: Optional[str] = Field(default=None, alias='storage_asset_id')
