```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods
from revenexx.models import Error
from revenexx.enums import PricingType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result: Error = shipping_methods.shipping_methods_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'position.asc', # optional
    code = 'express', # optional
    enabled = True, # optional
    pricing_type = PricingType.MATRIX, # optional
    carrier_id = '8a4d1c7e-2b93-4f61-b0d2-6c5a9e3f1a44', # optional
    carrier = 'acme-parcel', # optional
    tax_class = 'reduced' # optional
)

print(result.model_dump())
```
