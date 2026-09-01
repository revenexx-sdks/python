```python
from revenexx.client import Client
from revenexx.services.products_references import ProductsReferences
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_references = ProductsReferences(client)

result: Error = products_references.products_reference_entities_create(
    code = 'brand',
    image = 'reference-entities/brand.svg', # optional
    labels = {
        "de": "Marke",
        "en": "Brand"
    } # optional
)

print(result.model_dump())
```
