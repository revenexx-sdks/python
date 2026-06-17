```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages
from revenexx_revenexx.models import Page

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Page = pages.pages_pages_create(
    title = '',
    bundle = '', # optional
    host_options = {}, # optional
    meta = {}, # optional
    slug = '', # optional
    source_language = '' # optional
)

print(result.model_dump())
```
