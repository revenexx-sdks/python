```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result: Error = shipping_methods.shipping_tiers_list(
    method_id = '',
    limit = 1, # optional
    offset = 1, # optional
    order = 'position.asc', # optional
    from_value = 10 # optional
)

print(result.model_dump())
```
