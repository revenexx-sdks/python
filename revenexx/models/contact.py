from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_registration_status import ContactRegistrationStatus
from ..enums.contact_status import ContactStatus

class Contact(AppwriteModel):
    """
    A PERSON, and the unit that logs in: one platform user, one email, one role inside its organization. A contact without an organization is a standalone buyer, not an error.

    Attributes
    ----------
    created_at : Optional[str]
        When this person record was created in this app.
    email : Optional[str]
        Login identity and the unique key of a person within the tenant. Changing it changes the platform login with it. Two people at the same company therefore need two addresses — a shared purchasing mailbox is one contact, not several.
    external_user_id : Optional[str]
        Id of the platform USER this contact is mirrored as — the account that actually holds the password and the sessions. Written by the mirror and ignored on every write a caller sends.
    first_name : Optional[str]
        Given name. Optional: an ERP import often has only a mailbox.
    id : Optional[str]
        Primary key of the person record. What the timeline, the permission routes and the principal resolution all name.
    is_primary : Optional[bool]
        The main contact of its organization — who a merchant calls first. At most one per company is the intent; the tenant&#039;s `primary_contact_required` setting decides whether the last one may be demoted or deleted.
    job_title : Optional[str]
        What this person does at the company — free text on purpose, because it is a title and not a grant. The permission ladder is `role`; overloading a job title with authority silently un-grants everyone the day the ledger is enforced.
    last_name : Optional[str]
        Family name. Optional for the same reason.
    locale : Optional[str]
        The language this person is written to in — BCP 47, and one of the store&#039;s configured locales. Null falls back to the store default.
    order_approval_limit : Optional[float]
        Amount ceiling for this person, in the market&#039;s currency: with the `orders.approve` permission it is the most they may sign off. Null means no ceiling. An amount, never a grant — the grant comes from the role.
    organization_id : Optional[str]
        The company this person belongs to. NULL is a legitimate state, not a defect: a standalone buyer with no company behind them. Deleting the organization sets this null and keeps the person.
    phone : Optional[str]
        Direct number of this person, as somebody typed it — free text, no format is enforced or normalized. E.164 is what an integration should send.
    registration_decided_at : Optional[str]
        When a merchant approved or rejected the application. Null while nobody has decided.
    registration_decided_by : Optional[str]
        Who decided — free text as the deciding client supplied it (an operator id or an email address), not a resolvable user reference.
    registration_reason : Optional[str]
        Why the application was declined. Always recorded here; whether the APPLICANT is ever told it is the tenant&#039;s `registration_reason_disclosed` setting, because that is a legal decision and not a template one.
    registration_status : Optional[ContactRegistrationStatus]
        Where this person&#039;s own application stands: &#039;approved&#039; (the default, and what an open store creates), &#039;pending&#039; while a merchant has yet to decide, &#039;rejected&#039; once they declined. Only the approve/reject routes move it; it is ignored on an ordinary update.
    role : Optional[str]
        The person&#039;s role INSIDE its organization, and the only thing permissions are derived from. One of the tenant&#039;s own roles (GET /customers/roles); a tenant that never edited the ledger has viewer, requester, buyer, approver, admin. Also the team role on the platform mirror. There is no global role — the same person in two companies is two contacts.
    status : Optional[ContactStatus]
        Whether this person may act: &#039;invited&#039; has been created but has not accepted, &#039;active&#039; works, &#039;blocked&#039; cannot log in. A create through the API defaults to &#039;invited&#039;; a self-registration in an open store lands &#039;active&#039;.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    updated_at : Optional[str]
        When any column of this row last changed.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    email: Optional[str] = Field(default=None, alias='email')
    external_user_id: Optional[str] = Field(default=None, alias='external_user_id')
    first_name: Optional[str] = Field(default=None, alias='first_name')
    id: Optional[str] = Field(default=None, alias='id')
    is_primary: Optional[bool] = Field(default=None, alias='is_primary')
    job_title: Optional[str] = Field(default=None, alias='job_title')
    last_name: Optional[str] = Field(default=None, alias='last_name')
    locale: Optional[str] = Field(default=None, alias='locale')
    order_approval_limit: Optional[float] = Field(default=None, alias='order_approval_limit')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    phone: Optional[str] = Field(default=None, alias='phone')
    registration_decided_at: Optional[str] = Field(default=None, alias='registration_decided_at')
    registration_decided_by: Optional[str] = Field(default=None, alias='registration_decided_by')
    registration_reason: Optional[str] = Field(default=None, alias='registration_reason')
    registration_status: Optional[ContactRegistrationStatus] = Field(default=None, alias='registration_status')
    role: Optional[str] = Field(default=None, alias='role')
    status: Optional[ContactStatus] = Field(default=None, alias='status')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
