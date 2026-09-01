```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error
from revenexx.enums import OrderCommentVisibility

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_comments_create(
    id = '',
    body = 'Called the customer, delivery agreed for next week.',
    author = 'service-desk', # optional
    visibility = OrderCommentVisibility.INTERNAL # optional
)

print(result.model_dump())
```
