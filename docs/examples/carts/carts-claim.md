```python
from revenexx.client import Client
from revenexx.services.carts import Carts
from revenexx.models import Error
from revenexx.enums import CartMergeStrategy

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: Error = carts.carts_claim(
    contact_id = '',
    session_key = 'a1b2c3d4e5f6',
    strategy = CartMergeStrategy.MERGE, # optional
    target_cart_id = '' # optional
)

print(result.model_dump())
```
