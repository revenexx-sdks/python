```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging
from revenexx_revenexx.models import Subscriber

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Subscriber = messaging.messaging_get_subscriber(
    topic_id = '',
    subscriber_id = ''
)

print(result.model_dump())
```
