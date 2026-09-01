```python
from revenexx.client import Client
from revenexx.services.carts_items import CartsItems
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts_items = CartsItems(client)

result: Error = carts_items.carts_items_get(
    cart_id = '',
    id = ''
)

print(result.model_dump())
```
