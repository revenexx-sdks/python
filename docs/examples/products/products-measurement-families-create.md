```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import MeasurementFamilies

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: MeasurementFamilies = products.products_measurement_families_create(
    code = '',
    standard_unit = '',
    labels = {}, # optional
    units = {} # optional
)

print(result.model_dump())
```
