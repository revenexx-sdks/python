```python
from revenexx.client import Client
from revenexx.services.shipping_value_lists import ShippingValueLists

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_value_lists = ShippingValueLists(client)

result = shipping_value_lists.shipping_service_levels_list(
    limit = 1, # optional
    offset = 1 # optional
)
```
