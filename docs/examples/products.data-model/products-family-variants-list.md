```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result = products_data_model.products_family_variants_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    family_id = '', # optional
    code = 'clothing_by_colour_size', # optional
    labels = '{}', # optional
    axes = '[]', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)
```
