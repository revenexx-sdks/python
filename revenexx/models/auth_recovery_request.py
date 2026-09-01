from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthRecoveryRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        Who to send the recovery mail to. An address nobody holds is not distinguished here — do not build an account-existence check on the answer.
    url : str
        Where the mailed link points. `userId`, `secret` and `expire` are appended as query parameters — the first two are what the confirm call takes. Same shape the identity service&#039;s own mail used, so a storefront that already handles that link needs no change.
    """
    email: str = Field(..., alias='email')
    url: str = Field(..., alias='url')
