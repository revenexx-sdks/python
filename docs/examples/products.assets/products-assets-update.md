```python
from revenexx.client import Client
from revenexx.services.products_assets import ProductsAssets
from revenexx.models import Error
from revenexx.enums import AssetsSource

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_assets = ProductsAssets(client)

result: Error = products_assets.products_assets_update(
    id = '',
    asset_family_id = '', # optional
    attribute_values = {
        "common": {
            "copyright": "\u00a9 Acme Tools",
            "expires_on": "2028-12-31"
        },
        "locale_specific": {
            "de_DE": {
                "alt_text": "Akku-Bohrschrauber, freigestellt"
            }
        }
    }, # optional
    code = 'acme-4711-blk_packshot_1', # optional
    delivery_path = 'packshots/acme-4711-blk_1.jpg', # optional
    external_url = 'https://cdn.example.com/packshots/acme-4711-blk_1.jpg', # optional
    source = AssetsSource.STORAGE, # optional
    storage_asset_id = 'ast_01J8ZQ0000000000000000' # optional
)

print(result.model_dump())
```
