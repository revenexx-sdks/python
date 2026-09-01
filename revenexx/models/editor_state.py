from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class EditorState(AppwriteModel):
    """
    Everything the blökkli editor runs on, for one page in one language, materialized at the current point of the undo history. The theme adapter maps it 1:1 onto blökkli&#039;s MappedState.

    Attributes
    ----------
    currentuserisowner : Optional[bool]
        Whether the caller may write. False means every write answers 409 until `POST …/take-ownership` — so the editor should go read-only rather than let someone type into a refusal.
    droppablefieldvalues : Optional[List[Any]]
        Every entity-reference field of every block — the fields an editor drags a product or a media item into.
    editstate : Optional[Dict[str, Any]]
        The open working copy, or `null` when nobody has started editing — in which case the state shown is simply the published one.
    features : Optional[Dict[str, Any]]
        What the tenant&#039;s settings allow, so a client hides a control instead of discovering the refusal.
    fields : Optional[List[Any]]
        The block tree, flattened into one entry per (host, field) pair. This is the list the editor renders and drops into.
    ignoredanalyzeidentifiers : Optional[List[Any]]
        Analyze findings that were dismissed for this page, so the editor stops reporting them.
    langcode : Optional[str]
        The language this whole state was resolved for — the `?langcode` that was applied, or the page&#039;s source language.
    mutatedentity : Optional[Dict[str, Any]]
        The page-level field values the edit state changed, merged source-then-language — `{ &quot;title&quot;: …, &quot;slug&quot;: …, &quot;meta&quot;: … }`. Empty when nobody edited the page itself, only its blocks.
    mutatedhostoptions : Optional[Dict[str, Any]]
        The PAGE-level display options after the unpublished changes, as a flat `option key → value` map. Theme-defined.
    mutatedoptions : Optional[Dict[str, Any]]
        Every block&#039;s display options after the unpublished changes, keyed by block uuid: `{ &quot;&lt;uuid&gt;&quot;: { &quot;background&quot;: &quot;grey&quot; } }`.
    mutations : Optional[List[Any]]
        The undo/redo history, oldest first. Its length and `editState.currentIndex` are what an undo button and a history sidebar are drawn from.
    page : Optional[Dict[str, Any]]
        The page itself, with the unpublished edits already applied — so the title here is what publishing would store, not what is stored now.
    textfieldvalues : Optional[List[Any]]
        Every string field of every block, flattened. It is what the translation view and the CSV export are built on — one row per translatable string.
    translations : Optional[List[Any]]
        Every language this page exists in, so the editor can offer a language switcher that shows what is missing.
    violations : Optional[List[Any]]
        Why publishing would be refused right now. Empty means `POST …/publish` succeeds without `force`.
    """
    currentuserisowner: Optional[bool] = Field(default=None, alias='currentUserIsOwner')
    droppablefieldvalues: Optional[List[Any]] = Field(default=None, alias='droppableFieldValues')
    editstate: Optional[Dict[str, Any]] = Field(default=None, alias='editState')
    features: Optional[Dict[str, Any]] = Field(default=None, alias='features')
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
