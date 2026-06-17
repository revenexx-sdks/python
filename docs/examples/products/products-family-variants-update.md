```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import FamilyVariants

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: FamilyVariants = products.products_family_variants_update(
    id = '',
    axes = {}, # optional
    code = '', # optional
    family_id = '', # optional
    labels = {} # optional
)

print(result.model_dump())
```
