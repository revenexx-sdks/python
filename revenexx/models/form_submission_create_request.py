from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.form_submission_status import FormSubmissionStatus

class FormSubmissionCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    data : Dict[str, Any]
        What the visitor typed — the substance of the submission, and the reason this row is the payload of `form.submitted`.
        
        It is an object keyed by the `name` of the definition node that collected each value, so the keys of a submission are the named nodes of its form&#039;s `definition` and nothing else. There is no fixed set of keys across forms: a contact form yields `{name, email, message}`, a price request whatever its operator built.
        
        The VALUE type follows the input type, which is why this object is not typed further: a `text`, `email` or `textarea` yields a string, a `number` a number, a single `checkbox` a boolean, a `select`/`radio` the chosen option value, a multi-select or a checkbox set an array of them, and a `group` or `list` input nests an object or an array under its own name. Nothing coerces them — a value arrives as the storefront sent it and is stored as jsonb.
        
        Two values are NOT here: the honeypot field, if the tenant configured one, is stripped before the row is written (it is a trap, not an answer the visitor gave), and the resolved notification recipient lives in `metadata`, not in what somebody typed.
    form_id : str
        The form this submission was made against. It is resolved at insert, so an id no form in this tenant holds is a 404 and nothing is stored — a submission with no form is a lead nobody can read. Required on a create: it is the only thing that says which form was filled in.
    form_slug : Optional[str]
        The form&#039;s slug as it stood when this submission arrived, copied onto the row: the inbox filters by form without a join, and a submission still says which form collected it after that form has been renamed. It does not outlive a DELETED form — the foreign key cascades and takes the submission with it. On a write the body&#039;s value WINS; omit it and the form&#039;s own slug is copied in. So: OPTIONAL — send it and it is stored as sent, even if it disagrees with the form; omit it and the form&#039;s own slug is filled in from `form_id`.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata, yours to key as an integration needs. The resolved notification recipient is merged OVER it at insert, so `notify_email` and `notify_source` sent here are overwritten — see the `FormSubmissionMetadata` schema.
    source : Optional[str]
        Where the submission came from. The storefront sends the `window.location.pathname` of the page that carried the form, so this is normally a path rather than an absolute URL; any other surface (an app, an import) puts its own name here. Null when the caller sent none.
    status : Optional[FormSubmissionStatus]
        Inbox triage. `new` until somebody opens it, then `read`, and `archived` once it is dealt with. `spam` is set by code in exactly one place — the honeypot, and only while the tenant&#039;s spam_handling is &#039;flag&#039;; under &#039;reject&#039; the submission is never stored at all. Default &#039;new&#039;. A create may set it — an inbox importer records a submission that is already read — but nothing needs to: omit it and the row is &#039;new&#039;.
    """
    data: Dict[str, Any] = Field(..., alias='data')
    form_id: str = Field(..., alias='form_id')
    form_slug: Optional[str] = Field(default=None, alias='form_slug')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    source: Optional[str] = Field(default=None, alias='source')
    status: Optional[FormSubmissionStatus] = Field(default=None, alias='status')
