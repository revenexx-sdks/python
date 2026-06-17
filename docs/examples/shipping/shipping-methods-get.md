```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.shipping import Shipping
from revenexx_revenexx.models import ShippingMethod

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping = Shipping(client)

result: ShippingMethod = shipping.shipping_methods_get(
    id = ''
)

print(result.model_dump())
```
