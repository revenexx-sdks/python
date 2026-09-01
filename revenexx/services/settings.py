from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated

class Settings(Service):

    def __init__(self, client) -> None:
        super(Settings, self).__init__(client)

    def settings_get_app_settings(
        self,
        app: str,
        market: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The tenant's effective settings for the app — the declared schema's defaults merged with stored tenant/market values. Sensitive settings are masked (listed in `masked`, omitted from `settings`).

        Parameters
        ----------
        app : str
            App name, e.g. `pages`.
        market : Optional[str]
            Resolve market-scoped settings for this market code; falls back to the tenant value.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/settings/apps/{app}'
        api_params = {}
        if app is None:
            raise RevenexxException('Missing required parameter: "app"')

        api_path = api_path.replace('{app}', str(self._normalize_value(app)))

        if market is not None:
            api_params['market'] = self._normalize_value(market)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response

