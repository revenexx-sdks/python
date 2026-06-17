from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .template_function import TemplateFunction

class TemplateFunctionList(AppwriteModel):
    """
    Function Templates List

    Attributes
    ----------
    templates : List[TemplateFunction]
        List of templates.
    total : float
        Total number of templates that matched your query.
    """
    templates: List[TemplateFunction] = Field(..., alias='templates')
    total: float = Field(..., alias='total')
