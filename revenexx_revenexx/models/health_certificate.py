from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class HealthCertificate(AppwriteModel):
    """
    Health Certificate

    Attributes
    ----------
    issuerorganisation : str
        Issuer organisation
    name : str
        Certificate name
    signaturetypesn : str
        Signature type SN
    subjectsn : str
        Subject SN
    validfrom : str
        Valid from
    validto : str
        Valid to
    """
    issuerorganisation: str = Field(..., alias='issuerOrganisation')
    name: str = Field(..., alias='name')
    signaturetypesn: str = Field(..., alias='signatureTypeSN')
    subjectsn: str = Field(..., alias='subjectSN')
    validfrom: str = Field(..., alias='validFrom')
    validto: str = Field(..., alias='validTo')
