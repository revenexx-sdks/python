```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_association_types_update(
    id = '',
    code = 'cross_sell', # optional
    is_quantified = True, # optional
    is_two_way = True, # optional
    labels = {
        "de": "Querverkauf",
        "en": "Cross-sell"
    } # optional
)

print(result.model_dump())
```
