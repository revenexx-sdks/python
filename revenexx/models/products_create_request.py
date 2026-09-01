from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.products_kind import ProductsKind

class ProductsCreateRequest(AppwriteModel):
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
    completeness : Optional[Dict[str, Any]]
        How much of what this product&#039;s family REQUIRES it actually carries — the number a merchandiser works down. `required` counts the attributes the family marks `is_required`, `filled` how many of those carry a value in ANY bucket, `ratio` is filled/required between 0 and 1 (a family that requires nothing is 1, not undefined), `missing` lists the codes with no value anywhere, sorted, and `computed_at` is when it was measured.
        
        Written only by `POST /products/{id}/completeness` and by `POST /products/{id}/family`; a plain create or update never touches it, so it is null until one of the two has run. It also stays null for a product with no family — there is nothing to measure it against, and 0 % would be a lie.
    deleted_at : Optional[str]
        When the product was soft-deleted. `GET /products/grid` and every category-rule evaluation exclude a row that carries one; `GET /products` does NOT — filter on it to read the live catalog.
    enabled : Optional[bool]
        Whether the product is offered. A create defaults it from the `new_products_enabled_by_default` tenant setting rather than blindly to true, so an import does not publish twenty thousand unfinished products the moment it lands. An explicit value in the body always wins.
    family_id : Optional[str]
        The family that decides which attributes this product HAS. Without one nothing is required, completeness cannot be computed and the display name never resolves — `POST /products/{id}/family` is the call that sets it and computes completeness in the same step.
    family_variant_id : Optional[str]
        Which variant structure of the family this product follows — the axes it splits on. Null on a simple product.
    kind : Optional[ProductsKind]
        Where the product sits in the variant hierarchy. &#039;simple&#039; stands on its own. &#039;model&#039; carries the values its variants share and is never sold itself. &#039;variant&#039; carries the axis values and points at its model through `parent_id`.
    parent_id : Optional[str]
        The product MODEL this variant belongs to. Only a `variant` carries one. Deleting the model leaves its variants behind with a null parent rather than deleting them.
    quantified_associations : Optional[Dict[str, Any]]
        The import-side mirror of associations that carry a quantity — a bundle, a bill of materials, a spare-parts set. NOTHING IN THIS APP READS OR WRITES IT: no route produces it, no route consumes it, and it is null on every product this app has created. The surface that IS served is relational — `product_associations`, whose `quantity` column holds the number, guarded by `association_types.is_quantified`.
        
        It exists because a PIM import (Akeneo, BMEcat) carries these in one blob keyed by association type code, and the column lets that document round-trip instead of being dropped. The database enforces no shape on it, so what a reader finds is whatever the importer wrote; the example is the conventional form.
    sku : str
        The merchant&#039;s own article number — unique per tenant, and the value every integration (ERP, shop, feed, price list) joins on. The one identifier a person types, and the fallback this app shows when the catalog holds no name.
    tax_class : Optional[str]
        The tax class key the prices app resolves a VAT rate from. Free text here — the vocabulary belongs to the app that prices, and `POST /products/batch` exists to hand exactly this column to it in bulk.
    """
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    completeness: Optional[Dict[str, Any]] = Field(default=None, alias='completeness')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    family_variant_id: Optional[str] = Field(default=None, alias='family_variant_id')
    kind: Optional[ProductsKind] = Field(default=None, alias='kind')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    quantified_associations: Optional[Dict[str, Any]] = Field(default=None, alias='quantified_associations')
    sku: str = Field(..., alias='sku')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
