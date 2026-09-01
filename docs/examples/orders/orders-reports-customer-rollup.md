```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import OrderCustomerRollupResponse
from revenexx.enums import OrderStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: OrderCustomerRollupResponse = orders.orders_reports_customer_rollup(
    as_of = '2026-01-01T12:00:00Z', # optional
    cursor = '', # optional
    organization_ids = [], # optional
    statuses = [OrderStatus.PENDING] # optional
)

print(result.model_dump())
```
