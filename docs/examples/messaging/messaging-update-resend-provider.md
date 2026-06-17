```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging
from revenexx_revenexx.models import Provider

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Provider = messaging.messaging_update_resend_provider(
    provider_id = '',
    api_key = '', # optional
    enabled = None, # optional
    from_email = '', # optional
    from_name = '', # optional
    name = '', # optional
    reply_to_email = '', # optional
    reply_to_name = '' # optional
)

print(result.model_dump())
```
