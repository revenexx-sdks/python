```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result = shipping_methods.shipping_methods_defaults()
```
