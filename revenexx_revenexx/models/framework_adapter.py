from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FrameworkAdapter(AppwriteModel):
    """
    Framework Adapter

    Attributes
    ----------
    buildcommand : str
        Default command to build site into output directory.
    fallbackfile : str
        Name of fallback file to use instead of 404 page. If null, Appwrite 404 page will be displayed.
    installcommand : str
        Default command to download dependencies.
    key : str
        Adapter key.
    outputdirectory : str
        Default output directory of build.
    """
    buildcommand: str = Field(..., alias='buildCommand')
    fallbackfile: str = Field(..., alias='fallbackFile')
    installcommand: str = Field(..., alias='installCommand')
    key: str = Field(..., alias='key')
    outputdirectory: str = Field(..., alias='outputDirectory')
