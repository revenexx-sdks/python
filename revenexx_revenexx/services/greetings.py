from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.greeting import Greeting;

class Greetings(Service):

    def __init__(self, client) -> None:
        super(Greetings, self).__init__(client)

    def greetings_digest(
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

        api_path = '/v1/digest'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def greetings_list(
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

        api_path = '/v1/greetings'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def greetings_create(
        self,
        name: str,
        locale: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        name : str
            Who to greet
        locale : Optional[str]
            BCP-47 locale
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/greetings'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)
        api_params['name'] = self._normalize_value(name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def greetings_delete(
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

        api_path = '/v1/greetings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def greetings_get(
        self,
        id: str
    ) -> Greeting:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Greeting
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/greetings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Greeting)


    def greetings_update(
        self,
        id: str,
        locale: Optional[str] = None,
        message: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None
    ) -> Greeting:
        """
        

        Parameters
        ----------
        id : str
            
        locale : Optional[str]
            
        message : Optional[str]
            
        metadata : Optional[Dict[str, Any]]
            
        name : Optional[str]
            
        
        Returns
        -------
        Greeting
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/greetings/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)
        if message is not None:
            api_params['message'] = self._normalize_value(message)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Greeting)

