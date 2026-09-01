from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_update_request_registration_status import ContactUpdateRequestRegistrationStatus
from ..enums.contact_status import ContactStatus

class ContactUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value. external_user_id is mirror-managed and ignored, and so are the registration_* columns: registration state is only ever changed by the approve/reject routes.

    Attributes
    ----------
    email : Optional[str]
        Login identity and the unique key of a person within the tenant. Changing it changes the platform login with it. Two people at the same company therefore need two addresses — a shared purchasing mailbox is one contact, not several.
    first_name : Optional[str]
        Given name. Optional: an ERP import often has only a mailbox.
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
        The company this person belongs to. NULL is a legitimate state, not a defect: a standalone buyer with no company behind them. Deleting the organization sets this null and keeps the person. Membership is mirrored to the platform team.
    phone : Optional[str]
        Direct number of this person, as somebody typed it — free text, no format is enforced or normalized. E.164 is what an integration should send.
    registration_status : Optional[ContactUpdateRequestRegistrationStatus]
        Where this person&#039;s own application stands: &#039;approved&#039; (the default, and what an open store creates), &#039;pending&#039; while a merchant has yet to decide, &#039;rejected&#039; once they declined. Only the approve/reject routes move it; it is ignored on an ordinary update. On CREATE only, and only to file the contact as an application: &#039;pending&#039; creates the platform user disabled and routes the contact through approve/reject. Ignored on update.
    role : Optional[str]
        The person&#039;s role INSIDE its organization, and the only thing permissions are derived from. One of the tenant&#039;s own roles (GET /customers/roles); a tenant that never edited the ledger has viewer, requester, buyer, approver, admin. Also the team role on the platform mirror. There is no global role — the same person in two companies is two contacts. A tenant that never edited the ledger has viewer, requester, buyer, approver, admin; a create without a role gets the one flagged as default, and a role the tenant does not keep is a 400.
    status : Optional[ContactStatus]
        Whether this person may act: &#039;invited&#039; has been created but has not accepted, &#039;active&#039; works, &#039;blocked&#039; cannot log in. A create through the API defaults to &#039;invited&#039;; a self-registration in an open store lands &#039;active&#039;. Default &#039;invited&#039; on create.
    """
    email: Optional[str] = Field(default=None, alias='email')
    first_name: Optional[str] = Field(default=None, alias='first_name')
    is_primary: Optional[bool] = Field(default=None, alias='is_primary')
    job_title: Optional[str] = Field(default=None, alias='job_title')
    last_name: Optional[str] = Field(default=None, alias='last_name')
    locale: Optional[str] = Field(default=None, alias='locale')
    order_approval_limit: Optional[float] = Field(default=None, alias='order_approval_limit')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    phone: Optional[str] = Field(default=None, alias='phone')
    registration_status: Optional[ContactUpdateRequestRegistrationStatus] = Field(default=None, alias='registration_status')
    role: Optional[str] = Field(default=None, alias='role')
    status: Optional[ContactStatus] = Field(default=None, alias='status')
