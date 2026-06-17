from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.market_status import MarketStatus;
from ..models.market import Market;
from ..models.market_context import MarketContext;
from ..models.market_currency import MarketCurrency;
from ..models.market_locale import MarketLocale;
from ..models.market_tax_class import MarketTaxClass;

class Markets(Service):

    def __init__(self, client) -> None:
        super(Markets, self).__init__(client)

    def markets_list(
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

        api_path = '/v1/markets'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def markets_create(
        self,
        code: str,
        name: str,
        currency: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        status: Optional[MarketStatus] = None
    ) -> Market:
        """
        

        Parameters
        ----------
        code : str
            Market code (unique per tenant).
        name : str
            
        currency : Optional[str]
            ISO 4217 code (default 'EUR').
        is_default : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            Localized display names ({locale: label}).
        position : Optional[float]
            Sort position (default 0).
        status : Optional[MarketStatus]
            Default 'active'.
        
        Returns
        -------
        Market
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['code'] = self._normalize_value(code)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Market)


    def markets_delete(
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

        api_path = '/v1/markets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def markets_get(
        self,
        id: str
    ) -> Market:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Market
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Market)


    def markets_update(
        self,
        id: str,
        code: Optional[str] = None,
        currency: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        status: Optional[MarketStatus] = None
    ) -> Market:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            Market code (unique per tenant).
        currency : Optional[str]
            ISO 4217 code (default 'EUR').
        is_default : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            Localized display names ({locale: label}).
        name : Optional[str]
            
        position : Optional[float]
            Sort position (default 0).
        status : Optional[MarketStatus]
            Default 'active'.
        
        Returns
        -------
        Market
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if status is not None:
            api_params['status'] = self._normalize_value(status)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Market)


    def markets_context(
        self,
        id: str
    ) -> MarketContext:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        MarketContext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{id}/context'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MarketContext)


    def markets_currencies_list(
        self,
        market_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        market_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/currencies'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def markets_currencies_create(
        self,
        market_id: str,
        code: str,
        is_default: Optional[bool] = None,
        position: Optional[float] = None
    ) -> MarketCurrency:
        """
        

        Parameters
        ----------
        market_id : str
            
        code : str
            ISO 4217 code, e.g. EUR (unique per market).
        is_default : Optional[bool]
            
        position : Optional[float]
            Sort position (default 0).
        
        Returns
        -------
        MarketCurrency
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/currencies'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))

        api_params['code'] = self._normalize_value(code)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if position is not None:
            api_params['position'] = self._normalize_value(position)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MarketCurrency)


    def markets_currencies_delete(
        self,
        market_id: str,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        market_id : str
            
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

        api_path = '/v1/markets/{market_id}/currencies/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def markets_currencies_get(
        self,
        market_id: str,
        id: str
    ) -> MarketCurrency:
        """
        

        Parameters
        ----------
        market_id : str
            
        id : str
            
        
        Returns
        -------
        MarketCurrency
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/currencies/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MarketCurrency)


    def markets_currencies_update(
        self,
        market_id: str,
        id: str,
        code: Optional[str] = None,
        is_default: Optional[bool] = None,
        position: Optional[float] = None
    ) -> MarketCurrency:
        """
        

        Parameters
        ----------
        market_id : str
            
        id : str
            
        code : Optional[str]
            ISO 4217 code, e.g. EUR (unique per market).
        is_default : Optional[bool]
            
        position : Optional[float]
            Sort position (default 0).
        
        Returns
        -------
        MarketCurrency
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/currencies/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if position is not None:
            api_params['position'] = self._normalize_value(position)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MarketCurrency)


    def markets_locales_list(
        self,
        market_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        market_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/locales'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def markets_locales_create(
        self,
        market_id: str,
        code: str,
        country: str,
        language: str,
        is_default: Optional[bool] = None,
        position: Optional[float] = None
    ) -> MarketLocale:
        """
        

        Parameters
        ----------
        market_id : str
            
        code : str
            Locale code, e.g. 'de-DE' (unique per market).
        country : str
            ISO 3166-1 alpha-2 country code.
        language : str
            ISO 639-1 language code.
        is_default : Optional[bool]
            
        position : Optional[float]
            Sort position (default 0).
        
        Returns
        -------
        MarketLocale
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/locales'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if country is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "country"')

        if language is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "language"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))

        api_params['code'] = self._normalize_value(code)
        api_params['country'] = self._normalize_value(country)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['language'] = self._normalize_value(language)
        if position is not None:
            api_params['position'] = self._normalize_value(position)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MarketLocale)


    def markets_locales_delete(
        self,
        market_id: str,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        market_id : str
            
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

        api_path = '/v1/markets/{market_id}/locales/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def markets_locales_get(
        self,
        market_id: str,
        id: str
    ) -> MarketLocale:
        """
        

        Parameters
        ----------
        market_id : str
            
        id : str
            
        
        Returns
        -------
        MarketLocale
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/locales/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MarketLocale)


    def markets_locales_update(
        self,
        market_id: str,
        id: str,
        code: Optional[str] = None,
        country: Optional[str] = None,
        is_default: Optional[bool] = None,
        language: Optional[str] = None,
        position: Optional[float] = None
    ) -> MarketLocale:
        """
        

        Parameters
        ----------
        market_id : str
            
        id : str
            
        code : Optional[str]
            Locale code, e.g. 'de-DE' (unique per market).
        country : Optional[str]
            ISO 3166-1 alpha-2 country code.
        is_default : Optional[bool]
            
        language : Optional[str]
            ISO 639-1 language code.
        position : Optional[float]
            Sort position (default 0).
        
        Returns
        -------
        MarketLocale
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/locales/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if country is not None:
            api_params['country'] = self._normalize_value(country)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if language is not None:
            api_params['language'] = self._normalize_value(language)
        if position is not None:
            api_params['position'] = self._normalize_value(position)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MarketLocale)


    def markets_tax_classes_list(
        self,
        market_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        market_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/tax_classes'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def markets_tax_classes_create(
        self,
        market_id: str,
        code: str,
        name: str,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        rate: Optional[float] = None
    ) -> MarketTaxClass:
        """
        

        Parameters
        ----------
        market_id : str
            
        code : str
            Tax class code (unique per market).
        name : str
            
        is_default : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            Localized display names ({locale: label}).
        position : Optional[float]
            Sort position (default 0).
        rate : Optional[float]
            Tax rate in percent, 0–100 (default 0).
        
        Returns
        -------
        MarketTaxClass
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/tax_classes'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))

        api_params['code'] = self._normalize_value(code)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if rate is not None:
            api_params['rate'] = self._normalize_value(rate)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MarketTaxClass)


    def markets_tax_classes_delete(
        self,
        market_id: str,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        market_id : str
            
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

        api_path = '/v1/markets/{market_id}/tax_classes/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def markets_tax_classes_get(
        self,
        market_id: str,
        id: str
    ) -> MarketTaxClass:
        """
        

        Parameters
        ----------
        market_id : str
            
        id : str
            
        
        Returns
        -------
        MarketTaxClass
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/tax_classes/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MarketTaxClass)


    def markets_tax_classes_update(
        self,
        market_id: str,
        id: str,
        code: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        rate: Optional[float] = None
    ) -> MarketTaxClass:
        """
        

        Parameters
        ----------
        market_id : str
            
        id : str
            
        code : Optional[str]
            Tax class code (unique per market).
        is_default : Optional[bool]
            
        labels : Optional[Dict[str, Any]]
            Localized display names ({locale: label}).
        name : Optional[str]
            
        position : Optional[float]
            Sort position (default 0).
        rate : Optional[float]
            Tax rate in percent, 0–100 (default 0).
        
        Returns
        -------
        MarketTaxClass
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/markets/{market_id}/tax_classes/{id}'
        api_params = {}
        if market_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "market_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{marketId}', str(self._normalize_value(market_id)))
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
        if rate is not None:
            api_params['rate'] = self._normalize_value(rate)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MarketTaxClass)

