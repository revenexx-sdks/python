```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts
from revenexx_revenexx.models import CartItem
from revenexx_revenexx.enums import CartItemType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: CartItem = carts.carts_items_update(
    cart_id = '',
    id = '',
    configuration = {}, # optional
    currency = '', # optional
    metadata = {}, # optional
    name = '', # optional
    position = None, # optional
    product_id = '', # optional
    quantity = None, # optional
    sku = '', # optional
    snapshot = {}, # optional
    tax_rate = None, # optional
    type = CartItemType.PRODUCT, # optional
    unit = '', # optional
    unit_price = None # optional
)

print(result.model_dump())
```
