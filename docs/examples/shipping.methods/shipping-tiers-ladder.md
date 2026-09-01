```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result: Error = shipping_methods.shipping_tiers_ladder(
    method_id = '',
    base_price = 4.9,
    step = 5,
    to_value = 30,
    from_value = 0, # optional
    replace = True, # optional
    step_price = 2 # optional
)

print(result.model_dump())
```
