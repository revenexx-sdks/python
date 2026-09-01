from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;
from ..enums.status import Status;
from ..enums.registration_status import RegistrationStatus;
from ..enums.customers_contacts_create_registration_status import CustomersContactsCreateRegistrationStatus;
from ..enums.contact_status import ContactStatus;
from ..enums.contact_activity_kind import ContactActivityKind;

class CustomersContacts(Service):

    def __init__(self, client) -> None:
        super(CustomersContacts, self).__init__(client)

    def customers_contact_events_list(
        self,
        id: Optional[str] = None,
        contact_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        subject: Optional[str] = None,
        actor: Optional[str] = None,
        occurred_at: Optional[str] = None,
        created_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        A contact event is one entry on a customer's timeline: an activity somebody logged (a call, a visit, a meeting, a note) or a registration decision this app recorded itself. Every entry is keyed by a CONTACT and stamped with the organization derived from that contact, so a company's history is one indexed read rather than a join. Append-only — there is no update and no delete, which is what makes it usable as evidence. The activity feed, filtered by whichever column the question needs: `contact_id` for one person, `organization_id` for a whole company, `kind` for one type of activity. `kind: "system"` is this app's own registration decision trail (`registration.submitted` / `.approved` / `.rejected`), and no caller may file one of those. Paged with `limit`/`offset`/`order`; newest first is `order=occurred_at.desc`.

        Parameters
        ----------
        id : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the timeline entry.
        contact_id : Optional[str]
            Filter to one person's timeline.
        organization_id : Optional[str]
            Filter to one company timeline — the whole history, without fanning out over its people.
        kind : Optional[str]
            Filter by entry kind. One of the tenant's own activity types (GET /customers/contact-event-kinds); 'system' is the registration decision trail and is the one a caller may not file.
        name : Optional[str]
            Filter by event name — registration.submitted | registration.approved | registration.rejected | activity.<kind>. This one IS this app's own vocabulary, not the tenant's.
        subject : Optional[str]
            Filter to rows whose `subject` is exactly this value. One line a person can scan in a timeline. Required for an activity; a decision row carries the app's own wording.
        actor : Optional[str]
            Filter to rows whose `actor` is exactly this value. Who logged the entry — free text as the client supplied it (operator id or email). Null for a row the app wrote itself.
        occurred_at : Optional[str]
            Exact timestamp equality on when it happened — there is no range filter on this API. Use `order=occurred_at.desc` with limit/offset to walk a timeline.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the row was written. Together with `occurred_at` this is what tells a late entry from a live one.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact_events'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if contact_id is not None:
            api_params['contact_id'] = self._normalize_value(contact_id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if subject is not None:
            api_params['subject'] = self._normalize_value(subject)
        if actor is not None:
            api_params['actor'] = self._normalize_value(actor)
        if occurred_at is not None:
            api_params['occurred_at'] = self._normalize_value(occurred_at)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_contact_events_get(
        self,
        id: str
    ) -> Error:
        """
        A contact event is one entry on a customer's timeline: an activity somebody logged (a call, a visit, a meeting, a note) or a registration decision this app recorded itself. Every entry is keyed by a CONTACT and stamped with the organization derived from that contact, so a company's history is one indexed read rather than a join. Append-only — there is no update and no delete, which is what makes it usable as evidence. One timeline entry by id, as it was written. Entries are never edited, so what this answers is what was recorded at the time.

        Parameters
        ----------
        id : str
            The contact event to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contact_events/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_list(
        self,
        id: Optional[str] = None,
        organization_id: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        job_title: Optional[str] = None,
        role: Optional[str] = None,
        status: Optional[Status] = None,
        order_approval_limit: Optional[float] = None,
        registration_status: Optional[RegistrationStatus] = None,
        registration_decided_at: Optional[str] = None,
        registration_decided_by: Optional[str] = None,
        registration_reason: Optional[str] = None,
        locale: Optional[str] = None,
        is_primary: Optional[bool] = None,
        external_user_id: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        A contact is a PERSON, and the unit that logs in: one platform user, one email address, one role held inside its organization. A contact without an organization is a standalone buyer rather than an error, and two people at the same company are two contacts sharing an `organization_id`. The people list, and the read behind an approval queue: `registration_status=pending` is every application waiting for a decision. Every column is a filter — `external_user_id` in particular is how a storefront turns a platform auth id back into a customer — and the page is `limit`/`offset`/`order`.

        Parameters
        ----------
        id : Optional[str]
            Filter to exactly one person.
        organization_id : Optional[str]
            Filter to one company's people. The company address book.
        email : Optional[str]
            Filter by exact email — the one lookup that is guaranteed to return at most one person, because the address is unique per tenant.
        first_name : Optional[str]
            Filter to rows whose `first_name` is exactly this value. Given name. Optional: an ERP import often has only a mailbox.
        last_name : Optional[str]
            Filter to rows whose `last_name` is exactly this value. Family name. Optional for the same reason.
        phone : Optional[str]
            Filter to rows whose `phone` is exactly this value. Direct number of this person, as somebody typed it — free text, no format is enforced or normalized. E.164 is what an integration should send.
        job_title : Optional[str]
            Filter to rows whose `job_title` is exactly this value. What this person does at the company — free text on purpose, because it is a title and not a grant. The permission ladder is `role`; overloading a job title with authority silently un-grants everyone the day the ledger is enforced.
        role : Optional[str]
            Filter by role. One of the tenant's own roles (GET /customers/roles) — a tenant that never edited the ledger has viewer, requester, buyer, approver, admin.
        status : Optional[Status]
            Filter by status.
        order_approval_limit : Optional[float]
            Filter to rows whose `order_approval_limit` is exactly this value. Amount ceiling for this person, in the market's currency: with the `orders.approve` permission it is the most they may sign off. Null means no ceiling. An amount, never a grant — the grant comes from the role.
        registration_status : Optional[RegistrationStatus]
            Filter by registration state. `pending` IS the approval inbox — there is no second entity for it.
        registration_decided_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When a merchant approved or rejected the application. Null while nobody has decided.
        registration_decided_by : Optional[str]
            Filter to rows whose `registration_decided_by` is exactly this value. Who decided — free text as the deciding client supplied it (an operator id or an email address), not a resolvable user reference.
        registration_reason : Optional[str]
            Filter to rows whose `registration_reason` is exactly this value. Why the application was declined. Always recorded here; whether the APPLICANT is ever told it is the tenant's `registration_reason_disclosed` setting, because that is a legal decision and not a template one.
        locale : Optional[str]
            Filter to rows whose `locale` is exactly this value. The language this person is written to in — BCP 47, and one of the store's configured locales. Null falls back to the store default.
        is_primary : Optional[bool]
            Filter to the primary contacts — with `organization_id`, the one person a merchant calls first at that company.
        external_user_id : Optional[str]
            Find the contact behind a platform user id. What a storefront session resolves with when it has an auth id and needs the customer record.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When this person record was created in this app.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When any column of this row last changed.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if email is not None:
            api_params['email'] = self._normalize_value(email)
        if first_name is not None:
            api_params['first_name'] = self._normalize_value(first_name)
        if last_name is not None:
            api_params['last_name'] = self._normalize_value(last_name)
        if phone is not None:
            api_params['phone'] = self._normalize_value(phone)
        if job_title is not None:
            api_params['job_title'] = self._normalize_value(job_title)
        if role is not None:
            api_params['role'] = self._normalize_value(role)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if order_approval_limit is not None:
            api_params['order_approval_limit'] = self._normalize_value(order_approval_limit)
        if registration_status is not None:
            api_params['registration_status'] = self._normalize_value(registration_status)
        if registration_decided_at is not None:
            api_params['registration_decided_at'] = self._normalize_value(registration_decided_at)
        if registration_decided_by is not None:
            api_params['registration_decided_by'] = self._normalize_value(registration_decided_by)
        if registration_reason is not None:
            api_params['registration_reason'] = self._normalize_value(registration_reason)
        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)
        if is_primary is not None:
            api_params['is_primary'] = self._normalize_value(is_primary)
        if external_user_id is not None:
            api_params['external_user_id'] = self._normalize_value(external_user_id)
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

        return response


    def customers_contacts_create(
        self,
        email: str,
        first_name: Optional[str] = None,
        is_primary: Optional[bool] = None,
        job_title: Optional[str] = None,
        last_name: Optional[str] = None,
        locale: Optional[str] = None,
        order_approval_limit: Optional[float] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        registration_status: Optional[CustomersContactsCreateRegistrationStatus] = None,
        role: Optional[str] = None,
        status: Optional[ContactStatus] = None
    ) -> Error:
        """
        A contact is a PERSON, and the unit that logs in: one platform user, one email address, one role held inside its organization. A contact without an organization is a standalone buyer rather than an error, and two people at the same company are two contacts sharing an `organization_id`. Creates the person and their platform login together, so a contact that exists can always sign in. `role` names one of this tenant's own roles and decides what they may do; `registration_status` may only be set to `pending` or `approved` here, because a rejection has to carry a reason and that is the reject route's job. `email` is the only field a create cannot omit; everything else is optional or defaulted by the database. Two rows of this tenant may not share `email` or `external_user_id` (while external_user_id IS NOT NULL).

        Parameters
        ----------
        email : str
            Login identity and the unique key of a person within the tenant. Changing it changes the platform login with it. Two people at the same company therefore need two addresses — a shared purchasing mailbox is one contact, not several.
        first_name : Optional[str]
            Given name. Optional: an ERP import often has only a mailbox.
        is_primary : Optional[bool]
            The main contact of its organization — who a merchant calls first. At most one per company is the intent; the tenant's `primary_contact_required` setting decides whether the last one may be demoted or deleted.
        job_title : Optional[str]
            What this person does at the company — free text on purpose, because it is a title and not a grant. The permission ladder is `role`; overloading a job title with authority silently un-grants everyone the day the ledger is enforced.
        last_name : Optional[str]
            Family name. Optional for the same reason.
        locale : Optional[str]
            The language this person is written to in — BCP 47, and one of the store's configured locales. Null falls back to the store default.
        order_approval_limit : Optional[float]
            Amount ceiling for this person, in the market's currency: with the `orders.approve` permission it is the most they may sign off. Null means no ceiling. An amount, never a grant — the grant comes from the role.
        organization_id : Optional[str]
            The company this person belongs to. NULL is a legitimate state, not a defect: a standalone buyer with no company behind them. Deleting the organization sets this null and keeps the person. Membership is mirrored to the platform team.
        phone : Optional[str]
            Direct number of this person, as somebody typed it — free text, no format is enforced or normalized. E.164 is what an integration should send.
        registration_status : Optional[CustomersContactsCreateRegistrationStatus]
            Where this person's own application stands: 'approved' (the default, and what an open store creates), 'pending' while a merchant has yet to decide, 'rejected' once they declined. Only the approve/reject routes move it; it is ignored on an ordinary update. On CREATE only, and only to file the contact as an application: 'pending' creates the platform user disabled and routes the contact through approve/reject. Ignored on update.
        role : Optional[str]
            The person's role INSIDE its organization, and the only thing permissions are derived from. One of the tenant's own roles (GET /customers/roles); a tenant that never edited the ledger has viewer, requester, buyer, approver, admin. Also the team role on the platform mirror. There is no global role — the same person in two companies is two contacts. A tenant that never edited the ledger has viewer, requester, buyer, approver, admin; a create without a role gets the one flagged as default, and a role the tenant does not keep is a 400.
        status : Optional[ContactStatus]
            Whether this person may act: 'invited' has been created but has not accepted, 'active' works, 'blocked' cannot log in. A create through the API defaults to 'invited'; a self-registration in an open store lands 'active'. Default 'invited' on create.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts'
        api_params = {}
        if email is None:
            raise RevenexxException('Missing required parameter: "email"')


        api_params['email'] = self._normalize_value(email)
        api_params['first_name'] = self._normalize_value(first_name)
        if is_primary is not None:
            api_params['is_primary'] = self._normalize_value(is_primary)
        api_params['job_title'] = self._normalize_value(job_title)
        api_params['last_name'] = self._normalize_value(last_name)
        api_params['locale'] = self._normalize_value(locale)
        api_params['order_approval_limit'] = self._normalize_value(order_approval_limit)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        if registration_status is not None:
            api_params['registration_status'] = self._normalize_value(registration_status)
        if role is not None:
            api_params['role'] = self._normalize_value(role)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_events_create(
        self,
        contact_id: str,
        subject: str,
        actor: Optional[str] = None,
        kind: Optional[ContactActivityKind] = None,
        note: Optional[str] = None,
        occurred_at: Optional[str] = None
    ) -> Error:
        """
        This is how a call, a visit, a meeting, an email or a plain note reaches one person's timeline. It writes a contact_events row with kind != 'system' and emits contact_event.created, so an activity travels on the same bus as a registration decision and a timeline is one query rather than a union. organization_id is DERIVED from the contact, never taken from the body — an activity cannot be filed under a company the person does not belong to.

        Parameters
        ----------
        contact_id : str
            The person the entry is about. The organization is derived from them.
        subject : str
            One line a person can scan in a timeline. Required — an entry nobody can read at a glance is not worth the row.
        actor : Optional[str]
            Who logged it (operator id or email). Free text; this app does not resolve it.
        kind : Optional[ContactActivityKind]
            What happened. 'system' is deliberately NOT accepted — those rows are the registration decision trail and are written by the approve/reject routes. Default 'note'.
        note : Optional[str]
            The long form. Stored inside the event payload as `note`, not as a column of its own.
        occurred_at : Optional[str]
            When it actually happened. Defaults to now — a call logged on Monday about Friday should say Friday.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{contact_id}/events'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        if subject is None:
            raise RevenexxException('Missing required parameter: "subject"')

        api_path = api_path.replace('{contact_id}', str(self._normalize_value(contact_id)))

        api_params['actor'] = self._normalize_value(actor)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        api_params['note'] = self._normalize_value(note)
        api_params['occurred_at'] = self._normalize_value(occurred_at)
        api_params['subject'] = self._normalize_value(subject)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_invite(
        self,
        contact_id: str,
        url: str,
        invited_by: Optional[str] = None
    ) -> Error:
        """
        Tell somebody they were added to a company. A deliberate act rather than a side effect of creating the contact: a merchant entering a colleague from a business card is not always ready to mail them, and "added" and "told" are different decisions. No secret travels — the platform team membership is confirmed as it is created, so there is nothing to accept; the message says "you are in, here is the way in". Unlike the auth mails, a failure here IS a failure: the identity service sends nothing for this occasion, so this is the only message the person gets.

        Parameters
        ----------
        contact_id : str
            The person being told. They are already a member — this only sends the message.
        url : str
            Where the invitation points — the storefront sign-in, normally. There is no token in it: the person is already a member and only has to sign in.
        invited_by : Optional[str]
            Who did the inviting, as the recipient should read it. Absent, the company name is used — "Beispiel GmbH invited you" reads better than the name of somebody they have never heard of.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{contact_id}/invite'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        if url is None:
            raise RevenexxException('Missing required parameter: "url"')

        api_path = api_path.replace('{contact_id}', str(self._normalize_value(contact_id)))

        api_params['invited_by'] = self._normalize_value(invited_by)
        api_params['url'] = self._normalize_value(url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_permissions(
        self,
        contact_id: str
    ) -> Error:
        """
        Computed from contacts.role on every call — the grants are never persisted, so this always reflects the role the contact holds right now.

        Parameters
        ----------
        contact_id : str
            The person whose grants are being read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{contact_id}/permissions'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        api_path = api_path.replace('{contact_id}', str(self._normalize_value(contact_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_registrations_approve(
        self,
        contact_id: str,
        decided_by: Optional[str] = None
    ) -> Error:
        """
        Only reachable for a contact whose registration_status is 'pending' or 'rejected' (approving a rejection reinstates it). Enables the platform user FIRST — the password the applicant chose at submit time works immediately, no new credential is issued — then sets registration_status='approved' and status='active', and un-blocks the organization this registration itself founded. Approving an already-approved registration is a no-op that emits nothing, so a retry is safe. Writes a contact_events row named 'registration.approved'.

        Parameters
        ----------
        contact_id : str
            The applicant. It is the CONTACT that is approved — the organization it founded is unblocked with it.
        decided_by : Optional[str]
            Who approved it — recorded on the contact and carried in the event. Free text (operator id or email); this app does not resolve it.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{contact_id}/registration/approve'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        api_path = api_path.replace('{contact_id}', str(self._normalize_value(contact_id)))

        api_params['decided_by'] = self._normalize_value(decided_by)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_registrations_reject(
        self,
        contact_id: str,
        reason: str,
        decided_by: Optional[str] = None
    ) -> Error:
        """
        Only reachable from 'pending'. Sets registration_status='rejected' and status='blocked', keeps the platform user in place but disabled — the email must not fall free for a silent second identity, and the merchant keeps the record. Delete the contact to remove both. 'reason' is mandatory and is stored on the contact plus carried in the event payload, so the applicant can be told why. Rejecting an already-rejected registration is a no-op. Writes a contact_events row named 'registration.rejected'.

        Parameters
        ----------
        contact_id : str
            The applicant being declined.
        reason : str
            Why the application was declined. Always stored on the contact. It only reaches the APPLICANT when the tenant's registration_reason_disclosed setting is on — the event payload then carries it, and so does the 403 the login answers.
        decided_by : Optional[str]
            Who rejected it — recorded on the contact and carried in the event.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{contact_id}/registration/reject'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        if reason is None:
            raise RevenexxException('Missing required parameter: "reason"')

        api_path = api_path.replace('{contact_id}', str(self._normalize_value(contact_id)))

        api_params['decided_by'] = self._normalize_value(decided_by)
        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_delete(
        self,
        id: str
    ) -> Error:
        """
        A contact is a PERSON, and the unit that logs in: one platform user, one email address, one role held inside its organization. A contact without an organization is a standalone buyer rather than an error, and two people at the same company are two contacts sharing an `organization_id`. Removes the person and their platform login, so they can no longer sign in anywhere. Their company keeps trading; use `status: "blocked"` instead when the intent is to stop one person without erasing what they did. Deleting one takes every `contact_events` and `addresses` row that points at it with it — the foreign keys decide, not this route.

        Parameters
        ----------
        id : str
            The contact to delete.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_get(
        self,
        id: str
    ) -> Error:
        """
        A contact is a PERSON, and the unit that logs in: one platform user, one email address, one role held inside its organization. A contact without an organization is a standalone buyer rather than an error, and two people at the same company are two contacts sharing an `organization_id`. One person by id. What they are ALLOWED to do is not in here: permissions are derived from `role` at read time and answered by `GET /customers/contacts/{contact_id}/permissions`.

        Parameters
        ----------
        id : str
            The contact to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_contacts_update(
        self,
        id: str,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        is_primary: Optional[bool] = None,
        job_title: Optional[str] = None,
        last_name: Optional[str] = None,
        locale: Optional[str] = None,
        order_approval_limit: Optional[float] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        registration_status: Optional[CustomersContactsCreateRegistrationStatus] = None,
        role: Optional[str] = None,
        status: Optional[ContactStatus] = None
    ) -> Error:
        """
        A contact is a PERSON, and the unit that logs in: one platform user, one email address, one role held inside its organization. A contact without an organization is a standalone buyer rather than an error, and two people at the same company are two contacts sharing an `organization_id`. A partial update — send only what changes. `external_user_id` and every `registration_*` column are ignored: the link to platform auth is mirror-managed, and registration state is only ever moved by the approve and reject routes, which record why. Two rows of this tenant may not share `email` or `external_user_id` (while external_user_id IS NOT NULL).

        Parameters
        ----------
        id : str
            The contact to update.
        email : Optional[str]
            Login identity and the unique key of a person within the tenant. Changing it changes the platform login with it. Two people at the same company therefore need two addresses — a shared purchasing mailbox is one contact, not several.
        first_name : Optional[str]
            Given name. Optional: an ERP import often has only a mailbox.
        is_primary : Optional[bool]
            The main contact of its organization — who a merchant calls first. At most one per company is the intent; the tenant's `primary_contact_required` setting decides whether the last one may be demoted or deleted.
        job_title : Optional[str]
            What this person does at the company — free text on purpose, because it is a title and not a grant. The permission ladder is `role`; overloading a job title with authority silently un-grants everyone the day the ledger is enforced.
        last_name : Optional[str]
            Family name. Optional for the same reason.
        locale : Optional[str]
            The language this person is written to in — BCP 47, and one of the store's configured locales. Null falls back to the store default.
        order_approval_limit : Optional[float]
            Amount ceiling for this person, in the market's currency: with the `orders.approve` permission it is the most they may sign off. Null means no ceiling. An amount, never a grant — the grant comes from the role.
        organization_id : Optional[str]
            The company this person belongs to. NULL is a legitimate state, not a defect: a standalone buyer with no company behind them. Deleting the organization sets this null and keeps the person. Membership is mirrored to the platform team.
        phone : Optional[str]
            Direct number of this person, as somebody typed it — free text, no format is enforced or normalized. E.164 is what an integration should send.
        registration_status : Optional[CustomersContactsCreateRegistrationStatus]
            Where this person's own application stands: 'approved' (the default, and what an open store creates), 'pending' while a merchant has yet to decide, 'rejected' once they declined. Only the approve/reject routes move it; it is ignored on an ordinary update. On CREATE only, and only to file the contact as an application: 'pending' creates the platform user disabled and routes the contact through approve/reject. Ignored on update.
        role : Optional[str]
            The person's role INSIDE its organization, and the only thing permissions are derived from. One of the tenant's own roles (GET /customers/roles); a tenant that never edited the ledger has viewer, requester, buyer, approver, admin. Also the team role on the platform mirror. There is no global role — the same person in two companies is two contacts. A tenant that never edited the ledger has viewer, requester, buyer, approver, admin; a create without a role gets the one flagged as default, and a role the tenant does not keep is a 400.
        status : Optional[ContactStatus]
            Whether this person may act: 'invited' has been created but has not accepted, 'active' works, 'blocked' cannot log in. A create through the API defaults to 'invited'; a self-registration in an open store lands 'active'. Default 'invited' on create.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if email is not None:
            api_params['email'] = self._normalize_value(email)
        api_params['first_name'] = self._normalize_value(first_name)
        if is_primary is not None:
            api_params['is_primary'] = self._normalize_value(is_primary)
        api_params['job_title'] = self._normalize_value(job_title)
        api_params['last_name'] = self._normalize_value(last_name)
        api_params['locale'] = self._normalize_value(locale)
        api_params['order_approval_limit'] = self._normalize_value(order_approval_limit)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        if registration_status is not None:
            api_params['registration_status'] = self._normalize_value(registration_status)
        if role is not None:
            api_params['role'] = self._normalize_value(role)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_organizations_events_create(
        self,
        organization_id: str,
        contact_id: str,
        subject: str,
        actor: Optional[str] = None,
        kind: Optional[ContactActivityKind] = None,
        note: Optional[str] = None,
        occurred_at: Optional[str] = None
    ) -> Error:
        """
        Same row as the contact route, reached from the organization. 'contact_id' is required and must belong to THIS organization — the picker offering the contacts is not filtered, so the membership check here is what stops a call with one company being filed under someone else's person.

        Parameters
        ----------
        organization_id : str
            The company the entry is filed under. The `contact_id` in the body has to belong to it.
        contact_id : str
            The person dealt with. Must be a contact of this organization.
        subject : str
            One line a person can scan in a timeline. Required — an entry nobody can read at a glance is not worth the row.
        actor : Optional[str]
            Who logged it (operator id or email). Free text; this app does not resolve it.
        kind : Optional[ContactActivityKind]
            What happened. 'system' is deliberately NOT accepted — those rows are the registration decision trail and are written by the approve/reject routes. Default 'note'.
        note : Optional[str]
            The long form. Stored inside the event payload as `note`, not as a column of its own.
        occurred_at : Optional[str]
            When it actually happened. Defaults to now — a call logged on Monday about Friday should say Friday.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{organization_id}/events'
        api_params = {}
        if organization_id is None:
            raise RevenexxException('Missing required parameter: "organization_id"')

        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')

        if subject is None:
            raise RevenexxException('Missing required parameter: "subject"')

        api_path = api_path.replace('{organization_id}', str(self._normalize_value(organization_id)))

        api_params['actor'] = self._normalize_value(actor)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        api_params['note'] = self._normalize_value(note)
        api_params['occurred_at'] = self._normalize_value(occurred_at)
        api_params['subject'] = self._normalize_value(subject)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

