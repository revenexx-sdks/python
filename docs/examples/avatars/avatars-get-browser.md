```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.avatars import Avatars
from revenexx_revenexx.enums import Code

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

avatars = Avatars(client)

result = avatars.avatars_get_browser(
    code = Code.AA,
    width = None, # optional
    height = None, # optional
    quality = None # optional
)
```
