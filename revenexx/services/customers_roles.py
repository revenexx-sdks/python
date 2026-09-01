from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.role_catalog_response import RoleCatalogResponse;
from ..models.error import Error;

class CustomersRoles(Service):

    def __init__(self, client) -> None:
        super(CustomersRoles, self).__init__(client)

    def customers_roles_list(
        self
    ) -> RoleCatalogResponse:
        """
        The whole catalogue in one read: every role a contact of this tenant can hold, the permissions each one grants, and the built-in permission vocabulary those grants are drawn from. Roles are held by a CONTACT and apply inside that contact's organization; there is no global customer role. Permissions are derived from the role at read time and never stored per contact, so a role change takes effect immediately and cannot leave a stale grant. The role to permission MAPPING is per tenant and configurable (PUT /customers/roles/{key}/permissions); a tenant that has not configured anything gets the built-ins and 'source' says which of the two answered. Built-in roles, least to most privileged: viewer (Viewer), requester (Requester), buyer (Buyer), approver (Approver), admin (Administrator). The permission KEYS themselves come from the cross-app ledger — every installed app declares what it enforces — so a tenant may grant a key this list does not mention.

        Returns
        -------
        RoleCatalogResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/roles'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=RoleCatalogResponse)


    def customers_roles_defaults(
        self,
        data: Dict[str, Any]
    ) -> Error:
        """
        Idempotent: a role that already exists is left completely alone, its permissions included, so re-seeding never undoes a merchant's edits. Creates viewer, requester, buyer, approver, admin with the built-in mapping. A tenant that never calls this still behaves correctly — the catalogue and every permission read fall back to the same built-ins.

        Parameters
        ----------
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/roles/defaults'
        api_params = {}
        if data is None:
            raise RevenexxException('Missing required parameter: "data"')


        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_roles_permissions_replace(
        self,
        key: str,
        permissions: List[str]
    ) -> Error:
        """
        The whole new set in one call — the shape a role editor actually produces, and the one that cannot leave a half-applied grant behind if a second call fails. Seeds the built-in roles first when the tenant has none, so editing works without calling /defaults. Permission keys are free text on purpose: they belong to whichever app declared them, and a grant for an app that is not installed simply has nothing to act on.

        Parameters
        ----------
        key : str
            The role key — one of the tenant's own roles (GET /customers/roles).
        permissions : List[str]
            The complete new set. Duplicates and blanks are ignored; an empty array revokes everything.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/roles/{key}/permissions'
        api_params = {}
        if key is None:
            raise RevenexxException('Missing required parameter: "key"')

        if permissions is None:
            raise RevenexxException('Missing required parameter: "permissions"')

        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['permissions'] = self._normalize_value(permissions)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

