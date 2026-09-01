```python
from revenexx.client import Client
from revenexx.services.carts_items import CartsItems
from revenexx.models import Error
from revenexx.enums import CartItemType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_items = CartsItems(client)

result: Error = carts_items.carts_items_update(
    cart_id = '',
    id = '',
    configuration = {
        "colour": "RAL 7016",
        "finish": "brushed",
        "length_mm": 2400,
        "mounting": "wall"
    }, # optional
    currency = 'EUR', # optional
    metadata = {
        "campaign": "spring-catalogue",
        "locale": "de-DE",
        "source": "storefront"
    }, # optional
    name = 'Hex bolt M8', # optional
    position = 1, # optional
    product_id = '', # optional
    quantity = 9.99, # optional
    sku = 'BOLT-M8-30', # optional
    snapshot = {}, # optional
    tax_rate = 19, # optional
    type = CartItemType.PRODUCT, # optional
    unit = 'pcs', # optional
    unit_price = 9.99 # optional
)

print(result.model_dump())
```
