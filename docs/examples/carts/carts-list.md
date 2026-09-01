```python
from revenexx.client import Client
from revenexx.services.carts import Carts
from revenexx.models import Error
from revenexx.enums import CartStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

carts = Carts(client)

result: Error = carts.carts_list(
    id = '', # optional
    name = 'Weekly order', # optional
    status = CartStatus.ACTIVE, # optional
    contact_id = '', # optional
    session_key = 'a1b2c3d4e5f6', # optional
    channel_id = '', # optional
    currency = 'EUR', # optional
    is_current = True, # optional
    item_count = 100, # optional
    subtotal = 12, # optional
    abandoned_at = '2026-01-01T12:00:00Z', # optional
    ordered_at = '2026-01-01T12:00:00Z', # optional
    order_ref = 'SO-10042', # optional
    merged_into_cart_id = '', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
