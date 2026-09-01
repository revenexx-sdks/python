```python
from revenexx.client import Client
from revenexx.services.pages_collaboration import PagesCollaboration

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_collaboration = PagesCollaboration(client)

result = pages_collaboration.pages_editor_notifications_list(
    after = '', # optional
    mark_as_read = 'true' # optional
)
```
