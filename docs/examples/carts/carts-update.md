```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts
from revenexx_revenexx.models import Cart

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: Cart = carts.carts_update(
    id = '',
    channel_id = '', # optional
    currency = '', # optional
    market_id = '', # optional
    metadata = {}, # optional
    name = '' # optional
)

print(result.model_dump())
```
