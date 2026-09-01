from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.page_comment_list import PageCommentList;
from ..models.error import Error;

class PagesCollaboration(Service):

    def __init__(self, client) -> None:
        super(PagesCollaboration, self).__init__(client)

    def pages_editor_notifications_list(
        self,
        after: Optional[str] = None,
        mark_as_read: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The caller's own notifications, newest first, 20 at a time. Paged by an opaque cursor rather than by offset, so new arrivals never shift a page under the reader. It is also the one read in this app that writes: `?markAsRead=true` flags the notifications on the page it just returned as read, which is how a feed that has been looked at empties its badge without a second call — leave it off and reading changes nothing.

        Parameters
        ----------
        after : Optional[str]
            Continue after this cursor — pass back the `cursor` from the previous page. Omit for the first page. It encodes the last item's timestamp and id, so it is stable while new notifications arrive.
        mark_as_read : Optional[str]
            Send the literal `true` to mark the notifications ON THIS PAGE read as a side effect of reading them. Any other value, including `1` and `false`, is accepted and leaves them unread.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/notifications'
        api_params = {}

        if after is not None:
            api_params['after'] = self._normalize_value(after)
        if mark_as_read is not None:
            api_params['markAsRead'] = self._normalize_value(mark_as_read)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_notifications_mark_all_read(
        self
    ) -> Dict[str, Any]:
        """
        Empties the badge in one call. Every unread notification of the CURRENT user is flagged read — the user is the one the request's context token names and there is no body with which to name another. Nothing is deleted: `GET /pages/editor/notifications` still returns the same feed, just with `read` set. The answer is the new unread count, so a client can set the badge straight from it without a second read.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/notifications/mark-all-read'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def pages_editor_notifications_unread_count(
        self
    ) -> Dict[str, Any]:
        """
        The cheap poll behind the badge.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/notifications/unread-count'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_users(
        self
    ) -> Dict[str, Any]:
        """
        What the @mention picker is filled from. When the identity service cannot be reached this degrades to the authors who have already commented on this tenant's pages rather than answering an error — a mention list that is short is more useful than one that is missing.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/users'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_comments_list(
        self,
        page_id: str
    ) -> PageCommentList:
        """
        Every comment on the page in one flat list, oldest first, roots and replies together and resolved threads included — there is no filter and no paging, because the editor nests and filters them itself from `parentUuid` and pins each root to its blocks with `blockUuids`. Comments hang off the PAGE, not off a revision or an edit state, so publishing and reverting leave them standing; that is what makes them usable as a review trail across several rounds of edits.

        Parameters
        ----------
        page_id : str
            The page being edited.
        
        Returns
        -------
        PageCommentList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PageCommentList)


    def pages_editor_comments_create(
        self,
        page_id: str,
        body: str,
        block_uuids: Optional[List[str]] = None,
        parent_uuid: Optional[str] = None
    ) -> PageCommentList:
        """
        The same route writes both kinds, and which one you get is decided by the body: `blockUuids` starts a new thread pinned to those blocks, `parentUuid` hangs a reply under an existing root. Everyone named with an @mention in the body is notified, and on a reply so is everybody already in the thread — the actor never notifies themselves.

        Parameters
        ----------
        page_id : str
            The page being edited.
        body : str
            The comment, as editor HTML. `<span data-type="mention" data-id="USER_ID">` is what this app reads to decide whom to notify; `<li data-type="taskItem" data-checked="false">` makes a checkbox the toggle-task route can flip.
        block_uuids : Optional[List[str]]
            The blocks this thread is about, so the editor can draw a marker next to them. Leave empty for a comment about the page as a whole.
        parent_uuid : Optional[str]
            The root comment this replies to. Omit for a new thread — only roots can be resolved.
        
        Returns
        -------
        PageCommentList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if body is None:
            raise RevenexxException('Missing required parameter: "body"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))

        api_params['blockUuids'] = self._normalize_value(block_uuids)
        api_params['body'] = self._normalize_value(body)
        api_params['parentUuid'] = self._normalize_value(parent_uuid)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PageCommentList)


    def pages_editor_comments_delete(
        self,
        page_id: str,
        uuid: str
    ) -> PageCommentList:
        """
        A hard delete, and deleting a root takes its replies with it.

        Parameters
        ----------
        page_id : str
            The page being edited.
        uuid : str
            The comment id — the `uuid` of a `PageCommentItem`, not a row id of any other shape.
        
        Returns
        -------
        PageCommentList
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxException('Missing required parameter: "uuid"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=PageCommentList)


    def pages_editor_comments_update(
        self,
        page_id: str,
        uuid: str,
        body: str
    ) -> Error:
        """
        Rewrites what a comment says, and only its author may — a comment carries an `author_id` and anybody else is refused with 403. Only the body moves: what the comment is pinned to, whether the thread is resolved and who wrote it are all fixed when it is created. Rewriting a body does NOT re-run the @mention notifications, so mentioning somebody new by editing will not reach them. Answers the page's whole comment list rather than the one row, so a client can re-render from the response.

        Parameters
        ----------
        page_id : str
            The page being edited.
        uuid : str
            The comment id — the `uuid` of a `PageCommentItem`, not a row id of any other shape.
        body : str
            The comment, as editor HTML. Replaces the old body completely.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxException('Missing required parameter: "uuid"')

        if body is None:
            raise RevenexxException('Missing required parameter: "body"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))

        api_params['body'] = self._normalize_value(body)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_comments_resolve(
        self,
        page_id: str,
        uuid: str
    ) -> Error:
        """
        Marks a thread handled, so the editor stops surfacing it on the block it is pinned to. Only a ROOT can be resolved — resolved-ness is a property of the thread and not of a message in it, so pointing this at a reply is refused with 400 rather than quietly resolving its parent. Nothing is deleted, nobody is notified, and the thread stays in the list; `.../unresolve` is the way back. Answers the page's whole comment list.

        Parameters
        ----------
        page_id : str
            The page being edited.
        uuid : str
            The comment id — the `uuid` of a `PageCommentItem`, not a row id of any other shape.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}/resolve'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxException('Missing required parameter: "uuid"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_comments_toggle_task(
        self,
        page_id: str,
        uuid: str,
        task_index: float
    ) -> Error:
        """
        A comment body may carry a task list. This flips one checkbox by rewriting the body's markup, and answers the single comment rather than the whole list. A `taskIndex` that names no checkbox is refused and nothing is written — the comment's `updated_at` is the editor's "edited" marker, so a call that changes nothing must not move it.

        Parameters
        ----------
        page_id : str
            The page being edited.
        uuid : str
            The comment id — the `uuid` of a `PageCommentItem`, not a row id of any other shape.
        task_index : float
            The task item to toggle, counted in document order from 0. A comment with fewer tasks than that answers 400, and so does anything that is not a whole number at or above 0.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}/toggle-task'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxException('Missing required parameter: "uuid"')

        if task_index is None:
            raise RevenexxException('Missing required parameter: "task_index"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))

        api_params['taskIndex'] = self._normalize_value(task_index)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def pages_editor_comments_unresolve(
        self,
        page_id: str,
        uuid: str
    ) -> Error:
        """
        Clears the resolved flag and puts the thread back in front of whoever is editing — the mirror of `.../resolve` in every respect, including that only a root can be reopened and that a reply answers 400. A thread that was already open is accepted and stays open. Answers the page's whole comment list.

        Parameters
        ----------
        page_id : str
            The page being edited.
        uuid : str
            The comment id — the `uuid` of a `PageCommentItem`, not a row id of any other shape.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}/unresolve'
        api_params = {}
        if page_id is None:
            raise RevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxException('Missing required parameter: "uuid"')

        api_path = api_path.replace('{page_id}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

