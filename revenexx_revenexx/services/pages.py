from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.delivery_page import DeliveryPage;
from ..models.comment import Comment;
from ..models.mutation_response import MutationResponse;
from ..models.editor_state import EditorState;
from ..models.template import Template;
from ..models.library_item import LibraryItem;
from ..models.menu import Menu;
from ..models.page import Page;
from ..enums.page_status import PageStatus;

class Pages(Service):

    def __init__(self, client) -> None:
        super(Pages, self).__init__(client)

    def pages_delivery_menus(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/delivery/menus'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_delivery_page(
        self
    ) -> DeliveryPage:
        """
        

        Returns
        -------
        DeliveryPage
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/delivery/page'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=DeliveryPage)


    def pages_delivery_pages(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/delivery/pages'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_delivery_preview(
        self,
        token: str
    ) -> DeliveryPage:
        """
        

        Parameters
        ----------
        token : str
            
        
        Returns
        -------
        DeliveryPage
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/delivery/preview/{token}'
        api_params = {}
        if token is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "token"')

        api_path = api_path.replace('{token}', str(self._normalize_value(token)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=DeliveryPage)


    def pages_editor_edit_states(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/edit-states'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_notifications_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/notifications'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_notifications_mark_all_read(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
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
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/notifications/unread-count'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_translate(
        self,
        items: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : Optional[List[Dict[str, Any]]]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/translate'
        api_params = {}

        api_params['items'] = self._normalize_value(items)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_user_settings_get(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/user-settings'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_user_settings_put(
        self,
        settings: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        settings : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/user-settings'
        api_params = {}

        api_params['settings'] = self._normalize_value(settings)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_users(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
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
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_comments_create(
        self,
        page_id: str,
        body: str,
        block_uuids: Optional[List[str]] = None,
        parent_uuid: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        body : str
            
        block_uuids : Optional[List[str]]
            
        parent_uuid : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if body is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "body"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['blockUuids'] = self._normalize_value(block_uuids)
        api_params['body'] = self._normalize_value(body)
        api_params['parentUuid'] = self._normalize_value(parent_uuid)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_comments_delete(
        self,
        page_id: str,
        uuid: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        uuid : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "uuid"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def pages_editor_comments_update(
        self,
        page_id: str,
        uuid: str,
        body: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        uuid : str
            
        body : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "uuid"')

        if body is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "body"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))

        api_params['body'] = self._normalize_value(body)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_comments_resolve(
        self,
        page_id: str,
        uuid: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        uuid : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}/resolve'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "uuid"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def pages_editor_comments_toggle_task(
        self,
        page_id: str,
        uuid: str,
        task_index: float
    ) -> Comment:
        """
        

        Parameters
        ----------
        page_id : str
            
        uuid : str
            
        task_index : float
            
        
        Returns
        -------
        Comment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}/toggle-task'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "uuid"')

        if task_index is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "task_index"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))

        api_params['taskIndex'] = self._normalize_value(task_index)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Comment)


    def pages_editor_comments_unresolve(
        self,
        page_id: str,
        uuid: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        uuid : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/comments/{uuid}/unresolve'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if uuid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "uuid"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))
        api_path = api_path.replace('{uuid}', str(self._normalize_value(uuid)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def pages_editor_history(
        self,
        page_id: str,
        index: float,
        langcode: Optional[str] = None
    ) -> MutationResponse:
        """
        

        Parameters
        ----------
        page_id : str
            
        index : float
            
        langcode : Optional[str]
            
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/history'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if index is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "index"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['index'] = self._normalize_value(index)
        api_params['langcode'] = self._normalize_value(langcode)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_last_changed(
        self,
        page_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/last-changed'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_editor_mutation_status(
        self,
        page_id: str,
        enabled: bool,
        index: float,
        langcode: Optional[str] = None
    ) -> MutationResponse:
        """
        

        Parameters
        ----------
        page_id : str
            
        enabled : bool
            
        index : float
            
        langcode : Optional[str]
            
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/mutation-status'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if enabled is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "enabled"')

        if index is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "index"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['enabled'] = self._normalize_value(enabled)
        api_params['index'] = self._normalize_value(index)
        api_params['langcode'] = self._normalize_value(langcode)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_mutate(
        self,
        page_id: str,
        plugin: str,
        langcode: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None
    ) -> MutationResponse:
        """
        

        Parameters
        ----------
        page_id : str
            
        plugin : str
            Mutation plugin id (add, move, delete, duplicate, update_field_value, ...).
        langcode : Optional[str]
            
        payload : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/mutations'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if plugin is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "plugin"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['langcode'] = self._normalize_value(langcode)
        api_params['payload'] = self._normalize_value(payload)
        api_params['plugin'] = self._normalize_value(plugin)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_preview_grant(
        self,
        page_id: str,
        ttl_hours: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        ttl_hours : Optional[float]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/preview-grant'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        if ttl_hours is not None:
            api_params['ttlHours'] = self._normalize_value(ttl_hours)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_publish(
        self,
        page_id: str,
        force: Optional[bool] = None,
        label: Optional[str] = None
    ) -> MutationResponse:
        """
        

        Parameters
        ----------
        page_id : str
            
        force : Optional[bool]
            Publish despite violations.
        label : Optional[str]
            
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/publish'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['force'] = self._normalize_value(force)
        api_params['label'] = self._normalize_value(label)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_revert(
        self,
        page_id: str
    ) -> MutationResponse:
        """
        

        Parameters
        ----------
        page_id : str
            
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/revert'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_schedule(
        self,
        page_id: str,
        scheduled_at: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        scheduled_at : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/schedule'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if scheduled_at is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "scheduled_at"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['scheduledAt'] = self._normalize_value(scheduled_at)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_editor_state(
        self,
        page_id: str
    ) -> EditorState:
        """
        

        Parameters
        ----------
        page_id : str
            
        
        Returns
        -------
        EditorState
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/state'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=EditorState)


    def pages_editor_take_ownership(
        self,
        page_id: str
    ) -> MutationResponse:
        """
        

        Parameters
        ----------
        page_id : str
            
        
        Returns
        -------
        MutationResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/take-ownership'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=MutationResponse)


    def pages_editor_templates_create(
        self,
        page_id: str,
        label: str,
        uuids: List[str],
        description: Optional[str] = None,
        field_name: Optional[str] = None,
        is_default: Optional[bool] = None,
        page_bundle: Optional[str] = None
    ) -> Template:
        """
        

        Parameters
        ----------
        page_id : str
            
        label : str
            
        uuids : List[str]
            
        description : Optional[str]
            
        field_name : Optional[str]
            
        is_default : Optional[bool]
            
        page_bundle : Optional[str]
            
        
        Returns
        -------
        Template
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/templates'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        if label is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "label"')

        if uuids is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "uuids"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))

        api_params['description'] = self._normalize_value(description)
        api_params['fieldName'] = self._normalize_value(field_name)
        api_params['isDefault'] = self._normalize_value(is_default)
        api_params['label'] = self._normalize_value(label)
        api_params['pageBundle'] = self._normalize_value(page_bundle)
        api_params['uuids'] = self._normalize_value(uuids)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Template)


    def pages_editor_unschedule(
        self,
        page_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        page_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/editor/{page_id}/unschedule'
        api_params = {}
        if page_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "page_id"')

        api_path = api_path.replace('{pageId}', str(self._normalize_value(page_id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def pages_library_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/library'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_library_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/library/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def pages_library_get(
        self,
        id: str
    ) -> LibraryItem:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        LibraryItem
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/library/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LibraryItem)


    def pages_library_update(
        self,
        id: str,
        bundle: Optional[str] = None,
        label: Optional[str] = None,
        tree: Optional[Dict[str, Any]] = None
    ) -> LibraryItem:
        """
        

        Parameters
        ----------
        id : str
            
        bundle : Optional[str]
            
        label : Optional[str]
            
        tree : Optional[Dict[str, Any]]
            Serialized block tree ({ bundle, props, props_i18n, options, children }).
        
        Returns
        -------
        LibraryItem
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/library/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if bundle is not None:
            api_params['bundle'] = self._normalize_value(bundle)
        if label is not None:
            api_params['label'] = self._normalize_value(label)
        if tree is not None:
            api_params['tree'] = self._normalize_value(tree)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=LibraryItem)


    def pages_menus_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/menus'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_menus_upsert(
        self,
        label: str,
        menu_key: str,
        items: Optional[List[Dict[str, Any]]] = None
    ) -> Menu:
        """
        

        Parameters
        ----------
        label : str
            
        menu_key : str
            Stable menu identifier, e.g. "main", "footer", "account".
        items : Optional[List[Dict[str, Any]]]
            Ordered menu entries ({ label, to?, items? }).
        
        Returns
        -------
        Menu
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/menus'
        api_params = {}
        if label is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "label"')

        if menu_key is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "menu_key"')


        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['label'] = self._normalize_value(label)
        api_params['menuKey'] = self._normalize_value(menu_key)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Menu)


    def pages_menus_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/menus/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def pages_menus_get(
        self,
        id: str
    ) -> Menu:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Menu
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/menus/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Menu)


    def pages_menus_update(
        self,
        id: str,
        items: Optional[List[Dict[str, Any]]] = None,
        label: Optional[str] = None
    ) -> Menu:
        """
        

        Parameters
        ----------
        id : str
            
        items : Optional[List[Dict[str, Any]]]
            
        label : Optional[str]
            
        
        Returns
        -------
        Menu
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/menus/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if items is not None:
            api_params['items'] = self._normalize_value(items)
        if label is not None:
            api_params['label'] = self._normalize_value(label)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Menu)


    def pages_pages_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/pages'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_pages_create(
        self,
        title: str,
        bundle: Optional[str] = None,
        host_options: Optional[Dict[str, Any]] = None,
        meta: Optional[Dict[str, Any]] = None,
        slug: Optional[str] = None,
        source_language: Optional[str] = None
    ) -> Page:
        """
        

        Parameters
        ----------
        title : str
            
        bundle : Optional[str]
            
        host_options : Optional[Dict[str, Any]]
            
        meta : Optional[Dict[str, Any]]
            
        slug : Optional[str]
            
        source_language : Optional[str]
            
        
        Returns
        -------
        Page
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/pages'
        api_params = {}
        if title is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "title"')


        api_params['bundle'] = self._normalize_value(bundle)
        api_params['hostOptions'] = self._normalize_value(host_options)
        api_params['meta'] = self._normalize_value(meta)
        api_params['slug'] = self._normalize_value(slug)
        api_params['sourceLanguage'] = self._normalize_value(source_language)
        api_params['title'] = self._normalize_value(title)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Page)


    def pages_pages_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def pages_pages_get(
        self,
        id: str
    ) -> Page:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Page
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Page)


    def pages_pages_update(
        self,
        id: str,
        bundle: Optional[str] = None,
        meta: Optional[Dict[str, Any]] = None,
        slug: Optional[str] = None,
        status: Optional[PageStatus] = None,
        title: Optional[str] = None
    ) -> Page:
        """
        

        Parameters
        ----------
        id : str
            
        bundle : Optional[str]
            
        meta : Optional[Dict[str, Any]]
            
        slug : Optional[str]
            
        status : Optional[PageStatus]
            
        title : Optional[str]
            
        
        Returns
        -------
        Page
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if bundle is not None:
            api_params['bundle'] = self._normalize_value(bundle)
        if meta is not None:
            api_params['meta'] = self._normalize_value(meta)
        api_params['slug'] = self._normalize_value(slug)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if title is not None:
            api_params['title'] = self._normalize_value(title)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Page)


    def pages_pages_revisions(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/pages/{id}/revisions'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_seed(
        self,
        menus: Optional[List[Dict[str, Any]]] = None,
        pages: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        menus : Optional[List[Dict[str, Any]]]
            
        pages : Optional[List[Dict[str, Any]]]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/seed'
        api_params = {}

        api_params['menus'] = self._normalize_value(menus)
        api_params['pages'] = self._normalize_value(pages)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def pages_templates_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/templates'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def pages_templates_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def pages_templates_get(
        self,
        id: str
    ) -> Template:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Template
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Template)


    def pages_templates_update(
        self,
        id: str,
        description: Optional[str] = None,
        field_name: Optional[str] = None,
        is_default: Optional[bool] = None,
        label: Optional[str] = None,
        page_bundle: Optional[str] = None,
        tree: Optional[List[Dict[str, Any]]] = None
    ) -> Template:
        """
        

        Parameters
        ----------
        id : str
            
        description : Optional[str]
            
        field_name : Optional[str]
            
        is_default : Optional[bool]
            
        label : Optional[str]
            
        page_bundle : Optional[str]
            
        tree : Optional[List[Dict[str, Any]]]
            Serialized block trees ({ bundle, props, props_i18n, options, children }).
        
        Returns
        -------
        Template
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/pages/templates/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['description'] = self._normalize_value(description)
        api_params['field_name'] = self._normalize_value(field_name)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        if label is not None:
            api_params['label'] = self._normalize_value(label)
        api_params['page_bundle'] = self._normalize_value(page_bundle)
        if tree is not None:
            api_params['tree'] = self._normalize_value(tree)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Template)

