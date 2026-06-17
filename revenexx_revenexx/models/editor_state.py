from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class EditorState(AppwriteModel):
    """
    The blökkli adapter state: page, translations, edit state + mutation log, materialized field lists, mutated options/entity values, text field values, droppable field values and violations.

    Attributes
    ----------
    currentuserisowner : Optional[bool]
        Typed model field.
    droppablefieldvalues : Optional[List[Any]]
        Typed model field.
    editstate : Optional[Dict[str, Any]]
        Typed model field.
    fields : Optional[List[Any]]
        Typed model field.
    ignoredanalyzeidentifiers : Optional[List[Any]]
        Typed model field.
    langcode : Optional[str]
        Typed model field.
    mutatedentity : Optional[Dict[str, Any]]
        Typed model field.
    mutatedhostoptions : Optional[Dict[str, Any]]
        Typed model field.
    mutatedoptions : Optional[Dict[str, Any]]
        Typed model field.
    mutations : Optional[List[Any]]
        Typed model field.
    page : Optional[Dict[str, Any]]
        Typed model field.
    textfieldvalues : Optional[List[Any]]
        Typed model field.
    translations : Optional[List[Any]]
        Typed model field.
    violations : Optional[List[Any]]
        Typed model field.
    """
    currentuserisowner: Optional[bool] = Field(default=None, alias='currentUserIsOwner')
    droppablefieldvalues: Optional[List[Any]] = Field(default=None, alias='droppableFieldValues')
    editstate: Optional[Dict[str, Any]] = Field(default=None, alias='editState')
    fields: Optional[List[Any]] = Field(default=None, alias='fields')
    ignoredanalyzeidentifiers: Optional[List[Any]] = Field(default=None, alias='ignoredAnalyzeIdentifiers')
    langcode: Optional[str] = Field(default=None, alias='langcode')
    mutatedentity: Optional[Dict[str, Any]] = Field(default=None, alias='mutatedEntity')
    mutatedhostoptions: Optional[Dict[str, Any]] = Field(default=None, alias='mutatedHostOptions')
    mutatedoptions: Optional[Dict[str, Any]] = Field(default=None, alias='mutatedOptions')
    mutations: Optional[List[Any]] = Field(default=None, alias='mutations')
    page: Optional[Dict[str, Any]] = Field(default=None, alias='page')
    textfieldvalues: Optional[List[Any]] = Field(default=None, alias='textFieldValues')
    translations: Optional[List[Any]] = Field(default=None, alias='translations')
    violations: Optional[List[Any]] = Field(default=None, alias='violations')
