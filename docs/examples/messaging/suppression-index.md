```python
from revenexx.client import Client
from revenexx.services.messaging import Messaging
from revenexx.models import Error
from revenexx.enums import Scope
from revenexx.enums import Reason

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Error = messaging.suppression_index(
    channel = '', # optional
    scope = Scope.ALL, # optional
    reason = Reason.HARD_BOUNCE, # optional
    address = '', # optional
    limit = 1 # optional
)

print(result.model_dump())
```
