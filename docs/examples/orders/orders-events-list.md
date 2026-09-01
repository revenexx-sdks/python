```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_events_list(
    id = '',
    id_query = '', # optional
    name = 'order.shipment.created', # optional
    actor = '', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
