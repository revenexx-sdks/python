```python
from revenexx.client import Client
from revenexx.services.pages_delivery import PagesDelivery

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_delivery = PagesDelivery(client)

result = pages_delivery.pages_delivery_pages(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    bundle = 'standard' # optional
)
```
