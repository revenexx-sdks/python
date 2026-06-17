```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.orders import Orders
from revenexx_revenexx.models import OrderShipmentPosition

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result = orders.orders_ship(
    id = '',
    carrier = '', # optional
    metadata = {}, # optional
    number = '', # optional
    positions = [OrderShipmentPosition()], # optional
    shipped_at = '', # optional
    tracking_code = '', # optional
    tracking_url = '' # optional
)
```
