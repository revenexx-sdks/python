```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result = carts.carts_claim(
    contact_id = '',
    session_key = '',
    target_cart_id = '' # optional
)
```
