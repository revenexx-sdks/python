```python
from revenexx.client import Client
from revenexx.services.pages import Pages
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Error = pages.pages_pages_create(
    title = 'About us',
    bundle = 'standard', # optional
    host_options = {}, # optional
    meta = {}, # optional
    slug = 'about-us', # optional
    source_language = 'de' # optional
)

print(result.model_dump())
```
