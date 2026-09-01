```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_asset_families_update(
    id = '',
    code = 'packshots', # optional
    labels = {
        "de": "Packshots",
        "en": "Packshots"
    }, # optional
    naming_convention = {
        "allowed_extensions": [
            "jpg",
            "png"
        ],
        "pattern": "{sku}_{index}",
        "source": "sku"
    } # optional
)

print(result.model_dump())
```
