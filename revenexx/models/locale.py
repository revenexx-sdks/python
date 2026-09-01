from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Locale(AppwriteModel):
    """
    Locale

    Attributes
    ----------
    continent : str
        Continent name. This field support localization.
    continentcode : str
        Continent code. A two character continent code &quot;AF&quot; for Africa, &quot;AN&quot; for Antarctica, &quot;AS&quot; for Asia, &quot;EU&quot; for Europe, &quot;NA&quot; for North America, &quot;OC&quot; for Oceania, and &quot;SA&quot; for South America.
    country : str
        Country name. This field support localization.
    countrycode : str
        Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format
    currency : str
        Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format
    eu : bool
        True if country is part of the European Union.
    ip : str
        User IP address.
    """
    continent: str = Field(..., alias='continent')
    continentcode: str = Field(..., alias='continentCode')
    country: str = Field(..., alias='country')
    countrycode: str = Field(..., alias='countryCode')
    currency: str = Field(..., alias='currency')
    eu: bool = Field(..., alias='eu')
    ip: str = Field(..., alias='ip')
