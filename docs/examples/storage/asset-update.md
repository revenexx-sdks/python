```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.storage import Storage
from revenexx_revenexx.enums import Visibility

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

storage = Storage(client)

result = storage.asset_update(
    id = '',
    alt_text = '', # optional
    description = '', # optional
    display_name = '', # optional
    folder_id = '', # optional
    name = '', # optional
    tags = [], # optional
    visibility = Visibility.PUBLIC # optional
)
```
