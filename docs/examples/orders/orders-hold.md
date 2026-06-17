```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import Order

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Order = orders.orders_hold(
    id = '',
    reason = '' # optional
)

print(result.model_dump())
```
