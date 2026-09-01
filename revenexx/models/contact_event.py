from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ContactEvent(AppwriteModel):
    """
    One entry on a customer&#039;s timeline: an activity somebody logged (call, visit, note) or a registration decision this app recorded. Append-only — nothing here is ever edited.

    Attributes
    ----------
    actor : Optional[str]
        Who logged the entry — free text as the client supplied it (operator id or email). Null for a row the app wrote itself.
    contact_id : Optional[str]
        The person this entry is about. Always set: even a company-level activity is filed against somebody, so a timeline never has anonymous rows.
    created_at : Optional[str]
        When the row was written. Together with `occurred_at` this is what tells a late entry from a live one.
    id : Optional[str]
        Primary key of the timeline entry.
    kind : Optional[str]
        What kind of entry this is — one of the tenant&#039;s own activity types (GET /customers/contact-event-kinds), seeded with note, call, email, meeting, visit, task. &#039;system&#039; is reserved: those rows are this app&#039;s own registration decision trail and no caller may file one.
    name : Optional[str]
        The event name, and the one vocabulary here that is THIS APP&#039;s rather than the tenant&#039;s: `registration.submitted` | `registration.approved` | `registration.rejected` for decisions, `activity.&lt;kind&gt;` for everything somebody logged. It is also what travels on the bus as `contact_event.created`.
    occurred_at : Optional[str]
        When the thing actually HAPPENED, which is not when it was written down: a call logged on Monday about Friday says Friday. Defaults to now.
    organization_id : Optional[str]
        The company this entry belongs to, DERIVED from the contact and never taken from a request body — which is what stops a call with one company being filed under someone else&#039;s person. Null when the contact has no organization.
    payload : Optional[Dict[str, Any]]
        The machine-readable body, and its shape follows `name`. `activity.&lt;kind&gt;` carries `{ note }` — the long form of `subject`. `registration.submitted` carries the application itself: email, organization_id, organization_name, role, locale, vat_id, and `notify`, the recipients the approval mail goes to. `registration.approved` carries `{ decided_by }`; `registration.rejected` adds `reason`. Nothing validates it beyond that — a client writing its own entries decides what belongs in here.
    subject : Optional[str]
        One line a person can scan in a timeline. Required for an activity; a decision row carries the app&#039;s own wording.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    """
    actor: Optional[str] = Field(default=None, alias='actor')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    kind: Optional[str] = Field(default=None, alias='kind')
    name: Optional[str] = Field(default=None, alias='name')
    occurred_at: Optional[str] = Field(default=None, alias='occurred_at')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
    subject: Optional[str] = Field(default=None, alias='subject')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
