```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import OrderReturn

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: OrderReturn = orders.orders_returns_complete(
    id = '',
    rid = '',
    resolution = '' # optional
)

print(result.model_dump())
```
