```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging
from revenexx_revenexx.models import Message

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Message = messaging.messaging_update_email(
    message_id = '',
    attachments = [], # optional
    bcc = [], # optional
    cc = [], # optional
    content = '', # optional
    draft = None, # optional
    html = None, # optional
    scheduled_at = '', # optional
    subject = '', # optional
    targets = [], # optional
    topics = [], # optional
    users = [] # optional
)

print(result.model_dump())
```
