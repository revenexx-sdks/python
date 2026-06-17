```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import Order

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Order = orders.orders_update(
    id = '',
    billing_address = {}, # optional
    buyer = {}, # optional
    customer_order_number = '', # optional
    metadata = {}, # optional
    shipping_address = {}, # optional
    user_data = {} # optional
)

print(result.model_dump())
```
