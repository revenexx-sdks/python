```python
from revenexx.client import Client
from revenexx.services.messaging import Messaging
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Error = messaging.push_subscription_index(
    subscriber_id = ''
)

print(result.model_dump())
```
