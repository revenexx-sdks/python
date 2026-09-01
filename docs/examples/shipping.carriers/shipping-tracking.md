```python
from revenexx.client import Client
from revenexx.services.shipping_carriers import ShippingCarriers
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_carriers = ShippingCarriers(client)

result: Error = shipping_carriers.shipping_tracking(
    carrier = 'acme-parcel',
    country = 'DE', # optional
    postal_code = '12345', # optional
    tracking_code = 'ACME000000001DE' # optional
)

print(result.model_dump())
```
