```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import OrderReturn
from revenexx_revenexx.models import OrderReturnPosition

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: OrderReturn = orders.orders_return(
    id = '',
    positions = [OrderReturnPosition()],
    metadata = {}, # optional
    reason = '' # optional
)

print(result.model_dump())
```
