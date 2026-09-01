```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_family_attributes_create(
    attribute_id = '',
    family_id = '',
    is_required = True, # optional
    position = 1, # optional
    required_channels = [
        "shop",
        "b2b"
    ] # optional
)

print(result.model_dump())
```
