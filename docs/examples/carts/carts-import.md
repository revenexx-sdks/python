```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.carts import Carts

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result = carts.carts_import(
    contact_id = '', # optional
    csv = '', # optional
    name = '', # optional
    payload = {}, # optional
    profile_id = '', # optional
    session_key = '', # optional
    target_cart_id = '' # optional
)
```
