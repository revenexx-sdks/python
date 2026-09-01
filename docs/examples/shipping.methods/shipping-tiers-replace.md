```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods
from revenexx.models import Error
from revenexx.models import ShippingRateTierReplaceItem

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result: Error = shipping_methods.shipping_tiers_replace(
    method_id = '',
    tiers = [ShippingRateTierReplaceItem()]
)

print(result.model_dump())
```
