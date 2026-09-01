from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.role_catalog_response_source import RoleCatalogResponseSource

class RoleCatalogResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    permissions : Optional[List[Any]]
        The built-in permission vocabulary, one entry per grant. The authoritative, installed-app-aware list is the platform&#039;s permission ledger — this app deliberately does not duplicate it.
    roles : Optional[List[Any]]
        Every role a contact of this tenant can hold, least to most privileged.
    source : Optional[RoleCatalogResponseSource]
        &#039;tenant&#039; — the configured mapping answered. &#039;defaults&#039; — this tenant has no roles yet, or custom_roles_enabled locks the ledger, and the built-ins answered.
    """
    permissions: Optional[List[Any]] = Field(default=None, alias='permissions')
    roles: Optional[List[Any]] = Field(default=None, alias='roles')
    source: Optional[RoleCatalogResponseSource] = Field(default=None, alias='source')
