```python
from revenexx.client import Client
from revenexx.services.carts import Carts
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: Error = carts.carts_update(
    id = '',
    channel_id = '', # optional
    currency = 'EUR', # optional
    metadata = {
        "campaign": "spring-catalogue",
        "locale": "de-DE",
        "source": "storefront"
    }, # optional
    name = 'Weekly order' # optional
)

print(result.model_dump())
```
