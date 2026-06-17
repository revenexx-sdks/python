```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts
from revenexx_revenexx.models import CartItem

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: CartItem = carts.carts_items_get(
    cart_id = '',
    id = ''
)

print(result.model_dump())
```
