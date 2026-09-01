```python
from revenexx.client import Client
from revenexx.services.shipping_carriers import ShippingCarriers
from revenexx.models import Error
from revenexx.enums import ShippingCarriersListStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_carriers = ShippingCarriers(client)

result: Error = shipping_carriers.shipping_carriers_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'position.asc', # optional
    code = 'acme-parcel', # optional
    status = ShippingCarriersListStatus.ACTIVE, # optional
    service_level = 'express' # optional
)

print(result.model_dump())
```
