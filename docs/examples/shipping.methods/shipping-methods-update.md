```python
from revenexx.client import Client
from revenexx.services.shipping_methods import ShippingMethods
from revenexx.models import Error
from revenexx.enums import ShippingMethodMatrixBasis
from revenexx.enums import ShippingMethodPricingType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_methods = ShippingMethods(client)

result: Error = shipping_methods.shipping_methods_update(
    id = '',
    carrier = 'acme-parcel', # optional
    carrier_id = '8a4d1c7e-2b93-4f61-b0d2-6c5a9e3f1a44', # optional
    code = 'express', # optional
    countries = ["DE","AT","CH"], # optional
    currency = 'EUR', # optional
    description = 'Delivered by the next working day when ordered before the cut-off.', # optional
    enabled = True, # optional
    eta_days_max = 1, # optional
    eta_days_min = 1, # optional
    free_above = 100, # optional
    labels = {
        "de": "Expressversand",
        "en": "Express delivery"
    }, # optional
    matrix_attribute = 'volume_litres', # optional
    matrix_basis = ShippingMethodMatrixBasis.WEIGHT, # optional
    metadata = {
        "erp_key": "SHIP-EXPRESS",
        "printer": "label-2"
    }, # optional
    name = 'Express delivery', # optional
    position = 1, # optional
    price = 9.9, # optional
    pricing_type = ShippingMethodPricingType.FIXED, # optional
    quote_above = 31.5, # optional
    tax_class = 'reduced' # optional
)

print(result.model_dump())
```
