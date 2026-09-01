```python
from revenexx.client import Client
from revenexx.services.pages import Pages

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result = pages.pages_library_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    bundles = 'hero,teaser', # optional
    text = 'hero' # optional
)
```
