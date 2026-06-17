from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.address_type import AddressType;
from ..models.address import Address;
from ..models.auth_login_response import AuthLoginResponse;
from ..models.auth_me_response import AuthMeResponse;
from ..models.auth_register_response import AuthRegisterResponse;
from ..enums.contact_role import ContactRole;
from ..enums.contact_status import ContactStatus;
from ..models.contact import Contact;
from ..enums.organization_status import OrganizationStatus;
from ..models.organization import Organization;

class Customers(Service):

    def __init__(self, client) -> None:
        super(Customers, self).__init__(client)

    def customers_addresses_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/addresses'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_addresses_create(
        self,
        city: str,
        country: str,
        street: str,
        zip: str,
        company: Optional[str] = None,
        contact_id: Optional[str] = None,
        is_default: Optional[bool] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        region: Optional[str] = None,
        street2: Optional[str] = None,
        type: Optional[AddressType] = None
    ) -> Address:
        """
        

        Parameters
        ----------
        city : str
            
        country : str
            ISO 3166-1 alpha-2 code.
        street : str
            
        zip : str
            
        company : Optional[str]
            
        contact_id : Optional[str]
            Owning contact (personal address).
        is_default : Optional[bool]
            The default address of its owner and type.
        name : Optional[str]
            Recipient name.
        organization_id : Optional[str]
            Owning organization (company address).
        phone : Optional[str]
            
        region : Optional[str]
            
        street2 : Optional[str]
            
        type : Optional[AddressType]
            Default 'shipping'.
        
        Returns
        -------
        Address
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/addresses'
        api_params = {}
        if city is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "city"')

        if country is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "country"')

        if street is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "street"')

        if zip is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "zip"')


        api_params['city'] = self._normalize_value(city)
        api_params['company'] = self._normalize_value(company)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['country'] = self._normalize_value(country)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        api_params['region'] = self._normalize_value(region)
        api_params['street'] = self._normalize_value(street)
        api_params['street2'] = self._normalize_value(street2)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        api_params['zip'] = self._normalize_value(zip)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Address)


    def customers_addresses_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/addresses/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def customers_addresses_get(
        self,
        id: str
    ) -> Address:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Address
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/addresses/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Address)


    def customers_addresses_update(
        self,
        id: str,
        city: Optional[str] = None,
        company: Optional[str] = None,
        contact_id: Optional[str] = None,
        country: Optional[str] = None,
        is_default: Optional[bool] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        region: Optional[str] = None,
        street: Optional[str] = None,
        street2: Optional[str] = None,
        type: Optional[AddressType] = None,
        zip: Optional[str] = None
    ) -> Address:
        """
        

        Parameters
        ----------
        id : str
            
        city : Optional[str]
            
        company : Optional[str]
            
        contact_id : Optional[str]
            Owning contact (personal address).
        country : Optional[str]
            ISO 3166-1 alpha-2 code.
        is_default : Optional[bool]
            The default address of its owner and type.
        name : Optional[str]
            Recipient name.
        organization_id : Optional[str]
            Owning organization (company address).
        phone : Optional[str]
            
        region : Optional[str]
            
        street : Optional[str]
            
        street2 : Optional[str]
            
        type : Optional[AddressType]
            Default 'shipping'.
        zip : Optional[str]
            
        
        Returns
        -------
        Address
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/addresses/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if city is not None:
            api_params['city'] = self._normalize_value(city)
        api_params['company'] = self._normalize_value(company)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if country is not None:
            api_params['country'] = self._normalize_value(country)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        api_params['region'] = self._normalize_value(region)
        if street is not None:
            api_params['street'] = self._normalize_value(street)
        api_params['street2'] = self._normalize_value(street2)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if zip is not None:
            api_params['zip'] = self._normalize_value(zip)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Address)


    def customers_auth_login(
        self,
        email: str,
        password: str
    ) -> AuthLoginResponse:
        """
        

        Parameters
        ----------
        email : str
            
        password : str
            
        
        Returns
        -------
        AuthLoginResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/auth/login'
        api_params = {}
        if email is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "email"')

        if password is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "password"')


        api_params['email'] = self._normalize_value(email)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AuthLoginResponse)


    def customers_auth_logout(
        self,
        session_id: str,
        user_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        session_id : str
            
        user_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/auth/logout'
        api_params = {}
        if session_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "session_id"')

        if user_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "user_id"')


        api_params['session_id'] = self._normalize_value(session_id)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def customers_auth_me(
        self,
        user_id: str,
        session_id: Optional[str] = None
    ) -> AuthMeResponse:
        """
        

        Parameters
        ----------
        user_id : str
            
        session_id : Optional[str]
            Optional session to verify — answers 401 when the session is expired or revoked.
        
        Returns
        -------
        AuthMeResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/auth/me'
        api_params = {}
        if user_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "user_id"')


        api_params['session_id'] = self._normalize_value(session_id)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AuthMeResponse)


    def customers_auth_recovery(
        self,
        email: str,
        url: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        email : str
            
        url : str
            Redirect URL carrying userId + secret.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/auth/recovery'
        api_params = {}
        if email is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "email"')

        if url is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "url"')


        api_params['email'] = self._normalize_value(email)
        api_params['url'] = self._normalize_value(url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def customers_auth_recovery_confirm(
        self,
        password: str,
        secret: str,
        user_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        password : str
            
        secret : str
            
        user_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/auth/recovery'
        api_params = {}
        if password is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "password"')

        if secret is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "secret"')

        if user_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "user_id"')


        api_params['password'] = self._normalize_value(password)
        api_params['secret'] = self._normalize_value(secret)
        api_params['user_id'] = self._normalize_value(user_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def customers_auth_register(
        self,
        email: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        locale: Optional[str] = None,
        organization_id: Optional[str] = None,
        organization_name: Optional[str] = None
    ) -> AuthRegisterResponse:
        """
        

        Parameters
        ----------
        email : str
            
        password : str
            
        first_name : Optional[str]
            
        last_name : Optional[str]
            
        locale : Optional[str]
            BCP 47, e.g. de-DE
        organization_id : Optional[str]
            Join an existing organization.
        organization_name : Optional[str]
            Found a new organization; the contact becomes its admin.
        
        Returns
        -------
        AuthRegisterResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/auth/register'
        api_params = {}
        if email is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "email"')

        if password is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "password"')


        api_params['email'] = self._normalize_value(email)
        api_params['first_name'] = self._normalize_value(first_name)
        api_params['last_name'] = self._normalize_value(last_name)
        api_params['locale'] = self._normalize_value(locale)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['organization_name'] = self._normalize_value(organization_name)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AuthRegisterResponse)


    def customers_contacts_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/contacts'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_contacts_create(
        self,
        email: str,
        first_name: Optional[str] = None,
        is_primary: Optional[bool] = None,
        last_name: Optional[str] = None,
        locale: Optional[str] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        role: Optional[ContactRole] = None,
        status: Optional[ContactStatus] = None
    ) -> Contact:
        """
        

        Parameters
        ----------
        email : str
            
        first_name : Optional[str]
            
        is_primary : Optional[bool]
            The primary contact of its organization.
        last_name : Optional[str]
            
        locale : Optional[str]
            BCP 47, e.g. de-DE
        organization_id : Optional[str]
            Owning organization — membership is mirrored to the platform team.
        phone : Optional[str]
            
        role : Optional[ContactRole]
            Default 'buyer' — also the team role on the platform mirror.
        status : Optional[ContactStatus]
            Default 'invited' on create.
        
        Returns
        -------
        Contact
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/contacts'
        api_params = {}
        if email is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "email"')


        api_params['email'] = self._normalize_value(email)
        api_params['first_name'] = self._normalize_value(first_name)
        if is_primary is not None:
            api_params['is_primary'] = self._normalize_value(is_primary)
        api_params['last_name'] = self._normalize_value(last_name)
        api_params['locale'] = self._normalize_value(locale)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        if role is not None:
            api_params['role'] = self._normalize_value(role)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Contact)


    def customers_contacts_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def customers_contacts_get(
        self,
        id: str
    ) -> Contact:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Contact
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Contact)


    def customers_contacts_update(
        self,
        id: str,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        is_primary: Optional[bool] = None,
        last_name: Optional[str] = None,
        locale: Optional[str] = None,
        organization_id: Optional[str] = None,
        phone: Optional[str] = None,
        role: Optional[ContactRole] = None,
        status: Optional[ContactStatus] = None
    ) -> Contact:
        """
        

        Parameters
        ----------
        id : str
            
        email : Optional[str]
            
        first_name : Optional[str]
            
        is_primary : Optional[bool]
            The primary contact of its organization.
        last_name : Optional[str]
            
        locale : Optional[str]
            BCP 47, e.g. de-DE
        organization_id : Optional[str]
            Owning organization — membership is mirrored to the platform team.
        phone : Optional[str]
            
        role : Optional[ContactRole]
            Default 'buyer' — also the team role on the platform mirror.
        status : Optional[ContactStatus]
            Default 'invited' on create.
        
        Returns
        -------
        Contact
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/contacts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if email is not None:
            api_params['email'] = self._normalize_value(email)
        api_params['first_name'] = self._normalize_value(first_name)
        if is_primary is not None:
            api_params['is_primary'] = self._normalize_value(is_primary)
        api_params['last_name'] = self._normalize_value(last_name)
        api_params['locale'] = self._normalize_value(locale)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['phone'] = self._normalize_value(phone)
        if role is not None:
            api_params['role'] = self._normalize_value(role)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Contact)


    def customers_organizations_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/organizations'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_organizations_create(
        self,
        name: str,
        settings: Optional[Dict[str, Any]] = None,
        status: Optional[OrganizationStatus] = None,
        vat_id: Optional[str] = None
    ) -> Organization:
        """
        

        Parameters
        ----------
        name : str
            Company name — mirrored to the platform team.
        settings : Optional[Dict[str, Any]]
            Free-form organization settings.
        status : Optional[OrganizationStatus]
            Default 'active'.
        vat_id : Optional[str]
            
        
        Returns
        -------
        Organization
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/organizations'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['name'] = self._normalize_value(name)
        api_params['settings'] = self._normalize_value(settings)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['vat_id'] = self._normalize_value(vat_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Organization)


    def customers_organizations_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def customers_organizations_get(
        self,
        id: str
    ) -> Organization:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Organization
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Organization)


    def customers_organizations_update(
        self,
        id: str,
        name: Optional[str] = None,
        settings: Optional[Dict[str, Any]] = None,
        status: Optional[OrganizationStatus] = None,
        vat_id: Optional[str] = None
    ) -> Organization:
        """
        

        Parameters
        ----------
        id : str
            
        name : Optional[str]
            Company name — mirrored to the platform team.
        settings : Optional[Dict[str, Any]]
            Free-form organization settings.
        status : Optional[OrganizationStatus]
            Default 'active'.
        vat_id : Optional[str]
            
        
        Returns
        -------
        Organization
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/customers/organizations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['settings'] = self._normalize_value(settings)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        api_params['vat_id'] = self._normalize_value(vat_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Organization)

