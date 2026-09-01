from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .form_submission_metadata import FormSubmissionMetadata
from ..enums.form_submission_status import FormSubmissionStatus

T = TypeVar('T')

class FormSubmission(AppwriteModel, Generic[T]):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        When the submission arrived. This is the age the retention sweep measures against `submission_retention_days`, and the column an inbox sorts by (`order=created_at.desc`).
    data : Optional[Dict[str, Any]]
        What the visitor typed — the substance of the submission, and the reason this row is the payload of `form.submitted`.
        
        It is an object keyed by the `name` of the definition node that collected each value, so the keys of a submission are the named nodes of its form&#039;s `definition` and nothing else. There is no fixed set of keys across forms: a contact form yields `{name, email, message}`, a price request whatever its operator built.
        
        The VALUE type follows the input type, which is why this object is not typed further: a `text`, `email` or `textarea` yields a string, a `number` a number, a single `checkbox` a boolean, a `select`/`radio` the chosen option value, a multi-select or a checkbox set an array of them, and a `group` or `list` input nests an object or an array under its own name. Nothing coerces them — a value arrives as the storefront sent it and is stored as jsonb.
        
        Two values are NOT here: the honeypot field, if the tenant configured one, is stripped before the row is written (it is a trap, not an answer the visitor gave), and the resolved notification recipient lives in `metadata`, not in what somebody typed.
    form_id : Optional[str]
        The form this submission was made against. It is resolved at insert, so an id no form in this tenant holds is a 404 and nothing is stored — a submission with no form is a lead nobody can read.
    form_slug : Optional[str]
        The form&#039;s slug as it stood when this submission arrived, copied onto the row: the inbox filters by form without a join, and a submission still says which form collected it after that form has been renamed. It does not outlive a DELETED form — the foreign key cascades and takes the submission with it. On a write the body&#039;s value WINS; omit it and the form&#039;s own slug is copied in.
    id : Optional[str]
        The submission&#039;s own id — what the inbox links to, and what a workflow reading `form.submitted` gets handed.
    metadata : Optional[FormSubmissionMetadata[T]]
        Free-form metadata, plus what this app stamped on at insert. The recipient is resolved ONCE, here, because this row is the payload of `form.submitted` — a workflow reads the address off the event instead of re-resolving a form&#039;s settings that may since have changed.
    source : Optional[str]
        Where the submission came from. The storefront sends the `window.location.pathname` of the page that carried the form, so this is normally a path rather than an absolute URL; any other surface (an app, an import) puts its own name here. Null when the caller sent none.
    status : Optional[FormSubmissionStatus]
        Inbox triage. `new` until somebody opens it, then `read`, and `archived` once it is dealt with. `spam` is set by code in exactly one place — the honeypot, and only while the tenant&#039;s spam_handling is &#039;flag&#039;; under &#039;reject&#039; the submission is never stored at all. Default &#039;new&#039;.
    tenant_id : Optional[str]
        The tenant this row belongs to — the store slug, not an id. Set by the platform from the authenticated context, never by a caller; a write that carries it is ignored, and no request can read another tenant&#039;s rows by sending a different one.
    updated_at : Optional[str]
        When the row was last written — a triage status change. It is not evidence about the submitted data, which under the shipped policy cannot change at all.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    data: Optional[Dict[str, Any]] = Field(default=None, alias='data')
    form_id: Optional[str] = Field(default=None, alias='form_id')
    form_slug: Optional[str] = Field(default=None, alias='form_slug')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[FormSubmissionMetadata[T]] = Field(default=None, alias='metadata')
    source: Optional[str] = Field(default=None, alias='source')
    status: Optional[FormSubmissionStatus] = Field(default=None, alias='status')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormSubmission[T]':
        """Create FormSubmission instance with typed data."""
        instance = cls.model_validate(data)
        if 'metadata' in data and data['metadata'] is not None:
            instance.metadata = FormSubmissionMetadata.with_data(
                data['metadata'], model_type
            )
        return instance
