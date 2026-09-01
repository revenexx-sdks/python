```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error
from revenexx.enums import OrderReturnRefusal

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_returns_reject(
    id = '',
    rid = '',
    reason = 'Returned outside the agreed window', # optional
    resolution = OrderReturnRefusal.WEAR_AND_TEAR # optional
)

print(result.model_dump())
```
