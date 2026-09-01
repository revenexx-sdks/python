from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class IoProfileFormat(AppwriteModel):
    """
    Profile source/sink format. `bmecat` is profile-only — the ad-hoc
`/io/imports` and `/io/exports` endpoints do not accept it.

    """
    pass
