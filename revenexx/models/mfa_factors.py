from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MfaFactors(AppwriteModel):
    """
    MFAFactors

    Attributes
    ----------
    email : bool
        Can email be used for MFA challenge for this account.
    phone : bool
        Can phone (SMS) be used for MFA challenge for this account.
    recoverycode : bool
        Can recovery code be used for MFA challenge for this account.
    totp : bool
        Can TOTP be used for MFA challenge for this account.
    """
    email: bool = Field(..., alias='email')
    phone: bool = Field(..., alias='phone')
    recoverycode: bool = Field(..., alias='recoveryCode')
    totp: bool = Field(..., alias='totp')
