```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error
from revenexx.models import OrderReturnPosition

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_return(
    id = '',
    metadata = {
        "rma_portal_case": "C-2026-0917"
    }, # optional
    positions = [OrderReturnPosition()], # optional
    reason = 'Damaged on arrival', # optional
    restock = True # optional
)

print(result.model_dump())
```
