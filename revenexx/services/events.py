from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated

class Events(Service):

    def __init__(self, client) -> None:
        super(Events, self).__init__(client)

    def events_get_catalog(
        self,
        fields: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Every event type this tenant's installed apps and platform services declare — what can be published and subscribed to, independent of whether one has fired yet. Each entry says what causes it (`trigger`) and what it carries (`sample`, `data_schema`).

        Parameters
        ----------
        fields : Optional[str]
            Comma-separated keys to keep on each emit. Omit for the full entry. A consumer that reads two fields should say so: the response carries a sample and a JSON Schema per event, and asking for less is the difference between a few kB and tens. An unknown key is ignored; a list naming nothing this response has returns the full entry rather than an empty one.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/events/catalog'
        api_params = {}

        if fields is not None:
            api_params['fields'] = self._normalize_value(fields)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response

