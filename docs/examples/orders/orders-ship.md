```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error
from revenexx.models import OrderShipmentPosition

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_ship(
    id = '',
    carrier = 'DHL', # optional
    metadata = {
        "warehouse": "HAM-1"
    }, # optional
    number = 'DEL-000123', # optional
    positions = [OrderShipmentPosition()], # optional
    shipped_at = '2026-01-01T12:00:00Z', # optional
    tracking_code = '00340434161234567890', # optional
    tracking_url = 'https://example.com/track/00340434161234567890' # optional
)

print(result.model_dump())
```
