from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated

class Health(Service):

    def __init__(self, client) -> None:
        super(Health, self).__init__(client)

    def health_live(
        self
    ) -> Dict[str, Any]:
        """
        Answers as long as the process is running. Never touches a dependency, so it stays 200 while the gateway is degraded — use readiness to decide whether to send traffic.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/health/live'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def health_ready(
        self
    ) -> Dict[str, Any]:
        """
        Answers 200 once the gateway's registry source is reachable, 503 until then.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/health/ready'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response

