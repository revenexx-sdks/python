```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.shipping import Shipping
from revenexx_revenexx.models import ShippingRateTier

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping = Shipping(client)

result: ShippingRateTier = shipping.shipping_tiers_update(
    method_id = '',
    id = '',
    from_value = None, # optional
    position = None, # optional
    price = None # optional
)

print(result.model_dump())
```
