```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error
from revenexx.enums import OrderListCartMode

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_to_cart(
    id = '',
    cart_id = '', # optional
    currency = '', # optional
    mode = OrderListCartMode.APPEND # optional
)

print(result.model_dump())
```
