from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.page_status import PageStatus

class Page(AppwriteModel):
    """
    One addressable page of the storefront: its metadata and publish pointer. Its CONTENT is not here — blocks live behind the editor and delivery routes.

    Attributes
    ----------
    analyze_ignored : Optional[List[Any]]
        Identifiers of findings the blökkli analyze feature was told to stop reporting for this page. Written by the `set_ignored_analyze` mutation and carried through publish, so dismissing a finding survives the next edit.
    bundle : Optional[str]
        The page TYPE, e.g. `standard` or a landing-page type the theme defines. It decides which fields the editor offers and which template the theme renders; the value set belongs to the active theme, not to this app.
    created_at : Optional[str]
        When the page was created.
    created_by : Optional[str]
        The user id that created the page.
    deleted_at : Optional[str]
        The tombstone. A soft-deleted page is never listed, never delivered and answers 404 — and it drops out of the unique slug index at once, so deleting a page frees its slug immediately.
    host_options : Optional[Dict[str, Any]]
        Page-level blökkli display options, as a flat `option key → value` map — the options that belong to the PAGE rather than to a block (background, width, whether the header is shown). The keys are defined by the theme; this app stores whatever the `update_host_options` mutation set.
    id : Optional[str]
        The page id. Every editor and delivery route addresses a page by it, and it never changes — publishing replaces a page&#039;s blocks, never the page.
    meta : Optional[Dict[str, Any]]
        The page&#039;s free-form metadata bag — SEO fields, social preview data, whatever the theme asks the editor for. Nothing in this app reads a key of it: it is stored, versioned into revisions and handed back to the renderer untouched, so the theme owns its shape.
    published_revision_id : Optional[str]
        The revision the storefront is currently serving. `null` means nothing has ever been published, and delivery answers 404 for the page even when `status` says `published`.
    slug : Optional[str]
        The path segment the storefront routes this page under, without a leading slash. Unique per tenant among live pages, and `null` for a page that is only ever reached by id. `GET /pages/delivery/page?slug=` matches it first and the translations second.
    source_language : Optional[str]
        The language the page was authored in. It is the fallback for every field a translation leaves empty, so a page never renders as a hole.
    status : Optional[PageStatus]
        Where the page sits in the editorial lifecycle. Only `published` is ever delivered, and only together with a `published_revision_id`.
    title : Optional[str]
        The page title as an editor typed it, in the page&#039;s source language. Publishing overwrites it with the title the edit state carries, so this is always the last published (or last saved) wording.
    updated_at : Optional[str]
        When the page last changed. The default sort of `GET /pages/pages` is this column descending, because &quot;what did we touch last&quot; is the question an editorial list is opened with.
    updated_by : Optional[str]
        The user id that last changed the page — set by an update, a soft delete and by publishing.
    """
    analyze_ignored: Optional[List[Any]] = Field(default=None, alias='analyze_ignored')
    bundle: Optional[str] = Field(default=None, alias='bundle')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    host_options: Optional[Dict[str, Any]] = Field(default=None, alias='host_options')
    id: Optional[str] = Field(default=None, alias='id')
    meta: Optional[Dict[str, Any]] = Field(default=None, alias='meta')
    published_revision_id: Optional[str] = Field(default=None, alias='published_revision_id')
    slug: Optional[str] = Field(default=None, alias='slug')
    source_language: Optional[str] = Field(default=None, alias='source_language')
    status: Optional[PageStatus] = Field(default=None, alias='status')
    title: Optional[str] = Field(default=None, alias='title')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    updated_by: Optional[str] = Field(default=None, alias='updated_by')
