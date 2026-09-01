```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import OrderNumberRangesSeeded

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: OrderNumberRangesSeeded = orders.orders_number_ranges_defaults()

print(result.model_dump())
```
