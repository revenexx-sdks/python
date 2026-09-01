```python
from revenexx.client import Client
from revenexx.services.products import Products
from revenexx.models import Error
from revenexx.enums import ProductsKind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: Error = products.products_create(
    sku = 'ACME-4711-BLK',
    attribute_values = {
        "channel_locale_specific": {
            "b2b": {
                "de_DE": {
                    "description": "Staffelpreise auf Anfrage."
                }
            }
        },
        "channel_specific": {
            "b2b": {
                "minimum_order_quantity": 6
            }
        },
        "common": {
            "colour": "black",
            "manufacturer_aid": "4711-BLK",
            "net_weight": 2.4
        },
        "locale_specific": {
            "de_DE": {
                "description": "B\u00fcrstenloser Motor, 2 Akkus im Set.",
                "name": "Akku-Bohrschrauber 18V"
            },
            "en_GB": {
                "name": "18V cordless drill"
            }
        }
    }, # optional
    completeness = {
        "computed_at": "2026-01-01T12:00:00Z",
        "filled": 9,
        "missing": [
            "net_weight",
            "packaging_unit",
            "safety_datasheet"
        ],
        "ratio": 0.75,
        "required": 12
    }, # optional
    deleted_at = '2026-01-01T12:00:00Z', # optional
    enabled = True, # optional
    family_id = '', # optional
    family_variant_id = '', # optional
    kind = ProductsKind.SIMPLE, # optional
    parent_id = '', # optional
    quantified_associations = {
        "PRODUCT_SET": {
            "product_models": [],
            "products": [
                {
                    "identifier": "ACME-4711-CASTER",
                    "quantity": 4
                }
            ]
        }
    }, # optional
    tax_class = 'standard' # optional
)

print(result.model_dump())
```
