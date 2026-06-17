from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.message_list import MessageList;
from ..models.message import Message;
from ..enums.priority import Priority;
from ..models.log_list import LogList;
from ..models.target_list import TargetList;
from ..models.provider_list import ProviderList;
from ..models.provider import Provider;
from ..models.topic_list import TopicList;
from ..models.topic import Topic;
from ..models.subscriber_list import SubscriberList;
from ..models.subscriber import Subscriber;

class Messaging(Service):

    def __init__(self, client) -> None:
        super(Messaging, self).__init__(client)

    def messaging_list_messages(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> MessageList:
        """
        Get a list of all messages from the current Revenexx project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: scheduledAt, deliveredAt, deliveredTotal, status, description, providerType
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        MessageList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MessageList)


    def messaging_create_email(
        self,
        content: str,
        message_id: str,
        subject: str,
        attachments: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        cc: Optional[List[str]] = None,
        draft: Optional[bool] = None,
        html: Optional[bool] = None,
        scheduled_at: Optional[str] = None,
        targets: Optional[List[str]] = None,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None
    ) -> Message:
        """
        Create a new email message.

        Parameters
        ----------
        content : str
            Email Content.
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        subject : str
            Email Subject.
        attachments : Optional[List[str]]
            Array of compound ID strings of bucket IDs and file IDs to be attached to the email. They should be formatted as <BUCKET_ID>:<FILE_ID>.
        bcc : Optional[List[str]]
            Array of target IDs to be added as BCC.
        cc : Optional[List[str]]
            Array of target IDs to be added as CC.
        draft : Optional[bool]
            Is message a draft
        html : Optional[bool]
            Is content of type HTML
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        targets : Optional[List[str]]
            List of Targets IDs.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        
        Returns
        -------
        Message
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/email'
        api_params = {}
        if content is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "content"')

        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        if subject is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "subject"')


        if attachments is not None:
            api_params['attachments'] = self._normalize_value(attachments)
        if bcc is not None:
            api_params['bcc'] = self._normalize_value(bcc)
        if cc is not None:
            api_params['cc'] = self._normalize_value(cc)
        api_params['content'] = self._normalize_value(content)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        if html is not None:
            api_params['html'] = self._normalize_value(html)
        api_params['messageId'] = self._normalize_value(message_id)
        if scheduled_at is not None:
            api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        api_params['subject'] = self._normalize_value(subject)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def messaging_update_email(
        self,
        message_id: str,
        attachments: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        cc: Optional[List[str]] = None,
        content: Optional[str] = None,
        draft: Optional[bool] = None,
        html: Optional[bool] = None,
        scheduled_at: Optional[str] = None,
        subject: Optional[str] = None,
        targets: Optional[List[str]] = None,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None
    ) -> Message:
        """
        Update an email message by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        attachments : Optional[List[str]]
            Array of compound ID strings of bucket IDs and file IDs to be attached to the email. They should be formatted as <BUCKET_ID>:<FILE_ID>.
        bcc : Optional[List[str]]
            Array of target IDs to be added as BCC.
        cc : Optional[List[str]]
            Array of target IDs to be added as CC.
        content : Optional[str]
            Email Content.
        draft : Optional[bool]
            Is message a draft
        html : Optional[bool]
            Is content of type HTML
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        subject : Optional[str]
            Email Subject.
        targets : Optional[List[str]]
            List of Targets IDs.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        
        Returns
        -------
        Message
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/email/{messageId}'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        if attachments is not None:
            api_params['attachments'] = self._normalize_value(attachments)
        if bcc is not None:
            api_params['bcc'] = self._normalize_value(bcc)
        if cc is not None:
            api_params['cc'] = self._normalize_value(cc)
        if content is not None:
            api_params['content'] = self._normalize_value(content)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        if html is not None:
            api_params['html'] = self._normalize_value(html)
        if scheduled_at is not None:
            api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        if subject is not None:
            api_params['subject'] = self._normalize_value(subject)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def messaging_create_push(
        self,
        message_id: str,
        action: Optional[str] = None,
        badge: Optional[float] = None,
        body: Optional[str] = None,
        color: Optional[str] = None,
        content_available: Optional[bool] = None,
        critical: Optional[bool] = None,
        data: Optional[Dict[str, Any]] = None,
        draft: Optional[bool] = None,
        icon: Optional[str] = None,
        image: Optional[str] = None,
        priority: Optional[Priority] = None,
        scheduled_at: Optional[str] = None,
        sound: Optional[str] = None,
        tag: Optional[str] = None,
        targets: Optional[List[str]] = None,
        title: Optional[str] = None,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None
    ) -> Message:
        """
        Create a new push notification.

        Parameters
        ----------
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        action : Optional[str]
            Action for push notification.
        badge : Optional[float]
            Badge for push notification. Available only for iOS Platform.
        body : Optional[str]
            Body for push notification.
        color : Optional[str]
            Color for push notification. Available only for Android Platform.
        content_available : Optional[bool]
            If set to true, the notification will be delivered in the background. Available only for iOS Platform.
        critical : Optional[bool]
            If set to true, the notification will be marked as critical. This requires the app to have the critical notification entitlement. Available only for iOS Platform.
        data : Optional[Dict[str, Any]]
            Additional key-value pair data for push notification.
        draft : Optional[bool]
            Is message a draft
        icon : Optional[str]
            Icon for push notification. Available only for Android and Web Platform.
        image : Optional[str]
            Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage. It should be formatted as <BUCKET_ID>:<FILE_ID>.
        priority : Optional[Priority]
            Set the notification priority. "normal" will consider device state and may not deliver notifications immediately. "high" will always attempt to immediately deliver the notification.
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        sound : Optional[str]
            Sound for push notification. Available only for Android and iOS Platform.
        tag : Optional[str]
            Tag for push notification. Available only for Android Platform.
        targets : Optional[List[str]]
            List of Targets IDs.
        title : Optional[str]
            Title for push notification.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        
        Returns
        -------
        Message
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/push'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')


        if action is not None:
            api_params['action'] = self._normalize_value(action)
        if badge is not None:
            api_params['badge'] = self._normalize_value(badge)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if color is not None:
            api_params['color'] = self._normalize_value(color)
        if content_available is not None:
            api_params['contentAvailable'] = self._normalize_value(content_available)
        if critical is not None:
            api_params['critical'] = self._normalize_value(critical)
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        if icon is not None:
            api_params['icon'] = self._normalize_value(icon)
        if image is not None:
            api_params['image'] = self._normalize_value(image)
        api_params['messageId'] = self._normalize_value(message_id)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if scheduled_at is not None:
            api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        if sound is not None:
            api_params['sound'] = self._normalize_value(sound)
        if tag is not None:
            api_params['tag'] = self._normalize_value(tag)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def messaging_update_push(
        self,
        message_id: str,
        action: Optional[str] = None,
        badge: Optional[float] = None,
        body: Optional[str] = None,
        color: Optional[str] = None,
        content_available: Optional[bool] = None,
        critical: Optional[bool] = None,
        data: Optional[Dict[str, Any]] = None,
        draft: Optional[bool] = None,
        icon: Optional[str] = None,
        image: Optional[str] = None,
        priority: Optional[Priority] = None,
        scheduled_at: Optional[str] = None,
        sound: Optional[str] = None,
        tag: Optional[str] = None,
        targets: Optional[List[str]] = None,
        title: Optional[str] = None,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None
    ) -> Message:
        """
        Update a push notification by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        action : Optional[str]
            Action for push notification.
        badge : Optional[float]
            Badge for push notification. Available only for iOS platforms.
        body : Optional[str]
            Body for push notification.
        color : Optional[str]
            Color for push notification. Available only for Android platforms.
        content_available : Optional[bool]
            If set to true, the notification will be delivered in the background. Available only for iOS Platform.
        critical : Optional[bool]
            If set to true, the notification will be marked as critical. This requires the app to have the critical notification entitlement. Available only for iOS Platform.
        data : Optional[Dict[str, Any]]
            Additional Data for push notification.
        draft : Optional[bool]
            Is message a draft
        icon : Optional[str]
            Icon for push notification. Available only for Android and Web platforms.
        image : Optional[str]
            Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage. It should be formatted as <BUCKET_ID>:<FILE_ID>.
        priority : Optional[Priority]
            Set the notification priority. "normal" will consider device battery state and may send notifications later. "high" will always attempt to immediately deliver the notification.
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        sound : Optional[str]
            Sound for push notification. Available only for Android and iOS platforms.
        tag : Optional[str]
            Tag for push notification. Available only for Android platforms.
        targets : Optional[List[str]]
            List of Targets IDs.
        title : Optional[str]
            Title for push notification.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        
        Returns
        -------
        Message
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/push/{messageId}'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        if action is not None:
            api_params['action'] = self._normalize_value(action)
        if badge is not None:
            api_params['badge'] = self._normalize_value(badge)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if color is not None:
            api_params['color'] = self._normalize_value(color)
        if content_available is not None:
            api_params['contentAvailable'] = self._normalize_value(content_available)
        if critical is not None:
            api_params['critical'] = self._normalize_value(critical)
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        if icon is not None:
            api_params['icon'] = self._normalize_value(icon)
        if image is not None:
            api_params['image'] = self._normalize_value(image)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if scheduled_at is not None:
            api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        if sound is not None:
            api_params['sound'] = self._normalize_value(sound)
        if tag is not None:
            api_params['tag'] = self._normalize_value(tag)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def messaging_delete(
        self,
        message_id: str
    ) -> Dict[str, Any]:
        """
        Delete a message. If the message is not a draft or scheduled, but has been sent, this will not recall the message.

        Parameters
        ----------
        message_id : str
            Message ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/{messageId}'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def messaging_get_message(
        self,
        message_id: str
    ) -> Message:
        """
        Get a message by its unique ID.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        
        Returns
        -------
        Message
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/{messageId}'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Message)


    def messaging_list_message_logs(
        self,
        message_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> LogList:
        """
        Get the message activity logs listed by its unique ID.

        Parameters
        ----------
        message_id : str
            Message ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/{messageId}/logs'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def messaging_list_targets(
        self,
        message_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> TargetList:
        """
        Get a list of the targets associated with a message.

        Parameters
        ----------
        message_id : str
            Message ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, providerId, identifier, providerType
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        TargetList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/messages/{messageId}/targets'
        api_params = {}
        if message_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TargetList)


    def messaging_list_providers(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> ProviderList:
        """
        Get a list of all providers from the current Revenexx project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ProviderList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ProviderList)


    def messaging_create_mailgun_provider(
        self,
        name: str,
        provider_id: str,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        enabled: Optional[bool] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        is_eu_region: Optional[bool] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> Provider:
        """
        Create a new Mailgun provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        api_key : Optional[str]
            Mailgun API Key.
        domain : Optional[str]
            Mailgun Domain.
        enabled : Optional[bool]
            Set as enabled.
        from_email : Optional[str]
            Sender email address.
        from_name : Optional[str]
            Sender Name.
        is_eu_region : Optional[bool]
            Set as EU region.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email. Reply to email must have reply to name as well.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name. Reply to name must have reply to email as well.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/mailgun'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if is_eu_region is not None:
            api_params['isEuRegion'] = self._normalize_value(is_eu_region)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_mailgun_provider(
        self,
        provider_id: str,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        enabled: Optional[bool] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        is_eu_region: Optional[bool] = None,
        name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> Provider:
        """
        Update a Mailgun provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        api_key : Optional[str]
            Mailgun API Key.
        domain : Optional[str]
            Mailgun Domain.
        enabled : Optional[bool]
            Set as enabled.
        from_email : Optional[str]
            Sender email address.
        from_name : Optional[str]
            Sender Name.
        is_eu_region : Optional[bool]
            Set as EU region.
        name : Optional[str]
            Provider name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/mailgun/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if is_eu_region is not None:
            api_params['isEuRegion'] = self._normalize_value(is_eu_region)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_msg91_provider(
        self,
        name: str,
        provider_id: str,
        auth_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        sender_id: Optional[str] = None,
        template_id: Optional[str] = None
    ) -> Provider:
        """
        Create a new MSG91 provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        auth_key : Optional[str]
            Msg91 auth key.
        enabled : Optional[bool]
            Set as enabled.
        sender_id : Optional[str]
            Msg91 sender ID.
        template_id : Optional[str]
            Msg91 template ID
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/msg91'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if auth_key is not None:
            api_params['authKey'] = self._normalize_value(auth_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)
        if sender_id is not None:
            api_params['senderId'] = self._normalize_value(sender_id)
        if template_id is not None:
            api_params['templateId'] = self._normalize_value(template_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_msg91_provider(
        self,
        provider_id: str,
        auth_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        sender_id: Optional[str] = None,
        template_id: Optional[str] = None
    ) -> Provider:
        """
        Update a MSG91 provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        auth_key : Optional[str]
            Msg91 auth key.
        enabled : Optional[bool]
            Set as enabled.
        name : Optional[str]
            Provider name.
        sender_id : Optional[str]
            Msg91 sender ID.
        template_id : Optional[str]
            Msg91 template ID.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/msg91/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if auth_key is not None:
            api_params['authKey'] = self._normalize_value(auth_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if sender_id is not None:
            api_params['senderId'] = self._normalize_value(sender_id)
        if template_id is not None:
            api_params['templateId'] = self._normalize_value(template_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_resend_provider(
        self,
        name: str,
        provider_id: str,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> Provider:
        """
        Create a new Resend provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        api_key : Optional[str]
            Resend API key.
        enabled : Optional[bool]
            Set as enabled.
        from_email : Optional[str]
            Sender email address.
        from_name : Optional[str]
            Sender Name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/resend'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_resend_provider(
        self,
        provider_id: str,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> Provider:
        """
        Update a Resend provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        api_key : Optional[str]
            Resend API key.
        enabled : Optional[bool]
            Set as enabled.
        from_email : Optional[str]
            Sender email address.
        from_name : Optional[str]
            Sender Name.
        name : Optional[str]
            Provider name.
        reply_to_email : Optional[str]
            Email set in the Reply To field for the mail. Default value is Sender Email.
        reply_to_name : Optional[str]
            Name set in the Reply To field for the mail. Default value is Sender Name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/resend/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_sendgrid_provider(
        self,
        name: str,
        provider_id: str,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> Provider:
        """
        Create a new Sendgrid provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        api_key : Optional[str]
            Sendgrid API key.
        enabled : Optional[bool]
            Set as enabled.
        from_email : Optional[str]
            Sender email address.
        from_name : Optional[str]
            Sender Name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/sendgrid'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_sendgrid_provider(
        self,
        provider_id: str,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> Provider:
        """
        Update a Sendgrid provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        api_key : Optional[str]
            Sendgrid API key.
        enabled : Optional[bool]
            Set as enabled.
        from_email : Optional[str]
            Sender email address.
        from_name : Optional[str]
            Sender Name.
        name : Optional[str]
            Provider name.
        reply_to_email : Optional[str]
            Email set in the Reply To field for the mail. Default value is Sender Email.
        reply_to_name : Optional[str]
            Name set in the Reply To field for the mail. Default value is Sender Name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/sendgrid/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_telesign_provider(
        self,
        name: str,
        provider_id: str,
        api_key: Optional[str] = None,
        customer_id: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None
    ) -> Provider:
        """
        Create a new Telesign provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        api_key : Optional[str]
            Telesign API key.
        customer_id : Optional[str]
            Telesign customer ID.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/telesign'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if customer_id is not None:
            api_params['customerId'] = self._normalize_value(customer_id)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_telesign_provider(
        self,
        provider_id: str,
        api_key: Optional[str] = None,
        customer_id: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None,
        name: Optional[str] = None
    ) -> Provider:
        """
        Update a Telesign provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        api_key : Optional[str]
            Telesign API key.
        customer_id : Optional[str]
            Telesign customer ID.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender number.
        name : Optional[str]
            Provider name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/telesign/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if customer_id is not None:
            api_params['customerId'] = self._normalize_value(customer_id)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_textmagic_provider(
        self,
        name: str,
        provider_id: str,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None,
        username: Optional[str] = None
    ) -> Provider:
        """
        Create a new Textmagic provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        api_key : Optional[str]
            Textmagic apiKey.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        username : Optional[str]
            Textmagic username.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/textmagic'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)
        if username is not None:
            api_params['username'] = self._normalize_value(username)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_textmagic_provider(
        self,
        provider_id: str,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None,
        name: Optional[str] = None,
        username: Optional[str] = None
    ) -> Provider:
        """
        Update a Textmagic provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        api_key : Optional[str]
            Textmagic apiKey.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender number.
        name : Optional[str]
            Provider name.
        username : Optional[str]
            Textmagic username.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/textmagic/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if username is not None:
            api_params['username'] = self._normalize_value(username)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_twilio_provider(
        self,
        name: str,
        provider_id: str,
        account_sid: Optional[str] = None,
        auth_token: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None
    ) -> Provider:
        """
        Create a new Twilio provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        account_sid : Optional[str]
            Twilio account secret ID.
        auth_token : Optional[str]
            Twilio authentication token.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/twilio'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if account_sid is not None:
            api_params['accountSid'] = self._normalize_value(account_sid)
        if auth_token is not None:
            api_params['authToken'] = self._normalize_value(auth_token)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_twilio_provider(
        self,
        provider_id: str,
        account_sid: Optional[str] = None,
        auth_token: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None,
        name: Optional[str] = None
    ) -> Provider:
        """
        Update a Twilio provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        account_sid : Optional[str]
            Twilio account secret ID.
        auth_token : Optional[str]
            Twilio authentication token.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender number.
        name : Optional[str]
            Provider name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/twilio/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if account_sid is not None:
            api_params['accountSid'] = self._normalize_value(account_sid)
        if auth_token is not None:
            api_params['authToken'] = self._normalize_value(auth_token)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_create_vonage_provider(
        self,
        name: str,
        provider_id: str,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None
    ) -> Provider:
        """
        Create a new Vonage provider.

        Parameters
        ----------
        name : str
            Provider name.
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        api_key : Optional[str]
            Vonage API key.
        api_secret : Optional[str]
            Vonage API secret.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/vonage'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')


        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if api_secret is not None:
            api_params['apiSecret'] = self._normalize_value(api_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        api_params['name'] = self._normalize_value(name)
        api_params['providerId'] = self._normalize_value(provider_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_update_vonage_provider(
        self,
        provider_id: str,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        enabled: Optional[bool] = None,
        xfrom: Optional[str] = None,
        name: Optional[str] = None
    ) -> Provider:
        """
        Update a Vonage provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        api_key : Optional[str]
            Vonage API key.
        api_secret : Optional[str]
            Vonage API secret.
        enabled : Optional[bool]
            Set as enabled.
        xfrom : Optional[str]
            Sender number.
        name : Optional[str]
            Provider name.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/vonage/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if api_secret is not None:
            api_params['apiSecret'] = self._normalize_value(api_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_delete_provider(
        self,
        provider_id: str
    ) -> Dict[str, Any]:
        """
        Delete a provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def messaging_get_provider(
        self,
        provider_id: str
    ) -> Provider:
        """
        Get a provider by its unique ID.
        

        Parameters
        ----------
        provider_id : str
            Provider ID.
        
        Returns
        -------
        Provider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/{providerId}'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Provider)


    def messaging_list_provider_logs(
        self,
        provider_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> LogList:
        """
        Get the provider activity logs listed by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/providers/{providerId}/logs'
        api_params = {}
        if provider_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def messaging_list_subscriber_logs(
        self,
        subscriber_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> LogList:
        """
        Get the subscriber activity logs listed by its unique ID.

        Parameters
        ----------
        subscriber_id : str
            Subscriber ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/subscribers/{subscriberId}/logs'
        api_params = {}
        if subscriber_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{subscriberId}', str(self._normalize_value(subscriber_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def messaging_list_topics(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> TopicList:
        """
        Get a list of all topics from the current Revenexx project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, description, emailTotal, smsTotal, pushTotal
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        TopicList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TopicList)


    def messaging_create_topic(
        self,
        name: str,
        topic_id: str,
        subscribe: Optional[List[str]] = None
    ) -> Topic:
        """
        Create a new topic.

        Parameters
        ----------
        name : str
            Topic Name.
        topic_id : str
            Topic ID. Choose a custom Topic ID or a new Topic ID.
        subscribe : Optional[List[str]]
            An array of role strings with subscribe permission. By default all users are granted with any subscribe permission. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        
        Returns
        -------
        Topic
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics'
        api_params = {}
        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')

        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')


        api_params['name'] = self._normalize_value(name)
        if subscribe is not None:
            api_params['subscribe'] = self._normalize_value(subscribe)
        api_params['topicId'] = self._normalize_value(topic_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Topic)


    def messaging_delete_topic(
        self,
        topic_id: str
    ) -> Dict[str, Any]:
        """
        Delete a topic by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def messaging_get_topic(
        self,
        topic_id: str
    ) -> Topic:
        """
        Get a topic by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID.
        
        Returns
        -------
        Topic
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Topic)


    def messaging_update_topic(
        self,
        topic_id: str,
        name: Optional[str] = None,
        subscribe: Optional[List[str]] = None
    ) -> Topic:
        """
        Update a topic by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID.
        name : Optional[str]
            Topic Name.
        subscribe : Optional[List[str]]
            An array of role strings with subscribe permission. By default all users are granted with any subscribe permission. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        
        Returns
        -------
        Topic
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if subscribe is not None:
            api_params['subscribe'] = self._normalize_value(subscribe)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Topic)


    def messaging_list_topic_logs(
        self,
        topic_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> LogList:
        """
        Get the topic activity logs listed by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}/logs'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def messaging_list_subscribers(
        self,
        topic_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> SubscriberList:
        """
        Get a list of all subscribers from the current Revenexx project.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        SubscriberList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}/subscribers'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SubscriberList)


    def messaging_create_subscriber(
        self,
        topic_id: str,
        subscriber_id: str,
        target_id: str
    ) -> Subscriber:
        """
        Create a new subscriber.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID to subscribe to.
        subscriber_id : str
            Subscriber ID. Choose a custom Subscriber ID or a new Subscriber ID.
        target_id : str
            Target ID. The target ID to link to the specified Topic ID.
        
        Returns
        -------
        Subscriber
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}/subscribers'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "subscriber_id"')

        if target_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "target_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        api_params['subscriberId'] = self._normalize_value(subscriber_id)
        api_params['targetId'] = self._normalize_value(target_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Subscriber)


    def messaging_delete_subscriber(
        self,
        topic_id: str,
        subscriber_id: str
    ) -> Dict[str, Any]:
        """
        Delete a subscriber by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        subscriber_id : str
            Subscriber ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}/subscribers/{subscriberId}'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))
        api_path = api_path.replace('{subscriberId}', str(self._normalize_value(subscriber_id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def messaging_get_subscriber(
        self,
        topic_id: str,
        subscriber_id: str
    ) -> Subscriber:
        """
        Get a subscriber by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        subscriber_id : str
            Subscriber ID.
        
        Returns
        -------
        Subscriber
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/messaging/topics/{topicId}/subscribers/{subscriberId}'
        api_params = {}
        if topic_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))
        api_path = api_path.replace('{subscriberId}', str(self._normalize_value(subscriber_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Subscriber)

