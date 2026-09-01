from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;

class Customers(Service):

    def __init__(self, client) -> None:
        super(Customers, self).__init__(client)

    def customers_auth_login(
        self,
        email: str,
        password: str
    ) -> Error:
        """
        An email and a password go in; a session and the CONTACT behind it come back, so a storefront knows in one call both that the buyer is signed in and who they are. The session is minted server-side rather than handed back from the credential check, because the account route hides the session secret from non-privileged responses and a trusted BFF needs it. `permissions` carries the buyer's effective grants, so a BFF does not need a second call to decide what to render.

        Parameters
        ----------
        email : str
            The buyer's login address — the same one the contact carries.
        password : str
            The password from registration or recovery. Wrong credentials are a 401; a correct one on an undecided application is a 403.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/login'
        api_params = {}
        if email is None:
            raise RevenexxException('Missing required parameter: "email"')

        if password is None:
            raise RevenexxException('Missing required parameter: "password"')


        api_params['email'] = self._normalize_value(email)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_logout(
        self,
        session_id: str,
        user_id: str
    ) -> Error:
        """
        Ends ONE session — the buyer signs out on this device and stays signed in on the others, because the session id is what is revoked and not the account. The contact row is untouched: signing out is not blocking, and a caller wanting the second thing wants `status: "blocked"` on the contact instead. Both ids come from what `/customers/auth/login` answered, and a BFF should drop its own cookie whatever this answers — the session is unusable afterwards either way.

        Parameters
        ----------
        session_id : str
            The session to revoke — `session.$id` from the login.
        user_id : str
            The platform user — `session.userId` from the login.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/logout'
        api_params = {}
        if session_id is None:
            raise RevenexxException('Missing required parameter: "session_id"')

        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['session_id'] = self._normalize_value(session_id)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_magic_link(
        self,
        email: str,
        url: str
    ) -> Error:
        """
        Sign in without a password: a link goes to the address, and `PUT /customers/auth/magic-link` turns it into a session. Creates the account when the address is new, which makes this a registration path as much as a sign-in one — and why an address nobody holds is not distinguished in the answer. The mail is this shop's own template through the messaging service; the secret is not in this response, only in the link.

        Parameters
        ----------
        email : str
            Who to send the link to. An address that has never been seen creates an account rather than failing.
        url : str
            Where the mailed link points. `userId`, `secret` and `expire` are appended as query parameters; the first two are what the confirm call takes.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/magic-link'
        api_params = {}
        if email is None:
            raise RevenexxException('Missing required parameter: "email"')

        if url is None:
            raise RevenexxException('Missing required parameter: "url"')


        api_params['email'] = self._normalize_value(email)
        api_params['url'] = self._normalize_value(url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_magic_link_confirm(
        self,
        secret: str,
        user_id: str
    ) -> Error:
        """
        The buyer clicked the link and the storefront read `userId` and `secret` out of it. Answers exactly what a password login answers — session, contact and effective grants — because a shop must not have to branch on how somebody signed in.

        Parameters
        ----------
        secret : str
            The one-time secret the mailed link carried. Spent on first use and expiring, so a second attempt with the same one is a 401 rather than a second session.
        user_id : str
            The `userId` the mailed link carried.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/magic-link'
        api_params = {}
        if secret is None:
            raise RevenexxException('Missing required parameter: "secret"')

        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['secret'] = self._normalize_value(secret)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_me(
        self,
        user_id: str,
        session_id: Optional[str] = None
    ) -> Error:
        """
        The platform user, the customer record mirrored against it and the effective grants, in one call. The expected caller is a trusted storefront BFF holding the session on the buyer's behalf, which is why the ids travel in the body rather than in a browser-facing header. The grants are derived here on every call rather than returned from anywhere they could be cached, so a role changed a second ago is already reflected.

        Parameters
        ----------
        user_id : str
            The platform user to resolve — `session.userId` from the login.
        session_id : Optional[str]
            Optional session to verify. Pass it to ask "is this session still alive?" (a revoked one is then a 401); omit it to only ask who a user is.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/me'
        api_params = {}
        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['session_id'] = self._normalize_value(session_id)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_mfa_challenge(
        self,
        user_id: str,
        factor: Optional[str] = None
    ) -> Error:
        """
        Between the password and the finished session: the buyer has proved one thing and is asked for another. Created by user id, because the account route that creates challenges hides the code from whoever may call it — and answered with the half-finished session the sign-in is in the middle of, through `PUT /customers/auth/mfa/challenge`. Needs a platform build that returns the challenge code; without one there is no way to read what to send, and the call answers 502 rather than mailing an empty challenge.

        Parameters
        ----------
        user_id : str
            The platform user being challenged.
        factor : Optional[str]
            Which factor to challenge. Defaults to `email`, the only one this route mails.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/mfa/challenge'
        api_params = {}
        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['factor'] = self._normalize_value(factor)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_mfa_challenge_confirm(
        self,
        challenge_id: str,
        code: str,
        session_secret: str,
        user_id: Optional[str] = None
    ) -> Error:
        """
        The code the buyer typed, against the challenge it was sent for. The session becomes fully authenticated when this answers.

        Parameters
        ----------
        challenge_id : str
            The `$id` the send answered with.
        code : str
            What the buyer typed.
        session_secret : str
            The same session the challenge was created with.
        user_id : Optional[str]
            The platform user, for the caller's own bookkeeping. The challenge already knows whose it is.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/mfa/challenge'
        api_params = {}
        if challenge_id is None:
            raise RevenexxException('Missing required parameter: "challenge_id"')

        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if session_secret is None:
            raise RevenexxException('Missing required parameter: "session_secret"')


        api_params['challenge_id'] = self._normalize_value(challenge_id)
        api_params['code'] = self._normalize_value(code)
        api_params['session_secret'] = self._normalize_value(session_secret)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_otp(
        self,
        email: str
    ) -> Error:
        """
        The same token as the sign-in link, delivered as a short code instead — for a buyer on a phone, where leaving for a mail client and coming back loses the checkout they were in the middle of. Redeemed with `PUT /customers/auth/otp`.

        Parameters
        ----------
        email : str
            Who to send the code to. As with the sign-in link, an unknown address creates an account rather than failing.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/otp'
        api_params = {}
        if email is None:
            raise RevenexxException('Missing required parameter: "email"')


        api_params['email'] = self._normalize_value(email)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_otp_confirm(
        self,
        secret: str,
        user_id: str
    ) -> Error:
        """
        The code the buyer typed, plus the `userId` the send answered with. Answers exactly what a password login answers — session, contact and effective grants — so a storefront never has to branch on how somebody signed in. The code is spent on first use and expires, so a second attempt with the same one is a 401 rather than a second session.

        Parameters
        ----------
        secret : str
            The one-time secret the mailed code carried. Spent on first use and expiring, so a second attempt with the same one is a 401 rather than a second session.
        user_id : str
            The `userId` the mailed code carried.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/otp'
        api_params = {}
        if secret is None:
            raise RevenexxException('Missing required parameter: "secret"')

        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['secret'] = self._normalize_value(secret)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_recovery(
        self,
        email: str,
        url: str
    ) -> Error:
        """
        Step one of two: a link goes to the address given, and `PUT /customers/auth/recovery` is what the buyer's browser comes back to. The identity service mints the token; the MAIL is this shop's own — the tenant's template, layout, language and sending domain, through the messaging service. The secret is NOT in this answer: it exists only inside the mailed link, which is the whole point of the two-step shape, and echoing it here would make the mail decorative. Nothing about the contact changes; the password only moves in step two.

        Parameters
        ----------
        email : str
            Who to send the recovery mail to. An address nobody holds is not distinguished here — do not build an account-existence check on the answer.
        url : str
            Where the mailed link points. `userId`, `secret` and `expire` are appended as query parameters — the first two are what the confirm call takes. Same shape the identity service's own mail used, so a storefront that already handles that link needs no change.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/recovery'
        api_params = {}
        if email is None:
            raise RevenexxException('Missing required parameter: "email"')

        if url is None:
            raise RevenexxException('Missing required parameter: "url"')


        api_params['email'] = self._normalize_value(email)
        api_params['url'] = self._normalize_value(url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_recovery_confirm(
        self,
        password: str,
        secret: str,
        user_id: str
    ) -> Error:
        """
        Step two: the `userId` and `secret` the mailed link carried, plus the password the buyer just typed. The secret is spent on first use and expires, so a link cannot be replayed and a second attempt with the same one is a 401 rather than a second password change. The new password is in effect the moment this answers; what happens to sessions opened with the old one is the identity service's policy, not this app's.

        Parameters
        ----------
        password : str
            The new password. It replaces the old one immediately; existing sessions are the identity service's business, not this app's.
        secret : str
            The one-time secret from the mailed link. Only that value works — it is spent on first use and expires, and anything else is a 401, so no example here would be anything but a call that fails.
        user_id : str
            The `userId` the mailed link carried.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/recovery'
        api_params = {}
        if password is None:
            raise RevenexxException('Missing required parameter: "password"')

        if secret is None:
            raise RevenexxException('Missing required parameter: "secret"')

        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['password'] = self._normalize_value(password)
        api_params['secret'] = self._normalize_value(secret)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_register(
        self,
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        locale: Optional[str] = None,
        organization_id: Optional[str] = None,
        organization_name: Optional[str] = None,
        url: Optional[str] = None,
        vat_id: Optional[str] = None,
        verification_url: Optional[str] = None
    ) -> Error:
        """
        One call writes the whole buyer: the contact this app is the system of record for, and the platform user behind its login. When the body names a company it also FOUNDS one — an organization, mirrored into platform auth as a team, with this contact as its admin. The tenant setting registration_mode decides what a registration IS. 'open' (the default, unchanged behaviour) creates a finished account: registration_status='approved', status='active', login works. 'approval_required' creates an APPLICATION: registration_status='pending', status='invited', the platform user exists with the applicant's own password but is DISABLED, and a newly founded organization is parked as 'blocked' — check `approval_required` in the response and show a 'we will get back to you' screen instead of logging the buyer in. The registration gates below are all evaluated BEFORE anything is written, and a failure after that point rolls the organization and the contact back together.

        Parameters
        ----------
        email : str
            The buyer's address. It becomes the login AND the unique key of the contact, so a second registration with it is a 409 — including while the first one is still waiting for approval.
        password : str
            The password the buyer chooses. It is hashed by the identity service at this moment and never travels again: an approval later enables the account, it does not issue a new credential.
        first_name : Optional[str]
            Given name. Optional: an ERP import often has only a mailbox.
        last_name : Optional[str]
            Family name. Optional for the same reason.
        locale : Optional[str]
            The language this person is written to in — BCP 47, and one of the store's configured locales. Null falls back to the store default. One of the store's own locales, or the call is a 400.
        organization_id : Optional[str]
            JOIN an existing company — the invite shape. Neither b2b_registration_enabled nor b2c_registration_enabled applies to it.
        organization_name : Optional[str]
            FOUND a new company, with this contact as its admin. This is what makes the registration a B2B one; leaving it out registers a standalone buyer.
        url : Optional[str]
            Where the welcome mail's button points — the buyer's first stop in this shop. Absent, the mail still goes out and simply carries no button. Ignored when the registration is an APPLICATION: there is no account to send anybody to yet.
        vat_id : Optional[str]
            VAT identification number (USt-IdNr. in Germany) — the closest thing a B2B buyer has to a legal identity. Validated against the EU VIES service when the tenant's `organization_vat_id_required` setting is on, and stored verbatim otherwise, including for buyers outside the EU. Required when the tenant's `organization_vat_id_required` is on, and checked BEFORE the company is created so a bad one leaves no half-founded organization behind.
        verification_url : Optional[str]
            Where the address-confirmation link points, when the tenant's `email_verification` asks for one on registration. `userId`, `secret` and `expire` are appended, and `PUT /customers/auth/verification` takes the first two. Without it the registration still succeeds and `verification_sent` is false — this app cannot invent a storefront URL, and a link pointing nowhere is worse than none.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/register'
        api_params = {}
        if email is None:
            raise RevenexxException('Missing required parameter: "email"')

        if password is None:
            raise RevenexxException('Missing required parameter: "password"')


        api_params['email'] = self._normalize_value(email)
        api_params['first_name'] = self._normalize_value(first_name)
        api_params['last_name'] = self._normalize_value(last_name)
        api_params['locale'] = self._normalize_value(locale)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['organization_name'] = self._normalize_value(organization_name)
        api_params['password'] = self._normalize_value(password)
        api_params['url'] = self._normalize_value(url)
        api_params['vat_id'] = self._normalize_value(vat_id)
        api_params['verification_url'] = self._normalize_value(verification_url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_verification(
        self,
        url: str,
        user_id: str
    ) -> Error:
        """
        Confirm that the address belongs to the buyer. Needs no session: the verification is created through the identity service's users surface, because its account counterpart reads the authenticated user and a caller authenticating AS the user cannot see the secret it just created. The buyer still confirms with their own session, through `PUT /customers/auth/verification` — only the creation moved. Send it right after a registration, or from an account page.

        Parameters
        ----------
        url : str
            Where the mailed link points. `userId`, `secret` and `expire` are appended as query parameters; the first two are what the confirm call takes.
        user_id : str
            The platform user whose address is being confirmed — `user_id` from the registration, or `session.userId` from a login.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/verification'
        api_params = {}
        if url is None:
            raise RevenexxException('Missing required parameter: "url"')

        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['url'] = self._normalize_value(url)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_auth_verification_confirm(
        self,
        secret: str,
        user_id: str
    ) -> Error:
        """
        The `userId` and `secret` the mailed link carried. The address counts as confirmed the moment this answers; the secret is spent, so the link cannot be replayed.

        Parameters
        ----------
        secret : str
            The one-time secret the mailed link carried. Spent on first use and expiring, so a second attempt with the same one is a 401 rather than a second session.
        user_id : str
            The `userId` the mailed link carried.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/auth/verification'
        api_params = {}
        if secret is None:
            raise RevenexxException('Missing required parameter: "secret"')

        if user_id is None:
            raise RevenexxException('Missing required parameter: "user_id"')


        api_params['secret'] = self._normalize_value(secret)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_principal_resolve(
        self,
        contact_id: str
    ) -> Error:
        """
        The capability the API gateway calls to turn a caller's X-Revenexx-Principal assertion into the permission set it forwards to every other app as X-Revenexx-Permissions. This app is the platform's role provider (manifest#provides_roles), and this is the hot path of every attributed storefront request — one contact read plus the tenant's role map. A blocked or pending contact always resolves with active=false; what its `permissions` then say is the tenant's blocked_contact_behavior setting — 'keep' (the default, the role's grants), 'catalog_only' or 'deny_all'.

        Parameters
        ----------
        contact_id : str
            The contact the caller is acting for.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/principal/resolve'
        api_params = {}
        if contact_id is None:
            raise RevenexxException('Missing required parameter: "contact_id"')


        api_params['contact_id'] = self._normalize_value(contact_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

