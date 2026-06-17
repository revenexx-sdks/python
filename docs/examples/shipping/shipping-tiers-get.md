```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.shipping import Shipping
from revenexx_revenexx.models import ShippingRateTier

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping = Shipping(client)

result: ShippingRateTier = shipping.shipping_tiers_get(
    method_id = '',
    id = ''
)

print(result.model_dump())
```
