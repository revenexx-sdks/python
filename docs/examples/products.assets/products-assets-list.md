```python
from revenexx.client import Client
from revenexx.services.products_assets import ProductsAssets
from revenexx.enums import ProductsAssetsListSource

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_assets = ProductsAssets(client)

result = products_assets.products_assets_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    asset_family_id = '', # optional
    code = 'acme-4711-blk_packshot_1', # optional
    source = ProductsAssetsListSource.STORAGE, # optional
    storage_asset_id = 'ast_01J8ZQ0000000000000000', # optional
    delivery_path = 'packshots/acme-4711-blk_1.jpg', # optional
    external_url = 'https://cdn.example.com/packshots/acme-4711-blk_1.jpg', # optional
    attribute_values = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)
```
