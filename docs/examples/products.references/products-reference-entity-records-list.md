```python
from revenexx.client import Client
from revenexx.services.products_references import ProductsReferences

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_references = ProductsReferences(client)

result = products_references.products_reference_entity_records_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    reference_entity_id = '', # optional
    code = 'acme_tools', # optional
    labels = '{}', # optional
    attribute_values = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)
```
