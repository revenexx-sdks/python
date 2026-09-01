```python
from revenexx.client import Client
from revenexx.services.carts_items import CartsItems
from revenexx.models import Error
from revenexx.enums import CartItemType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_items = CartsItems(client)

result: Error = carts_items.carts_items_list(
    cart_id = '',
    id = '', # optional
    type = CartItemType.PRODUCT, # optional
    product_id = '', # optional
    sku = 'BOLT-M8-30', # optional
    name = 'Hex bolt M8', # optional
    quantity = 100, # optional
    unit = 'pcs', # optional
    unit_price = 0.12, # optional
    currency = 'EUR', # optional
    tax_rate = 19, # optional
    line_total = 12, # optional
    position = 0, # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
