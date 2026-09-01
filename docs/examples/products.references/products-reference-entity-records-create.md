```python
from revenexx.client import Client
from revenexx.services.products_references import ProductsReferences
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_references = ProductsReferences(client)

result: Error = products_references.products_reference_entity_records_create(
    code = 'acme_tools',
    reference_entity_id = '',
    attribute_values = {
        "common": {
            "country": "DE",
            "founded": 1946
        },
        "locale_specific": {
            "de_DE": {
                "description": "Werkzeughersteller aus S\u00fcddeutschland."
            }
        }
    }, # optional
    labels = {
        "de": "Acme Tools",
        "en": "Acme Tools"
    } # optional
)

print(result.model_dump())
```
