```python
from revenexx.client import Client
from revenexx.services.shipping_carriers import ShippingCarriers

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_carriers = ShippingCarriers(client)

result = shipping_carriers.shipping_carriers_catalog()
```
