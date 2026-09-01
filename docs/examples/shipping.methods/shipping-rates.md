```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result: Error = shipping_methods.shipping_rates(
    at = '2026-01-01T12:00:00Z', # optional
    attributes = {
        "volume_litres": 48
    }, # optional
    country = 'DE', # optional
    currency = 'EUR', # optional
    market_id = '3f2b6d10-7c41-4c0a-9a35-2f5b8e0d9c11', # optional
    order_value = 129.9, # optional
    order_value_gross = 129.9, # optional
    order_value_net = 109.16, # optional
    quantity = 3, # optional
    weight = 12.5, # optional
    weight_unit = 'kg' # optional
)

print(result.model_dump())
```
