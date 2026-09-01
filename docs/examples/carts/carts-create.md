```python
from revenexx.client import Client
from revenexx.services.carts import Carts
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: Error = carts.carts_create(
    channel_id = '', # optional
    contact_id = '', # optional
    currency = 'EUR', # optional
    is_current = True, # optional
    metadata = {
        "campaign": "spring-catalogue",
        "locale": "de-DE",
        "source": "storefront"
    }, # optional
    name = 'Weekly order', # optional
    session_key = 'a1b2c3d4e5f6' # optional
)

print(result.model_dump())
```
