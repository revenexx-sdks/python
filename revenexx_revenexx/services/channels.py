from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.channel_status import ChannelStatus;
from ..enums.channel_type import ChannelType;
from ..models.channel import Channel;
from ..models.channel_defaults import ChannelDefaults;

class Channels(Service):

    def __init__(self, client) -> None:
        super(Channels, self).__init__(client)

    def channels_list(
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

        api_path = '/v1/channels'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def channels_create(
        self,
        code: str,
        name: str,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        status: Optional[ChannelStatus] = None,
        type: Optional[ChannelType] = None
    ) -> Channel:
        """
        

        Parameters
        ----------
        code : str
            Stable channel code, unique per tenant (e.g. shop, punchout-acme).
        name : str
            Display name.
        is_default : Optional[bool]
            Mark as the default channel (default false).
        labels : Optional[Dict[str, Any]]
            Localized display names keyed by locale.
        position : Optional[float]
            Sort position (default 0).
        status : Optional[ChannelStatus]
            Lifecycle status (default 'active').
        type : Optional[ChannelType]
            Where business happens (default 'storefront').
        
        Returns
        -------
        Channel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/channels'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['code'] = self._normalize_value(code)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Channel)


    def channels_defaults(
        self
    ) -> ChannelDefaults:
        """
        

        Returns
        -------
        ChannelDefaults
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/channels/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=ChannelDefaults)


    def channels_delete(
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

        api_path = '/v1/channels/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def channels_get(
        self,
        id: str
    ) -> Channel:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Channel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/channels/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Channel)


    def channels_update(
        self,
        id: str,
        code: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        status: Optional[ChannelStatus] = None,
        type: Optional[ChannelType] = None
    ) -> Channel:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            Stable channel code, unique per tenant (e.g. shop, punchout-acme).
        is_default : Optional[bool]
            Mark as the default channel (default false).
        labels : Optional[Dict[str, Any]]
            Localized display names keyed by locale.
        name : Optional[str]
            Display name.
        position : Optional[float]
            Sort position (default 0).
        status : Optional[ChannelStatus]
            Lifecycle status (default 'active').
        type : Optional[ChannelType]
            Where business happens (default 'storefront').
        
        Returns
        -------
        Channel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/channels/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Channel)

