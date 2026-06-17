```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import OrderDetail
from revenexx_revenexx.models import OrderItemCreateRequest

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: OrderDetail = orders.orders_place(
    items = [OrderItemCreateRequest()],
    billing_address = {}, # optional
    buyer = {}, # optional
    cart_id = '', # optional
    channel_id = '', # optional
    contact_id = '', # optional
    currency = '', # optional
    customer_order_number = '', # optional
    grand_total = None, # optional
    market_id = '', # optional
    metadata = {}, # optional
    organization_id = '', # optional
    payment = {}, # optional
    shipping = {}, # optional
    shipping_address = {}, # optional
    shipping_total = None, # optional
    user_data = {} # optional
)

print(result.model_dump())
```
