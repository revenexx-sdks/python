from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_term_tone import PaymentTermTone

class PaymentTerm(AppwriteModel):
    """
    One value of the payment terms set. When a company has to pay. A wholesaler who agrees net 45 with one customer used to need a release of this app to say so.

    Attributes
    ----------
    code : Optional[str]
        What `organizations.payment_terms` stores, and the only part of this row other data depends on. Immutable once created: renaming it would orphan every record carrying it.
    created_at : Optional[str]
        When the value was added to this set.
    description : Optional[str]
        One line of help for an operator choosing this value. Null when there is nothing to add. A row seeded before 0.22.0 may hold a serialized locale map here instead (PE-443).
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions, keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Null when nobody translated this value — a client then falls back to `description`.
    id : Optional[str]
        Primary key of this value. What the update and delete routes address it by — the CODE is what records store.
    is_default : Optional[bool]
        The value a create falls back to when the caller names none. Exactly one row of the set carries it; promoting another one demotes this.
    is_system : Optional[bool]
        True for a value this app seeded on install. Still renameable and still removable — it only records where the value came from.
    labels : Optional[Dict[str, Any]]
        Localized titles, keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Null when nobody translated this value — a client then falls back to `title`.
    position : Optional[float]
        Where this value sits in the set, ascending. It is the order a select should offer.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    title : Optional[str]
        The fallback name — what a client shows when no locale in `labels` matches. A row seeded before 0.22.0 may hold a serialized locale map here instead (PE-443) — those rows were seeded with no `labels` at all.
    tone : Optional[PaymentTermTone]
        Semantic badge colour. The palette stays fixed — it is a render concern, not a merchant decision.
    updated_at : Optional[str]
        When it was last edited.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    is_system: Optional[bool] = Field(default=None, alias='is_system')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[PaymentTermTone] = Field(default=None, alias='tone')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
