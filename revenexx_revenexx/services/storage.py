from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.visibility import Visibility;

class Storage(Service):

    def __init__(self, client) -> None:
        super(Storage, self).__init__(client)

    def asset_index(
        self,
        search: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        search : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/assets'
        api_params = {}

        if search is not None:
            api_params['search'] = self._normalize_value(search)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def asset_store(
        self,
        file: str,
        alt_text: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        folder_id: Optional[str] = None,
        keep_archive: Optional[bool] = None,
        tags: Optional[List[str]] = None,
        unpack: Optional[bool] = None,
        visibility: Optional[Visibility] = None,
        on_progress = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        file : str
            
        alt_text : Optional[str]
            
        description : Optional[str]
            
        display_name : Optional[str]
            
        folder_id : Optional[str]
            
        keep_archive : Optional[bool]
            
        tags : Optional[List[str]]
            
        unpack : Optional[bool]
            Archives only: unpack the members after upload (see AssetController).
        visibility : Optional[Visibility]
            
                on_progress : callable, optional
            Optional callback for upload progress
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/assets'
        api_params = {}
        if file is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "file"')


        api_params['alt_text'] = self._normalize_value(alt_text)
        api_params['description'] = self._normalize_value(description)
        api_params['display_name'] = self._normalize_value(display_name)
        api_params['file'] = self._normalize_value(file)
        api_params['folder_id'] = self._normalize_value(folder_id)
        api_params['keep_archive'] = self._normalize_value(str(keep_archive).lower() if type(keep_archive) is bool else keep_archive)
        api_params['tags'] = self._normalize_value(tags)
        api_params['unpack'] = self._normalize_value(str(unpack).lower() if type(unpack) is bool else unpack)
        api_params['visibility'] = self._normalize_value(visibility)


        upload_id = ''

        response = self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

        return response


    def asset_bulk(
        self,
        folder_id: Optional[str] = None,
        visibility: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        folder_id : Optional[str]
            
        visibility : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/assets/bulk'
        api_params = {}

        if folder_id is not None:
            api_params['folder_id'] = self._normalize_value(folder_id)
        if visibility is not None:
            api_params['visibility'] = self._normalize_value(visibility)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def asset_destroy(
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

        api_path = '/v1/storage/assets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def asset_show(
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

        api_path = '/v1/storage/assets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def asset_update(
        self,
        id: str,
        alt_text: Optional[str] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        folder_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        visibility: Optional[Visibility] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        alt_text : Optional[str]
            
        description : Optional[str]
            
        display_name : Optional[str]
            
        folder_id : Optional[str]
            
        name : Optional[str]
            
        tags : Optional[List[str]]
            
        visibility : Optional[Visibility]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/assets/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['alt_text'] = self._normalize_value(alt_text)
        api_params['description'] = self._normalize_value(description)
        api_params['display_name'] = self._normalize_value(display_name)
        api_params['folder_id'] = self._normalize_value(folder_id)
        api_params['name'] = self._normalize_value(name)
        api_params['tags'] = self._normalize_value(tags)
        api_params['visibility'] = self._normalize_value(visibility)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def asset_download(
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

        api_path = '/v1/storage/assets/{id}/download'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def asset_permanent(
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

        api_path = '/v1/storage/assets/{id}/permanent'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def asset_reprocess(
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

        api_path = '/v1/storage/assets/{id}/reprocess'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def asset_restore(
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

        api_path = '/v1/storage/assets/{id}/restore'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def asset_sign(
        self,
        id: str,
        ttl_seconds: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        ttl_seconds : Optional[float]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/assets/{id}/sign'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['ttl_seconds'] = self._normalize_value(ttl_seconds)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def asset_unpack(
        self,
        id: str,
        keep_archive: Optional[bool] = None,
        target_folder_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        keep_archive : Optional[bool]
            
        target_folder_id : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/assets/{id}/unpack'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['keep_archive'] = self._normalize_value(keep_archive)
        api_params['target_folder_id'] = self._normalize_value(target_folder_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def folder_index(
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

        api_path = '/v1/storage/folders'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def folder_store(
        self,
        name: str,
        parent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        name : str
            
        parent_id : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/folders'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['name'] = self._normalize_value(name)
        api_params['parent_id'] = self._normalize_value(parent_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def folder_destroy(
        self,
        id: str,
        recursive: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        recursive : Optional[bool]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/folders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if recursive is not None:
            api_params['recursive'] = self._normalize_value(recursive)

        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def folder_show(
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

        api_path = '/v1/storage/folders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def folder_update(
        self,
        id: str,
        name: Optional[str] = None,
        parent_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        name : Optional[str]
            
        parent_id : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/folders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['name'] = self._normalize_value(name)
        api_params['parent_id'] = self._normalize_value(parent_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def sync_rule_index(
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

        api_path = '/v1/storage/sftp/rules'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def sync_rule_store(
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

        api_path = '/v1/storage/sftp/rules'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def sync_rule_destroy(
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

        api_path = '/v1/storage/sftp/rules/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def sync_rule_show(
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

        api_path = '/v1/storage/sftp/rules/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def sync_rule_update(
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

        api_path = '/v1/storage/sftp/rules/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('patch', api_path, {
        }, api_params)

        return response


    def sync_rule_run(
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

        api_path = '/v1/storage/sftp/rules/{id}/run'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def sync_rule_run_protocol(
        self,
        id: str,
        run_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        run_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/sftp/rules/{id}/runs/{runId}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if run_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "run_id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{runId}', str(self._normalize_value(run_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def sync_rule_history(
        self,
        rule_id: Optional[str] = None,
        xfrom: Optional[str] = None,
        to: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        rule_id : Optional[str]
            
        xfrom : Optional[str]
            
        to : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/storage/sftp/sync-history'
        api_params = {}

        if rule_id is not None:
            api_params['rule_id'] = self._normalize_value(rule_id)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if to is not None:
            api_params['to'] = self._normalize_value(to)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def tenant_stats(
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

        api_path = '/v1/storage/tenant/stats'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def tenant_usage(
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

        api_path = '/v1/storage/tenant/usage'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response

