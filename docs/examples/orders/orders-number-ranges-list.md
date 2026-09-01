```python
from revenexx.client import Client
from revenexx.services.orders import Orders

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result = orders.orders_number_ranges_list(
    id = '', # optional
    code = 'order', # optional
    prefix = 'ORD-', # optional
    suffix = '', # optional
    padding = 6, # optional
    counter = 123, # optional
    step = 1, # optional
    position_step = 10, # optional
    channel_id = '', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc' # optional
)
```
