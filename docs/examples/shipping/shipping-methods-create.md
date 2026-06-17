```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.shipping import Shipping
from revenexx_revenexx.models import ShippingMethod
from revenexx_revenexx.enums import ShippingMethodMatrixBasis
from revenexx_revenexx.enums import ShippingMethodPricingType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping = Shipping(client)

result: ShippingMethod = shipping.shipping_methods_create(
    code = '',
    name = '',
    carrier = '', # optional
    countries = [], # optional
    currency = '', # optional
    description = '', # optional
    enabled = None, # optional
    eta_days_max = None, # optional
    eta_days_min = None, # optional
    free_above = None, # optional
    labels = {}, # optional
    matrix_attribute = '', # optional
    matrix_basis = ShippingMethodMatrixBasis.WEIGHT, # optional
    metadata = {}, # optional
    position = None, # optional
    price = None, # optional
    pricing_type = ShippingMethodPricingType.FIXED # optional
)

print(result.model_dump())
```
