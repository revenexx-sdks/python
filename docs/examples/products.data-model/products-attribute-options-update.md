```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_attribute_options_update(
    id = '',
    attribute_id = '', # optional
    code = 'stainless_steel', # optional
    labels = {
        "de": "Edelstahl",
        "en": "Stainless steel"
    }, # optional
    position = 1, # optional
    swatch = {
        "hex": "#c0c0c0"
    } # optional
)

print(result.model_dump())
```
