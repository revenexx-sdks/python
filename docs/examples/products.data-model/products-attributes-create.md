```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_attributes_create(
    code = 'net_weight',
    type = 'select',
    config = {
        "reference_entity": "brand"
    }, # optional
    entity_ref = 'brand', # optional
    entity_type = 'product', # optional
    group_id = '', # optional
    is_filterable = True, # optional
    is_unique = True, # optional
    labels = {
        "de": "Nettogewicht",
        "en": "Net weight"
    }, # optional
    localizable = True, # optional
    position = 1, # optional
    scopable = True, # optional
    usable_in_grid = True, # optional
    validation = {
        "max_length": 64,
        "min_length": 3
    } # optional
)

print(result.model_dump())
```
