from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.form_status import FormStatus;
from ..models.error import Error;
from ..models.form_defaults_result import FormDefaultsResult;
from ..enums.form_submission_status import FormSubmissionStatus;
from ..enums.forms_submissions_prune_status import FormsSubmissionsPruneStatus;
from ..models.forms_vocabulary_index import FormsVocabularyIndex;
from ..enums.forms_vocabularies_get_name import FormsVocabulariesGetName;

class Forms(Service):

    def __init__(self, client) -> None:
        super(Forms, self).__init__(client)

    def forms_list(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        status: Optional[FormStatus] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        The catalogue of forms this tenant has authored, a page at a time. A row is the whole form — `definition`, `settings`, `status`, `slug` — so a list read is not a summary view that has to be followed by a read per row.
        
        Every column of a form except the three jsonb ones is an exact-match filter, and they combine: `?slug=contact&status=live&limit=1` is how the storefront resolves the form for a page, and it is why a page never needs the form's id. The jsonb columns are the deliberate exception — a comparison against `definition`, `settings` or `metadata` can only be equality against the WHOLE document, which matches only for a caller who already holds it, so there is no searching inside a form's fields from here. (Sending one anyway is not a silent failure: `?definition={}` is honoured as that whole-document equality, and `?definition=x` is refused with 400 `invalid_value` naming the parameter.) A query key that is not a filterable column is dropped rather than refused, and the `filter` echo in the answer is what tells you which of the two happened: an empty echo beside a query string that carried a filter means the filter was misspelled.
        
        Paging is `limit`/`offset` with a single-column `order`. The default page is 50 and 200 is the ceiling — a larger `limit` is clamped rather than refused, and `page.limit` reports what was applied — while `page.total` is the figure to show a merchant and `page.hasMore` answers whether another page follows instead of leaving it to be inferred from a short one. `order=created_at.desc` is the newest-first reading an editor wants.

        Parameters
        ----------
        id : Optional[str]
            Filter to one form by id, which answers a one-row page rather than the row — `GET /v1/forms/{id}` is the addressed form of the same read. It exists because it composes: `?id=…&status=live` answers "is this form live?" in one call. A value that is not a uuid is refused with 400 `invalid_value`.
        name : Optional[str]
            Filter to one form by its exact name. Whole-value equality and case-sensitive — there is no substring search on this API.
        slug : Optional[str]
            Filter to one form by its slug — unique per tenant, so this is how a storefront resolves a form without knowing its id. `?slug=contact&status=live&limit=1` is the call the cover BFF makes for every rendered form.
        status : Optional[FormStatus]
            Filter to one lifecycle status. `?status=live` is the set the storefront may render; `?status=draft` is what is still being built.
        created_at : Optional[str]
            Filter to forms created at EXACTLY this instant. Equality, not a range: a date alone matches only a row whose timestamp is exactly that, so it selects nothing for a whole day. To read by time, sort instead (`order=created_at.desc`) and page. A value the data plane cannot read as a timestamp is refused with 400 `invalid_value`.
        updated_at : Optional[str]
            Filter to forms last written at EXACTLY this instant — the same equality-not-range caveat as `created_at`.
        limit : Optional[float]
            Page size. Default 50; a value above 200 is clamped to 200 rather than refused, and `page.limit` says what was applied.
        offset : Optional[float]
            How many matching rows to skip. Page N is `offset = (N - 1) * limit`; `page.hasMore` says whether there is a next one.
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if slug is not None:
            api_params['slug'] = self._normalize_value(slug)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_create(
        self,
        name: str,
        slug: str,
        definition: Optional[List[Dict[str, Any]]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        settings: Optional[Dict[str, Any]] = None,
        status: Optional[FormStatus] = None
    ) -> Error:
        """
        A form is born a `draft` and stays off the storefront until somebody moves it to `live`, so creating one is safe: the cover BFF resolves live forms only, and nothing renders until the status says it may. `definition` may be omitted entirely — the row is then the empty shell the Form Builder fills in.
        
        `slug` is the one field that is not free. It is unique per tenant and it is what a storefront resolves a form by, so a create that reuses one is a 409 rather than a second form answering to the same page — and the collision is often with a form the caller has never opened. `name` is operator-facing only and may be anything.
        
        An unbounded definition is a storefront page nobody can load, so the tenant sets a ceiling on how many named inputs one form may declare. Only nodes carrying a non-empty `name` count against it: a form with twenty paragraphs of legal text and three inputs is a three-field form. A definition over the ceiling is a 422 and not a 400 — the payload is well formed and would have been accepted under a higher limit — and the body names both the count and the limit.

        Parameters
        ----------
        name : str
            What this form is called in the Cockpit's form list. Operator-facing only — the storefront never renders it, so renaming a form breaks no page.
        slug : str
            URL-safe identifier, unique per tenant. This is the name a storefront resolves a form by (`GET /v1/forms?slug=contact&status=live&limit=1`), so it is part of the page's contract: changing it changes which form a page renders. Lower-case letters, digits and inner hyphens. Taken already? That is the 409 — one slug answers for one form.
        definition : Optional[List[Dict[str, Any]]]
            The form itself: a FormKit schema, held as a flat ARRAY of nodes (it defaults to `[]`, never to an object) and rendered verbatim by the storefront.
            
            Read it as the field list. Every node carrying a non-empty `name` collects one value and writes it into a submission's `data` under exactly that name — the example below produces `{"company": …, "email": …, "message": …}` — while `$el` content nodes and `$rxStep` step markers collect nothing. Order is render order, and a `$rxStep` marker starts a new wizard step.
            
            See the `FormKitNode` schema for what a node may carry.
            
            On the way IN a node is any object: this is unconstrained jsonb, FormKit owns the grammar, and the one rule this app applies is the tenant's `max_form_fields` ceiling counted over the nodes with a non-empty `name`. Anything that is not an array at all is a 400.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata on the FORM, which this app neither reads nor writes: yours to key however an integration needs, stored and returned verbatim. (The metadata this app does write is on a SUBMISSION — see `FormSubmissionMetadata`.)
        settings : Optional[Dict[str, Any]]
            Submit label, success message, per-form notify email, post-submit actions, translations — see the `FormSettings` schema for every key that is read. Unconstrained jsonb on the way in: nothing here is required and no key is refused.
        status : Optional[FormStatus]
            Lifecycle. `draft` while it is being built; `live` once the storefront may render it — the cover BFF resolves live forms only, so a draft is a 404 on the storefront and never a broken page; `archived` for a form that is kept for its submissions but no longer offered. Default 'draft'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        if slug is None:
            raise RevenexxException('Missing required parameter: "slug"')


        if definition is not None:
            api_params['definition'] = self._normalize_value(definition)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['settings'] = self._normalize_value(settings)
        api_params['slug'] = self._normalize_value(slug)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_defaults(
        self
    ) -> FormDefaultsResult:
        """
        Every tenant starts with one sample form so the Form Builder is never empty and there is a live render and submit target from the first minute — the `contact` slug the read examples throughout this document resolve against.
        
        Normally nobody calls it. The same seeding runs on `app.installed`, so a tenant that has had the app for more than a moment already has the sample; this route is the manual re-run, for a tenant installed before the sample existed or one that removed it and wants it back.
        
        It is idempotent, and keyed on the SLUG rather than on content: a slug that is already taken is left exactly as it stands, so a sample form the merchant has since rewritten is never overwritten and a second call creates nothing at all. The answer says which of the two happened, slug by slug — `created` names what this call wrote, `existing` what was already there — and on a settled tenant `created` is empty.

        Returns
        -------
        FormDefaultsResult
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=FormDefaultsResult)


    def forms_submissions_list(
        self,
        id: Optional[str] = None,
        form_id: Optional[str] = None,
        form_slug: Optional[str] = None,
        source: Optional[str] = None,
        status: Optional[FormSubmissionStatus] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        The inbox: every submission this tenant has received, a page at a time. A row is the whole submission, `data` included, so the list is the inbox and the detail view at once — nothing has to be fetched per row to show what somebody wrote. Treat all of it as END-USER data.
        
        Every column except the two jsonb ones is an exact-match filter and they combine, so `?form_slug=contact&status=new&order=created_at.desc` is the unread inbox of one form, newest first. Two of those filters ask the same question differently: `form_id` is the reliable one and survives a rename of the form, while `form_slug` is the denormalised copy and needs neither a join nor a prior lookup. What was SUBMITTED is not searchable here — `data` is jsonb, and the only comparison available on it is equality against the whole document, which matches only for a caller who already holds the entire submission (`?data=x`, not being a JSON document at all, is refused with 400 `invalid_value`) — so an inbox search belongs on top of the rows this returns.
        
        Paging is `limit`/`offset` with a single-column `order`: the default page is 50, 200 is the ceiling, and a larger `limit` is clamped rather than refused. `page.total` is the count to put in front of a merchant while `page.returned` is only what fitted on this page, and `page.hasMore` says whether to ask for another.

        Parameters
        ----------
        id : Optional[str]
            Filter to one submission by id, as a one-row page. `GET /v1/forms/submissions/{id}` is the addressed form of the same read. A value that is not a uuid is refused with 400 `invalid_value`.
        form_id : Optional[str]
            Filter to one form's inbox, by id — the reliable one, because it survives a rename of the slug.
        form_slug : Optional[str]
            Filter to one form's inbox by slug — the denormalised copy, so neither a join nor a prior lookup of the form is needed.
        source : Optional[str]
            Filter to one origin, exactly as it was recorded — normally the page path the storefront sent. Whole-value equality, so it selects one page and not a prefix.
        status : Optional[FormSubmissionStatus]
            Filter to one inbox status. `?status=new` is the unread inbox; `?status=spam` is what the honeypot caught.
        created_at : Optional[str]
            Filter to submissions that arrived at EXACTLY this instant. Equality, not a range, so this is not how a date span is read — sort (`order=created_at.desc`) and page for that, and use POST /forms/submissions/prune for anything age-based.
        updated_at : Optional[str]
            Filter to submissions last written at EXACTLY this instant — the same equality-not-range caveat as `created_at`.
        limit : Optional[float]
            Page size. Default 50; a value above 200 is clamped to 200 rather than refused, and `page.limit` says what was applied.
        offset : Optional[float]
            How many matching rows to skip. Page N is `offset = (N - 1) * limit`; `page.hasMore` says whether there is a next one.
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/submissions'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if form_id is not None:
            api_params['form_id'] = self._normalize_value(form_id)
        if form_slug is not None:
            api_params['form_slug'] = self._normalize_value(form_slug)
        if source is not None:
            api_params['source'] = self._normalize_value(source)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_submissions_create(
        self,
        data: Dict[str, Any],
        form_id: str,
        form_slug: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        source: Optional[str] = None,
        status: Optional[FormSubmissionStatus] = None
    ) -> Error:
        """
        The storefront's path, and the moment a lead enters the platform. A stored submission emits `form.submitted` onto the tenant event bus with the row itself as the payload — that is the event an Integration Studio workflow or a notification email listens to, and it is the only event this app raises about a submission. A call that is refused therefore leaves no trace anywhere: no row, and no automation that ever hears about it.
        
        It is also the only moment anything is known about a submission, so the tenant's policy is applied here. If honeypot_field names a decoy and the submission filled it in, the field is stripped — it is a trap, not an answer the visitor gave, so it never reaches `data` — and spam_handling (flag | reject) decides between storing the row as 'spam' and refusing outright with 422.
        
        The notification recipient is resolved once, here: the form's own notify_email, else the tenant's, stamped into metadata.notify_email with metadata.notify_source naming which of the two won. It is resolved at insert rather than at delivery because the row IS the event payload — a workflow reads the address off the event instead of re-resolving a form's settings that may since have changed.

        Parameters
        ----------
        data : Dict[str, Any]
            What the visitor typed — the substance of the submission, and the reason this row is the payload of `form.submitted`.
            
            It is an object keyed by the `name` of the definition node that collected each value, so the keys of a submission are the named nodes of its form's `definition` and nothing else. There is no fixed set of keys across forms: a contact form yields `{name, email, message}`, a price request whatever its operator built.
            
            The VALUE type follows the input type, which is why this object is not typed further: a `text`, `email` or `textarea` yields a string, a `number` a number, a single `checkbox` a boolean, a `select`/`radio` the chosen option value, a multi-select or a checkbox set an array of them, and a `group` or `list` input nests an object or an array under its own name. Nothing coerces them — a value arrives as the storefront sent it and is stored as jsonb.
            
            Two values are NOT here: the honeypot field, if the tenant configured one, is stripped before the row is written (it is a trap, not an answer the visitor gave), and the resolved notification recipient lives in `metadata`, not in what somebody typed.
        form_id : str
            The form this submission was made against. It is resolved at insert, so an id no form in this tenant holds is a 404 and nothing is stored — a submission with no form is a lead nobody can read. Required on a create: it is the only thing that says which form was filled in.
        form_slug : Optional[str]
            The form's slug as it stood when this submission arrived, copied onto the row: the inbox filters by form without a join, and a submission still says which form collected it after that form has been renamed. It does not outlive a DELETED form — the foreign key cascades and takes the submission with it. On a write the body's value WINS; omit it and the form's own slug is copied in. So: OPTIONAL — send it and it is stored as sent, even if it disagrees with the form; omit it and the form's own slug is filled in from `form_id`.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata, yours to key as an integration needs. The resolved notification recipient is merged OVER it at insert, so `notify_email` and `notify_source` sent here are overwritten — see the `FormSubmissionMetadata` schema.
        source : Optional[str]
            Where the submission came from. The storefront sends the `window.location.pathname` of the page that carried the form, so this is normally a path rather than an absolute URL; any other surface (an app, an import) puts its own name here. Null when the caller sent none.
        status : Optional[FormSubmissionStatus]
            Inbox triage. `new` until somebody opens it, then `read`, and `archived` once it is dealt with. `spam` is set by code in exactly one place — the honeypot, and only while the tenant's spam_handling is 'flag'; under 'reject' the submission is never stored at all. Default 'new'. A create may set it — an inbox importer records a submission that is already read — but nothing needs to: omit it and the row is 'new'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/submissions'
        api_params = {}
        if data is None:
            raise RevenexxException('Missing required parameter: "data"')

        if form_id is None:
            raise RevenexxException('Missing required parameter: "form_id"')


        api_params['data'] = self._normalize_value(data)
        api_params['form_id'] = self._normalize_value(form_id)
        if form_slug is not None:
            api_params['form_slug'] = self._normalize_value(form_slug)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['source'] = self._normalize_value(source)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_submissions_prune(
        self,
        dry_run: Optional[bool] = None,
        form_slug: Optional[str] = None,
        older_than_days: Optional[float] = None,
        status: Optional[FormsSubmissionsPruneStatus] = None
    ) -> Error:
        """
        The retention sweep. It deletes submissions the tenant has stopped promising to keep — everything older than `submission_retention_days` — and it is the one route in this app that reads that promise at all.
        
        Nothing runs on a timer — an app that quietly deletes a merchant's leads on a schedule nobody watched is the failure mode worth avoiding. This is the only thing that acts on submission_retention_days, it previews unless dry_run is explicitly false, and it deletes at most 500 rows per call (`remaining` says whether to call again).
        
        The sweep is TENANT-WIDE and cannot be narrowed to a market. A submission carries no market: there is no such column, and the platform's scope register is written by a best-effort trigger that only fires when the writer sent `X-Revenexx-Market` — which the storefront omits whenever the visitor has selected no market, and the Cockpit never sends. So an unassigned row means "nobody recorded it" at least as often as it means "global", and attributing it either way would risk deleting one market's leads on another market's schedule.
        
        `submission_retention_days` is per market, because a retention period is a legal answer and the law is territorial. The floor this sweep applies is therefore the STRICTEST one in the tenant — the longest value configured anywhere, baseline or market — and not the one the calling market sees. `retention_days` reports it and `retention_market` names whose it was. The consequence worth knowing: one market cannot prune on a shorter schedule than another market promised, because the one sweep would take both markets' rows.
        
        The floor is established, never assumed. If the tenant's markets cannot be listed, or a settings read falls back to its declared defaults (which for retention is 0 — no floor at all), the answer is 503 and nothing is deleted.

        Parameters
        ----------
        dry_run : Optional[bool]
            Default TRUE. Nothing is deleted until this is explicitly false.
        form_slug : Optional[str]
            Narrow the sweep to one form.
        older_than_days : Optional[float]
            Age threshold. Omit to use the retention floor. A value BELOW the floor is raised to it — the setting is the floor, not a default, and the floor is the LONGEST submission_retention_days configured anywhere in the tenant (see the operation description).
        status : Optional[FormsSubmissionsPruneStatus]
            Narrow the sweep to one inbox status, e.g. 'spam'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/submissions/prune'
        api_params = {}

        api_params['dry_run'] = self._normalize_value(dry_run)
        api_params['form_slug'] = self._normalize_value(form_slug)
        api_params['older_than_days'] = self._normalize_value(older_than_days)
        api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_submissions_delete(
        self,
        id: str
    ) -> Error:
        """
        Removes one submission permanently. There is no soft delete anywhere in this app — no `deleted_at`, no trash, no undo — so the row and the end-user data in it are gone when this answers.
        
        Nothing is emitted when they go. This app publishes `form.submitted` on insert and has no delete event, so an automation that already acted on the submission is never told it was withdrawn; if that matters, the withdrawal has to be carried by whatever raised it.
        
        Nothing else is touched: the form keeps its `definition` and its other submissions. Reach for this for the one-off — an erasure request, a test row, a duplicate. For the many, use `POST /v1/forms/submissions/prune`, which previews before it acts and cannot go below the tenant's `submission_retention_days`; that floor does NOT apply here, so this route deletes a submission the retention policy would still be keeping. And if the point is to get a lead out of the inbox rather than out of the database, PUT its `status` to `archived` instead.

        Parameters
        ----------
        id : str
            The submission, by id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/submissions/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_submissions_get(
        self,
        id: str
    ) -> Error:
        """
        One received submission, whole — the detail view behind a row of `GET /v1/forms/submissions`.
        
        `data` is the substance: what the visitor actually typed, keyed by the `name` of each node in the form's `definition`. Around it are `source` (the page that carried the form), the inbox `status`, and the `metadata` this app stamped at insert — `notify_email` and `notify_source`, the recipient the `form.submitted` event carried, so a workflow and a human reading the inbox see the same answer.
        
        Treat what comes back as END-USER data: a name, an address, an enquiry, whatever the operator asked for. This is also the call the retention preview points at — `POST /v1/forms/submissions/prune` deliberately samples only id, form and date, so this route is where you look to see what a sweep would actually take.
        
        What you read here is what was sent: under the shipped `submission_edit` policy a PUT may move `status` and `metadata` and nothing else, so the submitted values, the form and the arrival time are the record rather than a draft.

        Parameters
        ----------
        id : str
            The submission, by id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/submissions/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_submissions_update(
        self,
        id: str,
        data: Optional[Dict[str, Any]] = None,
        form_id: Optional[str] = None,
        form_slug: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        source: Optional[str] = None,
        status: Optional[FormSubmissionStatus] = None
    ) -> Error:
        """
        Triage, not correction. What this route is FOR is moving the inbox `status` — 'new' to 'read' as somebody opens the lead, 'archived' once it is dealt with, 'spam' for what the honeypot did not catch — and stamping whatever an integration keeps in `metadata`.
        
        A received submission is a record of what somebody sent, so under submission_edit = 'status_only' (the default) those two are the only columns that may move. A patch that would alter the submitted data, its form or its timestamp is refused with 403, and the message names the columns it refused. A patch that merely echoes the stored value back is not a change and passes, so a client that PUTs the whole row still works.
        
        `updated_at` moves with the triage, which makes it evidence about the handling and never about the submitted values. And if the point is to get a lead out of the inbox rather than out of the database, this is the route for it: set `status` to `archived` here instead of reaching for the delete, which is permanent and has no undo.

        Parameters
        ----------
        id : str
            The submission, by id.
        data : Optional[Dict[str, Any]]
            What the visitor typed — the substance of the submission, and the reason this row is the payload of `form.submitted`.
            
            It is an object keyed by the `name` of the definition node that collected each value, so the keys of a submission are the named nodes of its form's `definition` and nothing else. There is no fixed set of keys across forms: a contact form yields `{name, email, message}`, a price request whatever its operator built.
            
            The VALUE type follows the input type, which is why this object is not typed further: a `text`, `email` or `textarea` yields a string, a `number` a number, a single `checkbox` a boolean, a `select`/`radio` the chosen option value, a multi-select or a checkbox set an array of them, and a `group` or `list` input nests an object or an array under its own name. Nothing coerces them — a value arrives as the storefront sent it and is stored as jsonb.
            
            Two values are NOT here: the honeypot field, if the tenant configured one, is stripped before the row is written (it is a trap, not an answer the visitor gave), and the resolved notification recipient lives in `metadata`, not in what somebody typed.
        form_id : Optional[str]
            The form this submission was made against. It is resolved at insert, so an id no form in this tenant holds is a 404 and nothing is stored — a submission with no form is a lead nobody can read. Required on a create: it is the only thing that says which form was filled in.
        form_slug : Optional[str]
            The form's slug as it stood when this submission arrived, copied onto the row: the inbox filters by form without a join, and a submission still says which form collected it after that form has been renamed. It does not outlive a DELETED form — the foreign key cascades and takes the submission with it. On a write the body's value WINS; omit it and the form's own slug is copied in. So: OPTIONAL — send it and it is stored as sent, even if it disagrees with the form; omit it and the form's own slug is filled in from `form_id`.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata, yours to key as an integration needs. The resolved notification recipient is merged OVER it at insert, so `notify_email` and `notify_source` sent here are overwritten — see the `FormSubmissionMetadata` schema.
        source : Optional[str]
            Where the submission came from. The storefront sends the `window.location.pathname` of the page that carried the form, so this is normally a path rather than an absolute URL; any other surface (an app, an import) puts its own name here. Null when the caller sent none.
        status : Optional[FormSubmissionStatus]
            Inbox triage. `new` until somebody opens it, then `read`, and `archived` once it is dealt with. `spam` is set by code in exactly one place — the honeypot, and only while the tenant's spam_handling is 'flag'; under 'reject' the submission is never stored at all. Default 'new'. A create may set it — an inbox importer records a submission that is already read — but nothing needs to: omit it and the row is 'new'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/submissions/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if form_id is not None:
            api_params['form_id'] = self._normalize_value(form_id)
        if form_slug is not None:
            api_params['form_slug'] = self._normalize_value(form_slug)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['source'] = self._normalize_value(source)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_vocabularies_list(
        self
    ) -> FormsVocabularyIndex:
        """
        The enums this app publishes, so a client can discover them instead of holding a copy. Names: form-statuses, submission-statuses.
        
        An entry carries the three things a menu needs — the `name` a URL is built from, the human `title`, and a `description` of what the set decides — and deliberately NOT the values. Enough to build a menu, not enough to fill a select: `GET /forms/vocabularies/{name}` is the call for that, and a client holding the qualified pair 'forms.<name>' builds that URL from the pair alone, which is what makes reading this index worth more than hard-coding two names.
        
        Both `title` and `description` come back either as a plain string or as a locale map keyed by language tag; read the tag you want and fall back to `en`.

        Returns
        -------
        FormsVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=FormsVocabularyIndex)


    def forms_vocabularies_get(
        self,
        name: FormsVocabulariesGetName
    ) -> Error:
        """
        One vocabulary WITH its values: every value the column permits, each carrying the `key` the database stores, the `title` and `description` a human reads, a semantic badge `tone`, and a `final` flag for the values that end the lifecycle. This is the call that fills a select or renders a status badge. Names: form-statuses, submission-statuses.
        
        The values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift — a value added to the constraint appears here even before anyone labels it, titled from its own key and falling back to `default_tone` for its badge. That is the whole reason to come here rather than hard-code three statuses in a UI.
        
        Values come back in constraint order, which is lifecycle order, and therefore the order a select should offer them in. `closed` says the set is exhaustive: there is no value outside it this API will accept. `title` and `description` are each either a plain string or a locale map keyed by language tag — read the tag you want and fall back to `en` — and a value nobody has translated is a bare string rather than an error.

        Parameters
        ----------
        name : FormsVocabulariesGetName
            The vocabulary name — the part after the dot in the qualified id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_delete(
        self,
        id: str
    ) -> Error:
        """
        Deleting a form deletes every submission it ever received.
        
        `submissions.form_id` is ON DELETE CASCADE — the one foreign key on this app's tables — so the inbox goes with the form, in the database, permanently. Nothing is archived on the way out, no event is emitted for the submissions that vanish, and there is no soft delete in this app to recover them from. A submission is an end user's data, which is why this is the first sentence rather than a footnote.
        
        That is what the tenant setting form_delete_policy (block | archive | cascade, default 'block') stands in front of: REFUSE with 409 and the count, ARCHIVE the form and keep everything, or CASCADE on purpose. A form with no submissions always deletes, under every policy.
        
        That setting is the one in this app with ONE value for the whole tenant. The other six are per-market, because what they decide is market-local; this one is not, so `X-Revenexx-Market` does not change the answer this route gives. A market that could set 'cascade' for itself would be deleting leads that belong to markets which had said 'block'.
        
        Both the 409 body and the 200 body carry `submissions`, the number of rows at stake. It counts the form's WHOLE inbox — every market, not the share belonging to the one a request names — because that is what the cascade takes. It is the only figure a merchant has to judge this by, so read it before allowing the cascade, and `GET /v1/forms/submissions?form_id=…` is how to see what they are first.
        
        The policy is a guard on THIS route, not a database constraint: the cascade is what the database does on its own, and a client that removes the row by some other path gets it with nothing in front of it.

        Parameters
        ----------
        id : str
            The form, by id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_get(
        self,
        id: str
    ) -> Error:
        """
        The whole form: `definition` — the flat FormKit node array the storefront renders verbatim — plus `settings`, `status` and `slug`.
        
        This is the route for an id you are already holding: a submission's `form_id`, a row the Cockpit list handed you. A storefront resolving a PAGE does not come here, because it has a slug and not an id — `GET /v1/forms?slug=contact&status=live&limit=1` is the call that answers that, and the `status` filter is what keeps a half-built form off a live page. There is no filtering on this route at all: a `draft` form comes back exactly like a published one, so a caller that must not render a draft has to check `status` itself.
        
        Nothing is folded in on the way out. The `definition` is returned in the language it was authored in — the per-form `i18n` overlay is applied by the storefront BFF, not by this API — and the submissions the form has collected are neither included nor counted here. The inbox for one form is `GET /v1/forms/submissions?form_id=…`, and it is worth asking for before a delete: see `DELETE /v1/forms/{id}`.

        Parameters
        ----------
        id : str
            The form, by id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def forms_update(
        self,
        id: str,
        definition: Optional[List[Dict[str, Any]]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        settings: Optional[Dict[str, Any]] = None,
        slug: Optional[str] = None,
        status: Optional[FormStatus] = None
    ) -> Error:
        """
        A partial update over everything a create may set — `definition`, `settings`, `status`, `name`, `slug`, `metadata` — where an omitted field keeps the value it has. It is the write behind the Form Builder's save, and equally behind the one-field change that publishes a form by moving `status` from `draft` to `live`. `updated_at` is stamped on every call, so it is the column an editor sorts by.
        
        The same field ceiling applies as on the create, or a form would simply grow past it later: the tenant's `max_form_fields` is counted over the nodes of the NEW `definition` that carry a non-empty `name`, and a definition above it is refused with 422 rather than stored truncated.
        
        Moving `slug` is the edit to think about twice. It is unique per tenant, so a rename onto a slug another form holds is a 409 — but it is the rename that SUCCEEDS that changes behaviour, because the slug is how a storefront page resolves this form: change it and the page naming the old one resolves nothing. The submissions already collected are unaffected either way; each keeps the slug it arrived under in its own `form_slug`, which is exactly what that copy is for.

        Parameters
        ----------
        id : str
            The form, by id.
        definition : Optional[List[Dict[str, Any]]]
            The form itself: a FormKit schema, held as a flat ARRAY of nodes (it defaults to `[]`, never to an object) and rendered verbatim by the storefront.
            
            Read it as the field list. Every node carrying a non-empty `name` collects one value and writes it into a submission's `data` under exactly that name — the example below produces `{"company": …, "email": …, "message": …}` — while `$el` content nodes and `$rxStep` step markers collect nothing. Order is render order, and a `$rxStep` marker starts a new wizard step.
            
            See the `FormKitNode` schema for what a node may carry.
            
            On the way IN a node is any object: this is unconstrained jsonb, FormKit owns the grammar, and the one rule this app applies is the tenant's `max_form_fields` ceiling counted over the nodes with a non-empty `name`. Anything that is not an array at all is a 400.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata on the FORM, which this app neither reads nor writes: yours to key however an integration needs, stored and returned verbatim. (The metadata this app does write is on a SUBMISSION — see `FormSubmissionMetadata`.)
        name : Optional[str]
            What this form is called in the Cockpit's form list. Operator-facing only — the storefront never renders it, so renaming a form breaks no page.
        settings : Optional[Dict[str, Any]]
            Submit label, success message, per-form notify email, post-submit actions, translations — see the `FormSettings` schema for every key that is read. Unconstrained jsonb on the way in: nothing here is required and no key is refused.
        slug : Optional[str]
            URL-safe identifier, unique per tenant. This is the name a storefront resolves a form by (`GET /v1/forms?slug=contact&status=live&limit=1`), so it is part of the page's contract: changing it changes which form a page renders. Lower-case letters, digits and inner hyphens. Taken already? That is the 409 — one slug answers for one form.
        status : Optional[FormStatus]
            Lifecycle. `draft` while it is being built; `live` once the storefront may render it — the cover BFF resolves live forms only, so a draft is a 404 on the storefront and never a broken page; `archived` for a form that is kept for its submissions but no longer offered. Default 'draft'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/forms/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if definition is not None:
            api_params['definition'] = self._normalize_value(definition)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['settings'] = self._normalize_value(settings)
        if slug is not None:
            api_params['slug'] = self._normalize_value(slug)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

