from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AlgoArgon2(AppwriteModel):
    """
    AlgoArgon2

    Attributes
    ----------
    memorycost : float
        Memory used to compute hash.
    threads : float
        Number of threads used to compute hash.
    timecost : float
        Amount of time consumed to compute hash
    type : str
        Algo type.
    """
    memorycost: float = Field(..., alias='memoryCost')
    threads: float = Field(..., alias='threads')
    timecost: float = Field(..., alias='timeCost')
    type: str = Field(..., alias='type')
