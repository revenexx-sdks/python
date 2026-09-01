```python
from revenexx.client import Client
from revenexx.services.avatars import Avatars

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

avatars = Avatars(client)

result = avatars.avatars_get_initials(
    name = 'Ada Lovelace', # optional
    width = 1, # optional
    height = 1, # optional
    background = '1a73e8' # optional
)
```
