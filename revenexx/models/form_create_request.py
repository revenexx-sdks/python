from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.form_status import FormStatus

class FormCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    definition : Optional[List[Any]]
        The form itself: a FormKit schema, held as a flat ARRAY of nodes (it defaults to `[]`, never to an object) and rendered verbatim by the storefront.
        
        Read it as the field list. Every node carrying a non-empty `name` collects one value and writes it into a submission&#039;s `data` under exactly that name — the example below produces `{&quot;company&quot;: …, &quot;email&quot;: …, &quot;message&quot;: …}` — while `$el` content nodes and `$rxStep` step markers collect nothing. Order is render order, and a `$rxStep` marker starts a new wizard step.
        
        See the `FormKitNode` schema for what a node may carry.
        
        On the way IN a node is any object: this is unconstrained jsonb, FormKit owns the grammar, and the one rule this app applies is the tenant&#039;s `max_form_fields` ceiling counted over the nodes with a non-empty `name`. Anything that is not an array at all is a 400.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata on the FORM, which this app neither reads nor writes: yours to key however an integration needs, stored and returned verbatim. (The metadata this app does write is on a SUBMISSION — see `FormSubmissionMetadata`.)
    name : str
        What this form is called in the Cockpit&#039;s form list. Operator-facing only — the storefront never renders it, so renaming a form breaks no page.
    settings : Optional[Dict[str, Any]]
        Submit label, success message, per-form notify email, post-submit actions, translations — see the `FormSettings` schema for every key that is read. Unconstrained jsonb on the way in: nothing here is required and no key is refused.
    slug : str
        URL-safe identifier, unique per tenant. This is the name a storefront resolves a form by (`GET /v1/forms?slug=contact&amp;status=live&amp;limit=1`), so it is part of the page&#039;s contract: changing it changes which form a page renders. Lower-case letters, digits and inner hyphens. Taken already? That is the 409 — one slug answers for one form.
    status : Optional[FormStatus]
        Lifecycle. `draft` while it is being built; `live` once the storefront may render it — the cover BFF resolves live forms only, so a draft is a 404 on the storefront and never a broken page; `archived` for a form that is kept for its submissions but no longer offered. Default &#039;draft&#039;.
    """
    definition: Optional[List[Any]] = Field(default=None, alias='definition')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: str = Field(..., alias='name')
    settings: Optional[Dict[str, Any]] = Field(default=None, alias='settings')
    slug: str = Field(..., alias='slug')
    status: Optional[FormStatus] = Field(default=None, alias='status')
