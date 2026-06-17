```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging
from revenexx_revenexx.models import Message
from revenexx_revenexx.enums import Priority

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Message = messaging.messaging_create_push(
    message_id = '',
    action = '', # optional
    badge = None, # optional
    body = '', # optional
    color = '', # optional
    content_available = None, # optional
    critical = None, # optional
    data = {}, # optional
    draft = None, # optional
    icon = '', # optional
    image = '', # optional
    priority = Priority.NORMAL, # optional
    scheduled_at = '', # optional
    sound = '', # optional
    tag = '', # optional
    targets = [], # optional
    title = '', # optional
    topics = [], # optional
    users = [] # optional
)

print(result.model_dump())
```
