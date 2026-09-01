```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error
from revenexx.models import OrderCancelPosition

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_items_cancel(
    id = '',
    positions = [OrderCancelPosition()],
    cancelled_by = 'service-desk', # optional
    reason = 'Out of stock, customer agreed' # optional
)

print(result.model_dump())
```
