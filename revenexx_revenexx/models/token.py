from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Token(AppwriteModel):
    """
    Token

    Attributes
    ----------
    createdat : str
        Token creation date in ISO 8601 format.
    id : str
        Token ID.
    expire : str
        Token expiration date in ISO 8601 format.
    phrase : str
        Security phrase of a token. Empty if security phrase was not requested when creating a token. It includes randomly generated phrase which is also sent in the external resource such as email.
    secret : str
        Token secret key. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    userid : str
        User ID.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    expire: str = Field(..., alias='expire')
    phrase: str = Field(..., alias='phrase')
    secret: str = Field(..., alias='secret')
    userid: str = Field(..., alias='userId')
