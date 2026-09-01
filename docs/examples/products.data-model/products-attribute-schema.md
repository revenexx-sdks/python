```python
from revenexx.client import Client
from revenexx.services.products_data_model import ProductsDataModel
from revenexx.models import Error
from revenexx.enums import EntityType
from revenexx.enums import Kind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_data_model = ProductsDataModel(client)

result: Error = products_data_model.products_attribute_schema(
    family_id = '', # optional
    family_code = '', # optional
    entity_type = EntityType.PRODUCT, # optional
    entity_ref = 'brand', # optional
    locale = 'de_DE', # optional
    channel = 'b2b', # optional
    kind = Kind.SIMPLE # optional
)

print(result.model_dump())
```
