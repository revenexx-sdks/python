```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import Assets

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: Assets = products.products_assets_update(
    id = '',
    asset_family_id = '', # optional
    attribute_values = {}, # optional
    code = '', # optional
    media_uuid = '' # optional
)

print(result.model_dump())
```
