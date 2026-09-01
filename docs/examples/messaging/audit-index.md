```python
from revenexx.client import Client
from revenexx.services.messaging import Messaging
from revenexx.models import Error
from revenexx.enums import ResourceType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Error = messaging.audit_index(
    resource_type = ResourceType.TEMPLATE, # optional
    resource_id = '', # optional
    subject = '', # optional
    limit = 1 # optional
)

print(result.model_dump())
```
