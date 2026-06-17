```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.shipping import Shipping

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping = Shipping(client)

result = shipping.shipping_rates(
    attributes = {}, # optional
    country = '', # optional
    currency = '', # optional
    market_id = '', # optional
    order_value = None, # optional
    quantity = None, # optional
    weight = None # optional
)
```
